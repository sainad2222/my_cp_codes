// NTFS: aaryamannx in stevenkplus twitch
// Idea is to replace odd or even position elements with 1 whichever sum is lower
#include <bits/stdc++.h>
using namespace std;
#define INT long long
#define endl "\n"
void solve()
{
    int n;
    cin >> n;
    vector<int> lis(n);
    INT total = 0;
    INT odd = 0;
    bool od = true;
    for (auto& it : lis) {
        cin >> it;
        total += it;
        if (od)
            odd += it;
        od = !od;
    }
    INT even = total - odd;
    if (odd < even) {
        od = true;
        for (auto& it : lis) {
            if (od)
                cout << 1 << " ";
            else
                cout << it << " ";
            od = !od;
        }
        cout << endl;
    } else {
        od = false;
        for (auto& it : lis) {
            if (od)
                cout << 1 << " ";
            else
                cout << it << " ";
            od = !od;
        }
        cout << endl;
    }
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
