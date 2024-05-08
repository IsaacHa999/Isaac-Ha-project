#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef int index;
typedef index set_pointer;

struct nodetype {
    index parent;
    int depth;
};

typedef nodetype universe;

vector<universe> U;

typedef pair<index, pair<index, int>> edge;
typedef vector<edge> set_of_edges;

void makeset(index i) {
    U[i].parent = i;
    U[i].depth = 0;
}

set_pointer find(index i) {
    index j = i;
    while (U[j].parent != j) j = U[j].parent;
    return j;
}

void merge(set_pointer p, set_pointer q) {
    if (U[p].depth == U[q].depth) {
        U[p].depth += 1;
        U[q].parent = p;
    } else if (U[p].depth < U[q].depth) {
        U[p].parent = q;
    } else {
        U[q].parent = p;
    }
}

void kruskal(int n, int m, set_of_edges E, set_of_edges& F) {
    F.clear();

    // Sort edges by weight in non-decreasing order
    sort(E.begin(), E.end(), [](const edge& a, const edge& b) {
        return a.second.second < b.second.second;
    });

    // Initialize sets
    U.resize(n + 1);
    for (index i = 1; i <= n; ++i) {
        makeset(i);
    }

    // Apply Kruskal's algorithm
    for (const auto& edge : E) {
        index i = edge.first;
        index j = edge.second.first;
        set_pointer p = find(i);
        set_pointer q = find(j);

        if (p != q) {
            merge(p, q);
            F.push_back(edge);
        }
    }
}

int main() {
    // Example Usage
    int n = 5;  // Number of vertices
    int m = 7;  // Number of edges
    // set_of_edges E = {
    //     {1, {2,1}},
    //     {1, {3,3}},
    //     {2, {3,3}},
    //     {2, {4,6}},
    //     {3, {4,4}},
    //     {3, {5,2}},
    //     {4, {5,5}}

    // };
    set_of_edges E = {
        {1, {2, 1}},
        {1, {3, 3}},
        {2, {3, 2}},
        {2, {4, 5}},
        {3, {4, 4}},
        {3, {5, 6}},
        {4, {5, 7}}
    };
    
    set_of_edges F;
    kruskal(n, m, E, F);

    // Output the minimum spanning tree
    cout << "Minimum Spanning Tree Edges:\n";
    for (const auto& edge : F) {
        cout << edge.first << " -- " << edge.second.first << " : " << edge.second.second << endl;
    }

    return 0;
}
