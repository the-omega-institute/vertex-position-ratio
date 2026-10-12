"""The explicit constructions in note/note.tex. All ray indices are 1-based."""
from graphs import edge

def original(m):
    assert m>=2
    g=[set()]; names={'y':0}; rays=[]
    for name,length in [('H',4*m)]+[(f'P{i}',4*m) for i in range(1,m+1)]+[(f'Q{j}',2*m+2*j) for j in range(1,m+1)]:
        ray=[0]
        for t in range(1,length+1):
            v=len(g);g.append(set());names[f'{name}:{t}']=v;edge(g,ray[-1],v);ray.append(v)
        rays.append(ray)
    for j in range(1,m+1):
        a,b=2*m+2*j,2*m+j+1
        edge(g,names[f'H:{b}'],names[f'Q{j}:{b}'])
        for i in range(1,m+1): edge(g,names[f'Q{j}:{a}'],names[f'P{i}:{a}'])
    M=2*m+1; f=[M]*len(g)
    for key,v in names.items():
        if ':' not in key: continue
        typ,t=key.split(':');t=int(t)
        if typ=='H':f[v]=min(M,4*m-t)
        elif typ[0]=='P':f[v]=2*m+t%2
        else:
            j=int(typ[1:]);f[v]=min(M,max(4*m+1-t,t-(2*j+1)))
    selected=[names[f'P{i}:{2*m+2*j+1}'] for i in range(1,m+1) for j in range(1,m)]
    return g,dict(y=0,x=names[f'H:{4*m}'],selected=selected,M=M,f=f,cover=rays)

def subcubic(m):
    assert m>=2
    C=m+1; L=2*C*(m+2); R=L+1-2*C; M=R+C
    k=1<<(2*m).bit_length()  # least power of 2 >= 2m+1
    g=[set() for _ in range(2*k-1)]
    for v in range(1,len(g)): edge(g,v,(v-1)//2)
    leaves=list(range(k-1,2*k-1)); paths=[]; names={};f=[M]*len(g)
    specs=[('H',L)]+[(f'P{i}',L) for i in range(1,m+1)]+[(f'Q{j}',2*C*(j+1)+m) for j in range(1,m+1)]
    for q,leaf in enumerate(leaves):
        prefix=[];v=leaf
        while True:
            prefix.append(v)
            if v==0:break
            v=(v-1)//2
        path=prefix[::-1]
        if q<len(specs):
            name,length=specs[q]
            for t in range(1,length+1):
                v=len(g);g.append(set());edge(g,path[-1],v);path.append(v);names[f'{name}:{t}']=v
                if name=='H':fv=min(M,L-t)
                elif name[0]=='Q':
                    j=int(name[1:]);a=2*C*(j+1);fv=min(M,max(L+1-t,t-a+R))
                else:
                    i=int(name[1:]);delta=min(abs(t-(2*C*(j+1)+i)) for j in range(1,m+1))
                    fv=min(M,R+i+delta)
                f.append(fv)
        paths.append(path)
    for j in range(1,m+1):
        a,b=2*C*(j+1),C*(j+2)
        edge(g,names[f'H:{b}'],names[f'Q{j}:{b}'])
        for i in range(1,m+1): edge(g,names[f'Q{j}:{a+i-1}'],names[f'P{i}:{a+i}'])
    selected=[names[f'P{i}:{2*C*(j+1)+C}'] for i in range(1,m+1) for j in range(1,m+1)]
    return g,dict(y=0,x=names[f'H:{L}'],selected=selected,M=M,f=f,cover=paths,k=k)

def cubic(m):
    base,meta=subcubic(m);n=len(base);k=meta['k']
    g=[set(a) for a in base]+[{v+n for v in a} for a in base]
    for u in range(n):
        if len(base[u])==2:edge(g,u,u+n)
        elif len(base[u])==1:
            c=len(g);g.extend(set() for _ in range(4))
            for i in range(4):edge(g,c+i,c+(i+1)%4)
            edge(g,u,c);edge(g,u,c+1);edge(g,u+n,c+2);edge(g,u+n,c+3)
    cover=[]
    for path in meta['cover']:
        u=path[-1];cap=sorted(g[u]-base[u]);assert len(cap)==2
        c=cap[0]
        cover += [path+[c,c+3],path+[c+1,c+2],[0]+[v+n for v in path]]
    f=meta['f']*2
    for u in range(n):
        if len(base[u])==1:f.extend([meta['f'][u]]*4)
    return g,dict(y=0,x=meta['x'],selected=meta['selected'],M=meta['M'],f=f,cover=cover,k=k)

def realize(a,b):
    assert a>=2 and a<=b<=3*a-1
    if a==b:
        g=[set() for _ in range(a+1)]
        for u in range(a+1):
            for v in range(u):edge(g,u,v)
        return g
    s=b+1-a;r=max(1,s-a);t=s-r
    assert 1<=r<=a and 1<=t<=a
    g=[set() for _ in range(b+2)]
    A=range(1,r+1);B=range(r+1,r+a+1);D=range(r+a+1,len(g))
    for v in A:edge(g,0,v)
    for u in A:
        for v in B:edge(g,u,v)
    for u in B:
        for v in D:edge(g,u,v)
        for v in B:
            if u<v:edge(g,u,v)
    return g

def fan(n):
    g=[set() for _ in range(n+1)]
    for v in range(1,n+1):edge(g,0,v)
    for v in range(1,n):edge(g,v,v+1)
    return g
