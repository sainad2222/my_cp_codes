#include<bits/stdc++.h>
using namespace std;
auto sgn = [&](int x) {
		if (x > 0) return 1;
		else return -1;
	};
int main(){
    int T;
    cin>>T;
    while(T--){
        int n;
        cin>>n;
        vector<int> a(n);
        for (int i=0;i<n;++i) cin >> a[i];
        long long sum = 0;
        for(int i=0;i<n;++i){
            int cur = a[i];
            int j = i;
            while (j < n && sgn(a[i]) == sgn(a[j])) {
				cur = max(cur, a[j]);
				++j;
			}
			sum += cur;
			i = j - 1;
        }
        cout << sum << "\n";
    }
    return 0;
}