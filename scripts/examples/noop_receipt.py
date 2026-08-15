#!/usr/bin/env python3
from __future__ import annotations

import json
from datetime import datetime, timezone

receipt = {
    "schema_version": "1.0",
    "result": "NOOP",
    "execution_enabled": False,
    "server_mutation": False,
    "generated_utc": datetime.now(timezone.utc).isoformat()
}
print(json.dumps(receipt, indent=2))
