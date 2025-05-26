
    def test_duplicate_cron_not_scheduled(self) -> None:
        monkeypatch = MonkeyPatch()

        log_messages = []

        def fake_info(message: str) -> None:
            log_messages.append(message)

        monkeypatch.setattr(Logger, "info", fake_info)

        cron_schedule = "*/1 * * * *"
        worker_id_first = ApplicationService.schedule_worker_as_cron(
            cls=HealthCheckWorker, cron_schedule=cron_schedule
        )
        assert worker_id_first

        worker_details = ApplicationService.get_worker_by_id(worker_id=worker_id_first)
        assert worker_details.id == worker_id_first
        assert worker_details.status == WorkflowExecutionStatus.RUNNING

        worker_id_duplicate = ApplicationService.schedule_worker_as_cron(
            cls=HealthCheckWorker, cron_schedule=cron_schedule
        )
        assert worker_id_first == worker_id_duplicate

        duplicate_log = (
            f"Worker {worker_id_first} already running, skipping starting new instance"
        )
        assert any(
            duplicate_log in log for log in log_messages
        ), "Expected duplicate log message not found"

        ApplicationService.terminate_worker(worker_id=worker_id_first)
        time.sleep(1)
        terminated_worker_details = ApplicationService.get_worker_by_id(
            worker_id=worker_id_first
        )
        assert terminated_worker_details.status == WorkflowExecutionStatus.TERMINATED