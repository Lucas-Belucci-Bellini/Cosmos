# Claude Code Instructions — Cosmos

**Canonical plan:** [docs/COSMOS_MASTER_PLAN.md](docs/COSMOS_MASTER_PLAN.md)

The master plan is the governing engineering document. Read it before substantial work. If this file and the master plan conflict, stop and report the conflict; do not silently choose.

## Mandatory startup sequence

Before editing:
1. Read this file, `README.md`, and `docs/COSMOS_MASTER_PLAN.md`.
2. Read the relevant system map, architecture, technology decision, security, data and test documents.
3. Inspect the current repository tree, build manifests, lockfiles, CI workflows, tests and scripts. Do not assume a runtime or test command exists.
4. Inspect the current diff/status and preserve unrelated user changes.
5. Search for an existing implementation and all callers before adding a new module.
6. For Baluarte migration tasks, inspect the source evidence and the current migration matrix/catalog. Record paths/ref and distinguish source presence from verified runtime behavior.
7. State a concise task plan, intended files, acceptance criteria, risks and checks before implementation.

## Core behavior

- Follow **Understand → Document → Classify → Plan → Decide → Rebuild/Adapt → Test → Record evidence**.
- Build the smallest complete vertical slice, not many disconnected placeholders.
- Treat Baluarte as a reference and evidence source, not as an architecture to copy blindly.
- Use migration states consistently: KEEP, ADAPT, REBUILD, REFERENCE, DEFER, REJECT or UNKNOWN.
- Keep public contracts versioned and typed. Avoid circular dependencies and hidden cross-module state.
- TypeScript is a candidate for UI and application integration; Rust for justified local/runtime components; Python for AI/data/automation workers; PostgreSQL for durable structured data. Follow the actual technology decision and ADRs; do not add languages merely for appearance or assumed security.
- Hermes is currently planned as a replaceable model/provider adapter for J.A.R.V.I.S. Verify the intended project/model, provider, availability, quotas, cost and terms before live integration. Keep a mock adapter for tests.
- Rebuild API contracts around validation, explicit errors, limits, authorization and observability. Source files in Baluarte do not prove that deployments, credentials or external services are recoverable.
- The model may suggest tool calls but must never authorize them. Validate arguments against server-owned schemas and independently authorize every operation.
- Deny by default. Unknown tools, invalid inputs, missing identity, policy failures and timeouts must not grant access.
- Never place secrets, access tokens, passwords, private keys, session credentials or raw sensitive payloads in source, documentation, issues, logs, test output or commits.
- Do not run destructive database migrations, delete/replace user data, change production credentials, deploy to production or incur new costs without explicit maintainer approval.
- Do not make broad unrelated refactors while implementing a focused task.

## Test and evidence rules

- Add or update tests with behavior changes.
- Run the narrowest relevant tests first; expand checks when feasible.
- Record exact commands and outcomes: **PASS**, **FAIL**, **BLOCKED**, or **NOT RUN**.
- Never claim that a build, test, benchmark, API request, provider integration, security scan or deployment succeeded unless it actually ran and returned evidence.
- When checks cannot run, explain why and create a precise follow-up issue/task.
- Distinguish static source review, automated tests, local runtime evidence, external-service checks and deployment evidence.
- A green compile alone does not prove authorization, privacy, migration safety or end-to-end correctness.

## Documentation and traceability

Update the relevant documents in the same change when practical:
- `docs/COSMOS_MASTER_PLAN.md` for phase/status or governing-scope changes;
- `docs/migration/MIGRATION_MATRIX.md` for source-to-target migration status;
- `docs/product/FEATURE_CATALOG.md` for capability inventory;
- `docs/INDEX.md` for new governing docs and reports;
- architecture/security/data/test documents and ADRs when contracts change;
- issue/task status and acceptance criteria where available.

Do not generate dozens of speculative subsystem plans at once. Create detailed module plans incrementally from verified inventory, and link each plan to evidence, decisions, dependencies, implementation and tests.

## Task completion report

At the end, report:
1. What changed and why.
2. Exact files created/modified.
3. Tests/checks run with commands and outcomes.
4. Checks not run and blockers.
5. Security/data/API/compatibility implications.
6. Documentation and issue updates.
7. Remaining risks and the next highest-value task.

## Required stop-and-ask cases

Stop and ask the maintainer when:
- a destructive or irreversible action is proposed;
- security policy, permission scope or identity semantics must change;
- the provider/model choice creates new cost or external commitments;
- data retention/privacy requirements are unclear;
- conflicting architectural documents cannot be reconciled from existing ADRs;
- a task would require publishing secrets or using production credentials;
- acceptance criteria cannot be met without broadening scope.

**Never invent file paths, scripts, commands, API endpoints, configuration names, test results, deployment status or feature completion.**
