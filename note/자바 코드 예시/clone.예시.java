/* 
clnoe의 깊은 복사와 얕은 복사 확인
1. clone 메서드를 사용하면 일차적으로 깊은 복사가 된는 것이 맞다.
단, 객체 내부의 refernce 값은 같은 대상을 가르킨다(얕은 복사)!!
2. 따라서 객체 내부의 refernce 값도 깊은 복사를 해야 하는 경우가 생긴다. (overide 구현)

헷: clone은 무조건 메모리 공간을 새롭게 할당하는게 맞는데, reference 주소값도 그대로 복사하므로 내부적으로는 얕은 복사가 수행된다.

*/

class Circle implements Cloneable {
    Point p; //원점
    double r; // 반지름
 
    Circle(Point p, double r){
        this.p = p;
        this.r = r;
    }
 
    public Circle shallowCopy() {    // 얕은 복사
        Object obj = null;
        try {
            obj = super.clone();
        } catch (CloneNotSupportedException e) {}
        return (Circle)obj;
    }
 
    public Circle deepCopy() {    // 깊은 복사
        Object obj = null;
        try {
            obj = super.clone();
        }catch (CloneNotSupportedException e) {}
        Circle c= (Circle)obj;
        c.p = new Point(this.p.x, this.p.y);
        return c;
    }
 
    public String toString() {
        return "p= " + p + " / r= " +r;
    }
}
 
class Point{
    int x, y;
 
    Point(int x, int y){
        this.x = x;
        this.y = y;
    }
 
    @Override
    public String toString() {
        return "("+x+", "+y+")";
    }
}
 
public class ShallowDeepCopy {
    public static void main(String[] args) {
        Circle c1 = new Circle(new Point(1, 1), 2.0); 
        Circle c2 = c1.shallowCopy(); // 얕은 복사
        Circle c3 = c1.deepCopy();      // 깊은 복사
 
        System.out.println("c1 : " + c1);
        System.out.println("c2 : " + c2);
        System.out.println("c3 : " + c3);
 
        c1.p.x = 9;
        c1.p.y = 9;
        System.out.println("c1의 변경 후");
        System.out.println("c1 : " + c1);
        System.out.println("c2 : " + c2);
        System.out.println("c3 : " + c3);
    }
}