import java.util.Scanner;

public class Main {
    public static long fibo(int n) {
        long[] fiboarray = new long[n+1];
        fiboarray[0] = 1;
        fiboarray[1] = 1;
        for (int i=2; i<=n-1; i++) {
            fiboarray[i] = fiboarray[i-1]+fiboarray[i-2];
        }
        return fiboarray[n-1];
    }
    public static void main (String args[]) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        long ans = fibo(n);
        System.out.println(ans);
    }
    
}
