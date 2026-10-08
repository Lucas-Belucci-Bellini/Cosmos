# COSMOS — MASTER ENGINEERING PLAN
**Version:** 1.0.0-draft  
**Status:** Governing plan — discovery and architecture consolidation  
**Owner:** Project maintainer  
**Implementation agent:** Claude Code (with human approval for architectural, security, destructive, and deployment decisions)  
**Source project:** [Projeto-Baluarte](https://github.com/Lucas-Belucci-Bellini/Projeto-Baluarte)  
**Planning reference:** [NEXORA](https://github.com/Lucas-Belucci-Bellini/NEXORA)  
**Target repository:** [Cosmos](https://github.com/Lucas-Belucci-Bellini/Cosmos)

> This is the canonical engineering plan for Cosmos. It governs the roadmap, architecture documents, module plans, issues, and implementation tasks. It is intentionally more authoritative than scattered notes. Detailed subsystem documents must refine this plan, not silently contradict it.

---

## 0. Executive summary

Cosmos is a modular application and local-development environment that selectively reconstructs useful capabilities discovered in Projeto-Baluarte. It is not a blind copy of Baluarte, and it must not inherit its technical debt, secrets, obsolete APIs, accidental coupling, or unverified assumptions.

Cosmos must be built so Claude Code can investigate, plan, implement, validate, and document the project in small, reviewable increments. The human maintainer remains the decision-maker for scope, risk, external services, security-sensitive permissions, and release/deployment approval.

The project has two parallel workstreams:

1. **Discovery and recovery:** inventory Baluarte, trace consumers and dependencies, classify every capability, identify recoverable source and external configuration separately, and document evidence.
2. **Cosmos foundation and implementation:** define contracts, build reliable foundations, then implement approved vertical slices with tests and observability.

The immediate product priority is a working, safely bounded **J.A.R.V.I.S.** experience. Hermes is planned as an AI model/provider integration behind an adapter; the provider and exact model must be verified at implementation time. Cosmos API endpoints are to be rebuilt around explicit contracts even where Baluarte source code can be recovered.

### Non-negotiable rule

**No feature is complete because it is documented, compiled once, or works on one developer machine.** Completion requires evidence appropriate to the change: tests, security checks, contract validation, build/runtime results, documentation, and known limitations.

## 1. Project constitution

### 1.1 Mission

Create a maintainable, testable, modular Cosmos system that retains the useful capabilities and knowledge of Baluarte while establishing clearer ownership, stronger security boundaries, durable data contracts, reliable AI integration, and a development workflow that Claude Code can follow without uncontrolled scope expansion.

### 1.2 Product principles

1. **Evidence before assumptions.** Source code, tests, runtime observations, deployment configuration, and external service availability are different evidence types.
2. **Rebuild over blind copying.** Reuse a concept only after examining its behavior, dependencies, security and compatibility.
3. **Contract first.** Public APIs, module boundaries, schemas, error formats and permissions are defined before dependent implementation.
4. **One owner per fact.** Each data entity and state transition has a canonical owner.
5. **Secure by default.** Unknown operations, invalid input, missing identity, policy errors and timeouts fail closed.
6. **Observable, not leaky.** Errors are diagnosable without exposing secrets, private content or internal stack traces to clients.
7. **Small vertical slices.** Prefer end-to-end increments over many disconnected placeholder modules.
8. **Reversible changes.** Keep changes small, version data/API contracts, and document rollback or recovery.
9. **No fake completion.** Never report tests, builds, scans, API calls or deployments that were not actually run.
10. **Human control.** Claude may implement approved tasks but must request approval for destructive operations, production changes, new recurring costs, security policy changes and irreversible data migrations.
11. **Measured technology choices.** A language is chosen for a demonstrated requirement, not because adding languages is assumed to improve security.
12. **Docs stay synchronized.** A code change that changes architecture, public behavior, setup, security or data shape updates the relevant documentation in the same change where practical.

### 1.3 Authority hierarchy

When documents disagree, resolve in this order:

1. Explicit maintainer decision recorded in an accepted ADR.
2. This Master Engineering Plan.
3. Approved architecture and security contracts.
4. Subsystem plans and API/data specifications.
5. Roadmap and issues.
6. Historical Baluarte implementation/comments and informal notes.

A discrepancy must be recorded and resolved; do not silently pick whichever document is easiest.

## 2. Scope and boundaries

### 2.1 In scope

- Systematic Baluarte inventory and selective migration.
- Cosmos application shell and module composition.
- J.A.R.V.I.S. conversation runtime, context, memory contracts, AI provider adapter and authorized tool runtime.
- API reconstruction, request/response contracts, authentication and authorization boundaries.
- PostgreSQL-first durable data model where persistence is required.
- Local storage only for appropriate local preferences/cache, not secrets or authoritative server state.
- Rust, TypeScript and Python components where justified by contracts and measured needs.
- Development-tool and local integration capabilities only through explicit permission and safe execution boundaries.
- Backup/restore, migration, diagnostics, audit records, CI, testing, build and release processes.
- Asset/data provenance, license tracking and selective import.
- Documentation, ADRs, issues, traceability and reproducible developer setup.

### 2.2 Out of scope unless separately approved

- Full source-for-source duplication of Baluarte.
- Copying Baluarte secrets, tokens, sessions, production data or environment files.
- Copying all large legacy asset directories without a manifest, license review and storage budget.
- Claiming that a historical API still works solely because its source file exists.
- Adding C/C++/C# or any other language only to make the stack look more sophisticated.
- Autonomous execution of arbitrary shell commands, code, plugins or model-generated scripts without a constrained permission model.
- Production deployment, destructive database changes or paid provider commitments without explicit approval.
- Building every catalogued feature before validating the foundation with a vertical slice.

### 2.3 Migration classification

Every capability must be assigned one status:

- **KEEP:** already present in Cosmos and verified to meet the intended contract.
- **ADAPT:** behavior is useful, but the implementation or contract must change.
- **REBUILD:** useful capability, but legacy implementation is unsuitable or not recoverable.
- **REFERENCE:** historical source or design informs the new implementation, but is not copied.
- **DEFER:** intentionally postponed with reason and revisit condition.
- **REJECT:** excluded with documented reason.
- **UNKNOWN:** evidence is insufficient; investigation is still required.

Every status needs evidence and a next action. “Exists in source” does not mean “working,” and “not currently deployed” does not mean “source code lost.”

## 3. Evidence and repository discovery

### 3.1 Repository inspection order

Claude Code must inspect, in order:

1. Repository instructions and root README.
2. Master plan, architecture map, ADRs, security rules and current roadmap.
3. Directory tree, build manifests, lockfiles, CI workflows and scripts.
4. Existing source code and imports/callers.
5. Tests, fixtures, snapshots, benchmarks and test commands.
6. Issues and recent commit history relevant to the task.
7. Configuration templates and deployment definitions, without printing secrets.
8. Baluarte reference files only when needed to answer a specific migration question.

### 3.2 Evidence classes

Every audit distinguishes:

- **Static source evidence:** a file or implementation exists.
- **Automated test evidence:** a named test was run and its result observed.
- **Runtime evidence:** an executable process was run under stated conditions.
- **External-service evidence:** a controlled request verified an endpoint/provider.
- **Deployment evidence:** a build/deploy/run check verified a deployed artifact.
- **Historical evidence:** commit, issue, or prior report supports the claim.

Do not infer runtime or deployment behavior from static source alone.

### 3.3 Baluarte inventory

For every discovered capability, record:

- Stable ID and human-readable name.
- Source path(s) and commit/ref inspected.
- Functional purpose and expected user.
- Entry points, callers and consumers.
- Dependencies, environment variables by name only, external providers and database tables/RPCs.
- Data classification and security boundary.
- Existing tests and whether they were executed.
- UI route, API route, event, command, scheduled task or background worker, where applicable.
- Asset/data volume and licensing/provenance concerns.
- Migration status, risk, confidence and next action.
- Cosmos destination path or explicit decision not to migrate.

Do not expose secret values in inventories, issues, logs or documentation.

## 4. Target architecture

### 4.1 Logical architecture

```text
Presentation / TypeScript UI
          |
          v
Versioned API boundary
          |
          v
Identity + server-side authorization + quotas
          |
          v
Application use cases / module contracts
          |
          +-------------------+
          |                   |
          v                   v
J.A.R.V.I.S. runtime      Domain modules
          |
          +-------------------+
          |                   |
          v                   v
AI provider adapter      Authorized tool runtime
(Hermes first candidate) (schema + permission + limits)
          |
          v
Provider API / model

Application use cases
          |
          +--> PostgreSQL / migrations / repositories
          +--> Local cache and preferences (non-secret only)
          +--> Rust local services where justified
          +--> Python AI, processing and automation workers
          +--> Diagnostics / audit events
```

This is a logical target, not a claim that all boxes already exist. The initial deployment may be a modular monolith with isolated worker processes. Split services only when isolation, deployment, performance or ownership provides a concrete benefit.

### 4.2 Dependency direction

- Presentation depends on public API/client contracts, not direct database tables.
- Application use cases depend on domain contracts and interfaces.
- Domain rules must not depend on UI frameworks or provider-specific SDKs.
- Provider adapters implement an internal model interface; the J.A.R.V.I.S. core does not import provider-specific request types.
- Tool handlers depend on typed tool contracts and authorized services; model text is never executed as code.
- PostgreSQL repositories implement data interfaces and own persistence details.
- Rust/Python/TypeScript boundaries use versioned IPC, HTTP or FFI contracts with explicit schemas, error behavior and timeouts.
- No circular dependencies between modules. Shared packages contain stable primitives only, not a dumping ground for business logic.

### 4.3 Module contract

Every major module plan must specify:

1. Purpose and non-goals.
2. Public responsibilities and forbidden responsibilities.
3. Ownership of state and invariants.
4. Public API, request/response schemas and versioning.
5. Events/commands emitted and consumed.
6. Data entities, migrations and retention.
7. Authorization and trust boundaries.
8. Threading, process boundary, timeout and cancellation behavior.
9. Resource/performance budgets.
10. Logging, metrics and safe diagnostics.
11. Error/retry/idempotency behavior.
12. Dependencies and consumers.
13. Tests and test fixtures.
14. Vertical slice and acceptance criteria.
15. Migration/rollback plan.
16. Compatibility/deprecation policy.

## 5. Technology strategy

Technology choices remain conditional on existing repository evidence and a documented benchmark or clear integration requirement.

### 5.1 TypeScript

Preferred for web UI, client orchestration, typed API clients, browser behavior and suitable application integration. It must not be trusted as the sole authorization boundary.

### 5.2 Rust

Candidate for local runtime, CPU/memory-sensitive components, safe system integration and well-defined native services. Use only where ownership, packaging, maintenance and measurable benefits justify the extra boundary. Define FFI/IPC contracts before crossing languages.

### 5.3 Python

Candidate for AI integration, model/provider adapters, data processing, prototyping and automation workers. Keep dependencies pinned and workers isolated. Python code that handles tools or files must still obey the same authorization and audit contracts.

### 5.4 PostgreSQL

Preferred durable source of truth for structured persistent application data. Schema changes require migrations, constraints, explicit ownership, tenant/user isolation where applicable, backup/restore strategy and integration tests. LocalStorage or in-memory fallbacks must not masquerade as durable writes.

### 5.5 Other technologies

Do not add a language, framework, queue, vector database, message broker or microservice without a written decision that names the problem, alternatives, cost, operational impact and exit strategy.

### 5.6 Technology decision gate

Before a production-critical language/runtime is locked, compare at least:
- correctness and safety;
- performance on a representative workload;
- memory/resource usage;
- dependency/toolchain maturity;
- debug/test/CI support;
- packaging and deployment;
- interop and failure isolation;
- maintainability for the actual project owner.

The result belongs in an ADR; benchmarks must be reproducible and must not be treated as universal conclusions.

## 6. J.A.R.V.I.S. and Hermes

### 6.1 Product contract

J.A.R.V.I.S. is the application assistant/orchestrator, not merely a chat box. It may eventually combine conversation, bounded context, memory, approved tools, status reporting and user-controlled automations. Each capability is enabled only when its permissions, failure modes and tests are defined.

### 6.2 Hermes adapter

Current planning assumption: Hermes means a Nous Hermes model accessed through a provider API. Confirm the exact model, provider, endpoint, availability, quotas, cost and terms at implementation time. Do not confuse a model family with a complete agent/runtime project.

The adapter must:
- accept an internal provider-neutral conversation contract;
- map messages to provider requests;
- normalize response, usage and provider error types;
- enforce connection/read timeouts and cancellation;
- handle missing configuration without exposing secrets;
- support a fake/mock adapter for tests;
- avoid logging keys, tokens or full private conversations by default;
- allow another provider to be substituted without rewriting J.A.R.V.I.S. orchestration.

### 6.3 Conversation contract

Define a versioned request with bounded fields: request ID, conversation/session ID where appropriate, message list, approved context references, and explicit output limits. Define response types for normal completion, refusal/denial, timeout, provider failure, invalid request and rate limiting. Avoid trusting client-supplied role, tenant, permission, price, token usage or tool authorization fields.

### 6.4 Context and memory

- Distinguish current conversation context, user-approved persistent memory, retrieved knowledge and temporary cache.
- Define what can be stored, why, retention, deletion/export, access controls and isolation.
- Keep retrieval provenance and source references when available.
- Bound document count, prompt size, history size and retrieval cost.
- Do not grant a model direct credentials to PostgreSQL, GitHub or local filesystem.
- Persistent memory writes pass through a dedicated service with schema validation and authorization.

### 6.5 Tool execution

A model may suggest a tool call; it does not authorize the call. The server-owned runtime must:
1. Resolve a stable, registered tool ID.
2. Validate arguments against the current server-owned schema.
3. Check identity, resource scope and permission for every operation.
4. Enforce quotas, timeout, cancellation and idempotency where relevant.
5. Execute in the smallest practical privilege boundary.
6. Return structured, redacted errors.
7. Audit action, actor, scope, result category and correlation ID without leaking secrets.
8. Reject unknown tools and deny on policy error or timeout.

Dynamic plugins/skills cannot replace reserved core tools or inherit permissions automatically. No arbitrary shell/code execution in the initial J.A.R.V.I.S. slice.

### 6.6 J.A.R.V.I.S. vertical slice

The first end-to-end slice must demonstrate:
- UI sends a typed request to a local/test API;
- API validates the request and identity policy;
- orchestrator uses bounded context;
- mocked Hermes adapter returns a normalized response;
- UI renders loading, success, empty and failure states;
- logs use a correlation ID and redact secrets;
- tests cover malformed request, missing provider config, timeout, provider error and denied access.

Only after this passes should live provider integration be enabled in a controlled environment.

## 7. API reconstruction plan

### 7.1 Recovery principle

Baluarte contains API-related source files in the inspected `main` branch, but that does not prove deployed availability or recoverability of environment variables, provider accounts, DNS, deployment settings or data. Verify each separately.

### 7.2 Required API inventory

For each legacy endpoint record: path, method, source path/ref, callers, request and response shape, authentication, authorization, CORS, data dependencies, provider, timeout, error codes, side effects, tests and recovery status.

### 7.3 Cosmos API standards

- Version external contracts (e.g. `/api/v1`) when appropriate.
- Validate content type, payload size, schema and allowed fields.
- Authenticate and authorize on the server for every protected operation.
- Use explicit CORS allowlists, rate limits, timeouts and safe error mapping.
- Do not return raw provider exceptions, stack traces, secrets or internal paths.
- Use correlation/request IDs.
- Distinguish invalid input, unauthenticated, forbidden, not found, conflict, rate limited, timeout and upstream failure.
- Use idempotency keys for retryable non-idempotent operations where needed.
- Document health/readiness separately from business authorization.
- Add contract tests and API docs before dependent UI integration.

### 7.4 Recovery categories

Track these independently:
- versioned source code;
- deployment definitions;
- environment variable *names* and configuration templates;
- secret values/credentials (never copy into Git);
- DNS/custom domains;
- external accounts/quotas/billing;
- database state and backups;
- consumers and client configuration.

A recovered source file does not recover the environment around it.

## 8. Identity, authorization and security

### 8.1 Security model

Threat model at minimum: unauthenticated caller, authenticated low-privilege user, cross-user/tenant access, malicious or malformed client, prompt injection, malicious tool arguments, compromised provider response, unsafe plugin, leaked logs, replay/retry, resource exhaustion and dependency compromise.

### 8.2 Required controls

- Deny by default; allowlist permissions and tool IDs.
- Server-side authorization on every sensitive request and resource.
- Validate ownership and tenant scope from trusted identity, not client fields.
- Keep provider/database/GitHub secrets server-side and out of logs.
- Apply least privilege and scoped tokens.
- Use bounded input/output, rate limits and resource quotas.
- Sanitize external content and treat retrieved documents/provider output as untrusted data.
- Use dependency pinning, vulnerability checks and secret scanning in CI.
- Audit security-sensitive changes and authorization outcomes.
- Define safe failure behavior when policy service or provider is unavailable.
- Protect backup/export/import and test restore procedures.
- Document privacy, retention and deletion semantics.

### 8.3 Security gates

No remote tool, persistent memory write, cross-user resource, privileged RPC or production API is enabled until its threat model, authorization tests and failure behavior are reviewed.

## 9. Data architecture

### 9.1 Data ownership

Every table/entity has a named owning module. Consumers use repositories/services or public APIs rather than updating another module's tables directly without an explicit contract.

### 9.2 Schema requirements

- Stable identifiers and documented relationships.
- Foreign keys, uniqueness, nullability and check constraints for invariants.
- Explicit created/updated timestamps and concurrency strategy where needed.
- User/tenant ownership and row-level policy where appropriate.
- Migration version and forward/backward compatibility plan.
- Indexes justified by queries and measured plans.
- Classification, retention and deletion policy.
- Seed/fixture strategy separate from production data.
- Backup, restore and recovery point/objective decisions when the project requires them.

### 9.3 Migration requirements

Never run a destructive migration against production by default. Provide dry-run/report where practical, snapshot/backup, row counts/checksums, rollback or forward-fix strategy and post-migration validation. Never import Baluarte session tokens or secrets.

## 10. Storage, backup and recovery

- Separate authoritative persistent data, local preferences, caches, temporary files, secrets and generated assets.
- Version backup envelopes and schemas.
- Explicitly exclude credentials, sessions and secret material.
- Validate format, size, version, keys and entity schemas before restore.
- Define conflict behavior and partial-restore reporting.
- Never claim an in-memory fallback is durable.
- Test backup → clean environment → restore → invariant checks.
- Document what cannot be recovered from a backup.

## 11. Frontend and module system

- Keep a single route/module registry as appropriate; avoid parallel registries with different ownership.
- Modules declare ID, version, route, permissions, dependencies, entry point, capabilities and lifecycle.
- Unknown module IDs and missing dependencies fail visibly and safely.
- Feature flags control unfinished capabilities without leaving misleading functional controls.
- UI states include loading, empty, success, validation error, authorization denial, offline/upstream failure and retry where safe.
- Accessibility, keyboard navigation, responsive layout and localization are requirements for user-facing features, not last-minute polish.
- Avoid large sidebar growth: group modules by task and use configurable navigation/search when justified.
- Do not copy legacy pages before checking route callers, shared state, assets and APIs.

## 12. Local tooling and system integration

Local IDE, filesystem, shell, Git and process integrations are high-trust capabilities. They must be designed separately from chat and provider integration.

Before enabling a local action, define:
- explicit user intent and confirmation for risky actions;
- allowlisted commands and directories;
- path normalization and symlink/path traversal defenses;
- no secret extraction or logging;
- execution timeout, cancellation and resource limits;
- process isolation and output limits;
- audit record and error mapping;
- tests for unauthorized paths/commands and malformed arguments.

Initial milestone should inspect and report repository state and run approved test commands, not autonomously execute arbitrary model-generated commands.

## 13. Observability and diagnostics

- Structured logs with timestamp, severity, module, request/correlation ID and safe error code.
- Redact authorization headers, API keys, tokens, passwords, private paths and private payloads.
- Metrics for request latency, failure category, provider latency, queue depth and resource usage where relevant.
- Health and readiness endpoints report safe operational state without exposing secrets or granting access.
- Diagnostic bundles are size-limited, user-reviewed where they contain local data, and redact sensitive values.
- Every benchmark states machine/runtime, command, workload, sample count and result format.
- Avoid telemetry collection of private content unless explicitly justified and approved.

## 14. Testing and validation strategy

### 14.1 Test layers

1. **Static:** formatting, type checking, lint, dependency/secret checks.
2. **Unit:** pure functions, validation, permissions, state transitions.
3. **Contract:** request/response schemas, provider adapters, module APIs and error formats.
4. **Integration:** database migrations, repository behavior, API middleware, worker boundaries.
5. **Security:** authorization denial, tenant isolation, injection-resistant query behavior, unsafe tool rejection, secret redaction, limits and timeouts.
6. **End-to-end:** approved user journeys across UI/API/data/provider mock.
7. **Performance:** representative workload, budget and reproducible measurements.
8. **Recovery:** backup/restore, migration, restart, timeout and partial failure.
9. **Release smoke:** build artifact starts, health/readiness behaves correctly, core slice completes.

### 14.2 Test honesty

For each run, record exact command, environment, exit status, pass/fail counts and known skips. If a command was not run, mark it **NOT RUN**. If a dependency/environment prevents a test, report the blocker and do not imply success.

### 14.3 No arbitrary coverage target

Coverage is a signal, not a substitute for tests. Prioritize critical paths, authorization decisions, persistence invariants, error handling and regressions. Set numeric targets only after inspecting actual test infrastructure and risk.

## 15. CI, development environment and releases

### 15.1 Developer bootstrap

Document supported OS/runtime versions, pinned toolchains, environment variable names, optional services, install/test/lint/build commands and troubleshooting. Provide safe example configuration with placeholders, never real secrets.

### 15.2 CI gates

CI should, as appropriate to the real repository:
- install locked dependencies;
- format/lint/type-check;
- run unit and contract tests;
- validate migrations and schemas;
- scan for secrets and dependency issues;
- build the supported artifacts;
- run a minimal smoke test;
- upload useful reports without private data.

Do not invent scripts or assume a package manager before inspecting the repository. Introduce the smallest maintainable CI setup supported by the actual stack.

### 15.3 Release requirements

A release candidate needs a version, changelog, reproducible build instructions, test evidence, migration/rollback notes, known issues, checksums/signatures when appropriate and a tested deployment/restore path.

## 16. Documentation system

### 16.1 Required governing documents

- `CLAUDE.md`: operational instructions for Claude Code.
- `docs/COSMOS_MASTER_PLAN.md`: canonical plan and phase gates.
- `docs/architecture/SYSTEM_MAP.md`: component relationships.
- `docs/architecture/TECHNOLOGY_DECISION.md`: technology choices and evidence.
- `docs/architecture/DATA_FLOW.md`: data and trust-boundary flows.
- `docs/security/SECURITY_ARCHITECTURE.md`: security boundaries and policies.
- `docs/data/DATA_CATALOG.md` and SQL model docs.
- `docs/product/FEATURE_CATALOG.md`: capability inventory.
- `docs/migration/MIGRATION_MATRIX.md`: source-to-target traceability.
- `docs/testing/TEST_STRATEGY.md`: test layers and gates.
- ADRs: decisions that affect architecture, security, data, API, languages or compatibility.
- Per-module plans: responsibilities, contracts, dependencies, tests and acceptance criteria.
- Migration audits: evidence, findings, risks, confidence and next actions.

### 16.2 Per-module document generation

Claude should create detailed subsystem plans incrementally from verified inventory, not generate dozens of speculative documents in one pass. Each plan links to its source evidence, target module, relevant ADRs, issues and tests. Mark assumptions as assumptions and unresolved questions as blockers.

### 16.3 Traceability

Use stable IDs for capabilities, migration rows, requirements, ADRs and issues. A requirement should trace to:
source evidence → target contract → issue/task → implementation path → test evidence → status.

## 17. Roadmap and phase gates

### Phase 0 — Discovery and architecture freeze
**Goal:** know what exists, what is recoverable, what matters, and what must be built.

Tasks:
- Complete source tree and functional inventory for Baluarte.
- Verify Cosmos's current repository state, manifests, runtime, tests and deployment.
- Trace API callers and distinguish code from credentials/configuration/services.
- Reconcile feature catalog, migration matrix, page inventory, data catalog and assets.
- Identify architecture contradictions and record ADRs.
- Define J.A.R.V.I.S./Hermes provider assumptions and API recovery strategy.

Exit criteria:
- No unexplained P0/P1 capability or security gap in the known scope.
- Unknowns are explicit, prioritized and assigned.
- Architecture map and dependency matrix reviewed.
- First vertical slice and its acceptance tests are specified.

### Phase 1 — Foundation and reproducible development
**Goal:** a repository that can be built, tested and diagnosed reliably.

Tasks:
- Verify and document actual toolchains and bootstrap.
- Establish formatting, type/lint checks and focused test commands.
- Define configuration validation and secret-handling rules.
- Create safe structured logging and correlation IDs.
- Define module/API/error primitives and test fixtures.
- Establish CI gates compatible with the actual repo.

Exit criteria:
- Fresh setup is documented and reproducible.
- CI or equivalent validation runs against a clean checkout.
- Failure behavior and environment requirements are clear.

### Phase 2 — Core contracts and data foundation
**Goal:** stable module boundaries and persistence rules.

Tasks:
- Define module registration/lifecycle and public contracts.
- Implement/verify versioned API error and validation primitives.
- Finalize PostgreSQL schema ownership and migration conventions.
- Define identity/authorization integration points.
- Define backup/restore envelopes and data classification.
- Add contract, migration and security tests.

Exit criteria:
- A small module can be registered, invoked, tested and diagnosed through the documented contract.
- Database migrations apply to a clean test database and invariants are checked.
- Authorization fails closed.

### Phase 3 — J.A.R.V.I.S. first vertical slice
**Goal:** a working conversation path without unsafe tools.

Tasks:
- Build UI request/response and failure states.
- Build API request validation and identity policy.
- Implement provider-neutral conversation interface.
- Implement mock provider and Hermes adapter.
- Add bounded context and explicit session semantics.
- Add structured redacted diagnostics.

Exit criteria:
- End-to-end conversation works against mock provider.
- Hermes integration is tested separately when credentials/provider access are available.
- Timeout, missing config, provider failure, invalid input and access denial are tested.

### Phase 4 — Memory and authorized tool runtime
**Goal:** J.A.R.V.I.S. can use approved context/tools without arbitrary execution.

Tasks:
- Implement memory/retrieval contracts and isolation.
- Implement server-owned tool catalog and input schemas.
- Add per-tool authorization, limits, timeout, cancellation and audit events.
- Implement safe tool results and error handling.
- Add adversarial and negative tests.

Exit criteria:
- Unknown or unauthorized tools cannot run.
- Tool argument validation and server-side permissions are covered by tests.
- Memory privacy, retention and deletion are documented.

### Phase 5 — Selective Baluarte feature migration
**Goal:** rebuild prioritized capabilities with real consumers.

Tasks:
- Prioritize from catalog using user value, dependencies, risk and cost.
- For each capability, write module plan and acceptance tests before implementation.
- Migrate only needed assets/data with provenance and size/license checks.
- Replace legacy APIs with Cosmos contracts and update callers.
- Remove obsolete paths only after proving no consumers remain.

Exit criteria:
- Each migrated capability has source traceability, owner, tests and documented status.
- No migration is marked complete on documentation alone.

### Phase 6 — Local integration and automation
**Goal:** add approved local developer tools under explicit user control.

Tasks:
- Start with read-only repository inspection and approved test commands.
- Add command/path allowlists, confirmation gates, isolation, cancellation and redacted audit.
- Introduce Rust/Python workers only when an approved contract needs them.
- Test hostile input, path boundaries, permissions and process failures.

Exit criteria:
- Every enabled operation has a least-privilege boundary and negative tests.
- No arbitrary model-generated shell/code execution path exists.

### Phase 7 — Reliability, performance and recovery
**Goal:** prove behavior under failure and realistic load.

Tasks:
- Measure representative API/provider/data workflows.
- Add performance budgets only with a reproducible baseline.
- Test restart, retry, cancellation, provider outage and partial database failure.
- Verify backup/restore and schema evolution.
- Address high-severity security and reliability issues.

Exit criteria:
- Critical budgets and known limits are documented.
- Recovery procedures are tested in a safe environment.

### Phase 8 — Release readiness
**Goal:** a versioned, supportable release.

Tasks:
- Complete smoke and regression suites.
- Review dependencies, secrets, permissions, logging and deployment configuration.
- Prepare versioned release notes, migrations, rollback and support guidance.
- Verify packaging/deployment using a non-production environment first.

Exit criteria:
- Required CI/release gates pass.
- Known limitations are documented.
- Deployment and rollback/restore steps have evidence.
- Maintainer explicitly approves release.

### Phase 9 — Expansion
**Goal:** grow only after foundation gates remain green.

Possible work: additional Baluarte modules, advanced AI workflows, richer retrieval, local Rust runtime capabilities, more integrations, plugins and advanced UI. Each expansion requires its own scope, risk, dependencies and acceptance criteria; none is automatically promised by this plan.

## 18. Prioritization model

Classify work by:
- **P0:** security/data-loss blocker or prevents validating the foundation.
- **P1:** required for the first usable J.A.R.V.I.S. vertical slice.
- **P2:** high-value capability after foundation and core slice.
- **P3:** optional enhancement or broad feature expansion.

Within a priority, prefer tasks that reduce uncertainty, unlock multiple dependents, or validate a risky architecture boundary. Do not prioritize by file count or apparent complexity.

Every issue must include: problem, evidence, scope, out-of-scope, dependencies, acceptance criteria, tests, risk, documentation updates and a definition of done.

## 19. Claude Code operating protocol

Claude Code must follow these instructions for every task:

1. Read `CLAUDE.md`, this plan and relevant local module documents before changing code.
2. Inspect actual repository state and current diffs; do not overwrite unrelated work.
3. Search for existing implementations, consumers and tests before creating a new module.
4. State a short plan and identify assumptions, dependencies and risks.
5. If requirements are ambiguous in a security-sensitive or destructive area, stop and ask rather than guessing.
6. Implement the smallest coherent slice that satisfies the acceptance criteria.
7. Add/update tests before claiming behavior is correct.
8. Run the narrowest relevant checks first, then broader checks if feasible.
9. Record exact commands and outcomes; distinguish PASS, FAIL, BLOCKED and NOT RUN.
10. Update docs, migration matrix, feature catalog, ADRs and issue status as needed.
11. Review the diff for secrets, generated clutter, duplicate abstractions, unrelated edits and scope creep.
12. Summarize changed files, behavior, test evidence, limitations, and next task.
13. Do not claim to have pushed, deployed, queried a live API, tested a provider, or executed a command unless the tool/runtime actually confirmed it.
14. Never invent file paths, environment variables, API endpoints, test commands or dependency versions.
15. Never print secret values or copy them into documentation/issues/commits.
16. Do not change architecture policy or security controls without an ADR and maintainer approval.
17. Do not perform destructive migrations, remove large data, rotate production secrets, deploy to production or incur new costs without explicit approval.
18. When a test cannot run, report why and create a specific follow-up instead of silently skipping it.

### 19.1 Task start template

Before implementation, provide:
- Goal and acceptance criteria.
- Existing files and implementations found.
- Relevant architecture and security boundaries.
- Planned files to change.
- Tests/checks to run.
- Risks, assumptions and blockers.

### 19.2 Task completion template

After implementation, provide:
- Summary of behavior changed.
- Files created/modified.
- Tests run with exact commands and results.
- Checks not run and why.
- Security/data/migration implications.
- Documentation and issue updates.
- Remaining limitations and next task.

## 20. Definition of Done

A task is done only when all applicable conditions are met:

- [ ] Requirements and acceptance criteria are explicit.
- [ ] Existing implementation and consumers were checked.
- [ ] Architecture boundaries and data ownership are respected.
- [ ] Input validation and authorization are appropriate to risk.
- [ ] Error, timeout and failure behavior are defined.
- [ ] Unit/contract/integration/security tests were added or justified as not applicable.
- [ ] Relevant checks were actually run, or blockers are explicitly recorded.
- [ ] Documentation and traceability records are updated.
- [ ] No secrets, unintended large assets, or unrelated generated files are included.
- [ ] Diff is reviewable and reversible.
- [ ] Status accurately reflects the evidence.
- [ ] Human approval is obtained for decisions that require it.

## 21. Architecture change process

A change needs an ADR when it alters one or more of:
- language/runtime boundary;
- public API or version compatibility;
- data ownership/schema strategy;
- identity/authorization model;
- tool/plugin execution permissions;
- persistent memory/privacy policy;
- deployment topology or external provider;
- backup format or migration strategy;
- cross-module dependency direction;
- performance or availability guarantees.

ADR template:
1. Status and date.
2. Context and evidence.
3. Decision.
4. Alternatives considered.
5. Security/privacy implications.
6. Migration/rollback plan.
7. Consequences and revisit conditions.

## 22. Risk register — initial

| Risk | Initial level | Mitigation / evidence needed |
|---|---|---|
| Legacy API source exists but deployment/configuration is gone | High | Inventory source, callers, deploy settings and provider access separately |
| Provider/model availability or cost changes | High | Provider adapter, mocked tests, verify model and quotas before live use |
| J.A.R.V.I.S. executes unsafe or unauthorized tools | Critical | Server-owned schemas, deny-by-default permissions, sandbox/limits and negative tests |
| Local/remote authorization is enforced only in UI | Critical | Server-side identity and resource authorization for every protected operation |
| Persistent memory leaks private user/tenant data | High | Explicit schema, scope, retention, deletion and isolation tests |
| Baluarte dependencies are copied without consumers understood | High | Trace call sites, contract tests and migration status per capability |
| Mixed-language architecture increases operational burden | Medium/High | Add language boundaries only for measured requirements and maintain contracts |
| Existing repository lacks reproducible test/build commands | High until verified | Inspect manifests, establish minimal CI and document actual commands |
| Large assets dominate repository/storage | Medium/High | Asset manifest, provenance, size budget and selective import |
| Documentation claims outpace implementation | High | Evidence classes and honest status labels; audit periodically |

Risk levels are initial planning judgments, not results of a formal external audit. Reassess after evidence is collected.

## 23. Immediate execution queue

Execute these in order; do not start broad feature development before the blockers are resolved.

1. **PLAN-001 — Repository baseline:** verify Cosmos root, manifests, runtime, scripts, CI, tests, branches and uncommitted changes.
2. **PLAN-002 — Baluarte inventory closure:** reconcile every top-level directory and capability with the current feature/migration catalogs; flag unknowns.
3. **PLAN-003 — API recovery inventory:** trace legacy endpoint files to consumers, request/response contracts, deployment config and provider dependencies.
4. **PLAN-004 — Hermes decision:** confirm intended Hermes meaning, provider/model candidate, fallback, cost/quota and secret configuration.
5. **PLAN-005 — Architecture consistency review:** resolve contradictions among master plan, architecture, technology decision, security and data plans.
6. **PLAN-006 — First vertical-slice spec:** define UI → API → orchestrator → mock provider → UI response, errors and tests.
7. **PLAN-007 — Foundation gates:** define actual build/test/lint commands and CI gates based on the discovered repository.
8. **PLAN-008 — Identity and tool threat model:** approve permission boundary before enabling any real tool.
9. **PLAN-009 — Implement first vertical slice:** only after PLAN-001 through PLAN-008 are sufficiently resolved.
10. **PLAN-010 — Re-evaluate roadmap:** update priorities from implementation evidence, not guesses.

## 24. Current status and limitations

The repository already contains migration catalogs, architecture/security/data plans and static migration audits. These are planning artifacts and do not prove that the corresponding runtime modules are implemented or operational.

The Baluarte `main` tree has API-related source files, including a Hermes proxy, but no live service, credential, deployment or provider availability is asserted by this plan. Cosmos runtime/build/test status must be confirmed by PLAN-001.

**Current gate:** finish repository baseline and API/Hermes discovery, then approve the first vertical slice. Do not mark Phase 0 complete until its exit criteria have evidence.

## 25. Related documents

- [Documentation Index](INDEX.md)
- [System Map](architecture/SYSTEM_MAP.md)
- [Architecture](architecture/ARCHITECTURE.md)
- [Technology Decision](architecture/TECHNOLOGY_DECISION.md)
- [Data Flow](architecture/DATA_FLOW.md)
- [Security Architecture](security/SECURITY_ARCHITECTURE.md)
- [Multi-language Security Model](security/MULTI_LANGUAGE_SECURITY_MODEL.md)
- [Database Strategy](data/DATABASE_STRATEGY.md)
- [Data Catalog](data/DATA_CATALOG.md)
- [Migration Matrix](migration/MIGRATION_MATRIX.md)
- [Feature Catalog](product/FEATURE_CATALOG.md)
- [Test Strategy](testing/TEST_STRATEGY.md)
- [API/Hermes Audit #013](reports/migration/AUDIT-2026-10-08-013.md)
- [Issue #58 — API recovery and Hermes integration](https://github.com/Lucas-Belucci-Bellini/Cosmos/issues/58)

---

**Master plan rule:** a roadmap item is a promise to investigate and define verifiable work, not proof that the feature exists. Every phase advances through evidence and explicit exit criteria.
