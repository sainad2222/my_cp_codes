// for new year magic(grandmaster)
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

void solve()
{

    string s;
    cin>>s;
    int n =s.size();
    if(s[0]==')' || s[n-1]=='(' || n&1) cout<<"NO"<<endl;
    else cout<<"YES"<<endl;
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
