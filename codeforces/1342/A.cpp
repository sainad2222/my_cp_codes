#include<bits/stdc++.h>
using namespace std;
int main(){
ios_base::sync_with_stdio(false);
cin.tie(NULL);

    int n,i,t;
    cin>>t;
    while(t--){
        long long a,b,x,y,cost=0;
        cin>>x>>y;
        cin>>a>>b;
        if(min(x,y)*b<=2*a*(min(x,y))) cost = abs(x-y)*a+min(x,y)*b;
        else cost = a*(abs(x-y))+min(x,y)*a*2;
        cout<<cost<<"\n";

    }

    return 0;
    
}