import random
import math
import matplotlib.pyplot as plt

prob_win = 0.55
win = 2
loss = 1
trades_per_run = 10000
runs = 200
start_equity = 0

def simulate_one_run(prob_win: float, win: float, loss: float, trades: int, start_equity: float = 0):

    equity = start_equity
    peak = equity
    max_drawdown = 0

    for _ in range(trades):
        if random.random() < prob_win:
            equity += win
        else:
            equity -= loss
        if equity > peak:
            peak = equity
        drawdown = peak - equity
        if drawdown > max_drawdown:
            max_drawdown = drawdown

    final_pnl = equity - start_equity
    return final_pnl, max_drawdown

def percentile (values, p: float):

    sorted_vals = sorted(values)
    if not sorted_vals:
        return None
    
    k = (len(sorted_vals) - 1) * (p / 100.0)
    f = math.floor(k)
    c = math.ceil(k)

    if f == c:
        return sorted_vals[int(k)]
    
    d0 = sorted_vals[f] * (c - k)
    d1 = sorted_vals[c] * (k - f)
    return d0 + d1
def main():
    ending_pnls = []
    max_dds = []

    for _ in range (runs):
        pnl, dd = simulate_one_run(prob_win, win, loss, trades_per_run, start_equity)
        ending_pnls.append(pnl)
        max_dds.append(dd)

    p5 = percentile(ending_pnls, 5)
    avg = sum(ending_pnls) / len(ending_pnls)

    print("--Day 9: Histogram of Outcomes--")
    print(f"Runs: {runs}")
    print(f"Trades per run: {trades_per_run}")
    print(f"Avg ending P&L: {avg:.2f}")
    print(f"5th percentile ending P&L: {p5:.2f}")
    print(f"avg max drawdown (per run): {sum(max_dds)/len(max_dds):.2f}")
    print(f"Worst max drawdown (per run): {max(max_dds):.2f}")

    plt.hist(ending_pnls, bins=25)
    plt.title("Distribution of Ending P&L (200 runs)")
    plt.xlabel("Ending P&L")
    plt.ylabel("Frequency")
    plt.axvline(p5, linestyle="--", linewidth=2, label="5th percentile")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
