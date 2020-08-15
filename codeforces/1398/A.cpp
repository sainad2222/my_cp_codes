#include<bits/stdc++.h>

#define w(t)            int t;cin>>t;while(t--)
#define INT             long long
#define mod             1000000007
#define inf             (int)1e18
#define endl            "\n"
#define inpArr(vec)          for(auto &it:vec) cin>>it
#define outArr(vec)          for(auto &it:vec) cout<<it<<" ";cout<<endl;
using namespace std;
int main(){
ios_base::sync_with_stdio(0);cin.tie(NULL);

w(t) {
	int n;
	cin>>n;
	vector<int> lis(n);
	inpArr(lis);
	if (lis[0]+lis[1]<=lis[n-1]) cout<<"1 2 "<<n<<endl;
	else cout<<"-1"<<endl;
}
	return 0;
	
}