public class Main {
    public static void main(String[] args) {
        System.out.println("Hello world!");
        Sorting selection = new Sorting();
        selection.Selection_Sort();

    }
}

class Sorting {
    // Insertion Sort, Selection Sort, Merge Sort, Quick Sort
    private int[] arrInt = {22, 14, 1, 10, 29, 19, 6, 4, 30, 18, 27, 9, 20, 21, 24, 16, 26, 11, 3, 5, 13, 7, 31, 17, 8, 2, 23, 15, 28, 0, 25, 12};


    void Selection_Sort() {
        int max = 0, temp = 0, target = 0;

        for (int i = 0; i < arrInt.length; i++) {
            //max 값 찾기
            max = arrInt[0];
            for (int j = 0; j < arrInt.length - i; j++) {
                if (max < arrInt[j]) {
                    max = arrInt[j];
                    target = j;
                }
            }
            //swap
            temp = arrInt[arrInt.length-1-i];
            arrInt[arrInt.length-1-i] = arrInt[target];
            arrInt[target] = temp;
        }
        //출력
        for(int i = 0; i < arrInt.length; i++)
            System.out.print(arrInt[i]+ " ");
        System.out.println();
    }
}