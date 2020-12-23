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
    deque<int> lis(n);
    inpArr(lis);

    if (n == 1) {
        cout << 1 << endl
             << "L" << endl;
        return;
    }

    string ans = "";
    int curMax = 0;
    if (lis.front() < lis.back()) {
        ans += 'L';
        curMax = lis.front();
        lis.pop_front();
    } else {
        ans += 'R';
        curMax = lis.back();
        lis.pop_back();
    }
    while (true) {
        if (lis.size() == 1) {
            break;
        }
        if (lis.front() < lis.back()) {
            if (lis.front() >= curMax) {
                ans += 'L';
                curMax = lis.front();
                lis.pop_front();
            } else {
                if (lis.back() >= curMax) {
                    ans += 'R';
                    curMax = lis.back();
                    lis.pop_back();
                } else {
                    break;
                }
            }
        } else {
            if (lis.back() >= curMax) {
                ans += 'R';
                curMax = lis.back();
                lis.pop_back();
            } else {
                if (lis.front() >= curMax) {
                    ans += 'L';
                    curMax = lis.front();
                    lis.pop_front();
                } else {
                    break;
                }
            }
        }
    }
    if (lis.size() == 1) {
        if (lis.front() >= curMax) {
            ans += 'L';
            lis.clear();
        }
    }
    cout << n - lis.size() << endl
         << ans << endl;
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
