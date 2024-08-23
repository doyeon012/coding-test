import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt(); 
		
		int array1[] = new int[n];
		
		for(int i=0;i<array1.length;i++) {
			array1[i] = sc.nextInt();
		}
		
		sc.close();
		
		int min = array1[0];
		int max = array1[0];
		
		for(int i=0;i<array1.length;i++) {
			if(min>array1[i]) min = array1[i];
			if(max<array1[i]) max = array1[i];
		}
		System.out.println(min+" "+max);
		
	}
}