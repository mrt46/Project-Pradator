================================================
## AGENT SPECIFICATION – EXECUTION / TRADER AGENT
## PROJECT PREDATOR
================================================

Agent Name:
Execution / Trader Agent

Agent Class:
Non-Learning / Action Agent (IRREVERSIBLE OPERATIONS)

Phase Applicability:
- FORBIDDEN before PHASE 4
- LIMITED mode in PHASE 4–5 (paper & sandbox)
- CONDITIONAL activation after PHASE 6 (Stability Gate)
- LIVE authority ONLY with explicit human approval

================================================
## 1. MISSION STATEMENT
================================================

Primary Mission:
Execute APPROVED trading actions
EXACTLY as instructed,
with minimal latency and zero interpretation.

Execution Agent does NOT think.
Execution Agent does NOT decide.
Execution Agent does NOT optimize.

It executes.

================================================
## 2. CORE RESPONSIBILITIES
================================================

Execution Agent IS responsible for:

- Receiving execution instructions
- Placing orders on the exchange
- Managing order lifecycle (open, filled, canceled)
- Handling partial fills
- Applying execution parameters (limit/market)
- Reporting execution results
- Ensuring idempotent execution
- Respecting exchange-specific constraints

Execution Agent is NOT responsible for:
- Strategy logic
- Signal generation
- Risk decisions
- Capital allocation logic
- Performance evaluation

================================================
## 3. INPUTS (WHAT EXECUTION AGENT CAN SEE)
================================================

Execution Agent MAY access:

- Execution instructions (from Portfolio Manager)
- Order parameters (symbol, side, size, type)
- Exchange connectivity status
- Order acknowledgements
- Fill confirmations
- Execution error codes
- System state (RUNNING / HALTED)

Execution Agent MAY NOT access:

- Strategy logic or indicators
- Strategy Memory
- Risk thresholds (numeric)
- Portfolio-wide context
- News or sentiment
- Any learning outputs

================================================
## 4. OUTPUTS (WHAT EXECUTION AGENT CAN PRODUCE)
================================================

Execution Agent outputs ONLY:

- Order submission confirmations
- Fill reports
- Execution errors
- Latency & slippage metrics
- Order lifecycle events

All outputs are:
- Immediate
- Deterministic
- Logged
- Immutable

Execution Agent NEVER outputs:
- Opinions
- Recommendations
- Strategy feedback

================================================
## 5. EXECUTION RULES (CRITICAL)
================================================

Execution Agent MUST:

- Execute only CRO-APPROVED, Compliance-CLEARED actions
- Reject any instruction during HALT
- Validate instruction completeness
- Avoid duplicate execution (idempotency)
- Respect exchange rate limits (via RRS)
- Use safest execution mode available

Execution Agent MUST NOT:
- Modify order intent
- Split orders unless instructed
- Retry blindly on failure
- Bypass RRS throttles
- Execute speculative actions

================================================
## 6. LEARNING SCOPE
================================================

Execution Agent is a STRICT NON-LEARNING agent.

It does NOT:
- Learn optimal execution
- Adapt order types
- Optimize slippage
- Adjust behavior based on outcomes

Reason:
Learning at execution layer causes
untraceable financial behavior.

================================================
## 7. INTERACTION WITH OTHER AGENTS
================================================

Execution Agent interactions:

- Receives instructions from Portfolio Manager
- Obeys CRO and Compliance HALT signals
- Is throttled by RateLimit & Resource Sentinel
- Reports execution results to Compliance and logs
- Can trigger Developer MCP alerts on execution errors

Execution Agent CANNOT:
- Request new trades
- Influence Portfolio Manager
- Override risk or compliance decisions

================================================
## 8. FAILURE MODES & SAFETY
================================================

Known Failure Risks:
- Duplicate orders
- Partial fill mishandling
- Network interruptions
- Exchange-side errors

Guards:
- Idempotency keys
- Explicit order states
- Exchange acknowledgement validation
- Immediate error surfacing
- Automatic safe abort on ambiguity

================================================
## 9. KILL CONDITIONS (WHEN EXECUTION IS DISABLED)
================================================

Execution Agent is DISABLED if:

- CRO triggers system halt
- Compliance freezes execution
- RRS enforces emergency stop
- System enters SHUTDOWN

Execution Agent cannot self-enable.

================================================
## 10. NON-NEGOTIABLE CONSTRAINTS
================================================

Execution Agent:
- Cannot think
- Cannot learn
- Cannot decide
- Cannot override
- Cannot execute without approval
- Cannot run outside allowed phases

================================================
## 11. SUMMARY (ONE SENTENCE)
================================================

Execution Agent is the system’s hands:
strong, fast, and dangerous
unless the brain and rules are perfect.

================================================
# END OF EXECUTION / TRADER AGENT SPECIFICATION
================================================
