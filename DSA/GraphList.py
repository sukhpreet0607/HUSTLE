# A utility function to add a vertex to the graph                      
''' 
     The purpose of using global variables inside all the 
     functions defined below is that global variables can be 
     used both inside and outside the functions
'''


def addVertex(vertex):
    global graph

    # This variable is used to count the number of vertices in the graph
    global vertexCount

    # If the vertex already exists in the graph
    if vertex in graph:
        print("Vertex ", vertex, " already exists in the graph ")

    # Otherwise create a new list for this vertex and increase the count of
    # vertices in the vertexCount variable
    else:
        vertexCount += 1
        graph[vertex] = []


# A utility function to add an edge between
# vertex source and destination

def addEdge(source, destination):
    global graph

    # Check if the source vertex exists in the graph
    if source not in  graph:
        print("Source vertex ", source, " does not exist in the graph")

    # Check if the destination vertex exists in the graph
    elif destination not in graph:
        print("Destination vertex ", destination,
              " do not exist in the graph")

    # If both the source and destination vertex exists in the
    # graph, an edge can be added.
    else:
        
        # Create a new list by passing in the data of the destination vertex
        temp = [destination]

        # The append() method adds a single item to the list. A new list is
        # not created. Instead, the original list is modified by adding the new
        # item to the rear of the original list
        graph[source].append(temp)


# A utility function to print the adjacency list representation of
# a graph
def printGraph():
    global graph

    # Pick each vertex
    for vertex in graph:
    # Pick all the vertices that form an edge with the picked vertex above.
        for edges in graph[vertex]:
            print(vertex, "->", edges[0])


if __name__ == '__main__':

    # Initializing the graph with an empty list
    # This will store all the vertices
    graph = {}

    # This variable is used to store the count of vertices in the graph
    vertexCount = 0

    # Creating 5 vertices in the graph. Initially none
    # of them is connected to each other or have an edge
    # between them
    addVertex(1)
    addVertex(2)
    addVertex(3)
    addVertex(4)
    addVertex(5)
    # Adding the edges between source and destination vertices
    addEdge(1, 2)
    '''
    1 --------> 2
    '''

    addEdge(2, 3)
    '''
    1 ---------> 2
                 |
                 |
                \|/
                 3
    '''

    addEdge(3, 4)
    '''
    1 ----------> 2
                  |
                  |
                 \|/
    4 <---------- 3
    '''

    addEdge(4, 1)
    '''
    1 ----------> 2
   /|\            |
    |             |
    |            \|/
    4 <---------- 3
    '''

    addEdge(3,1)
    addEdge(4,2)

    # Function call to printGraph() function 
    printGraph()
    print("Internal representation of graph is: ", graph)