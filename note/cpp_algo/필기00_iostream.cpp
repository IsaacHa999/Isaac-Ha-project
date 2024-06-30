/*
cin 관련 함수
- cin.fail(), cin.clear(), cin.ignore() // 스트림 상태 확인, 스트림 상태 초기화, 버퍼 비우기
- cin.get(), cin.getline(), cin.peek(), cin.putback()   // 문자, 문자열, 문자 하나 읽기, 문자 되돌리기
- cin.ignore(), cin.ignore(n, c)
- cin.getline(), cin.getline(s, n)  // 문자열 입력받기, 공백 포함 문자열 입력받기
- cin.get(), cin.get(c) // 문자 입력받기
- cin.putback(), cin.putback(c) // 문자 되돌리기
- cin.peek()    // 문자 하나 읽기
- cin.sync()    
- cin.tie() 
- cin.rdbuf()
- cin.getloc()
- cin.setstate()
- cin.rdstate()
- cin.exceptions()
- cin.setf(), cin.unsetf(), cin.flags()
- cin.width(), cin.fill(), cin.precision()

cout 관련 함수
- cout.put(), cout.write()  
- cout.flush()
- cout.tie()
- cout.rdbuf()
- cout.getloc()
- cout.setf(), cout.unsetf(), cout.flags()
- cout.width(), cout.fill(), cout.precision()


// 필수 암기
- cin >> a; // 입력받기
- cout << a; // 출력하기
- cin.fail(), cin.clear(), cin.ignore() // 스트림 상태 확인
- cin.ignore(100, '\n'); // 버퍼 비우기 // (100개의 문자를 무시하고 개행문자를 만날 때까지 무시)
- getline(cin, s); // 공백 포함 문자열 입력받기
- cin.getline(s, n); // 공백 포함 문자열 입력받기
- cin.get(c); // 문자 입력받기
- cin.putback(c); // 문자 되돌리기
- cin.peek(); // 문자 하나 읽기
- cin.sync(); // 버퍼 비우기
- cin.tie(); // 스트림 연결하기
- cin.rdbuf(); // 버퍼 설정하기
- cin.getloc(); // 로케일 가져오기
- cin.setstate(); // 스트림 상태 설정하기
- cin.rdstate(); // 스트림 상태 가져오기

*/

#include <iostream>

using namespace std;

int main()
{
    ;
}
// cin 관련 함수
// 기본 사용법
void cin_basic()
{
    int a;
    cin >> a;
    cout << a << endl;

    char c;
    cin >> c;

    string s;
    cin >> s;
}

void 문자열_입력받기()
{
    string s;
    cin >> s;
    cout << s << endl;
}

void 공백포함_문자열_입력받기()
{
    string s; // ex) "Hello World"
    getline(cin, s);
    cout << s << endl;
}

// cin.fail(), cin.clear(), cin.ignore()
void 스트림_상태확인()
{
    int a;
    cin >> a;
    if (cin.fail()) // 스트림의 상태가 실패 상태인지 확인
    {
        cout << "입력이 잘못되었습니다." << endl;
        cin.clear();           // 스트림의 상태를 초기화,
        cin.ignore(100, '\n'); // 100개의 문자를 무시하고, 개행문자를 만날 때까지 무시
    }
    cout << a << endl;
}

void cin_버퍼비우기()
{
    int num;
    cout << "Enter an integer: ";
    cin >> num;
    cin.ignore(1000, '\n'); // 버퍼 비우기, 1000개의 문자를 무시하고 개행문자를 만날 때까지 무시
    cout << "You entered: " << num << endl;
}

void putback_사용하기()
{
    char c;
    cin.get(c);
    cout << c << endl;

    cin.putback(c); // 문자 되돌리기
    cin.get(c);
    cout << c << endl;
}

void unget_사용하기()
{
    char c;
    cin.get(c);
    cout << c << endl;

    cin.unget(); // 문자 되돌리기
    cin.get(c);
    cout << c << endl;
}
