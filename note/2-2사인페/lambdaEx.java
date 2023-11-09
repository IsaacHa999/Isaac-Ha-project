// Lambda: functional expression 함수로 취급해준다. 식!
public class View {
    @FunctionalInterface
    public interface OnClickListener {
        public void onClick(View v);
    }
}

/// setOnclickListerner은 onClick를 실행시키는 함수
MainActivity {
    onCreate() {
        ...
        /////onClickListener객체가 인수로 들어오고 onClick메서드가 실행된다.
        btn .setOnclickListerner(View.OnClickListener listener);

        // Ananymous Class  ///onClickListener객체가 생성되고 onClick메서드가 실행된다.
        btn .setOnclickListerner(new View.OnClickListener() {
            @override
            public void onClick(View v) {
                this // View.OnClickListener 타입 // 왜냐하면 내부 클래스이므로 익명 클래스 객체로 해석
                MainActivity.this //MainActivity 타입
                getApplicationContext() /// MainActivity 것!
                ...
            }
        });

        //Lambda: 람다는 하나의 식이다. ///onClickListener객체가 생성되고 onClick메서드가 실행된다.
        btn .setOnclickListerner( v -> {
                this    //MainActivity를 가르킨다!
                ...
            }
        );
        

    }
}

