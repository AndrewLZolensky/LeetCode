class Solution {
    public int romanToInt(String s) {
        Map<Character, Integer> roman_values = new HashMap<>();
        roman_values.put('I', 1);
        roman_values.put('V', 5);
        roman_values.put('X', 10);
        roman_values.put('L', 50);
        roman_values.put('C', 100);
        roman_values.put('D', 500);
        roman_values.put('M', 1000);

        int count = 0;
        int curr = 0;
        int last = 0;

        for (int i = 0; i < s.length(); i++) {
            curr = roman_values.get(s.charAt(i));
            count += curr;
            if (curr > last) {
                count -= 2*last;
            }
            last = curr;
        }

        return count;
    }
}