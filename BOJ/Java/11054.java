import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int[] arr;
    static int[][] dp;
    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        arr = new int[n];
        dp = new int[n][2];
        for (int i = 0; i<n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        
        dp[0][0] = 0;
        dp[n-1][1] = 0;

        for (int j = 0; j<n; j++) {
            for (int k = 0; k<j; k++) {
                if (arr[j]>arr[k]) {
                    dp[j][0] = Math.max(dp[j][0],dp[k][0]+1);
                }
            }
        }

        for (int j = n-2; j>=0; j--) {
            for (int k = n-1; k>j; k--) {
                if (arr[j]>arr[k]) {
                    dp[j][1] = Math.max(dp[j][1],dp[k][1]+1);
                }

            }
        }

        int ans = 0 ;
        for (int i = 0; i<n ; i++) {
            int sum = dp[i][0]+dp[i][1];
            if (ans< sum) {
                ans = sum;
            }
        }

        System.out.println(ans+1);
    }
}