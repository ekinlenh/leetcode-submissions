class Solution {
    public int maxProfit(int[] prices) {
        
        int buyPrice = prices[0];
        int maxProfit = 0;

        for (int i = 0; i < prices.length - 1; i++) {
            int sellPrice = prices[i + 1];
            if (prices[i] < buyPrice) {
                buyPrice = prices[i];
            }

            maxProfit = Math.max(sellPrice - buyPrice, maxProfit);
        }

        return maxProfit;
    }
}
