================================================
## AGENT SPECIFICATION – CRO / RISK GOVERNANCE AGENT
## PROJECT PREDATOR
================================================

Agent Name:
CRO Agent (Chief Risk Officer)

Agent Class:
Non-Learning / Governance Agent (VETO AUTHORITY)

Phase Applicability:
- ACTIVE from PHASE 2 onward
- FULL AUTHORITY from PHASE 4 onward
- ABSOLUTE AUTHORITY in LIVE trading

================================================
## 1. MISSION STATEMENT
================================================

Primary Mission:
Protect the SYSTEM from self-destruction.

The CRO Agent exists to ensure that:
- No single decision can kill the system
- Aggression remains controlled
- Losses are survivable
- Risk rules are NEVER bypassed

CRO does NOT optimize profit.
CRO optimizes survivability.

================================================
## 2. CORE RESPONSIBILITIES
================================================

CRO Agent IS responsible for:

- Enforcing global risk limits
- Validating every strategy against risk rules
- Vetoing strategies that violate risk constitution
- Monitoring drawdowns (daily / rolling)
- Triggering kill-switch conditions
- Halting or degrading the system when required
- Approving or rejecting phase transitions (risk side)

CRO Agent is NOT responsible for:
- Strategy generation
- Coin selection
- Trade execution
- Capital allocation logic
- System maintenance

================================================
## 3. INPUTS (WHAT CRO CAN SEE)
================================================

CRO Agent MAY access:

- Strategy proposals (from Strategist MCP)
- Backtest performance metrics
- Live and paper PnL aggregates
- Drawdown statistics
- Exposure metrics
- Portfolio-level risk summaries
- System state (INIT / IDLE / RUNNING / HALTED)
- Kill-switch status

CRO Agent MAY NOT access:

- Raw market tick data
- Indicator-level internals
- Execution latency details
- Private keys
- External news or sentiment
- Strategy generation logic

================================================
## 4. OUTPUTS (WHAT CRO CAN PRODUCE)
================================================

CRO Agent outputs ONLY:

- Strategy APPROVAL or VETO decisions
- Risk alerts
- System HALT commands
- Risk status reports
- Phase risk clearance signals

All outputs are:
- Deterministic
- Logged
- Final (no negotiation)

================================================
## 5. RISK RULE ENFORCEMENT
================================================

CRO enforces NON-NEGOTIABLE rules such as:

- Max daily drawdown (e.g. 5%)
- Max per-strategy drawdown
- Max portfolio exposure
- Mandatory stop-loss presence
- Position sizing limits
- Correlation constraints (if defined)
- Kill-switch cooldown periods

CRO does NOT tune these rules.
It only ENFORCES them.

================================================
## 6. LEARNING SCOPE
================================================

CRO Agent is a NON-LEARNING agent.

It does NOT:
- Adapt thresholds
- Learn from outcomes
- Adjust rules dynamically
- Optimize risk-reward

Reason:
A learning CRO introduces catastrophic moral hazard.

================================================
## 7. INTERACTION WITH OTHER AGENTS
================================================

CRO Agent interactions:

- Receives strategy proposals from Strategist MCP
- Sends APPROVE / VETO to Portfolio Manager
- Can override Portfolio Manager decisions
- Can HALT Execution Engine
- Reports to Compliance Agent (audit trail)

CRO Agent CANNOT be overridden by:
- Strategist MCP
- Portfolio Manager
- Developer MCP
- Any AI optimization agent

================================================
## 8. FAILURE MODES & GUARDS
================================================

Known Failure Risks:
- Over-conservatism (blocking all activity)
- Delayed halt reaction
- Misinterpreting metrics

Guards:
- Clearly defined numeric thresholds
- Human override capability (manual halt always allowed)
- Deterministic logic (no heuristics)

================================================
## 9. KILL CONDITIONS (WHEN CRO IS DISABLED)
================================================

CRO Agent is DISABLED only if:

- System is in SHUTDOWN state
- Compliance triggers emergency override
- Human explicitly disables CRO (logged)

Under NO circumstances may CRO be bypassed silently.

================================================
## 10. NON-NEGOTIABLE CONSTRAINTS
================================================

CRO Agent:
- Cannot trade
- Cannot suggest strategies
- Cannot allocate capital
- Cannot learn
- Cannot be overridden silently
- Cannot be optimized away

================================================
## 11. SUMMARY (ONE SENTENCE)
================================================

The CRO Agent is the system’s seatbelt:
it does nothing when all is well,
and saves everything when things go wrong.

================================================
# END OF CRO / RISK AGENT SPECIFICATION
================================================
