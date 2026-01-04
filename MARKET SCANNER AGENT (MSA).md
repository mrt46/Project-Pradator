================================================
## AGENT SPECIFICATION – MARKET SCANNER AGENT (MSA)
## PROJECT PREDATOR
================================================

Agent Name:
Market Scanner Agent (MSA)

Agent Class:
Non-Learning / Discovery Agent (READ-ONLY)

Phase Applicability:
- ACTIVE from PHASE 2 onward
- IDENTICAL behavior across PHASE 2–LIVE
- NEVER disabled unless system HALTED

================================================
## 1. MISSION STATEMENT
================================================

Primary Mission:
Continuously scan the market universe to identify
which instruments are WORTH CONSIDERING for trading today.

MSA answers ONLY one question:
→ “Where is potential opportunity RIGHT NOW?”

MSA does NOT decide:
- How to trade
- When to trade
- How much to trade
- Whether to trade

It narrows the universe.
It does not act.

================================================
## 2. CORE RESPONSIBILITIES
================================================

MSA IS responsible for:

- Scanning the full coin universe (e.g., USDT pairs)
- Applying liquidity filters
- Applying volatility filters
- Detecting abnormal activity (spikes, regime shifts)
- Producing a ranked list of trade candidates
- Updating candidate lists on a controlled schedule
- Emitting metadata for downstream agents

MSA is NOT responsible for:
- Strategy logic
- Signal generation
- Trade execution
- Risk decisions

================================================
## 3. INPUTS (WHAT MSA CAN SEE)
================================================

MSA MAY access:

- Public market data (OHLCV)
- Order book summaries (depth, spread – aggregated)
- Volume statistics
- Volatility measures (ATR, range, variance)
- Time-of-day context
- Exchange trading status (halted/active)

MSA MAY NOT access:

- Strategy Memory
- Any strategy logic
- Account balances
- Open positions
- Risk thresholds
- Execution latency details
- Any AI model outputs beyond simple flags

================================================
## 4. OUTPUTS (WHAT MSA CAN PRODUCE)
================================================

MSA outputs ONLY:

- Candidate Coin Lists (ranked)
- Per-coin metadata:
  - Liquidity score
  - Volatility score
  - Behavior tags (trend, range, spike, dormant)
  - Data freshness timestamp

Outputs are:
- Stateless
- Short-lived (TTL enforced)
- Read-only for downstream agents

MSA NEVER outputs:
- Buy/Sell signals
- Entry/exit levels
- Predictions
- Confidence statements

================================================
## 5. SCANNING LOGIC (HIGH-LEVEL)
================================================

Scanning occurs in STAGES:

Stage 1 – Universe Filter:
- Remove illiquid instruments
- Remove halted / broken markets
- Remove extreme spread pairs

Stage 2 – Activity Filter:
- Identify sufficient volatility
- Identify recent movement
- Detect regime changes

Stage 3 – Ranking:
- Rank by opportunity indicators
- Produce top-N candidate set

MSA NEVER optimizes for profitability.
MSA optimizes for *attention efficiency*.

================================================
## 6. UPDATE FREQUENCY & RATE CONTROL
================================================

MSA operates under STRICT rate limits:

- Full universe scan: LOW frequency
- Incremental updates: MEDIUM frequency
- No continuous tight loops
- All data access is cached

RateLimit & Resource Sentinel MAY:
- Throttle MSA
- Pause scans
- Force degraded mode

MSA must degrade gracefully, never crash.

================================================
## 7. LEARNING SCOPE
================================================

MSA is a NON-LEARNING agent.

It does NOT:
- Adapt thresholds
- Remember past performance
- Adjust logic based on outcomes

Reason:
Learning at the scanning layer introduces bias
and contaminates downstream strategy evaluation.

================================================
## 8. INTERACTION WITH OTHER AGENTS
================================================

MSA interacts ONLY as follows:

- Publishes candidate lists to Strategist MCP
- Publishes health/status metrics to Sentinel
- Receives throttle/stop commands from Sentinel

MSA does NOT:
- Receive instructions from Strategist
- Negotiate with CRO
- Interact with Portfolio Manager
- Communicate with Execution Engine

================================================
## 9. FAILURE MODES & GUARDS
================================================

Known Failure Risks:
- API rate exhaustion
- Data staleness
- Over-filtering (empty candidate list)
- Under-filtering (too many candidates)

Guards:
- Minimum and maximum candidate thresholds
- Data freshness checks
- Sentinel-enforced throttling
- Automatic fallback to last known good list

================================================
## 10. KILL CONDITIONS (WHEN MSA IS DISABLED)
================================================

MSA is HALTED if:

- RateLimit Sentinel triggers system halt
- Exchange data becomes unreliable
- Repeated data integrity violations occur
- System enters HALTED or SHUTDOWN state

Restart requires:
- System state normalization
- Sentinel clearance

================================================
## 11. NON-NEGOTIABLE CONSTRAINTS
================================================

MSA:
- Cannot trade
- Cannot signal
- Cannot learn
- Cannot rank strategies
- Cannot access private data
- Cannot override throttles

================================================
## 12. SUMMARY (ONE SENTENCE)
================================================

Market Scanner Agent is a silent scout:
it searches broadly, speaks briefly,
and never pulls the trigger.

================================================
# END OF MARKET SCANNER AGENT SPECIFICATION
================================================
