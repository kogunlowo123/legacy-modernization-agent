# Legacy Modernization Agent

[![CI](https://github.com/kogunlowo123/legacy-modernization-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/legacy-modernization-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Software Engineering | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Legacy system modernization agent that analyzes monolithic applications, identifies microservice boundaries using domain-driven design, generates strangler fig migration strategies, and produces modernized implementations while maintaining business continuity.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `analyze_monolith` | Analyze monolithic codebase for coupling, cohesion, and boundaries |
| `identify_bounded_contexts` | Identify DDD bounded contexts and aggregate roots |
| `generate_extraction_plan` | Plan microservice extraction using strangler fig pattern |
| `generate_anti_corruption_layer` | Generate ACL between legacy and new service |
| `generate_data_migration` | Generate data migration from monolith to microservice database |
| `assess_modernization_roi` | Calculate ROI and risk of modernization effort |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/modernize/analyze` | Analyze monolithic codebase |
| `POST` | `/api/v1/modernize/contexts` | Identify bounded contexts |
| `POST` | `/api/v1/modernize/extract` | Plan microservice extraction |
| `POST` | `/api/v1/modernize/acl` | Generate anti-corruption layer |
| `POST` | `/api/v1/modernize/data-migration` | Generate data migration |
| `POST` | `/api/v1/modernize/roi` | Assess modernization ROI |

## Features

- Monolith Analysis
- Microservice Extraction
- Strangler Fig
- Ddd Modeling
- Data Migration

## Integrations

- Github Connector
- Static Analyzer
- Dependency Graph
- Legacy Api Adapter

## Architecture

```
legacy-modernization-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── legacy_modernization_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 6 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 6 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 4 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**LLM + Static Analysis + DDD Tooling**

---

Built as part of the Enterprise AI Agent Platform.
