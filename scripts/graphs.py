"""Small pure-Python graph utilities, independent of the C++ implementation."""
from collections import deque

def decode(s):
    n = ord(s[0])-63
    g = [set() for _ in range(n)]
    bit = 0
    for j in range(1,n):
        for i in range(j):
            if ((ord(s[1+bit//6])-63) >> (5-bit%6)) & 1:
                g[i].add(j); g[j].add(i)
            bit += 1
    return g

def encode(g):
    n=len(g)
    if n > 62: raise ValueError('small graph6 encoder supports n<=62')
    bits=[int(i in g[j]) for j in range(1,n) for i in range(j)]
    bits += [0] * (-len(bits)%6)
    return chr(n+63)+''.join(chr(63+sum(bits[k+i]<<(5-i) for i in range(6)))
                           for k in range(0,len(bits),6))

def edge(g,u,v):
    assert u != v
    g[u].add(v); g[v].add(u)

def bfs(g,r,blocked=frozenset()):
    d=[-1]*len(g); d[r]=0; q=deque([r])
    while q:
        u=q.popleft()
        for v in g[u]:
            if v not in blocked and d[v]<0: d[v]=d[u]+1; q.append(v)
    return d

def position_numbers(g):
    # A separate list-based matching implementation for construction checks.
    n=len(g)
    if n==1: return [1]
    d=[bfs(g,u) for u in range(n)]
    result=[]
    for r in range(n):
        rel={u:[v for v in range(n) if v!=u and v!=r and d[r][u]+d[u][v]==d[r][v]]
             for u in range(n) if u!=r}
        match={}
        def augment(u,seen):
            for v in rel[u]:
                if v in seen: continue
                seen.add(v)
                if v not in match or augment(match[v],seen): match[v]=u; return True
            return False
        k=sum(augment(u,set()) for u in rel)
        result.append(n-1-k)
    return result

def local_numbers_bruteforce(g):
    """All subsets; all induced paths for monophonic, deletion BFS for visibility."""
    n=len(g)
    # Optional singleton convention in the archived data. The observer-excluding
    # local definitions in the note apply to connected graphs with n >= 2.
    if n==1: return dict(vp=[1], monophonic=[1], visibility=[1])
    d=[bfs(g,u) for u in range(n)]
    result={k:[] for k in ('vp','monophonic','visibility')}
    for r in range(n):
        induced=[set() for _ in range(n)]
        def paths(path):
            u=path[-1]
            induced[u].update(path[:-1])
            for v in g[u]:
                if v not in path and not (g[v] & set(path[:-1])): paths(path+[v])
        paths([r])
        other=[v for v in range(n) if v!=r]
        best={k:0 for k in result}
        for mask in range(1<<(n-1)):
            s={v for j,v in enumerate(other) if (mask>>j)&1}
            if all(not any(u!=v and d[r][u]+d[u][v]==d[r][v] for u in s) for v in s):
                best['vp']=max(best['vp'],len(s))
            if all(not ((s-{v}) & induced[v]) for v in s):
                best['monophonic']=max(best['monophonic'],len(s))
            if all(bfs(g,r,s-{v})[v]==d[r][v] for v in s):
                best['visibility']=max(best['visibility'],len(s))
        for k in result: result[k].append(best[k])
    return result
