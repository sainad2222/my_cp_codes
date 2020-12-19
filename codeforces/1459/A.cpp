#include<bits/stdc++.h>
using namespace std;
#define INT             long long
#define endl            "\n"
#define inpArr(vec)          for(auto &it:vec) cin>>it
#define outArr(vec)          for(auto &it:vec) cout<<it<<" ";cout<<endl;

void solve(){

    int n;
    cin>>n;
    string a,b;
    cin>>a>>b;

    int red=0,blue=0;
    for(int i=0;i<n;i++){
        if(a[i]<b[i]) blue++;
        else if(a[i]>b[i]) red++;
    }

    if(red>blue) cout<<"RED"<<endl; 
    else if(red<blue) cout<<"BLUE"<<endl;
    else cout<<"EQUAL"<<endl;

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
