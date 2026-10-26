# 05 · Best Time to Buy and Sell Stock (Easy) · Sliding Window

Valid Palindrome was the only easy problem in Two Pointers, so today we move on to the next section, **Sliding Window**. This one is a classic, and it builds right on the "walk through the list once" idea from last time.

## The problem, in plain words
You get a list `prices`, where `prices[i]` is the price of a stock on day `i`. You can buy on one day and sell on a **later** day, just once. What's the most profit you can make? If there's no way to make money, return `0`.

- `[7, 1, 5, 3, 6, 4]` → `5` (buy at 1 on day 1, sell at 6 on day 4)
- `[7, 6, 4, 3, 1]` → `0` (the price only goes down, so don't trade at all)

Note: you can't sell before you buy. In the first example, buying at 1 and "selling" at 7 isn't allowed, because the 7 came first.

## Beginner-friendly hint
Walk through the prices one day at a time and keep track of the **cheapest price you've seen so far**. On each day, ask: "If I sold today, having bought at that cheapest price, how much would I make?" Keep the biggest answer.

## Key concept: sliding window (and "remember the best so far")
A sliding window is a range of the list, with a left edge and a right edge, that moves forward as you go. Here:
- the **left** edge is your buy day (the cheapest day so far),
- the **right** edge is today, your possible sell day.

If today's price is lower than your buy price, there's no point keeping the old buy day. Slide the left edge up to today. Otherwise, check the profit `prices[right] - prices[left]`.

```python
prices = [3, 8, 2, 9]
lowest = prices[0]
for price in prices:
    lowest = min(lowest, price)
    print(price, "lowest so far:", lowest)
```

That one pass gives you **O(n)** time and **O(1)** extra space. The slow way, trying every buy day with every later sell day, is O(n²), which gets painfully slow on big lists.

### Connecting back to hash maps
No dictionary today either. A hash map helps when you need to remember *lots* of things you've seen (like every number in Two Sum). Here you only need to remember *one* thing: the lowest price. When one variable is enough, you don't need a dictionary.

## How to run
```bash
python solution.py
```
