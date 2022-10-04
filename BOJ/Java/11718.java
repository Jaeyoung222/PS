import java.io.BufferedReader;
import java.io.InputStreamReader;
public class Main {
    static String s;
    public static void main (String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while ((s = br.readLine())!=null){
            System.out.println(s);
        }
    }
}
    
