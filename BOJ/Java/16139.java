import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String target = br.readLine();
        int n = Integer.parseInt(br.readLine());
        int[][] prefix_sum = new int[26][target.length()];
        prefix_sum[target.charAt(0)-'a'][0] += 1;

        for(int i = 1; i<target.length();i++){
            int curr = target.charAt(i);

            for (int j=0;j<26;j++){
                prefix_sum[j][i]=prefix_sum[j][i-1];
            }
            prefix_sum[curr-'a'][i] += 1 ;
        }
        StringBuilder sb = new StringBuilder();

        for (int i=0;i<n;i++){
            StringTokenizer st= new StringTokenizer(br.readLine());
            char t = st.nextToken().charAt(0);
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            if (start==0) sb.append(prefix_sum[t-'a'][end]).append('\n');
            else sb.append(prefix_sum[t-'a'][end]-prefix_sum[t-'a'][start-1]).append('\n'); 
        }
        System.out.println(sb);
    }
}