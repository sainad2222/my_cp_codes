#include<bits/stdc++.h>

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

using namespace std;
void solve(){
   readTwo(n,k);
   vector<int> a(n), b(n);
   inpArr(a);
   inpArr(b);
   vector<int> res(k, 0);
   vector<int> ans;
   FOR(0, n)
   {
     if (res[a[i] - 1] < b[i])
     {
       ans.push_back(res[a[i] - 1]);
       res[a[i] - 1] = b[i];
     }
     else{
       ans.push_back(b[i]);
     }
   }
   sort(ans.begin(), ans.end());
   vector<int> fin;
   for (auto i:ans){
     if(i!=0)
       fin.push_back(i);
   }
   int count = 0;
   for (auto i : res)
   {
     if(i==0){
       count++;
     }
   }
   INT result = 0;

   for (int i = 0; i < count;i++){
     result += fin[i];
   }
   cout << result << endl;
}

int main(){
ios_base::sync_with_stdio(0);cin.tie(NULL);

int tt=1;
// cin >> tt;
while(tt--){
	solve();
}

return 0;
	
}
