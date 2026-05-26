import argparse

from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG


def build_config():
    config = DEFAULT_CONFIG.copy()

    # Keep env overrides from .env, but force lite behavior here.
    config["max_debate_rounds"] = 1
    config["max_risk_rounds"] = 1

    return config


def main():
    parser = argparse.ArgumentParser(description="MAMUYY Hunter Lite Mode")
    parser.add_argument("--ticker", default="NVDA", help="Ticker symbol, contoh: NVDA")
    parser.add_argument("--date", default="2024-05-10", help="Tanggal analisis YYYY-MM-DD")
    args = parser.parse_args()

    config = build_config()

    # Lite mode: market analyst only.
    # This reduces analyst calls compared with full mode.
    ta = TradingAgentsGraph(
        selected_analysts=["market"],
        debug=False,
        config=config,
    )

    _, decision = ta.propagate(args.ticker.upper(), args.date)

    print("\n==============================")
    print("MAMUYY HUNTER LITE RESULT")
    print("==============================")
    print(f"Ticker : {args.ticker.upper()}")
    print(f"Date   : {args.date}")
    print("------------------------------")
    print(decision)


if __name__ == "__main__":
    main()
