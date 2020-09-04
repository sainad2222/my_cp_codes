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
	readThree(n, x, y);
	int i = 1;
	while(i<n){
		if((y-x)%(n-i)==0)
			break;
		i++;
	}
	INT diff = (y - x) / (n - i);
	vector<int> res;
	INT cur = x;
	while(cur<=y){
		res.push_back(cur);
		cur += diff;
	}
	int l = res.size();
	int rem = n - l;
	int tmp = rem;
	cur = x;
	int count = 0;
	while(rem>0 && cur-diff>0){
		rem--;
		cur -= diff;
		res.push_back(cur);
		count++;
	}
	rem = (tmp - count);
	cur = y;
	while(rem>0){
		cur += diff;
		res.push_back(cur);
		rem--;
	}
	outArr(res);
}




int main(){
ios_base::sync_with_stdio(0);cin.tie(NULL);

ww(t) {
	solve();
}

	return 0;
	
}