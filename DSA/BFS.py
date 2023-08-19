def bfsOfGraph(V, adj):
    vis = [0]
    unvis = adj[0]
    # print ("adj  :",adj)
    while (len(unvis) != 0):
        if unvis[0] not in vis:
            vis.append(unvis[0])
            unvis.pop(0)
            for i in adj[vis[-1]]:
                if i not in unvis:
                    if i not in vis:
                        unvis.append(i)

    return vis


print (bfsOfGraph(5,))