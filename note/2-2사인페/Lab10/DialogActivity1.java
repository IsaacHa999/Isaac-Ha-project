package com.example.lab10modi;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;

import com.example.lab10modi.databinding.ActivityDialog1Binding;

public class DialogActivity1 extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        ActivityDialog1Binding binding = ActivityDialog1Binding.inflate(getLayoutInflater());
        setContentView(binding.getRoot());

        binding.finishButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                finish();   //액티비티의 메서드 resumed 상태에서 --> finish() backButton과 같은 효과!
            }
        });
    }
}