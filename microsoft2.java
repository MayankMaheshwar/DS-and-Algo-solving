import java.util.*
// you can also use imports, for example:
// import java.util.*

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message")


class Solution {
    public boolean solution(int N, int[] A, int[] B) {
        // write your code in Java SE 8
        Set < String > edges = new HashSet <> (N)
        for (int i=0
             i < A.length
             i++) {
            int lo = Math.min(A[i], B[i])
            int hi = Math.max(A[i], B[i])
            edges.add("" + lo + "-" + hi)
        }

        for (int i=1
             i < N
             i++) {
            if (! edges.contains("" + i + "-" + (i+1))) {
                return false
            }
        }
        return true
    }
}
