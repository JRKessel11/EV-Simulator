import random

prob_win = 0.65
win_amount = 2
loss_amount = 1
trials = 10000

theoretical_ev = prob_win * win_amount - (1 - prob_win) * loss_amount

equity = 0
peak = 0
max_drawdown = 0
wins = 0

for _ in range (trials):

    if random.random() < prob_win:
        equity += win_amount
        wins += 1
    else:
        equity -= loss_amount

    if equity > peak:
        peak = equity
    
    drawdown = peak - equity

    if drawdown > max_drawdown:
        max_drawdown = drawdown

simulated_ev = equity / trials
win_rate = wins / trials

print("EV SIMULATOR")
print(f"prob win: {prob_win:.2f}")
print(f"Win/Loss: +{win_amount} / -{loss_amount}")
print(f"Trials: {trials}")
print(f"Theoretical EV per trade: {theoretical_ev:.4f}")
print(f"Simulated EV per trade: {simulated_ev:.4f}")
print(f"Total profit: {equity}")
print(f"Simulated win rate: {win_rate:.4f}")
print(f"Max drawdown: {max_drawdown}")
