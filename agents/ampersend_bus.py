"""Project-specific context module."""

from __future__ import annotations

PROJECT_CONTEXT = {
  "project_name": "Ampersend Settlement Bus",
  "track": "Ampersend",
  "pitch": "A settlement bus that packages intent metadata together with payments and routing instructions so downstream tracks can share one transport layer.",
  "overlap_targets": [
    "Lido MCP Server",
    "Uniswap Agentic Finance",
    "MetaMask Delegations",
    "Filecoin",
    "OpenServ",
    "ERC-8004 Receipts"
  ],
  "goals": [
    "discover a bounded opportunity",
    "plan a dry-run-first action",
    "verify receipts and proofs"
  ]
}


def seed_targets() -> list[str]:
    """Return the first batch of overlap targets for planning."""
    return list(PROJECT_CONTEXT['overlap_targets'])
