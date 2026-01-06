================================================
PROJECT PREDATOR
STRATEGY GOVERNANCE & MULTI-STRATEGY CONSTITUTION
================================================

Status: LOCKED POLICY  
Scope: Strategy selection, scoring, risk, lifecycle, and AI improvement loop  
This document is binding for ALL agents, including AI agents.

================================================
1. CORE PRINCIPLES
================================================

1. The system SHALL NEVER operate with a single strategy.
2. The system SHALL ALWAYS use a Strategy Pool.
3. At most ONE (1) strategy may actively trade at any given time (two only in special low-risk modes).
4. Strategy selection SHALL be fully automatic and score-based.
5. Risk discipline SHALL override profit.
6. No strategy is “trusted forever”.
7. Any strategy can be disabled, demoted, or killed by the system.

================================================
2. STRATEGY CLASSES (RISK PROFILES)
================================================

Each strategy MUST belong to exactly one class:

- CORE:
  Stable, low drawdown, main portfolio candidates.
  Can receive large capital allocation.

- AGGRESSIVE:
  Volatile, higher risk.
  Capital allocation MUST be capped.

- TAIL_RISK:
  High return, rare but severe losses possible.
  Capital allocation MUST be very small.
  NEVER allowed to be primary strategy.

================================================
3. MULTI-STRATEGY ARCHITECTURE
================================================

Market Data
    ↓
Strategy Pool (N strategies)
    ↓
Strategy Scoring Engine
    ↓
Strategy Selector
    ↓
CRO (Risk Governor - VETO POWER)
    ↓
Execution Engine

Strategies do NOT decide.
The system decides.

================================================
4. STRATEGY SCORING MODEL
================================================

Each strategy receives a score in range:

    StrategyScore ∈ [0, 100]

Score is computed as:

    StrategyScore =
        w1 * PerformanceScore
      + w2 * StabilityScore
      + w3 * RegimeScore
      + w4 * RiskScore
      + w5 * FreshnessScore

Default weights:

- w1 = 0.35  (Performance)
- w2 = 0.20  (Stability)
- w3 = 0.20  (Regime fit)
- w4 = 0.15  (Risk behavior)
- w5 = 0.10  (Freshness)

================================================
5. SCORE COMPONENT DEFINITIONS
================================================

5.1 PerformanceScore
- Based on:
  - Net PnL
  - Profit Factor
  - PnL / MaxDrawdown ratio
- Rewards profitability adjusted for pain.

5.2 StabilityScore
- Based on:
  - Equity curve smoothness
  - Loss streaks
  - Volatility of returns
- Rewards consistency and penalizes chaos.

5.3 RegimeScore
- Each strategy declares supported regimes:
  - Trend
  - Range
  - High Volatility
  - Low Volatility
- Score depends on match with current detected regime.

5.4 RiskScore
- Penalizes:
  - Recent drawdown spikes
  - Stop-loss violations
  - Abnormal volatility behavior
- ANY strategy that violates risk discipline MUST be penalized heavily.

5.5 FreshnessScore
- Detects performance decay over time.
- Penalizes strategies whose edge appears to be dying.

================================================
6. SCORE INTERPRETATION RULES
================================================

- Score >= 80:
  Primary candidate

- Score 60–80:
  Secondary candidate

- Score 40–60:
  Standby / observation only

- Score < 40:
  Disabled

- Score < 30:
  Sent to improvement or kill pipeline

================================================
7. STRATEGY SELECTION RULES
================================================

1. Only the highest scoring eligible strategy may trade.
2. At most ONE strategy trades at a time (unless explicitly allowed by CRO).
3. CRO has absolute veto power regardless of score.

================================================
8. GLOBAL vs LOCAL KILL-SWITCH
================================================

8.1 GLOBAL KILL-SWITCH
Triggered ONLY if:
- Total portfolio drawdown > daily limit (e.g. 5%)
- Systemic failure
- API / execution / infrastructure chaos

Effect:
- ALL trading stops
- System enters cooldown

8.2 STRATEGY-LOCAL KILL
Triggered if:
- A single strategy violates its risk envelope
- A single strategy causes abnormal losses

Effect:
- That strategy is DISABLED
- System continues with other strategies

================================================
9. HANDLING HIGH RETURN BUT DANGEROUS STRATEGIES
================================================

Strategies that:
- Make good money
- But occasionally cause large losses

MUST be classified as:

    CLASS = TAIL_RISK

Rules:
- NEVER primary strategy
- VERY SMALL capital allocation
- NEVER allowed with leverage
- Used only in specific regimes and conditions

================================================
10. LEVERAGE RULES
================================================

1. Leverage is NOT a default mode.
2. Leverage eligibility is defined PER STRATEGY.
3. Only CORE or selected AGGRESSIVE strategies may ever use leverage.
4. TAIL_RISK strategies are NEVER allowed to use leverage.
5. CRO has absolute veto over leverage usage.

================================================
11. STRATEGY LIFECYCLE MANAGEMENT
================================================

Each strategy has a status:

- CANDIDATE
- ACTIVE
- DISABLED
- UNDER_REVIEW
- KILLED

Transitions:

- If Score < 40 → DISABLED
- If Score < 30 → UNDER_REVIEW
- If catastrophic violation → KILLED

================================================
12. AUTOMATIC STRATEGY IMPROVEMENT PIPELINE
================================================

Any strategy that enters:

    UNDER_REVIEW

MUST be automatically sent to:

    Strategist MCP (AI)

Strategist MCP is required to:
- Analyze failure reasons
- Attempt:
  - Parameter optimization
  - Structural modification
  - Variant generation

Results:

- If improved variant passes tests:
    → New strategy enters CANDIDATE pool

- If no viable improvement is found:
    → Strategy is permanently KILLED

================================================
13. AI LIMITATIONS
================================================

- AI agents CANNOT:
  - Bypass scoring
  - Bypass CRO
  - Force-activate a strategy
  - Override kill rules

- AI agents CAN:
  - Propose new strategies
  - Propose improved variants
  - Propose parameter changes

Final authority ALWAYS belongs to:
- Risk Engine
- CRO
- This policy

================================================
14. NON-NEGOTIABLE RULE
================================================

> Profit NEVER justifies loss of control.

Any component violating this principle
is considered a system failure.

================================================
END OF STRATEGY GOVERNANCE CONSTITUTION
================================================