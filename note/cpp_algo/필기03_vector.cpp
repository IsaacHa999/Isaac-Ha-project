#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    // 선언
    vector<int> A; // 1차원 벡터 선언, 괄호 없음
    // vector<vector<int>> D(N + 1, vector<int>(N + 1, 0)); // 2차원 벡터 선언

    // 초기화
    vector<int> B(5);    // 0으로 초기화된 5개의 원소를 가진 벡터
    vector<int> C(5, 1); // 1로 초기화된 5개의 원소를 가진 벡터

    // iterator 사용
    auto it = A.begin();
    distance(A.begin(), it); // A.begin()부터 it까지의 거리 반환(== 인덱스와 동일)

    // 삽입 연산
    A.push_back(1);
    A.insert(A.begin(), 7); // 이터레이터 위치에 삽입
    A.insert(A.begin() + 2, 10);

    // 값 변경
    A[4] = -5;

    // 삭제 연산
    A.pop_back();
    A.erase(A.begin() + 3);
    A.clear();

    // 정보 가져오기
    A.size();
    A.front();
    A.back();
    A[3];
    A.at(5);   // A[5]와 동일
    A.begin(); // 첫번째 원소의 이터레이터 반환
    A.end();   // 마지막 원소의 다음 원소의 이터레이터 반환

    // 기타
    fill(A.begin(), A.end(), false);
    max_element(A.begin(), A.end()); // 반환값   포인터
    reverse(A.begin(), A.begin());
    auto iter = find(A.begin(), A.end(), 3); // find()? 찾는 값의 이터레이터 반환 : A.end()의 이터레이터 반환

    // 출력
    for (int i : A)
    {
        cout << i << " ";
    }
}
