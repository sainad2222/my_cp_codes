#include<bits/stdc++.h>
using namespace std;
#define INT             long long
#define endl            "\n"
#define inpArr(vec)          for(auto &it:vec) cin>>it
#define outArr(vec)          for(auto &it:vec) cout<<it<<" ";cout<<endl;

void solve(){

	int n,k;
	cin>>n>>k;
	
	string s="abc";
	for(int i=0;i<(n/3);i++){
			cout<<s;
		}
	if(n%3==1){
		cout<<'a'<<endl;
	}
	else if(n%3==2) cout<<"ab"<<endl;
	else cout<<endl;
	 
	

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
