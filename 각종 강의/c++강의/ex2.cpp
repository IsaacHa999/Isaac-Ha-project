#include <iostream>
using namespace std;
int func_by_ref(int a,int b) {
    a = 100;
    b = 200;
    
}


int main(void) {
	int a = 10;
	int b = 20;
	cout << "before function" << endl;
	cout << "a : " << a << endl;
	cout << " b : " << b << endl;


	func_by_ref(a, b);

	cout << "after function" << endl;
	cout << "a : " << a << endl;
	cout << " b : " << b << endl;

	return 0;
}