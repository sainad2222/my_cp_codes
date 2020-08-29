#include <bits/stdc++.h>
using namespace std;
int mod = 1e9+7;

int visited[200005];
vector<int> ar[200005];
int cc;

void dfs(int employee){
    visited[employee]=1;
    cc++;
    for(int emp:ar[employee]){
        if(!visited[emp]){
            dfs(emp);
        }
    }
}

int main() {
	// your code goes here
	int n,m,a,b;
	    cin>>n>>m;
	    for(int i=1;i<=n;i++){
	        visited[i]=0;
	    }
	    for(int i=1;i<=m;i++){
	        cin>>a>>b;
	        ar[a].push_back(b);
	        ar[b].push_back(a);
	    }
        int ans=-1;
	    for(int i=1;i<=n;i++){
	        if(!visited[i]){
	            cc=0;
	            dfs(i);
	            ans = max(ans,cc);
	        }
	    }
	    cout<<ans<<endl;
	return 0;
}
