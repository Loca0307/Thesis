#include <bits/stdc++.h>
using namespace std;

// Graph using Adjacency Matrix

// Function to print the graph represented by an adjacency matrix
void PrintGraph(vector<vector<bool>> v, int vertex) {
    cout << "Graph: " << endl;
    // Loop through each vertex
    for (int i = 0; i < vertex; i++) {
        // Loop through each edge
        for (int j = 0; j < vertex; j++) {
            // Print the value of the adjacency matrix at position (i, j)
            cout << v[i][j] << " ";
        }
        // Print a new line after each row of the matrix
        cout << endl;
    }
}

int main() {
    int vertex, edge;
    // Prompt the user to enter the number of vertices
    cout << "Vertex: ";
    cin >> vertex;
    // Prompt the user to enter the number of edges
    cout << "Edges: ";
    cin >> edge;
    // Undirected, unweighted graph
    vector<vector<bool>> AdjMat(vertex, vector<bool>(vertex, 0));
    int u, v;
    // Read the edges and update the adjacency matrix
    for (int i = 0; i < edge; i++) {
        cin >> u >> v;
        AdjMat[u][v] = 1;
        AdjMat[v][u] = 1;
    }
    // Print the graph
    PrintGraph(AdjMat, vertex);

    return 0;
}