// 탑 boj 2493
/*
문제 분석:
    1. 가장 큰 탑만 찾아야 하므로 스택을 사용한다.(최대값을 찾아야 하므로),
    2. 최댓값 이외에 다른 값들은 필요없다.
*/

#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second

int N;
stack<pair<int, int>> tower;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    cin >> N;
    tower.push({100000001, 0}); // empty stack 에러 방지
    for (int i = 1; i <= N; i++)
    {
        int height;
        cin >> height;

        while (tower.top().X < height)
            tower.pop();

        cout << tower.top().Y << " ";

        tower.push({height, i});
    }
}

void another_soulution()
{

    int N;
    cin >> N;
    vector<pair<int, int>> A(N);

    for (int i = 0; i < N; i++)
    {
        cin >> A[i].first;
        A[i].second = i + 1;
    }

    stack<pair<int, int>> S;

    for (int i = 0; i < N; i++)
    {
        while (!S.empty() && S.top().first < A[i].first)
        {
            S.pop();
        }
        if (S.empty())
        {
            cout << 0 << " ";
        }
        else
        {
            cout << S.top().second << " ";
        }
        S.push(A[i]);
    }
}