package com.example.lab10modi;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;

import com.example.lab10modi.databinding.ActivityDialog1Binding;
import com.example.lab10modi.databinding.ActivitySecondBinding;

public class SecondActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {    //onCreate가 실행--> 이미 인텐트를 받았다.
        super.onCreate(savedInstanceState);
        ActivitySecondBinding binding = ActivitySecondBinding.inflate(getLayoutInflater());
        setContentView(binding.getRoot());

        binding.textViewFromMainActivity.setText(getIntent().getStringExtra("extra")); //키값     //문자열 리턴!

        binding.finishButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                finish();   //액티비티의 메서드 resumed 상태에서 --> finish() backButton과 같은 효과!
            }
        });

        binding.finishWithResultButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                //결과를 mainActivity에 반환 하는 함수 setResult
                setResult(RESULT_OK, new Intent().putExtra("result","from second activity"));    //result data intent!
                //setResult 는 생명주기 함수 안에서 호출하면x, 외부(프레임워크)에 전달x, 액티비티가 가지고 있음 전달은 finish()에서 전달
                //resumed 상태에서 setResult를 호출
                finish();   //액티비티의 메서드 resumed 상태에서 --> finish() backButton과 같은 효과!
            }
        });

        binding.finishWithForwardResultButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(new Intent(SecondActivity.this, ThirdActivity.class))
                        .putExtra("extra", "from main activity").addFlags(Intent.FLAG_ACTIVITY_FORWARD_RESULT));

            }
        });
    }
}