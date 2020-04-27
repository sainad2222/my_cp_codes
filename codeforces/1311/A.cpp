#include <bits/stdc++.h>

#define w(t)            int t;cin>>t;while(t--)
#define INT             long long
#define mod             1000000007
#define inf             (int)1e18
#define endl            "\n"

using namespace std;
int main(){
ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);

    w(t){
        INT a,b;
        cin>>a>>b;
        int ans;
        if(a==b) ans=0;
        else if((a<b && (b-a)&1!=0) || (a>b && (a-b)%2==0)) ans=1; 
        else ans=2;
        
        cout<<ans<<endl;
    }
    
}