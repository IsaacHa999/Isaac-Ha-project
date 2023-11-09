package com.example.test7;

import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import android.content.DialogInterface;
import android.os.Bundle;
import android.widget.Toast;

import com.example.test7.databinding.ActivityMainBinding;

public class MainActivity extends AppCompatActivity {
    ActivityMainBinding binding;

    //
    AlertDialog alertDialog;
    AlertDialog listDialog;
    AlertDialog customDialog;

    //
    private void showToast(String message) {
        Toast toast =  Toast.makeText(this, message, Toast.LENGTH_SHORT);
        toast.show();
    }

    //Dialog 버튼 이벤트 처리
    DialogInterface.OnClickListener dialogListener = new DialogInterface.OnClickListener() {
        @Override
        public void onClick(DialogInterface dialog, int which) {
            if(dialog ==customDialog && which == DialogInterface.BUTTON_POSITIVE) {
                showToast("custom dialog 확인 click");
            } else if (dialog == listDialog) {
                String[] datas = getResources().getStringArray(R.array.dialog_array);
                showToast(datas[which]+"선택 하셨습니다.");
            } else if (dialog == alertDialog && which == DialogInterface.BUTTON_POSITIVE) {
                showToast("alert dialog ok click");
            }
        }
    };

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        binding = ActivityMainBinding.inflate(getLayoutInflater());
        setContentView(binding.getRoot());

//        binding.alertButton.setOnClickListener(view -> {
//            //
//            AlertDialog.Builder builder = new AlertDialog.Builder(this);
//            builder.setTitle("알림");
//            builder.setMessage("정말 종료 하시겠습니까?");
//            builder.setPositiveButton("yes", dialogListener);
//            builder.setNegativeButton("NO",null);
//            alertDialog = builder.create();
//        });
    }
}