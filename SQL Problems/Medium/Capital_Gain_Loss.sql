-- LC#1393 - Capital Gain/Loss
-- Difficulty: Medium
-- Topics: SQL, GROUP BY, CASE WHEN
--
-- Approach: For each stock, sum prices with sign:
--           Sell → +price, Buy → -price.
--           GROUP BY stock_name gives net gain/loss.
--
-- ML Connection: Signed aggregation mirrors reward
-- calculation in reinforcement learning where buy/sell
-- actions have positive/negative rewards summed per episode.

SELECT stock_name,
       SUM(CASE WHEN operation = 'Sell' THEN price ELSE -price END) AS capital_gain_loss
FROM Stocks
GROUP BY stock_name;
