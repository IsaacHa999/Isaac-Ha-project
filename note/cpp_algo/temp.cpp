#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

// 거리 제곱을 계산하는 함수
int distance_squared(pair<int, int> P1, pair<int, int> P2)
{
    int x1 = P1.first;
    int y1 = P1.second;
    int x2 = P2.first;
    int y2 = P2.second;

    int d2 = (x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1);
    return d2;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;
    cin >> N;
    vector<pair<int, int>> P;
    vector<int> check(1001, 0);

    for (int i = 0; i < N; i++)
    {
        int x, y;
        cin >> x >> y;
        P.push_back(make_pair(x, y));
    }

    for (int i = 0; i < N; i++)
    {
        for (int j = i + 1; j < N; j++)
        {
            int value = distance_squared(P[i], P[j]);
            if (value < 1001)
            { // check 배열의 범위 내에 있는 경우에만 증가
                check[value]++;
            }
        }
    }

    int max_distance_squared = 0;
    for (int i = 0; i < 1001; i++)
    {
        if (check[i] >= 4)
        { // 적어도 4번 등장한 거리 제곱 값 찾기
            if (i > max_distance_squared)
                max_distance_squared = i;
        }
    }

    float area = (float)max_distance_squared;
    cout << fixed;
    cout.precision(2);
    cout << area << endl;

    return 0;
}
