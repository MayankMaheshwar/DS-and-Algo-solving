
import java.util.*;
class Solution {
    public int solution(int[] A) {
    Map<Integer, Integer> indexs = new HashMap<>();
    int prev = 0;
    int count = 0;
    for (int i = 1; i < A.length; i++) {
        int s = A[i - 1] + A[i];
        if (s == prev && count > 0) {
            count--;
            continue;
        }
        prev = s;
        count++;
        indexs.put(s, indexs.getOrDefault(s, 0) + 1);
    }

    return indexs.values().stream().mapToInt(k -> k).max().getAsInt();
}
}
