// NTFS: Editorial
// gcd(a,b) = gcd(a-b,b) euclidean gcd I guess
// now this holds for multiple arguments too
// so gcd(a1+bj,...,an+bj) = gcd(a1+bj,a2-a1,a3-a2,...) after subtracting a1+bj from all other elements except first
// so for every j only first element is changing
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

    int n, m;
    cin >> n >> m;
    vector<INT> a(n);
    vector<INT> b(m);
    inpArr(a);
    inpArr(b);

    INT g = 0;
    for (int i = 1; i < n; i++) {
        g = __gcd(g, a[i] - a[0]);
    }
    for (int i = 0; i < m; i++) {
        cout << abs(__gcd(g, a[0] + b[i])) << " ";
    }
    cout << endl;
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
