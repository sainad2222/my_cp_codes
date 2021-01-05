#include <bits/stdc++.h>
using namespace std;
#define INT long long
#define endl "\n"
#define all(x) (x).begin(),(x).end()
#define inpArr(vec)      \
    for (auto& it : vec) \
    cin >> it
#define outArr(vec)        \
    for (auto& it : vec)   \
        cout << it << " "; \
    cout << endl;

INT ceil(INT x,INT y){
    return (x+y-1)/y;
}

void solve()
{

    int n,x;
    cin>>n>>x;

    vector<int> lis(n);
    inpArr(lis);

    int i =0;
    INT bank = 0;
    INT mi = 0;
    while(i<n-1){
        if((bank+lis[i])%x==0){
            mi += (bank+lis[i])/x;
            bank = 0;
        }
        else{
            bank += lis[i];
        }
        i++;
    }
    mi += ceil(bank+lis[n-1],x);
    INT ma = 0;
    bank = 0;
    i = 0;
    while(i<n-1){
        if((bank+lis[i])%x){
            ma += ceil(bank+lis[i],x);
            bank = 0;
        }
        else{
            bank += lis[i];
        }
        i ++;
    }
    ma += ceil(bank+lis[n-1],x);
    cout<<mi<<" "<<ma<<endl;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);
    int tt = 1;
    cin >> tt;
    while (tt--) {
        solve();
    }

    return 0;
}
