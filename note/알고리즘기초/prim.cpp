#include <iostream>
#include <vector>
#include <limits>

using namespace std;

const int INF = numeric_limits<int>::max();

// Assuming the types and structures are defined as follows
using index = int;
using number = int;
using edge = pair<index, index>;
using set_of_edges = vector<edge>;

void prim(int n, const vector<vector<number>>& W, set_of_edges& F) {
    index i, vnear;
    number min;
    edge e;
    vector<index> nearest(n + 1);
    vector<number> distance(n + 1);

    F.clear();

    for (i = 2; i <= n; i++) {
        nearest[i] = 1;
        distance[i] = W[1][i];
    }

    for (int k = 0; k < n - 1; k++) {
        min = INF;
        for (i = 2; i <= n; i++) {
            if (0 <= distance[i] && distance[i] <= min) {
                min = distance[i];
                vnear = i;
            }
        }

        e = make_pair(vnear, nearest[vnear]);
        F.push_back(e);
        distance[vnear] = -1;

        for (i = 2; i <= n; i++) {
            if (W[i][vnear] < distance[i]) {
                distance[i] = W[i][vnear];
                nearest[i] = vnear;
            }
        }
    }
}

int main() {
    // Example Usage
    int n = 5;  // Number of vertices
    vector<vector<number>> W(n + 1, vector<number>(n + 1, 0));  // Weight matrix
    set_of_edges F;

    // Initialize your weight matrix W

    prim(n, W, F);

    // Output the minimum spanning tree
    cout << "Minimum Spanning Tree Edges:\n";
    for (const auto& e : F) {
        cout << e.first << " -- " << e.second << endl;
    }

    return 0;
}
