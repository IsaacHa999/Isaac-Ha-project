package com.example.lab10modi;

import androidx.activity.result.ActivityResult;
import androidx.activity.result.ActivityResultCallback;
import androidx.activity.result.ActivityResultLauncher;
import androidx.activity.result.contract.ActivityResultContracts;
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.res.Configuration;
import android.os.Bundle;
import android.util.Log;
import android.view.View;

import com.example.lab10modi.databinding.ActivityMainBinding;

public class MainActivity extends AppCompatActivity {
    private ActivityMainBinding binding;    //onCreate 외 다른 함수에서 binding를 사용하려고

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        Log.d("isaac", "onCreate()");

        String isNull = (savedInstanceState == null) ? "bundle is null" : "buㅇdle is ot null";
        super.onCreate(savedInstanceState);binding = ActivityMainBinding.inflate(getLayoutInflater());
        setContentView(binding.getRoot());

        //액티비티를 띄우고, 데이터를 보내고, 다시 받는데 일반화된 방식으로 한다 매개변수(리스너가 어떤 종류의 일인지 ,리스너)
        ActivityResultLauncher<Intent> launcher = registerForActivityResult(new ActivityResultContracts.StartActivityForResult(),
                new ActivityResultCallback<ActivityResult>() {
                    @Override
                    public void onActivityResult(ActivityResult o) {    //o.getData()가 인텐트
                        Log.d("isaac", "onActivityResult()-callback");
                        if (o.getResultCode() == RESULT_OK)
                            binding.resultFromSecondActivityTextView.setText(o.getData().getStringExtra("result"));
                    }
                });  //등록해야함

        binding.toDialogActivityButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(MainActivity.this, DialogActivity1.class));
            }
        });

        binding.toSecondActivityButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(new Intent(MainActivity.this, SecondActivity.class));
                intent.putExtra("extra", "from main activity");  //키와 벨류 형식으로
                startActivity(intent);
            }
        });

        binding.toSecondActivityForResultButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                //쓰지말라는 표시 --> 콜백(리스너) 형태로 바꿔주자!!
//                startActivityForResult(new Intent(new Intent(MainActivity.this, SecondActivity.class))
//                        .putExtra("extra", "from main activity"),1000);
                launcher.launch(new Intent(new Intent(MainActivity.this, SecondActivity.class))
                        .putExtra("extra", "from main activity")
                        .addFlags(Intent.FLAG_ACTIVITY_NO_HISTORY));
                        //.addFlags(Intent.FLAG_ACTIVITY_FORWARD_RESULT));  //startactivityresult와 같은 효과 : 다른 액태비티가 뜬다
            }
        });
    }

    //데이터를 전달 받는 함수

    //전체를 주석처리해도 돈다 == 부모인 AppCompatActivity의 onActivityResult()는 호출된다.(오버라이드는x)
    @Override   //데이터가 전달될 때 호출되는 메서드 결과값도 인텐트로 만들어 돌려준다
    protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
        Log.d("isaac", "onActivityResult()");
        super.onActivityResult(requestCode, resultCode, data);

        if(requestCode == 1000 && resultCode == RESULT_OK) {
            binding.resultFromSecondActivityTextView.setText(data.getStringExtra("result"));
            data.getStringExtra("resut");
        }
    }

    @Override
    protected void onStart() {
        Log.d("isaac", "onStart()");
        super.onStart();
    }

    @Override
    protected void onResume() {
        Log.d("isaac","onResume()");
        super.onResume();
    }

    @Override
    protected void onPause() {
        Log.d("isaac","onPause()");
        super.onPause();
    }

    @Override
    protected void onStop() {
        Log.d("isaac","onStop()");
        super.onStop();
    }

    @Override
    protected void onDestroy() {
        Log.d("isaac","onDestroy()");
        super.onDestroy();
    }

    @Override
    protected void onSaveInstanceState(@NonNull Bundle outState) {  //번들이 자료구조(map)임
        Log.d("isaac", "onSaveInstanceState");
        super.onSaveInstanceState(outState);

        outState.putString("save", binding.sampleEditText.getText().toString());
    }

    @Override
    protected void onRestoreInstanceState(@NonNull Bundle savedInstanceState) {
        Log.d("isaac", "onRestoreInstanceState()");
        super.onRestoreInstanceState(savedInstanceState);

        binding.sampleEditText.setText(savedInstanceState.getString("save"));

    }

    @Override
    public void onConfigurationChanged(@NonNull Configuration newConfig) {
        Log.d("isaac", "onConfigurationChanged()");
        super.onConfigurationChanged(newConfig);
    }
}