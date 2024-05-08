#include <iostream>
#include <vector>

using namespace std;

class Graph {
private:
    int vertices; // 정점의 수
    vector<vector<int>> adjacencyList; // 인접 리스트

public:
    Graph(int V) : vertices(V), adjacencyList(V) {}

    // 간선 추가 함수
    void addEdge(int from, int to) {
        adjacencyList[from].push_back(to);
        adjacencyList[to].push_back(from); // 무방향 그래프일 경우
    }

    // DFS 수행 함수
    void DFS(int start, vector<bool>& visited) {
        visited[start] = true;
        cout << start << " ";

        for (int neighbor : adjacencyList[start]) {
            if (!visited[neighbor]) {
                DFS(neighbor, visited);
            }
        }
    }

    // 전체 DFS 호출 함수
    void performDFS() {
        vector<bool> visited(vertices, false); // 방문 여부를 저장하는 배열

        for (int i = 0; i < vertices; ++i) {
            if (!visited[i]) {
                DFS(i, visited);
            }
        }
    }
};

int main() {
    // 그래프 생성
    Graph graph(5);

    // 간선 추가
    graph.addEdge(0, 1);
    graph.addEdge(0, 2);
    graph.addEdge(1, 3);
    graph.addEdge(1, 4);

    cout << "DFS traversal starting from vertex 0:\n";
    graph.performDFS();

    return 0;
}
