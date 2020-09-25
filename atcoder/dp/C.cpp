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

int a[100005][4];
int dp[100005][4];
int n;

int DP(int day,int flag){
  if(day==n)
    return 0;
  
  if(dp[day][flag]!=-1){
    return dp[day][flag];
  }

  int ans = 0;
  if (flag == 0)
  {
    ans = max(ans, a[day][0] + DP(day + 1, 1));
    ans = max(ans, a[day][1] + DP(day + 1, 2));
    ans = max(ans, a[day][2] + DP(day + 1, 3));
  }
  else if(flag==1){
    ans = max(ans, a[day][1] + DP(day + 1, 2));
    ans = max(ans, a[day][2] + DP(day + 1, 3));
  }
  else if(flag==2){
    ans = max(ans, a[day][0] + DP(day + 1, 1));
    ans = max(ans, a[day][2] + DP(day + 1, 3));
  }
  else{
    ans = max(ans, a[day][0] + DP(day + 1, 1));
    ans = max(ans, a[day][1] + DP(day + 1, 2));
  }
  dp[day][flag] = ans;
  return ans;
}

void solve(){
  cin >> n;
  FOR(0, n)
  cin >> a[i][0] >> a[i][1] >> a[i][2];
  memset(dp, -1, sizeof(dp));
  cout << DP(0, 0) << endl;

  // for (int i = 0; i <= n;i++){
  //   for (int j = 0; j < 3;j++){
  //     cout << a[i][j] << " ";
  //   }
  //   cout << endl;
  // }
}

int main()
        {
          ios_base::sync_with_stdio(0);
          cin.tie(NULL);

          int tt = 1;
          // cin >> tt;
          while (tt--)
          {
            solve();
          }

          return 0;
        }