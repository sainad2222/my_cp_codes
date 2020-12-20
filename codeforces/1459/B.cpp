// NTFS: Editorial
// if n is even we have to make n//2 steps in N/S and n//2 in E/W
// for n//2 steps we can have n//2 +1 different moves(see editorial for possible moves like 0 steps North n//2 steps South)
// and if n is odd we can have n//2 +1 for either N/S or E/W and n//2 +2 ways for
// other direction but for selection we multiply with 2 to select which direction
#include <bits/stdc++.h>
using namespace std;
#define INT long long
#define endl "\n"
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

    int tmp = n / 2;
    if (n & 1) {
        cout << 2 * (tmp + 1) * (tmp + 2) << endl;
    } else {
        cout << (tmp + 1) * (tmp + 1) << endl;
    }
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
