import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
public class Main {
    static long ans;
    static int min;
    static int n;
    static long[] cost;
    static long[] dist;

    public static void main(String args[]) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        dist = new long[n-1];
        cost = new long[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i<n-1;i++) {
            dist[i] = Long.parseLong(st.nextToken());
        }
        StringTokenizer st1 = new StringTokenizer(br.readLine());
        for (int i = 0; i<n; i++) {
            cost[i] = Long.parseLong(st1.nextToken());
        }
        min = 0;
        ans = 0;
        for (int i = 0; i<n; i++) {
            if (cost[i] < cost[min]) {
                min = i;
            }
            else {
                cost[i]=cost[min];
            }
        }
        for (int i = 0; i<n-1;i++) {
            ans += cost[i]*dist[i];
        }
        
        System.out.println(ans);
    }
}
