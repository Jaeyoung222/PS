import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String[] arr = new String[n];
        for (int i = 0; i<n; i++) {
            arr[i] = br.readLine();
        }
        
        Arrays.sort(arr);
        Arrays.sort(arr, (s1, s2) -> s1.length() - s2.length());
        
        for (int j=0; j<n; j++) {
            if(j!=n-1 && arr[j].equals(arr[j+1])) {
                continue;
            }
            else {
                System.out.println(arr[j]);
            }
        }
    }
}
