# Live readiness

- **Project:** Ampersend Settlement Bus
- **Track:** Ampersend
- **Latest verification:** `verified`
- **Execution mode:** `offline_prepared`
- **Generated at:** `2026-03-19T03:52:07+00:00`

## Trust boundaries

- **Ampersend** — `rest_json` — Bundle payment and transport metadata for downstream agents.
- **Lido MCP Server** — `contract_call` — Call MCP-style Lido verbs behind policy envelopes.
- **Uniswap** — `rest_json` — Quote swaps and bounded liquidity moves.
- **MetaMask Delegations** — `contract_call` — Enforce delegation scopes, expiries, and intent envelopes.
- **Filecoin** — `file_upload` — Persist proofs, logs, and evidence bundles offchain.
- **OpenServ** — `rest_json` — Dispatch jobs and expose swarm service endpoints.
- **ERC-8004 Receipts** — `contract_call` — Anchor identity, task receipts, and reputation updates.

## Offline-ready partner paths

- **Lido MCP Server** — prepared_contract_call
- **MetaMask Delegations** — prepared_contract_call
- **Filecoin** — prepared_filecoin_bundle
- **ERC-8004 Receipts** — prepared_contract_call

## Live-only partner blockers

- **Ampersend**: AMPERSEND_API_KEY, AMPERSEND_PAYMENT_URL — https://docs.ampersend.ai/
- **Uniswap**: UNISWAP_API_KEY, UNISWAP_QUOTE_URL — https://developers.uniswap.org/
- **OpenServ**: OPENSERV_API_KEY, OPENSERV_AGENT_URL — https://docs.openserv.ai/

## Highest-sensitivity actions

- `metamask_delegations_delegate_scope` — MetaMask Delegations — Use MetaMask Delegations for a bounded action in this repo.

## Exact next steps

- Copy .env.example to .env and fill the required keys.
- Deploy the contract with forge script script/Deploy.s.sol --broadcast for SettlementBus.
- Run python3 scripts/run_agent.py to produce a dry run for ampersend_bus.
- Set LIVE_MODE=true and rerun python3 scripts/run_agent.py with real credentials.
- Run python3 scripts/render_submission.py and attach TxIDs plus repo links.
