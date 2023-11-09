// 인터페이스 예제: 자료형 관리를 위해서!!!

interface Predator {
}

class Animal {
    String name;

    void setName(String name) {
        this.name = name;
    }
}

//
class Tiger extends Animal implements Predator {
}

class Lion extends Animal implements Predator {    
}

// 변경 전
class ZooKeeper {
    void feed(Tiger tiger) {
        System.out.println("feed apple");
    }

    void feed(Lion lion) {
        System.out.println("feed banana");
    }
}

// 변경 후: 자료형 선언이 편리해 진다!!!!
class ZooKeeper {
    void feed(Predator predator) {
        System.out.println("feed apple");
    }
}



