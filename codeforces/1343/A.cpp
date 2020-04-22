#include<bits/stdc++.h>
using namespace std;
int main(){
    int T,i,n;
    cin>>T;
    while(T--){
        cin>>n;
        for(i=2;i<30;i++){
            int val = (1<<i)-1;
            if(n%val==0){
                cout<<n/val<<"\n";
                break;
            }
        }
    }
    return 0;
}