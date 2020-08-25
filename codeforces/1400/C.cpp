#include<bits/stdc++.h>

int i = 0,j = 0,k = 0;
#define w(t)            int t;cin>>t;while(t--)
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
    string s;
    cin >> s;
    read(x);
    int n = s.length();
    vector<char> W(n, '1');
    vector<char> S(n, '0');
    FOR(0,n){
        if(s[i]=='0'){
            if(i>=x){
                W[i - x] = '0';
            }
            if(i+x<n){
                W[i + x] = '0';
            }
        }
    }
    FOR(0,n){
        if(i>=x&&W[i-x]=='1'){
            S[i] = '1';
        }
        if(i+x<n&&W[i+x]=='1'){
            S[i] = '1';
        }
    }
    string tmp(S.begin(), S.end());
    if(tmp==s){
        string tmp2(W.begin(), W.end());
        cout << tmp2 << endl;
    }
    else
        cout << "-1" << endl;
}




int main(){
ios_base::sync_with_stdio(0);cin.tie(NULL);

w(t) {
    solve();
}

    return 0;
    
}