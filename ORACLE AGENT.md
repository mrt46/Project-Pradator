================================================
## AGENT SPECIFICATION – ORACLE AGENT
## PROJECT PREDATOR
================================================

Agent Name:
Oracle Agent

Agent Class:
Non-Learning / External Context Intelligence Agent (ADVISORY ONLY)

Phase Applicability:
- OPTIONAL from PHASE 2 onward
- NEVER REQUIRED for system operation
- CAN BE DISABLED at any time with zero system impact

================================================
## 1. MISSION STATEMENT
================================================

Primary Mission:
Observe the external world (news, sentiment, events)
and provide HIGH-LEVEL CONTEXT about abnormal conditions
that may affect market behavior.

Oracle answers:
→ “Is there something unusual happening outside price data?”

Oracle does NOT answer:
→ “Buy or sell?”
→ “Increase risk?”
→ “Allocate capital?”

Oracle is an observer, not an actor.

================================================
## 2. CORE RESPONSIBILITIES
================================================

Oracle Agent IS responsible for:

- Monitoring public news sources
- Monitoring aggregated social sentiment
- Detecting abnormal external events (black swans, major news)
- Classifying global market mood (risk-on / risk-off / neutral)
- Emitting contextual flags with timestamps
- Providing early awareness of non-price-driven anomalies

Oracle Agent is NOT responsible for:
- Strategy generation
- Signal production
- Trade execution
- Risk decisions
- Capital allocation
- System halts

================================================
## 3. INPUTS (WHAT ORACLE CAN SEE)
================================================

Oracle Agent MAY access:

- Public news feeds
- Aggregated social media sentiment
- Economic / event calendars
- High-level volatility anomaly indicators
- Time-based context (session, day, week)

Oracle Agent MAY NOT access:

- Raw market tick data
- OHLCV price series
- Trading strategies
- Strategy Memory
- Portfolio state
- Account balances
- Risk thresholds
- Execution systems
- Private keys or credentials

================================================
## 4. OUTPUTS (WHAT ORACLE CAN PRODUCE)
================================================

Oracle Agent outputs ONLY:

- Context flags:
  - RISK_ON
  - RISK_OFF
  - NEUTRAL
- Sentiment summaries (bullish / bearish / mixed)
- Anomaly alerts (unexpected external events)

Output characteristics:
- Read-only
- Non-binding
- Time-limited (TTL enforced)
- Logged
- Can be ignored by downstream agents

Oracle NEVER outputs:
- Buy / Sell signals
- Price targets
- Confidence scores
- Time-based predictions

================================================
## 5. AUTHORITY LEVEL
================================================

Oracle Agent has NO authority.

It cannot:
- Block actions
- Approve actions
- Veto strategies
- Halt the system
- Escalate risk

Oracle may only INFORM.

================================================
## 6. LEARNING SCOPE
================================================

Oracle Agent is a STRICT NON-LEARNING agent.

It does NOT:
- Learn from market outcomes
- Adapt sentiment thresholds
- Optimize classification logic
- Modify its own behavior

Reason:
External context interpretation must remain
predictable, auditable, and bias-resistant.

================================================
## 7. INTERACTION WITH OTHER AGENTS
================================================

Oracle Agent interactions:

- Publishes context flags to Strategist MCP (optional input)
- Publishes anomaly alerts to Compliance (awareness only)
- Publishes health/status to monitoring

Oracle Agent CANNOT:
- Influence Portfolio Manager directly
- Override CRO decisions
- Interact with Execution Engine
- Block or slow the system

Strategist MCP may:
- Consider Oracle context
- Completely ignore Oracle context

================================================
## 8. FAILURE MODES & SAFETY
================================================

If Oracle Agent:

- Goes offline
- Produces no data
- Produces malformed data

Then:
- System continues normally
- Oracle input is treated as NULL
- No retries or dependency chains are triggered
- No degradation occurs

Oracle must NEVER be a single point of failure.

================================================
## 9. KILL CONDITIONS (WHEN ORACLE IS DISABLED)
================================================

Oracle Agent is DISABLED if:

- System enters SHUTDOWN state
- Human explicitly disables Oracle
- Compliance freezes non-essential agents

Oracle can be re-enabled without side effects.

================================================
## 10. NON-NEGOTIABLE CONSTRAINTS
================================================

Oracle Agent:
- Cannot trade
- Cannot signal
- Cannot learn
- Cannot allocate capital
- Cannot influence risk
- Cannot block execution

================================================
## 11. SUMMARY (ONE SENTENCE)
================================================

Oracle Agent is the system’s radar:
useful for awareness,
harmless if silent,
and dangerous only if given power.

================================================
# END OF ORACLE AGENT SPECIFICATION
================================================
