// 스택 수열
#pragma GCC optimize("O3")

#include <bits/stdc++.h>

#define endl '\n'
#define ll long long
using namespace std;

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    stack<int> S;
    int cnt = 1; // 오름차순 다루기 위한 변수
    string ans;

    while (n--)
    {
        int t;
        cin >> t;

        while (cnt <= t)
        { // push
            S.push(cnt++);
            ans += "+\n";
        }

        if (S.top() != t)
        { // 예외 처리
            cout << "NO" << endl;
            return 0;
        }

        S.pop(); // pop
        ans += "-\n";
    }
    cout << ans;
}