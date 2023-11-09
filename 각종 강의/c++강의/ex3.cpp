#include <iostream>
using namespace std;
struct names {
    int korean;
    int math;
    int english;
    int history;

};

int main(void) {
    struct names C[10];
    C[0].korean = 100;
    C[1].korean = 90;



    cout << "korean: " << C[0].korean << endl; 
    cout << "korean: " << C[1].korean; 


	return 0;
}