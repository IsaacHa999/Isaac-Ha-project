package com.example.lab10modi;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;

import com.example.lab10modi.databinding.ActivityThirdBinding;

public class ThirdActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        ActivityThirdBinding binding = ActivityThirdBinding.inflate(getLayoutInflater());
        setContentView(R.layout.activity_third);

        binding.finishWithResultButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                //결과를 mainActivity에 반환 하는 함수 setResult
                setResult(RESULT_OK, new Intent().putExtra("result","from third activity"));    //result data intent!
                //setResult 는 생명주기 함수 안에서 호출하면x, 외부(프레임워크)에 전달x, 액티비티가 가지고 있음 전달은 finish()에서 전달
                //resumed 상태에서 setResult를 호출
                finish();   //액티비티의 메서드 resumed 상태에서 --> finish() backButton과 같은 효과!
            }
        });
    }
}