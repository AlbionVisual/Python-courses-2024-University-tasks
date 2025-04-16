import sys

def greedy_coin_change(coins, amount):
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        count += amount // coin
        amount %= coin
    return count if amount == 0 else float('inf')

def dp_coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else float('inf')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python coinchange.py <coins> <amount>")
        sys.exit(1)

    coins = [int(x) for x in sys.argv[1].split(',')]
    amount = int(sys.argv[2])

    print(f"greedy: {greedy_coin_change(coins, amount)}")
    print(f"dynamic: {dp_coin_change(coins, amount)}")
