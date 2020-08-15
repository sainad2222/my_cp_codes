#include<bits/stdc++.h>

#define w(t)            int t;cin>>t;while(t--)
#define INT             long long
#define mod             1000000007
#define inf             (int)1e18
#define endl            "\n"
#define inpArr(vec)          for(auto &it:vec) cin>>it
#define outArr(vec)          for(auto &it:vec) cout<<it<<" ";cout<<endl;
using namespace std;
void solve(){
	int n;
	cin>>n;
	vector<int> lis(n);
	inpArr(lis);
	sort(lis.begin(), lis.end());
	for (int i=1;i<n;i++) {
		if(lis[i]-lis[i-1]>1){
			cout<<"NO"<<endl;
			return;
		};
	};
	cout<<"YES"<<endl;
	return;
}






int main(){
ios_base::sync_with_stdio(0);cin.tie(NULL);

w(t) {
	solve();
}
	return 0;
	
}