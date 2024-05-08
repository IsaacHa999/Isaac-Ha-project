#include<iostream>
#include<queue>

using namespace std;

int input_data[8] = {1,1,0,9,1,1,1,2};

class My_queue{
    public:
    //Q1) 큐 선언 : queue<자료형> 큐 이름;
    queue<int> qu;
    My_queue(){
        cout<<"my queue"<<endl;
        //Q2) 큐에 데이터 입력. push()함수 사용
    }

    //Q3) 큐 데이터 출력과 삭제

    void flush(){
        //while() 문 안에 큐가 비어있는지를 확인하는 empty 함수사용
        //큐의 front 데이터 출력. front()을 사용
        //큐의 front 데이터 삭제. pop()을 사용
        while(!qu.empty()){// 큐가 비어있지 않다면,
            cout<<qu.front()<<" "; //가장 나중에 들어온 데이터(queue)을 출력하고,
            qu.pop();// 그것을 삭제한다.
        }
        cout<<endl;
    }


};

class Example_queue{
    public:
    // 큐 선언. queue<자료형> 큐 이름;
    queue<int> qu;
    Example_queue(){
        cout<< "Example queue"<<endl;
        for(int i = 0; i < 8; ++i){
            //큐에 데이터를 넣을때는 push()함수를 이용한다.
            qu.push(input_data[i]);    
        }
    }
    
    void check(){
        //큐가 비어있으면, qu.empty()는 true를 반환한다.
        if(qu.empty()) cout<<"emtpy queue"<<endl;
        else cout<<"queue is not empty"<<endl;
    }
    void print_st(){
        while(!qu.empty()){// 큐가 비어있지 않다면,
            cout<<qu.front()<<" "; //가장 나중에 들어온 데이터(queue)을 출력하고,
            qu.pop();// 그것을 삭제한다.
        }
        cout<<endl;
    }

};


int main(){
    //=== 예시 ===
    Example_queue example;
    example.print_st();

    //=== 본인이 작성한 큐 클래스 인스턴스화===
    
    /*
    My_queue myQueue;
    myQueue.flush();
    
    */


    return 0;
}