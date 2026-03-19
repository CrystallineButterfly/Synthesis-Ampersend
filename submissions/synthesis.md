# Ampersend Settlement Bus

- **Repo:** https://github.com/CrystallineButterfly/Synthesis-Ampersend
- **Primary track:** Ampersend
- **Overlap targets:** Lido MCP Server, Uniswap Agentic Finance, MetaMask Delegations, Filecoin, OpenServ, ERC-8004 Receipts
- **Primary contract:** SettlementBus
- **Primary operator module:** ampersend_bus
- **Live TxIDs:** PENDING
- **ERC-8004 registrations:** PENDING
- **Demo link:** docs/demo_video_script.md

A settlement bus that packages intent metadata together with payments and routing instructions so downstream tracks can share one transport layer.

## Track evidence

- `artifacts/onchain_intents/lido_mcp_server_mcp_call.json`
- `artifacts/onchain_intents/metamask_delegations_delegate_scope.json`
- `artifacts/filecoin/0x42cee98fd52baa4086226d06a8e70adf619c738fcfe60ff8730879c6a84dcf57.json`
- `artifacts/onchain_intents/erc_8004_receipts_receipt_anchor.json`

## Latest verification

```json
{
  "status": "verified",
  "project_name": "Ampersend Settlement Bus",
  "track": "Ampersend",
  "plan_id": "0x42cee98fd52baa4086226d06a8e70adf619c738fcfe60ff8730879c6a84dcf57",
  "simulation_hash": "0x0caca35c25ad71d244ab6e4c37c27f76011a2ba8da486879e8cc670ad1510956",
  "execution_status": "offline_prepared",
  "tx_ids": [],
  "artifact_paths": [
    "artifacts/onchain_intents/lido_mcp_server_mcp_call.json",
    "artifacts/onchain_intents/metamask_delegations_delegate_scope.json",
    "artifacts/filecoin/0x42cee98fd52baa4086226d06a8e70adf619c738fcfe60ff8730879c6a84dcf57.json",
    "artifacts/onchain_intents/erc_8004_receipts_receipt_anchor.json"
  ],
  "partner_statuses": {
    "Ampersend": "awaiting_credentials",
    "Lido MCP Server": "prepared_contract_call",
    "Uniswap": "awaiting_credentials",
    "MetaMask Delegations": "prepared_contract_call",
    "Filecoin": "prepared_filecoin_bundle",
    "OpenServ": "awaiting_credentials",
    "ERC-8004 Receipts": "prepared_contract_call"
  },
  "created_at": "2026-03-19T03:52:07+00:00"
}
```
