#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() 
{
    int N = 0, sum = 0;;
    long long number;
    string numberS;
    cin >> N;
    cin >> number;
    numberS = to_string(number);    // 숫자형 -> string

    for (int i = 0; i < N; i++) {
        sum += numberS[i] - 48;    // 아스키코드를 활용한 숫자형 변환
    }
    
    cout << sum;

}