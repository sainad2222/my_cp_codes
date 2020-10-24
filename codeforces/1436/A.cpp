#include<bits/stdc++.h>
using namespace std;



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


void solveA(){
    int tt;
    cin>>tt;
    while(tt--){
        readTwo(n,k);
        vector<int> lis(n);
        inpArr(lis);
        int su = 0;
        for(auto i:lis) su+=i;
        if(su==k) cout<<"YES"<<endl;
        else cout<<"NO"<<endl;
    }
}

int isPrime(int n){
    int i=2;
    while(i*i<=n){
        if(n%i==0) return false;
        i++;
    }
    return true;
}


void solveB(){
    int tt;
    cin>>tt;
    while(tt--){
        read(n);
        int cur = n-1;
        int tmp=1;
        while(!(isPrime(cur+tmp) && !isPrime(tmp))){
            tmp+=1;
        }
        bool flag = true;
        vector<vector<int>> matrix(n);
        for(int i=0;i<n;i++){
            matrix[i].resize(n,1);
        }

        int i=0;j=0;
        int one=0,two=n-1;
        while(i<n && j<n){
            if(flag) j = one,one++,flag=false;
            else j = two,two--,flag=true;
            matrix[i][j] = tmp;
            i++;
        }
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                cout<<matrix[i][j]<<" ";
            }
            cout<<endl;
        }
    }
}



int main(){
ios_base::sync_with_stdio(0);cin.tie(NULL);

solveA();
// solveB();
return 0;
    
}