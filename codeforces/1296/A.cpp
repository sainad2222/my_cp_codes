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
void solve(){
	read(n);
	int a[n];
	inpArr(a);
	int odd = 0;
	for (auto i : a)
	{
		if(i&1){
			odd++;
		}
	}
	int even = n - odd;
	if(n&1){
		if(odd>=1)
			cout << "YES" << endl;
		else
			cout << "NO" << endl;
	}
	else
	{
		if(odd>=1 && even>=1)
			cout << "YES" << endl;
		else
			cout << "NO" << endl;
	}
}

int main(){
ios_base::sync_with_stdio(0);cin.tie(NULL);

int t;
cin >> t;
while(t--){
	solve();
}

return 0;
	
}