from __future__ import annotations

import json
from dataclasses import dataclass


@dataclass(slots=True)
class JobDraft:
    job_id: str
    server_id: str
    enabled: bool = False
    entrypoint: str = "scripts/examples/noop_receipt.py"

    def to_job(self) -> dict:
        return {
            "schema_version": "1.0",
            "job_id": self.job_id,
            "enabled": bool(self.enabled),
            "target": {"server_id": self.server_id},
            "execution": {"entrypoint": self.entrypoint, "mode": "disabled-placeholder"},
            "policy": {"timeout_seconds": 1800, "concurrency": "forbid", "retry_count": 0},
        }

    def to_json(self) -> str:
        return json.dumps(self.to_job(), indent=2) + "\n"
