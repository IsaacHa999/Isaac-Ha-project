//Hello World
public class Main {
    public static void main(String[] args) {
       System. out.println("Hello World" );
    }
}

//자바 기본 데이터 타입
public class Main {
    public static void main(String[] args) {
        /* 기본 데이터 타입 */
        int i = 1;
        float f = 1.1f;
        double d = 1.2;
        boolean b = true;
        char c = 'a';
        System. out.println(i );
        System. out.println(f );
        System. out.println( d);
        System. out.println(b );
        System. out.println(c );
    }
}

// 자바 레퍼런스 데이터 타입
public class Main {
       public static void main(String[] args) {
             /* 레퍼런스 데이터 타입 */
       Integer i = 1;
       Float f = 1.1f;
       Double d = 1.2;
       Boolean b = true;
       Character c = 'a';
       String s = "Hello World";
       System. out.println( i);
       System. out.println( f);
       System. out.println( d);
       System. out.println( b);
       System. out.println( c);
       System. out.println(s );
      }
}


// 자바 배열 선언
public class Main {
       public static void main(String[] args) {
             /* 배열 선언 */
       int[] arr = {1,2,3,4};
       System. out.println(arr .getClass());
      }
}

// 비정방형 배열
public class Main {
    public static void main(String[] args) {
        int intArray[][] = new int[4][];
        intArray[0] = new int[3];
        intArray[1] = new int[2];
        intArray[2] = new int [3];
        intArray[3] = new int[2];

        for (int i = 0; i < intArray.length; i++)
            for (int j = 0; j < intArray[i].length; j++)
                intArray[i][j] = (i+1)*10 + j;

        for (int i = 0; i <intArray.length; i++) {
            for (int j =0 ; j < intArray[i].length; j++)
                System.out.print(intArray[i][j] + " " );
            System.out.println();
        }
    }
}

// 자바 배열 사용
import java.lang.reflect.Array;

public class Main {
       public static void main(String[] args) {
       /* Array */
       Integer[] a = {1,2,3,4}; // Array Type
       //Integer a[] = {1,2,3,4}; // Array Type
       System.out.println(a );
       System.out.println(a [1]);
      }
}

// 자바 List 클래스 사용
import java.util.ArrayList;

public class Main {
       public static void main(String[] args) {
             /* List */
       ArrayList a = new ArrayList();
       a.add(1);
       a.add(2);
       a.add("Hello");
       System. out.println(a );
      }
}

// 자바 Generics 사용
import java.util.ArrayList;

public class Main {
       public static void main(String[] args) {
             /* Generics */
       ArrayList<String> list = new ArrayList<String>();
       list.add("Hello" );
       list.add("Hello" );
       //list.add(123); // Error
      }
}

// 자바 Map 사용
import java.util.HashMap;

public class Main {
       public static void main(String[] args) {
             /* Map */
       HashMap<String, Integer> map = new HashMap<String, Integer>();
       // HashMap<String, int> map = new HashMap<String, int >(); // Error
       map.put("one" , 1);
       map.put("two" , 2);
       System. out.println(map .get("one"));
       System. out.println(map .get("three")); // null
       //System.out.println(map.containsKey("three"));
       //System.out.println(map.remove("one"));
       //System.out.println(map.get("one"));
       //System.out.println(map.size());
      }
}

// 자바 if ~ else 문 사용
public class Main {
       public static void main(String[] args) {
             /* if ~ else 1 */
       boolean b = true;
       if(b == true){
              System. out.println("변수 b는 true 입니다." );
       } else{
              System. out.println("변수 b는 false 입니다." );
       }
      }
}

// 자바 if ~ else 문 중첩 사용
public class Main {
       public static void main(String[] args) {
             /* if ~ else 2 */
       int i = 3;
      
       if(i == 1){
              System. out.println("변수 i는 1 입니다." );
       } else if (i == 2){
              System. out.println("변수 i는 2입니다." );
       } else if (i == 3){
              System. out.println("변수 i는 3입니다." );
       } else{
              System. out.println("변수 1,2,3이 아닌 값입니다." );
       }
      }
}



// 자바 switch ~ case 문 사용
public class Main {
       public static void main(String[] args) {
             /* switch case */
       int i = 3;
      
       switch(i ){
       case 1:
              System. out.println("변수 i는 1 입니다." );
              break;
       case 2:
              System. out.println("변수 i는 2입니다." );
              break;
       case 3:
              System. out.println("변수 i는 3입니다." );
              break;
       default:
              System. out.println("변수 1,2,3이 아닌 값입니다." );
              break;
       }
      }
}

// 자바 while 반복문 사용
public class Main {
       public static void main(String[] args) {
             /* While */
       int i = 0;
      
       while(i < 5){
              i = i + 1;
              //i++;
              //i += 1;
              System. out.println(i );
       }
      }
}


// 자바 for 반복문 사용
public class Main {
       public static void main(String[] args) {
             /* for */
       int i ;
      
       for(i = 0; i < 5; i++){
              System. out.println(i );
       }
      }
}


// 자바 for 반복문을 활용한 배열 순회
public class Main {
       public static void main(String[] args) {
             /* for을 활용한 배열 순환*/
       String[] numbers = {"one" , "two" , "three" };
       for( int i =0; i<numbers.length; i++) {
           System. out.println(numbers [i ]);
       }
      }
}


// 자바 for ~ each 문을 활용한 배열 순회
public class Main {
       public static void main(String[] args) {
             /* for..each 을 활용한 배열 순환*/
       String[] numbers = {"one" , "two" , "three" };
       for(String number : numbers ) {
           System. out.println(number );
       }
      }
}


// 자바 for 반복문과 continue 
public class Main {
       public static void main(String[] args) {
       int i ;
      
       for(i = 0; i < 5; i++){
              if(i == 3){
                    continue;
              }
              System. out.println(i );
       }
      }
}

// 자바 while 반복문과 continue 
public class Main {
       public static void main(String[] args) {
             int i = 0;
         while(i < 5){
                if(i == 3){
                      continue;
                }
                System. out.println(i );
                i++;
         }
      }
}


// 자바 for 반복문과 break
public class Main {
       public static void main(String[] args) {
             /* 반복문과 break */
       int i ;
       for(i = 0; i < 5; i++){
              if(i == 3){
                    break;
              }
              System. out.println(i );
       }
      }
}

// 자바 while 반복문과 break
public class Main {
       public static void main(String[] args) {
             /* While 문 기반 break */
             int i = 0;
         while(i < 5){
                if(i == 3){
                      break;
                }
                System.out.println( i);
                i++;
         }
      }
}