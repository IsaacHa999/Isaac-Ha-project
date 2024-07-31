/*
정의: 브루트포스 알고리즘
    탐색할 데이터의 범위가 100만 단위 이하일 때 사용 가능
    모든 경우의 수를 탐색하는 방법
    시간 복잡도: O(n!), O(2^n), O(n^3) 등
    예시: 완전 탐색, 순열, 조합, 백트래킹 등

대표적인 예제
    1. 부분 집합 합 문제(Subset Sum Problem)
    2. 배낭 문제(Knapsack Problem)
    3. 모든 순열 생성(Generate All Permutations)
    4. 모든 조합 생성(Generate All Combinations)
    5. 문자열 매칭(String Matching)
    6. 외판원 문제(Traveling Salesman Problem)
    7. N-Queens 문제

브루트포스 알고리즘의 최적화
    1. 가지치기(Pruning)
    2. 동적 계획법(Dynamic Programming), 메모이제이션(Memoization)
    3. 휴리스틱(Heuristic)
*/

#pragma GCC optimize("O3") // 최적화 레벨 3

#include <bits/stdc++.h>

#define endl '\n'
#define ll long long
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
}

void 예제1순열생성()
{
    std::vector<int> arr = {1, 2, 3};

    std::sort(arr.begin(), arr.end()); // Ensure the array is sorted

    std::cout << "All permutations:\n";
    do
    {
        for (int num : arr)
        {
            std::cout << num << " ";
        }
        std::cout << "\n";
    } while (std::next_permutation(arr.begin(), arr.end()));
}