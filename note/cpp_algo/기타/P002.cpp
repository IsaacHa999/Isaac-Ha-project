#include <iostream>

using namespace std;

int main() 
{
    int N = 0;
    int A[1000];
    cin >> N;

    for (int i = 0; i < N; i++) {
        cin >> A[i];
    }

    long sum = 0;
    long max = 0;   // int로 선언하면 오답이 나올 수 있음

    for (int i = 0; i < N; i++) {
        if (A[i] > max) {
            max = A[i];
        }
        sum = sum + A[i];
    }

    double result = sum * 100.0 / max / N;
    cout << result << "\n";


}