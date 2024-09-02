import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
        
		Scanner sc = new Scanner(System.in); // 입력 받기 위해서

		int n = sc.nextInt(); // 입력받을 사람의 수 (n) 을 저장
		HashMap<String, String> map = new HashMap<String, String>(); // 이름과 상태를 저장할 HashMap 생성

		// n명의 사람 정보를 입력받는 루프
		for (int i = 0; i < n; i++) {
            
			String name = sc.next(); // 이름을 입력받음
			String state = sc.next(); // 상태(입장 또는 퇴장)를 입력받음

			// 이름이 이미 맵에 존재하는지 확인
			if (map.containsKey(name)) {
				map.remove(name); // 이미 존재한다면 맵에서 제거 (퇴장)
			} else {
				map.put(name, state); // 존재하지 않는다면 맵에 추가 (입장)
			}
		}

		// 현재 맵에 남아있는 키(이름)들을 리스트에 담음
		ArrayList<String> list = new ArrayList<String>(map.keySet());
        
		// 리스트(내림차순) 정렬
		Collections.sort(list, Collections.reverseOrder());
		
		// 출력
		for(var li : list) {
			System.out.print(li + " ");
		}
	}
}
