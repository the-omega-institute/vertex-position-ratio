// Exact vertex-position numbers from graph6; C++17, one thread.
// For n >= 2, the observer-excluding order has width (n-1) minus a matching.
#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
using namespace std;
using Mask = uint64_t;
struct Graph { int n; vector<Mask> adj; };
Graph decode(string s) {
    if (s.rfind(">>graph6<<",0)==0) s=s.substr(10);
    int n=s.at(0)-63;
    if(n<1 || n>62) throw runtime_error("only graph6 orders 1..62 supported");
    Graph g{n,vector<Mask>(n)}; int bit=0;
    for(int j=1;j<n;j++) for(int i=0;i<j;i++,bit++)
        if(((s.at(1+bit/6)-63)>>(5-bit%6))&1) {
            g.adj[i]|=Mask(1)<<j;g.adj[j]|=Mask(1)<<i;
        }
    return g;
}
vector<int> numbers(const Graph& g) {
    int n=g.n;
    if(n==1) return {1};
    vector<vector<int>> d(n,vector<int>(n,1000));
    for(int r=0;r<n;r++) {
        array<int,64> q; int h=0,t=0; q[t++]=r;d[r][r]=0;
        while(h<t) {int u=q[h++];Mask a=g.adj[u];while(a){int v=__builtin_ctzll(a);a&=a-1;
            if(d[r][v]==1000){d[r][v]=d[r][u]+1;q[t++]=v;}}}
        if(t!=n) throw runtime_error("disconnected graph");
    }
    vector<int> out;
    for(int r=0;r<n;r++) {
        vector<Mask> rel(n);
        for(int u=0;u<n;u++) if(u!=r)
            for(int v=0;v<n;v++) if(v!=u && v!=r && d[r][u]+d[u][v]==d[r][v])
                rel[u]|=Mask(1)<<v;
        vector<int> match(n,-1);int size=0;
        auto augment=[&](auto&& self,int u,Mask& seen)->bool {
            Mask a=rel[u]&~seen;
            while(a){int v=__builtin_ctzll(a);a&=a-1;seen|=Mask(1)<<v;
                if(match[v]<0 || self(self,match[v],seen)){match[v]=u;return true;}}
            return false;
        };
        for(int u=0;u<n;u++) if(u!=r){Mask seen=0;if(augment(augment,u,seen))size++;}
        out.push_back(n-1-size);
    }
    return out;
}
int main(int argc,char** argv) {
    if(argc!=3){cerr<<"usage: position INPUT.g6 OUTPUT.csv\n";return 2;}
    ifstream in(argv[1]);ofstream out(argv[2]);
    if(!in || !out) return 2;
    out<<"graph6,n,vp_minus,vp,p\n";string s;uint64_t count=0;
    while(getline(in,s)) {
        if(s.empty() || s==">>graph6<<")continue;
        Graph g=decode(s);auto p=numbers(g);
        out<<s<<','<<g.n<<','<<*min_element(p.begin(),p.end())<<','<<*max_element(p.begin(),p.end())<<",\"";
        for(int i=0;i<g.n;i++){if(i)out<<' ';out<<p[i];}out<<"\"\n";count++;
    }
    cerr<<count<<" graphs checked\n";
}
