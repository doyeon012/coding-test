import java.util.Scanner; // 사용자 입력을 받기 위한 Scanner 클래스 import

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in); // 사용자 입력을 받기 위한 Scanner 객체 생성
        
        // 사용자로부터 x, y, w, h 값을 입력받음
        int x = sc.nextInt(); // 현재 위치의 x좌표
        int y = sc.nextInt(); // 현재 위치의 y좌표
        int w = sc.nextInt(); // 직사각형의 너비
        int h = sc.nextInt(); // 직사각형의 높이

        // 각 변까지의 거리를 저장할 배열 생성
        int[] distances = new int[4];
        distances[0] = x;            // 왼쪽 변까지의 거리
        distances[1] = y;            // 아래쪽 변까지의 거리
        distances[2] = w - x;        // 오른쪽 변까지의 거리
        distances[3] = h - y;        // 위쪽 변까지의 거리

        // 최소 거리를 찾기 위해 초기값을 distances[0]으로 설정
        int min = distances[0];

        // 배열을 순회하며 최소 거리 찾기
        for (int distance : distances) {
            if (distance < min) min = distance;
        }

        // 최소 거리 출력
        System.out.println(min);
    }
}