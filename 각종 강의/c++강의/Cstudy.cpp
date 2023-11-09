#include <iostream>
using namespace std;

int main() {
	int num = 80;
    cin >> num;
	
	if (num >= 95) {
		cout << "A+";
	}
	else if (num >= 90) {
        cout << "A0";
    }
    else if (num >= 85){
        cout << "B+";
    }
    else if (num >= 80){
        cout << "B0";
    }    
	else {
		cout << "c0";
	}
	return 0;
}

//PS g++ ex1.cpp
//PS ./a.exe