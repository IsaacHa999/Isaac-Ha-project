#include <iostream>
using namespace std;

int add(int a,int b) {
    int res = a+b;
    return a+b;
}
int minus1(int a, int b) {
    return a-b;
}
int multi(int a, int b) {
    return a*b;
}
int divide(int a, int b) {
    return a/b;
}
int main() {
    int A = add(100,5);
    int B = minus1(100,5);
    int C = multi(100,5);
    int D = divide(100,5);
    cout << A << endl;
    cout << B << endl;
    cout << C << endl;
    cout << D << endl;
}