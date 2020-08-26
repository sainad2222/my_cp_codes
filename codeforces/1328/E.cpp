#include<bits/stdc++.h>

int i = 0,j = 0,k = 0;
#define ww(t)            int t;cin>>t;while(t--)
#define INT             long long
#define mod             1000000007
#define inf             (int)1e18
#define endl            "\n"
#define FOR(a, b)       for (int i = a; i < b;i++)
#define inpArr(vec)          for(auto &it:vec) cin>>it
#define outArr(vec)          for(auto &it:vec) cout<<it<<" ";cout<<endl;
#define read(n) 			INT n;cin >> n;
#define readTwo(x, y) 		INT x, y;cin>>x>>y;
#define readThree(x, y, z) 	INT x, y, z;cin>>x>>y>>z;
#define readFour(x, y, z,a) INT x, y, z, a;cin>>x>>y>>z>>a;

using namespace std;
// declaring in global space
vector<int> intime, outtime;
vector<int> parent, depth;
vector<vector<int>> g;
vector<int> visited;
int timer = 1;

void dfs(int v, int par=-1,int dep=0){
    visited[v] = 1;
    parent[v] = par;
    depth[v] = dep;
    intime[v] = timer++;
    for(auto child:g[v]){
        if(visited[child]!=1){
            dfs(child, v, dep + 1);
        }
    }
    outtime[v] = timer++;
}

bool inPath(int u,int v){
    return intime[u] <= intime[v] && outtime[u] >= outtime[v];
}

int main(){
ios_base::sync_with_stdio(0);cin.tie(NULL);

readTwo(n, m);
//resizing to size n
intime = outtime = vector<int>(n+1);
parent = depth = vector<int>(n+1);
visited = vector<int>(n+1,0);
g = vector<vector<int>>(n+1);

FOR(0,n-1){
    readTwo(x, y);
    g[x].push_back(y);
    g[y].push_back(x);
}
dfs(1);
FOR(0,m){
    int k;
    cin>>k;
    vector<int> lis(k);
    for(auto &it:lis){
        cin >> it;
    }
    int deep = lis[0];
    for(auto it:lis) if(depth[deep]<depth[it])
            deep = it;
    
    for(auto &it:lis){
        if(it==deep)
            continue;
        if(parent[it]!=-1)
            it = parent[it];
    }

    bool ok = true;
    for(auto it:lis)
        ok &= inPath(it, deep);
    if(ok)
        cout << "YES" << endl;
    else
        cout << "NO" << endl;
}
// outArr(intime);
// outArr(outtime);
// for(auto it:g){
//     for(auto it2:it){
//         cout << it2 << " ";    // this is literally print(g.neighbours) in python f*ck C++
//     }
//     cout << endl;
// }



return 0;
    
}