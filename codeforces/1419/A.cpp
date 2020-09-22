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
	string s;
	cin >> s;
	if(n&1){
		int odd = 0;
		for (int i = 0; i < n;i+=2){
			if(int(s[i])&1!=0)
				odd++;
		}
		if(odd>= 1)
			cout << 1 << endl;
		else
			cout << 2 << endl;
	}
	else{
		int even = 0;
		for (int i = 1; i < n;i+=2){
			if(int(s[i]&1)==0)
				even++;
		}
		if(even>=1)
			cout << 2 << endl;
		else
			cout << 1 << endl;
	}
}

int main(){
ios_base::sync_with_stdio(0);cin.tie(NULL);

int tt=1;
cin >> tt;
while(tt--){
	solve();
}

return 0;
	
}