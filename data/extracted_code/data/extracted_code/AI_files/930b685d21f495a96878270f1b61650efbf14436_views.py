from rest_framework.permissions import AllowAny
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from decimal import Decimal
from payments.models import Payment


@method_decorator(csrf_exempt, name="dispatch")
class PaymeAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data
        method = data.get("method")
        params = data.get("params", {})
        request_id = data.get("id")

        handler = {
            "CheckPerformTransaction": self.check_perform_transaction,
            "CreateTransaction": self.create_transaction,
            "PerformTransaction": self.perform_transaction,
            "CheckTransaction": self.check_transaction,
            "CancelTransaction": self.cancel_transaction,
        }.get(method)

        if handler:
            return handler(params, request_id)

        return Response({
            "jsonrpc": "2.0",
            "error": {"code": -32601, "message": "Method not found"},
            "id": request_id
        })

    def check_perform_transaction(self, params, request_id):
        try:
            payment_id = params["account"]["payment_id"]
            amount = Decimal(params["amount"]) / 100  # Payme sends amount in tiyin
            payment = get_object_or_404(Payment, id=payment_id)

            if payment.status != Payment.StatusChoices.PENDING:
                return self.error_response(-31050, "Transaction already processed", request_id)

            if amount != payment.amount:
                return self.error_response(-31001, "Incorrect amount", request_id)

            return self.success_response({"allow": True}, request_id)
        except Exception:
            return self.error_response(-31099, "Error in checking transaction", request_id)

    def create_transaction(self, params, request_id):
        try:
            payment_id = params["account"]["payment_id"]
            payme_transaction_id = params["id"]
            payment = get_object_or_404(Payment, id=payment_id)

            if payment.transaction_id and payment.transaction_id != payme_transaction_id:
                return self.error_response(-31008, "Transaction already exists", request_id)

            payment.transaction_id = payme_transaction_id
            payment.save()

            return self.success_response({
                "create_time": int(time.time() * 1000),
                "transaction": payme_transaction_id,
                "state": 1,
                "receivers": None,
            }, request_id)

        except Exception:
            return self.error_response(-31099, "Failed to create transaction", request_id)

    def perform_transaction(self, params, request_id):
        try:
            transaction_id = params["id"]
            payment = get_object_or_404(Payment, transaction_id=transaction_id)

            if payment.status == Payment.StatusChoices.COMPLETED:
                return self.success_response({
                    "transaction": transaction_id,
                    "perform_time": int(payment.updated_at.timestamp() * 1000),
                    "state": 2,
                }, request_id)
