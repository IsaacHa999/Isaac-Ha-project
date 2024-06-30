#include <iostream>
#include <cmath>
using namespace std;

// 완전 이진 트리에서 두 리프 노드 간의 거리를 계산하는 함수
int distance(int k, int leaf1, int leaf2)
{
    // 리프 노드의 시작 인덱스
    int start_index = pow(2, k - 1);

    // 실제 트리에서의 인덱스 계산
    int node1 = start_index + leaf1 - 1;
    int node2 = start_index + leaf2 - 1;

    int steps = 0;
    // 두 노드가 같아질 때까지 부모 노드로 올라감
    while (node1 != node2)
    {
        if (node1 > node2)
        {
            node1 /= 2; // 부모 노드로 이동
        }
        else
        {
            node2 /= 2; // 부모 노드로 이동
        }
        steps++; // 거리 증가
    }
    return steps;
}

// distance 함수를 테스트하는 코드
void test_distance()
{
    int k = 4; // 트리의 레벨
    int leaf1;
    int leaf2;

    for (int i = 1; i < 9; i++)
    {
        for (int j = i + 1; j < 9; j++)
        {
            leaf1 = i;
            leaf2 = j;
            cout << "Distance between leaf " << leaf1 << " and leaf " << leaf2
                 << " in a level-" << k << " complete binary tree is: "
                 << distance(k, leaf1, leaf2) << endl;
        }
    }
}

int main()
{
    test_distance();

    return 0;
}
