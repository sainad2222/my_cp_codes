#include<bits/stdc++.h>

#define w(t)            int t;cin>>t;while(t--)
#define INT             long long
#define mod             1000000007
#define inf             (int)1e18
#define endl            "\n"
#define inpArr(vec)          for(auto &it:vec) cin>>it
#define outArr(vec)          for(auto &it:vec) cout<<it<<" ";cout<<endl;
#define read(n) 			INT n;cin >> n;
#define readTwo(x, y) 		INT x, y;cin>>x>>y;
#define readThree(x, y, z) 	INT x, y, z;cin>>x>>y>>z;
#define readFour(x, y, z,a) INT x, y, z, a;cin>>x>>y>>z>>a;

using namespace std;
void solve(){
    read(n);
    string s, ans;
    cin >> s;
    for (int i = 0; i < 2 * n;i++){
        if(i%2==0)
            ans += s[i];
    }
    cout << ans << endl;
}




int main(){
ios_base::sync_with_stdio(0);cin.tie(NULL);

w(t) {
    solve();
}

    return 0;
    
}