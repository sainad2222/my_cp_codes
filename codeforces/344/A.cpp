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
    int count=1;
    string s;
    cin>>s;
    char prev = s[1];
//    cout<<prev;

    FOR(1,n){
            string s;
            cin>>s;
            if(s[1]!=prev){
                    count++;
                    prev = s[1];
            }
    }
    cout<<count<<endl;
    
}




int main(){
ios_base::sync_with_stdio(0);cin.tie(NULL);

int tt=1;
// cin >> tt;
while(tt--){
	solve();
}

return 0;
	
}
