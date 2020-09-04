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
void solve(){
	INT a, b, x, y, n;
cin >> a >> b >> x >> y >> n;
INT tmp = n;
INT ac = 0, bc = 0;
if(n<=(a-x)){
	ac = n;
}
else{
	ac = (a - x);
	n -= ac;
	bc = min((b - y), n);
}
INT cost1 = (a - ac) * (b - bc);
n = tmp;
ac = 0, bc = 0;
if(n<=(b-y)){
	bc = n;
}
else{
	bc = b - y;
	n -= bc;
	ac = min((a - x), n);
}
INT cost2 = (a - ac) * (b - bc);
cout << min(cost1, cost2) << endl;
}




int main(){
ios_base::sync_with_stdio(0);cin.tie(NULL);

ww(t) {
	solve();
}

	return 0;
	
}