def func(row_values, matrix):
    parent = [0] * 303
    rank = [1] * 303
    edges = []


    def find(u):
        if (u == parent[u]): return u
        parent[u] = find(parent[u])
        return parent[u]


    def is_diff(a, b):
        a = find(a)
        b = find(b)
        if a==b: return False
        if rank[a] > rank[b]:
            a,b = b,a
        parent[a] = b
        if (rank[a] == rank[b]): rank[b] += 1
        return True

    n = row_values[0]


    for j in range(n): # 모든 노드는 임의의 n+1노드와 연결되어있기에 이 반복문을 사용한다.
        cost = row_values[j+1]
        edges.append([cost, j, n]) # cost, 노드1, 노드2
        parent[j] = j # 부모를 자기 자신으로 초기화

    parent[n] = n # 마지막 노드도 자신으로 초기화

    for j in range(n):
        arr = matrix[j]
        for k in range(n):
            if(j==k): continue
            edges.append([arr[k], j, k]) # cost, 노드1, 노드2
            
    edges[0:len(edges)] = sorted(edges[0:len(edges)])
    cnt = 0
    sum = 0

    for i in range(len(edges)):
        cost, a, b = edges[i]
        if(is_diff(a, b) == False): continue
        sum += cost
        cnt += 1
        if(cnt == n): break # 노드 개수는 총 n+1개

    return sum
