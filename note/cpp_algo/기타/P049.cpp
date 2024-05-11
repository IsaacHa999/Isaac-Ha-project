// 물의 양 구하기

#include <iostream>
#include <vector>
#include <algorithm>
#include <deque>
#include <stack>
#include <queue>
#include <string>
#include <cmath>

using namespace std;

void BFS();
static int Sender[] = {0, 0, 1, 1, 2, 2};
static int Receiver[] = {1, 2, 0, 2, 0, 1};
static bool visited[201][201];
static bool answer[201];
static int now[3];

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> now[0] >> now[1] >> now[2];
    BFS();

    for (int i = 0; i < 201; i++)
}