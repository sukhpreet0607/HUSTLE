#include <stdio.h>

int main()
{
	// n is the number of vertices
	// m is the number of edges
	int n, m;
	scanf("%d %d", &n, &m);
	int adjMat[n + 1][n + 1];
	for (int i = 0; i < m; i++) {
		int u, v;
		scanf("%d %d", &u, &v);
		adjMat[u][v] = 1;
		adjMat[v][u] = 1;
		// for a directed graph with an edge pointing from u
		// to v,we just assign adjMat[u][v] as 1
	}

	return 0;
}


