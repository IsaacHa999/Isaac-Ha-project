#include "iostream"
#include "typeinfo"

int main()
{
	int i = 0;
	float f = 0.0;
	double d = 0.0;
	bool b = false;

	std::cout << "int : " << typeid(i).name() << std::endl;
	std::cout << "float : " << typeid(f).name() << std::endl;
	std::cout << "double : " << typeid(d).name() << std::endl;
	std::cout << "bool : " << typeid(b).name() << std::endl;
}

/* 출력결과
int : i
float : f
double : d
bool : b
*/