// 배열의 복사
// Java에서 배열을 복사하는 방법에는 크게 두 가지가 있습니다.

// 1. System.arraycopy() 메서드를 사용하는 방법
// 2. Arrays 클래스의 copyOf() 메서드 또는 copyOfRange() 메서드를 사용하는 방법

System.arraycopy(elements, 0, data, manyItems, elements.length); 
    
    int[] source = {1, 2, 3, 4, 5};
    int[] destination = new int[5];

    // source 배열의 요소를 destination 배열로 복사
    System.arraycopy(source, 0, destination, 0, source.length);

    // 복사된 배열의 값 출력
    System.out.println(Arrays.toString(destination)); // [1, 2, 3, 4, 5]


import java.util.Random;

public class RandomExample {
    public static void main(String[] args) {
        Random random = new Random();

        // 0 이상 1 미만의 랜덤한 실수 값 생성
        double randomValue = random.nextDouble();


