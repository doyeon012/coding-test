import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        
        Scanner scanner = new Scanner(System.in);
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        // 초기 테스트 케이스 입력
        int t = scanner.nextInt();

        for (int h = 0; h < t; h++) {

            // 입력
            int a = scanner.nextInt();
            int b = scanner.nextInt();

            // a와 b 중 더 작은 값과 큰 값을 구함
            int min = a > b ? b : a; // 작은 수
            int max = a > b ? a : b; // 큰 수

            int res = 0; // 최소 공배수를 저장
            int x = 0; // 최대 공약수를 구하는 과정 -> 나머지를 저장할 변수
            
            // 최대 공약수를 구하는 반복문 (유클리드 호제법)
            for (int i = 0; i < 9999; i++) {
                
                x = max % min; // max를 min으로 나눈 나머지를 x에 저장
                max = min; // max에 min의 값을 할당 (다음 반복에서 min으로 비교)
                
                if (x == 0) { // 나머지가 0이 되면 최대 공약수를 찾음
                    res = (a * b) / min; // 최소 공배수는 두 수의 곱을 최대 공약수로 나눈 값
                    break; 
                }
                min = x; // 나머지 값을 min에 할당 (다음 반복에서 사용)
            }
            
            // 계산된 최소 공배수 출력
            bw.write(res + "\n");
        }

        // 버퍼에 남아 있는 데이터를 출력, BufferedWriter를 닫음
        bw.flush();
        bw.close();
    }
}
