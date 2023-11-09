//
interface Predator {
    (... 생략 ...)
}

//
interface Barkable {
    void bark();
}

class Animal {
    (... 생략 ...)
}

class Tiger extends Animal implements Predator, Barkable {
    public String getFood() {
        return "apple";
    }

    public void bark() {
        System.out.println("어흥");
    }
}

class Lion extends Animal implements Predator, Barkable {
    public String getFood() {
        return "banana";
    }

    public void bark() {
        System.out.println("으르렁");
    }
}

class ZooKeeper {
    (... 생략 ...)
}

class Bouncer {
    void barkAnimal(Barkable animal) {  // Animal 대신 Barkable을 사용
        animal.bark();
    }
}

public class Sample {
    (... 생략 ...)
}


// 바뀌기 전
void barkAnimal(Animal animal) {
    if (animal instanceof Tiger) {
        System.out.println("어흥");
    } else if (animal instanceof Lion) {
        System.out.println("으르렁");
    }
}

// 바꾼 후
void barkAnimal(Barkable animal) {
    animal.bark();
}