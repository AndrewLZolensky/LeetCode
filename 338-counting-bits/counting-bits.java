class Solution {
    public int[] countBits(int n) {
        int[] results = new int[n+1];
        int is_odd;
        int compare_index;
        for (int i = 0; i <=n ; i++) {
            if (i == 0) {
                results[i] = 0;
            } else {
                is_odd = i % 2;
                compare_index = (i - is_odd) / 2;
                results[i] = results[compare_index] + is_odd;
            }
        }

        return results;
    }
}