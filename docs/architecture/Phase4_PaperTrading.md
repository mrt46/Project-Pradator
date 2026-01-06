================================================================================
PROJECT PREDATOR
PHASE 4 – PAPER TRADING ENGINE
ARCHITECTURE SPECIFICATION
================================================================================

Status: DESIGN LOCKED  
Purpose: First end-to-end trading simulation with ZERO real money risk  
Scope: Event flow, modules, data model, risk enforcement, strategy integration

================================================================================
0. PHASE 4 GOALS
================================================================================

Phase 4 introduces:

- Full trading loop:
  Market Data → Strategy → Risk → Execution → Portfolio → Performance
- BUT:
  - No real exchange
  - No real orders
  - No real money

Objectives:
- Validate system architecture
- Validate risk enforcement
- Validate strategy scoring integration
- Validate kill-switch logic
- Validate portfolio & PnL accounting

================================================================================
1. HIGH LEVEL FLOW
================================================================================

Fake / Historical Market Data
        ↓
Market Scanner Agent
        ↓
Strategy Pool
        ↓
Strategy Scoring Engine
        ↓
Strategy Selector
        ↓
CRO (Risk Governor - VETO)
        ↓
Paper Execution Engine
        ↓
Paper Portfolio & Position Manager
        ↓
Performance & Analytics
        ↓
Logs + Database

================================================================================
2. CORE MODULES
================================================================================

2.1 Market Data Provider
- Source:
  - CSV
  - Parquet
  - or API historical data
- Emits:
  - MARKET_TICK events

2.2 Strategy Engine
- Hosts:
  - Strategy Pool
  - Strategy interface
- Each strategy:
  - Receives ticks
  - Produces SIGNAL (BUY/SELL/HOLD)

2.3 Strategy Scoring Engine
- Periodically computes:
  - StrategyScore for each strategy
- Uses:
  - Performance history
  - Drawdown
  - Regime match
  - Stability
- Produces:
  - Strategy ranking
  - Enable / Disable / UnderReview decisions

2.4 Strategy Selector
- Chooses:
  - ONE active strategy (max two in special mode)
- Enforces:
  - StrategyGovernance.md rules

2.5 CRO – Risk Engine
- Receives:
  - Proposed trade
- Checks:
  - Position size
  - Daily drawdown
  - Strategy class rules
  - Kill-switch conditions
- Can:
  - APPROVE
  - REJECT
  - DISABLE STRATEGY
  - TRIGGER GLOBAL HALT

2.6 Paper Execution Engine
- Simulates:
  - Order fill
  - Slippage
  - Fees
- Produces:
  - FILLED_ORDER event

2.7 Portfolio & Position Manager
- Maintains:
  - Cash balance
  - Open positions
  - Unrealized PnL
  - Realized PnL
  - Equity curve

2.8 Performance & Analytics
- Computes:
  - PnL
  - Drawdown
  - Win rate
  - Sharpe (optional)
- Feeds:
  - Strategy Scoring Engine
  - Logs
  - Database

================================================================================
3. EVENT TYPES
================================================================================

- MARKET_TICK
- STRATEGY_SIGNAL
- TRADE_PROPOSAL
- TRADE_APPROVED
- TRADE_REJECTED
- ORDER_FILLED
- POSITION_UPDATED
- STRATEGY_DISABLED
- GLOBAL_HALT_TRIGGERED

================================================================================
4. DATA MODEL (LOGICAL)
================================================================================

4.1 Trade
- id
- strategy_id
- symbol
- side
- size
- entry_price
- exit_price
- pnl
- timestamp

4.2 Position
- symbol
- size
- avg_price
- unrealized_pnl

4.3 StrategyStats
- strategy_id
- total_trades
- win_rate
- profit_factor
- max_drawdown
- equity_curve

4.4 PortfolioSnapshot
- timestamp
- cash
- equity
- drawdown

================================================================================
5. RISK ENFORCEMENT POINTS
================================================================================

Risk is enforced at:

1. Before trade approval (CRO gate)
2. After each trade (update drawdown)
3. On portfolio level:
   - If daily DD > 5% → GLOBAL HALT
4. On strategy level:
   - If strategy violates envelope → STRATEGY DISABLED

NO MODULE may bypass CRO.

================================================================================
6. STRATEGY SCORING INTEGRATION
================================================================================

- Scoring runs:
  - Every N trades or
  - Every T minutes

- Outputs:
  - Score per strategy
  - Status changes:
    - ACTIVE
    - DISABLED
    - UNDER_REVIEW

- If strategy enters UNDER_REVIEW:
  → Event sent to Strategist MCP (later phase)

================================================================================
7. KILL-SWITCH LOGIC
================================================================================

7.1 GLOBAL
Triggered if:
- Portfolio DD > daily limit
- System instability

Effect:
- All trading stops
- System enters COOLDOWN mode

7.2 LOCAL
Triggered if:
- Strategy violates its own risk limits

Effect:
- Only that strategy is disabled
- System continues with others

================================================================================
8. MODES
================================================================================

- BACKTEST MODE:
  - Fast-forward historical data

- PAPER LIVE MODE:
  - Slow, real-time simulation

Both use SAME engine.

================================================================================
9. NON-GOALS OF PHASE 4
================================================================================

- No real exchange
- No real money
- No AI optimization
- No leverage (unless explicitly simulated)

================================================================================
10. SUCCESS CRITERIA
================================================================================

Phase 4 is SUCCESS if:

- System can:
  - Run for days
  - Simulate trades
  - Enforce risk
  - Kill bad strategies
  - Produce logs & stats

- No crashes
- No rule bypasses
- Deterministic behavior

================================================================================
11. PHASE 4 EXIT GATE
================================================================================

Before moving to Phase 5:

- At least 2–4 weeks paper run
- Stable operation
- No architecture changes
- Only bugfixes allowed

================================================================================
END OF PHASE 4 ARCHITECTURE
================================================================================