#include <bits/stdc++.h>
using namespace std;
#define INT long long
#define endl "\n"
#define all(x) (x).begin(), (x).end()
#define inpArr(vec)      \
    for (auto& it : vec) \
    cin >> it
#define outArr(vec)        \
    for (auto& it : vec)   \
        cout << it << " "; \
    cout << endl;

void solve()
{

    int n;
    cin >> n;
    vector<int> arr(n);
    inpArr(arr);

    map<int, int> mp;
    for (auto i : arr) {
        mp[i]++;
    }
    int ans = -1;
    for (auto i : mp)
        ans = max(ans, i.second);
    cout << ans << endl;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);
    int tt = 1;
    // cin >> tt;
    while (tt--) {
        solve();
    }

    return 0;
}
