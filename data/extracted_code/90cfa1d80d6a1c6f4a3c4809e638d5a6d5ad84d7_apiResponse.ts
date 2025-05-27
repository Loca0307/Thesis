}

export interface GetSettings {
  withdrawal_fee: number;
  tokens_fee: number;
  epoch: number;
  switching_epoch: boolean;
  frontend_version: string;
  backend_version: string;
  min_balance: number;
  confirmations_required: number;
  max_assets_in_request: number;
}

export interface GetEstimateFees {
  withdrawal_fee: string;
  tokens_fee: number;
  fee: number;
  deposit: number;
}

export interface GetCustomRequest {
  request_id: string;
  deposit: number;
  overhead_fee: number;
  withdrawal_address: string;
  is_whitelisted: boolean;
}

export interface GetTokenRequest {
  token_id: string;
  logo: string;
  ticker: string;
  name: string;
  balance: string;
  decimals: string;
}

export interface GetDeliveredRewards {
  id: string;
  staking_address: string;
  epoch: string;
  token: string;
  amount: string;
  withdrawal_request: string;
  expiry_return_pool_id: string | null;
  expiry: string;
  return_policy: string;
  delivered_on: string;
}

export interface GetPendingTxCount {
  pending_tx_count: number;
}

export interface GetTx {
  tx: string;
  slot: string;
  info: string;