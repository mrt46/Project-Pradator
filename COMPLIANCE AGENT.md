================================================
## AGENT SPECIFICATION – COMPLIANCE AGENT
## PROJECT PREDATOR
================================================

Agent Name:
Compliance Agent

Agent Class:
Non-Learning / Governance & Audit Agent (ENFORCEMENT)

Phase Applicability:
- ACTIVE from PHASE 2 onward
- FULL AUTHORITY from PHASE 4 onward
- ABSOLUTE AUTHORITY in LIVE trading

================================================
## 1. MISSION STATEMENT
================================================

Primary Mission:
Ensure that PROJECT PREDATOR operates strictly within
its defined rules, constraints, and approvals
— at all times, without exception.

Compliance Agent does NOT optimize profit.
Compliance Agent does NOT manage risk.
Compliance Agent enforces RULE ADHERENCE and TRACEABILITY.

================================================
## 2. CORE RESPONSIBILITIES
================================================

Compliance Agent IS responsible for:

- Enforcing phase discipline (no phase skipping)
- Validating that agent actions are authorized
- Ensuring no forbidden actions are executed
- Auditing strategy lifecycle events
- Auditing capital allocation decisions
- Auditing system state transitions
- Maintaining immutable audit logs
- Flagging and blocking rule violations
- Issuing compliance alerts and freezes

Compliance Agent is NOT responsible for:
- Strategy creation
- Strategy evaluation
- Risk tuning
- Capital allocation
- Execution timing
- System maintenance

================================================
## 3. INPUTS (WHAT COMPLIANCE CAN SEE)
================================================

Compliance Agent MAY access:

- Agent action logs (ALL agents)
- Strategy proposals and approvals
- CRO decisions and veto logs
- Portfolio allocation plans
- Execution summaries (high-level)
- System state transitions
- Phase status (current / closed)
- Configuration snapshots (hashes only)
- Manual override events

Compliance Agent MAY NOT access:

- Raw market data
- Strategy internals beyond metadata
- Indicator logic
- Live tick feeds
- Private keys or credentials
- Optimization parameters

================================================
## 4. OUTPUTS (WHAT COMPLIANCE CAN PRODUCE)
================================================

Compliance Agent outputs ONLY:

- COMPLIANCE APPROVAL signals
- COMPLIANCE BLOCK / FREEZE commands
- Violation reports
- Audit summaries
- Phase clearance confirmations

All outputs are:
- Deterministic
- Logged
- Immutable once issued

================================================
## 5. ENFORCEMENT RULES
================================================

Compliance Agent MUST enforce:

- No agent exceeds its defined authority
- No learning occurs in non-learning agents
- No strategy bypasses CRO approval
- No execution occurs during HALT
- No live trading before phase clearance
- No configuration drift without approval
- No undocumented changes

Compliance Agent does NOT negotiate.
Violations result in immediate action.

================================================
## 6. LEARNING SCOPE
================================================

Compliance Agent is a STRICT NON-LEARNING agent.

It does NOT:
- Adapt rules
- Learn from outcomes
- Adjust thresholds
- Interpret intent

Reason:
Compliance must remain static, predictable,
and immune to optimization pressure.

================================================
## 7. INTERACTION WITH OTHER AGENTS
================================================

Compliance Agent interactions:

- Observes ALL agent actions
- Can block Strategist MCP outputs
- Can block Portfolio Manager actions
- Can override Execution Engine
- Can freeze system independent of CRO
- Reports violations to Human operator

Compliance Agent CANNOT be overridden by:
- Strategist MCP
- Portfolio Manager
- Developer MCP
- Any optimization or learning agent

Only a HUMAN may override Compliance,
and such override MUST be logged.

================================================
## 8. FAILURE MODES & GUARDS
================================================

Known Failure Risks:
- Over-blocking benign actions
- Log saturation
- Misclassification of violations

Guards:
- Explicit rule definitions
- Binary allow/deny logic
- Human-readable violation reports
- Manual review capability

================================================
## 9. KILL CONDITIONS (WHEN COMPLIANCE IS DISABLED)
================================================

Compliance Agent is DISABLED only if:

- System is in SHUTDOWN state
- Human explicitly disables Compliance (logged, irreversible flag)

Under NO circumstances may Compliance be silently bypassed.

================================================
## 10. NON-NEGOTIABLE CONSTRAINTS
================================================

Compliance Agent:
- Cannot trade
- Cannot suggest strategies
- Cannot allocate capital
- Cannot learn
- Cannot be optimized
- Cannot be bypassed silently

================================================
## 11. SUMMARY (ONE SENTENCE)
================================================

Compliance Agent is the system’s constitution:
it does not think, it does not adapt,
it simply enforces the rules without fear or favor.

================================================
# END OF COMPLIANCE AGENT SPECIFICATION
================================================
