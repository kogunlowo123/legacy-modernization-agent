#!/bin/bash
set -euo pipefail
echo "Setting up Legacy Modernization Agent..."
pip install -e ".[dev]"
echo "Setup complete!"
