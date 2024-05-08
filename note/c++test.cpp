#pragma GCC optimize("O3")

#include <bits/stdc++.h>

#define endl '\n'
#define ll long long
using namespace std;

int func1(int a, int b, int m);

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n = func1(6, 10, 5);
    cout << n << endl;
}

int func1(int a, int b, int m)
{
    int val = 1;
    while (b--)
        val *= a;
    return val % m;
}