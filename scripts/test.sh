#!/usr/bin/env bash
set -euo pipefail

pytest -q
mypy src/
black --check src/ tests/