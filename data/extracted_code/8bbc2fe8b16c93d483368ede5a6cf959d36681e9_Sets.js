# Graph Data Structure: A Theoretical Overview

## Introduction

A **graph** is a collection of nodes (also called **vertices**) and edges, which connect pairs of nodes. Graphs can represent various real-world systems like social networks, transportation routes, and web page links.

Graphs are either **directed** or **undirected**:

-   In **directed graphs**, edges have a direction, indicating the relationship flows from one node to another.
-   In **undirected graphs**, edges represent a two-way relationship, meaning the connection between the nodes is mutual.

```
{
  +---+-----------+
| V | Neighbors |
+---+-----------+
| A |   B, C   |
| B |   A, D   |
| C |     A     |
| D |     B     |
+---+-----------+
}
```

## Definition

A graph can be defined as:

-   A set of vertices (nodes).
-   A set of edges (connections) between the vertices.

Graphs are often represented as:

-   **Adjacency List**: Where each node has a list of nodes it's connected to.
-   **Adjacency Matrix**: A 2D array indicating whether there is a direct connection between pairs of nodes.

## Common Use Cases

Graphs are used in many applications, such as:

-   **Social Networks**: Representing users as nodes and their connections as edges.
-   **Maps and Routes**: Cities as nodes, and roads as edges between them.
-   **Recommendation Systems**: Connecting users to products based on behavior.

## Graph Operations

Some common graph operations include:

-   **Add Vertex**: Add a new node to the graph.
-   **Add Edge**: Create a connection between two nodes.
-   **Remove Vertex**: Remove a node and its associated edges.
-   **Remove Edge**: Delete a connection between two nodes.
-   **Search**: Find a path between two nodes (using algorithms like BFS, DFS).

### Example Methods

Below are some typical methods associated with a graph:

-   **`addVertex(vertex)`**: Adds a new vertex to the graph.
-   **`addEdge(vertex1, vertex2)`**: Creates an edge between two vertices.
-   **`removeVertex(vertex)`**: Removes a vertex from the graph.
-   **`removeEdge(vertex1, vertex2)`**: Removes an edge between two vertices.
-   **`hasEdge(vertex1, vertex2)`**: Checks if there's an edge between two vertices.

## Conclusion

Graphs are incredibly versatile data structures used in modeling relationships between entities. Whether you need to track connections in a network or design algorithms to traverse structures, graphs are essential tools in computer science and many real-world applications.