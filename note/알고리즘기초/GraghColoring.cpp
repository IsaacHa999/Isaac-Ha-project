#include <iostream>
#include <vector>

using namespace std;

const int n = 4; // 노드의 수
const int m = 3; // 사용 가능한 색의 수
vector<int> vcolor(n + 1, 0); // 노드의 색을 저장하는 배열
vector<vector<int>> W = {
    {0, 0, 0, 0, 0},
    {0, 0, 1, 0, 1},
    {0, 1, 0, 1, 1},
    {0, 0, 1, 0, 1},
    {0, 1, 1, 1, 0}
}; // 인접 행렬

bool promising1(int i) {
    int j = 1;
    bool switch1 = true;

    while (j < i && switch1) {
        if (W[i][j] && vcolor[i] == vcolor[j]) {
            switch1 = false;
        }
        j++;
    }

    return switch1;
}
// Graph Coloring
void m_coloring(int i) {
    for (int color = 1; color <= m; color++) {
        vcolor[i] = color;

        if (promising1(i)) {
            if (i == n) {
                cout << "Coloring: ";
                for (int j = 1; j <= n; j++) {
                    cout << vcolor[j] << " ";
                }
                cout << endl;
            } else {
                m_coloring(i + 1);
            }
        }

        vcolor[i] = 0; // Backtrack
    }
}



int main() {
    cout << "Possible Colorings:\n";
    m_coloring(1);

    return 0;
}
