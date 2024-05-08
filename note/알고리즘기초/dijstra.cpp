#include <iostream>
#include <vector>
#include <limits>

using namespace std;

const int INF = numeric_limits<int>::max();

struct Edge {
    int start;
    int end;
};

void dijkstra(int n, vector<vector<int>>& W, vector<Edge>& F) {
    vector<int> touch(n + 1);
    vector<int> length(n + 1, INF);

    F.clear();

    for (int i = 2; i <= n; ++i) {
        touch[i] = 1;
        length[i] = W[1][i];
    }

    for (int count = 1; count <= n - 1; ++count) {
        int vnear = -1;
        int min = INF;

        for (int i = 2; i <= n; ++i) {
            if (length[i] != -1 && length[i] < min) {
                min = length[i];
                vnear = i;
            }
        }

        Edge e = {touch[vnear], vnear};
        F.push_back(e);

        for (int i = 2; i <= n; ++i) {
            if (length[vnear] + W[vnear][i] < length[i]) {
                length[i] = length[vnear] + W[vnear][i];
                touch[i] = vnear;
            }
        }

        length[vnear] = -1;
    }
}

int main() {
    // Example Usage
    int n = 5;  // Number of vertices
    vector<vector<int>> W = {
        {INF, INF, INF, INF, INF, INF},
        {INF, 0, 7, 4, 6, 1},
        {INF, INF, 0, INF, INF, INF},
        {INF, INF, 2, 0, 5, INF},
        {INF, INF, 3, INF, 0, INF},
        {INF, INF, INF, INF, 1, 0}
    };

    vector<Edge> F;
    dijkstra(n, W, F);

    // Output the shortest path
    cout << "Shortest Paths (Edges):\n";
    for (const auto& e : F) {
        cout << e.start << " -- " << e.end << endl;
    }

    return 0;
}
