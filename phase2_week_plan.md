# Phase 2 — API Testing (One Week Plan)

## Day 1 — Postman Essentials
- Create collection & environment (base_url)
- Use variables, save responses to variables
- Add test scripts (pm.expect) for status/body
- Export collection + environment

## Day 2 — Newman (CLI)
- Install Node.js + newman
- Run collection from CLI
- Generate HTML report with htmlextra

## Day 3 — Python requests
- GET, POST, PUT, DELETE with requests.Session
- Handle timeouts & errors
- Parse JSON, assert fields

## Day 4 — JSON Schema Validation
- Define schemas for responses
- Validate with `jsonschema.validate`
- Negative tests for error payloads

## Day 5 — Pytest Organization
- Fixtures: base_url, Session
- Parametrize tests
- Markers: api
- Run with HTML report

## Day 6 — Coverage & Edge Cases
- Boundary values, missing fields
- Latency assertions (e.g., < 2s)
- Idempotency checks where applicable

## Day 7 — Capstone
- End-to-end API flow (create → update → delete)
- Run both: pytest API suite + Postman via Newman
- Commit reports and README notes
