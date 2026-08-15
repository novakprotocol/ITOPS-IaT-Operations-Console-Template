from __future__ import annotations

import json
from dataclasses import dataclass, asdict


@dataclass(slots=True)
class JobDraft:
    job_id: str
    server_id: str
    enabled: bool
    schedule_type: str
    schedule_value: str
    timezone: str
    mode: str
    entrypoint: str
    timeout_seconds: int
    working_directory: str
    credential_reference: str
    output_path: str

    def to_job(self) -> dict:
        return {
            "schema_version": "1.0",
            "job_id": self.job_id,
            "display_name": self.job_id.replace("-", " ").title(),
            "enabled": bool(self.enabled),
            "target": {"server_id": self.server_id},
            "schedule": {
                "type": self.schedule_type,
                "value": self.schedule_value,
                "timezone": self.timezone,
                "missed_run_policy": "skip"
            },
            "execution": {
                "mode": self.mode,
                "entrypoint": self.entrypoint,
                "arguments": [],
                "working_directory": self.working_directory,
                "credential_reference": self.credential_reference
            },
            "outputs": {"root": self.output_path},
            "policy": {
                "timeout_seconds": int(self.timeout_seconds),
                "concurrency": "forbid",
                "retry_count": 0
            }
        }

    def to_json(self) -> str:
        return json.dumps(self.to_job(), indent=2) + "\n"
