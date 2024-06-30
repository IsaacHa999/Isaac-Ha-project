// boj 1654 랜선 자르기
#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int K, N;
    cin >> K >> N;
    long long arr[K];
    for (int i = 0; i < K; i++)
        cin >> arr[i];
    
    long long left = 1, right = *max_element(arr, arr + K);
    long long ans = 0;
    while (left <= right)
    {
        long long mid = (left + right) / 2;
        long long cnt = 0;  // 자른 개수
        for (int i = 0; i < K; i++) // 자른 개수 구하기
            cnt += arr[i] / mid;
        
        if (cnt >= N)   // N개 이상을 만들 수 있으면
        {
            ans = max(ans, mid);    // 최대 길이 갱신
            left = mid + 1; // 더 길게 잘라도 됨
        }
        else    // N개 이상을 만들 수 없으면
            right = mid - 1;    // 더 짧게 잘라야 함
    }

    cout << ans;

}