#include<bits/stdc++.h>
using namespace std;
#define INT             long long
#define endl            "\n"

void solve(){

    int a,b,c;
    cin>>a>>b>>c;
    INT su = (a+b+c);
    int k = su/9;
    if(su%9==0 && min(a,min(b,c))>=k) cout<<"YES"<<endl;
    else cout<<"NO"<<endl;

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
