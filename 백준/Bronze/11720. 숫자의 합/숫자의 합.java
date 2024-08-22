import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		String str = sc.next();
		int sum = 0;
		
		sc.close();
		
		for(int i=0;i<n;i++) {
			sum += str.charAt(i) - '0'; // 0이 아스키 코드의 48번째이기 때문에
		}
		
		System.out.println(sum);
	}

}