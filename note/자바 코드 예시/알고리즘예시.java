// Linear Search
public static int linearSearch(int[] arr, int target) {
    for (int i = 0; i < arr.length; i++) {
        if (arr[i] == target) {
            return i;
        }
    }
    return -1; // 타겟이 배열에 없는 경우 -1을 리턴합니다.
}
