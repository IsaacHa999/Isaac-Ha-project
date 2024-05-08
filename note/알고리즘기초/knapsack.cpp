#include <iostream>
#include <vector>

using namespace std;
bool promising(int i, int n, const vector<int>& p, const vector<int>& w, int weight);

const int W = 16; // 배낭의 최대 무게
int maxprofit = 0; // 최대 이익
int numbest = 0; // 최적해를 만드는 아이템의 수 //레벨
vector<string> bestset; // 최적해를 저장하는 배열   // 최종 답을 갱신해 나간다
vector<string> include(10, "NO"); // include 배열 초기화

// 배낭 문제 알고리즘
void knapsack(int i, int profit, int weight, const vector<int>& p, const vector<int>& w, int n) {
    if (weight <= W && profit > maxprofit) {
        maxprofit = profit;
        numbest = i;
        bestset = include;
    }

    if (promising(i, n, p, w, weight)) {
        include[i + 1] = "YES";
        knapsack(i + 1, profit + p[i + 1], weight + w[i + 1], p, w, n);
        include[i + 1] = "NO";
        knapsack(i + 1, profit, weight, p, w, n);
    }
}

bool promising(int i, int n, const vector<int>& p, const vector<int>& w, int weight) {
    int j = i + 1;
    int totweight = weight;
    float bound = maxprofit;

    while (j <= n && totweight + w[j] <= W) {
        totweight += w[j];
        bound += p[j];
        j++;
    }

    int k = j;
    if (k <= n) {
        bound += (W - totweight) * (static_cast<float>(p[k]) / w[k]);
    }

    return bound > maxprofit;
}

int main() {
    // 예시로 사용할 이익과 무게 배열
    vector<int> profits = {40,30,50,10};
    vector<int> weights = {2,5,10,5};
    int n = profits.size();

    // 초기 호출
    knapsack(-1, 0, 0, profits, weights, n);

    // 결과 출력
    cout << "Maximum Profit: " << maxprofit << endl;
    cout << "Selected Items: ";
    for (int i = 0; i <= numbest; ++i) {
        if (bestset[i] == "YES") {
            cout << i + 1 << " ";
        }
    }
    cout << endl;

    return 0;
}
