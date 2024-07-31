#include <iostream>
#include <vector>
#include <queue>

using namespace std;

// 간선 추가 함수
void addEdge(vector<vector<int>> &adj, int v, int w)
{
    adj[v].push_back(w);
}

// BFS 함수
void BFS(const vector<vector<int>> &adj, int s)
{
    int V = adj.size();
    vector<bool> visited(V, false); // 정점 방문 여부 저장
    queue<int> q;                   // BFS를 위한 큐

    visited[s] = true; // 시작 정점을 방문 표시
    q.push(s);         // 시작 정점을 큐에 추가

    while (!q.empty())
    {
        int v = q.front(); // 큐의 맨 앞 정점을 가져옴
        cout << v << " ";  // 정점을 출력
        q.pop();           // 큐에서 정점을 제거

        // 현재 정점의 모든 인접한 정점을 확인
        for (int u : adj[v])
        {
            if (!visited[u])
            {                      // 인접한 정점이 방문되지 않았다면
                visited[u] = true; // 방문 표시
                q.push(u);         // 큐에 추가
            }
        }
    }
}

int main()
{
    int V = 4;                  // 정점의 수
    vector<vector<int>> adj(V); // 그래프의 인접 리스트 표현

    // 간선 추가
    addEdge(adj, 0, 1);
    addEdge(adj, 0, 2);
    addEdge(adj, 1, 2);
    addEdge(adj, 2, 0);
    addEdge(adj, 2, 3);
    addEdge(adj, 3, 3);

    cout << "정점 2에서 시작하는 너비 우선 탐색 결과: ";
    BFS(adj, 2); // 정점 2에서 시작하는 BFS 수행

    return 0;
}
