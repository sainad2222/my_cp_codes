#include<bits/stdc++.h>

int i = 0,j = 0,k = 0;
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
int sol(int x){
	int count = 0;
	int i = 1;
	int flag = 0;
	while(i*i<=x){
		if(x%i==0){
			if(i==x/i)
				flag = 1;
			count++;
		}
		i++;
	}
	if (flag){
		return 2 * count - 1;
	}
	return 2 * count;
}
void solve(){
	read(n);
	INT ans = 0;
	for (int i = 1; i < n; i++)
	{
		ans += sol(i);
	}
	cout << ans << endl;
}

int main(){
ios_base::sync_with_stdio(0);cin.tie(NULL);

int t=1;
// cin >> t;
while(t--){
	solve();
}

return 0;
	
}