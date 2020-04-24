#include<bits/stdc++.h>
using namespace std;
int main(){
    int T;
    cin>>T;
    while (T--)
    {
        int n,i,j;
        cin>>n;
        int a[n];
        for(int i=0;i<n;i++) cin>>a[i];
        int ok=0;
        for(i=0;i<n;i++){
            for(j=i+2;j<n;++j){
                if(a[i]==a[j]){
                    ok = 1;
                    break;
                }
            }
        }
        if(ok==1){
            cout<<"YES"<<"\n";
        }
        else{
            cout<<"NO"<<"\n";
        }

    }
    
        
    return 0;
}
