#include<iostream>
#include<stack>

using namespace std;

int input_data[8] ={9,1,2,0,3,2,5,0};

class My_stack{
    public:
    //Q1) 스택 선언 : stack<자료형> 스택 이름;
    stack<int> st;
    My_stack(){
        cout<<"my stack"<<endl;
        //Q2) 스택에 데이터 입력. push()함수 사용
        for (int i = 0; i < 8; ++i) {
            st.push(input_data[i]);
        }
    }

    //Q3) 스택의 데이터 출력과 삭제

    void flush(){
        //while() 문 안에 스택이 비어있는지를 확인하는 empty 함수사용
        //스택의 최상단 데이터 출력. top()을 사용
        //스택의 최상단 데이터 삭제. pop()을 사용
        while(!st.empty()) {
            cout<<st.top() << " ";
            st.pop();
        }
        cout<<endl;
    }


};

class Example_stack{
    public:
    // 스택 선언. stack<자료형> 스택이름;
    stack<int> st;
    Example_stack(){
        cout<< "Example stack"<<endl;
        for(int i = 0; i < 8; ++i){
            //스택에 데이터를 넣을때는 push()함수를 이용한다.
            st.push(input_data[i]);    
        }
    }
    
    void check(){
        //스택이 비어있으면, st.empty()는 true를 반환한다.
        if(st.empty()) cout<<"emtpy stack"<<endl;
        else cout<<"stack is not empty"<<endl;
    }
    void print_st(){
        while(!st.empty()){// 스택이 비어있지 않다면,
            cout<<st.top()<<" "; //가장 최근에 들어온 데이터(top)을 출력하고,
            st.pop();// 그것을 삭제한다.
        }
        cout<<endl;
    }

};


int main(){
    //=== 예시 ===
    Example_stack example;
    example.print_st();

    //=== 본인이 작성한 스택 클래스 ===
    
    
    My_stack myStack;
    myStack.flush();
    
    


    return 0;
}