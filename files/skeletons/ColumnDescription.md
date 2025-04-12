# Description of the names of the columns

This is a descrition of the names of the columns in the excel spreadsheets SkeletonsData-3000.xlsx and PolyhedralSkeletonsData-3000.xlsx that contain information about all the graphs that appear as skeletons of rotary maps on at most 3000 edges. Each row in the spreadsheet corresponds to one of these graphs.

**``Name``**: This is the name of the graph. The name has the form  "Sk$(n;i)$" or "Sk$(n;i)^t$", where $n,i$ and $t$ are some positive integers. In the first case, the skeleton graph is simple, has $n$ vertices, and is the $i$-th simple skeleton among all skeletons on $n$ vertices. In the second case, the graph is not simple and $t\ge 2$ is the number of edges between two adjacent vertices. (When $n=1$, the parameter $t$ counts the number of loops attached to the vertex.) The corresponding simple graph (the graph obtained by removing all but one edge between every pair of adjacent vertices) is Sk(n;i).

**``#V``**: The number of vertices of the graph (always equal to $n$ in the name "Sk$(n;i)^t$").

**``ID``**: The index of the graph among all the simple skeletons with the same number of vertices (always equal to $i$ in the name "Sk$(n;i)^t$").

**``v-mult``**: The number of edges between two adjacent vertices. If not equal to $1$, then equal to the value of $t$ in the name "Sk$(n;i)^t$" of the graph.

**``#E``,``val``,``girth``,``diam``**: The number of edges, the valence, the girth and the diameter of the graph. Note that the girth is 1 for graph with one vertex, and is 2 for other non-simple graphs.

**``bip``**: "b" if the graph is bipartite and "nb" if it is not.

**``O-genus``**: A sequence of integers (separated by a colon) representing the genera of the regular orientable maps with this skeleton. 

**``N-genus``**: A sequence of integers (separated by a colon) representing the genera of the regular non-orientable maps with this skeleton. 

**``C-genus``**: A sequence of integers (separated by a colon) representing the genera of the chiral maps with this skeleton. 

**``OM``**: The names of the regular orientable maps with this skeleton.

**``NM``**: The names of the regular non-orientable maps with this skeleton.

**``CM``**: The names of the chiral maps with this skeleton.