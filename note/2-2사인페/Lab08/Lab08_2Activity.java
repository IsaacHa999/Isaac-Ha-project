package com.foo.lab08;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;

public class Lab08_2Activity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_lab08_2);

        //androidx.fragment.app.FragmentManager
        //androidx.fragment.app.FragmentTransaction
        ///액티비티 메소드 리턴타입 FragmentManager(관리자) -> add, replace , remove 세 가지를 부탁할 수 있다[transaction]
        getSupportFragmentManager()
                .beginTransaction()
                .add(R.id.main_content, new OneFragment())
                .commit();      /// bigin ~ commit() 사이의 일들을 수행 / 물리적으로는 여려개 연산인데 논리적으로는 하나의 연산 = transaction
    }
}