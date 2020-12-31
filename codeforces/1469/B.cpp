// submitting again for new year magic
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
    vector<int> reds(n);
    inpArr(reds);
    int m;
    cin >> m;
    vector<int> blues(m);
    inpArr(blues);

    int i = 0, j = 0;
    int ans = 0;
    while (i < n && reds[i] >= 0)
        ans += reds[i++];
    while (j < m && blues[j] >= 0)
        ans += blues[j++];

    int tmpr = 0;
    int maxReds = -1e9;
    while (i < n) {
        tmpr += reds[i];
        maxReds = max(maxReds, tmpr);
        i++;
    }
    if (maxReds > 0)
        ans += maxReds;

    int tmpb = 0;
    int maxBlues = -1e9;
    while (j < m) {
        tmpb += blues[j];
        maxBlues = max(maxBlues, tmpb);
        j++;
    }
    if (maxBlues > 0)
        ans += maxBlues;
    cout << ans << endl;
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