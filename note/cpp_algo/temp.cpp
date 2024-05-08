#pragma GCC optimize("O3")

#include <bits/stdc++.h>

#define endl '\n'
#define ll long long
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    vector<int> v = {0, 1, 2, 3, 4, 5};

    // 벡터의 1번 인덱스부터 마지막 인덱스까지의 원소를 역순으로 뒤집기
    reverse(v.begin(), v.end());

    for (int i : v)
    {
        cout << i << " ";
    }

    cout << "\n";
    cout << *v.begin() << "\n";
    cout << *(v.begin() + 4) << "\n";
    cout << *v.end() << endl; // 쓰레기 값

    auto it = find(v.begin(), v.end(), 2);
    cout << "find 2: " << *it << endl;
}