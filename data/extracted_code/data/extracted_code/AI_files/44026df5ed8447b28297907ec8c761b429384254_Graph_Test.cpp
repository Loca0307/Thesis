#include <iostream>
#include "../../general/Graph.hpp"

void testVertex() {
    // Test default constructor
    Vertex v1;
    assert(v1.x == -1 && v1.y == -1 && v1.color == "");

    // Test constructor with two arguments
    Vertex v2(1, 2);
    assert(v2.x == 1 && v2.y == 2 && v2.color == "");

    // Test constructor with three arguments
    Vertex v3(3, 4, "red");
    assert(v3.x == 3 && v3.y == 4 && v3.color == "red");

    // Test up() method
    Vertex v4 = v2.up();
    assert(v4.x == 1 && v4.y == 3 && v4.color == "");

    // Test down() method
    Vertex v5 = v2.down();
    assert(v5.x == 1 && v5.y == 1 && v5.color == "");

    // Test left() method
    Vertex v6 = v2.left();
    assert(v6.x == 0 && v6.y == 2 && v6.color == "");

    // Test right() method
    Vertex v7 = v2.right();
    assert(v7.x == 2 && v7.y == 2 && v7.color == "");

    // Test distance() method
    unsigned int d1 = v2.distance(v3);
    assert(d1 == 4);

    unsigned int d2 = v3.distance(v2);
    assert(d2 == 4);

    // Test operator== method
    assert(v2 == v2);
    assert(!(v2 == v3));
}

void testGraph() {
    // Test constructor with no arguments
    Graph g1;
    assert(g1.size() == 0);

    // Test constructor with one argument
    Graph g2(5);
    assert(g2.size() == 5);

    // Test constructor with vector argument (vector of vertices)
    std::vector<Vertex> vertices;
    vertices.push_back(Vertex(1, 2));
    vertices.push_back(Vertex(3, 4));
    Graph g3(vertices);
    assert(g3.size() == 2);

    // Test constructor with unordered_map argument (map of max_edges)
    std::unordered_map<Vertex, int> max_edges;
    max_edges[Vertex(1, 2)] = 3;
    max_edges[Vertex(3, 4)] = 5;
    Graph g4(max_edges);
    assert(g4.size() == 2);

    // Test constructor with unordered_map argument (map of edges)
    std::unordered_map<Vertex, std::vector<Edge> > adj;
    adj[Vertex(1, 2)] = std::vector<Edge>();
    adj[Vertex(3, 4)] = std::vector<Edge>();
    Graph g5(adj);
    assert(g5.size() == 2);

    // Test addVertex() method
    g1.addVertex(Vertex(1, 2));
    assert(g1.size() == 1);

    // Test addDirEdge() and getEdges() methods
    g1.addDirEdge(Edge(Vertex(1, 2), Vertex(3, 4)));
    assert(g1.getEdges(Vertex(1, 2)).size() == 1);

    // Test addUndirEdge() method
    g1.addUndirEdge(Edge(Vertex(1, 2), Vertex(5, 6)));
    assert(g1.getEdges(Vertex(1, 2)).size() == 2);
    assert(g1.getEdges(Vertex(5, 6)).size() == 1);

    // Test setAsVisited() and getVisitedStatus() methods
    g1.setAsVisited(Vertex(1, 2));
    assert(g1.getVisitedStatus(Vertex(1, 2)) == true);

    // Test setMaxEdges() and getMaxEdges() method
    g1.setMaxEdges(Vertex(1, 2), 3);
    assert(g1.getMaxEdges(Vertex(1, 2)) == 3);
}

int main() {
    testVertex();
    testGraph();
    std::cout << "Tests passed" << std::endl;
    return 0;
}