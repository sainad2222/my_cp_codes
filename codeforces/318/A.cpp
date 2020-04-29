#include <bits/stdc++.h>

#define w(t)            int t;cin>>t;while(t--)
#define INT             long long
#define mod             1000000007
#define inf             (int)1e18
#define endl            "\n"

using namespace std;

int main(){
ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);

    
       INT n,k;cin>>n>>k;
        if(k<=(n+1)/2) {
            cout<<2*k-1<<endl;
           }
           else{
               cout<<2*(k-(n+1)/2)<<endl; 
           }
       
       


    
    return 0;
}