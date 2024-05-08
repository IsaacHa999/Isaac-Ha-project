#include <iostream>
#include <string>

using namespace std;

int main()
{
    // string -> 숫자형
    string sNum = "1234";
    string sNum_d = "1234.56";
    int inum = stoi(sNum);
    long lnum = stol(sNum);
    double dnum = stod(sNum);
    float fnum = stof(sNum);

    // 숫자형 -> string
    int inum = 1234;
    long lnum = 1234;
    double dnum = 1234.56;
    float fnum = 1234.56f;
    string intToString = to_string(inum);
    string longToString = to_string(lnum);
    string doubleToString = to_string(dnum);
    string floatToString = to_string(fnum);

    // string -> char*
    string str = "Hello, world!";
    char myStr[100];
    sprintf(myStr, "%d", 10);
}
