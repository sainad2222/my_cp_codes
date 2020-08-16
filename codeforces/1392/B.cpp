#include<bits/stdc++.h>

#define w(t)            int t;cin>>t;while(t--)
#define INT             long long
#define mod             1000000007
#define inf             (int)1e18
#define endl            "\n"
#define inpArr(vec)          for(auto &it:vec) cin>>it
#define outArr(vec)          for(auto &it:vec) cout<<it<<" ";cout<<endl;
using namespace std;
void solveA(){
	int n;
	cin>>n;
	vector<int> a(n);
	inpArr(a);
	set<int> s;
	for (auto i:a) s.insert(i);
	if (s.size()>1) cout<<1<<endl;
	else cout<<n<<endl;
}

void solveB(){
	INT n, k;
	cin>>n>>k;
	vector<INT> a(n);
	inpArr(a);
	vector<INT> tmp1;
	INT d = *max_element(a.begin(), a.end());
	for (auto i:a) tmp1.push_back(d-i);
	vector<INT> tmp2;
	d = *max_element(tmp1.begin(), tmp1.end());
	for (auto i:tmp1) tmp2.push_back(d-i);
	if(k&1)
	{
			outArr(tmp1);
	}
	else
	{
			outArr(tmp2);
	}
}




int main(){
ios_base::sync_with_stdio(0);cin.tie(NULL);

// w(t) {
// 	solveA();
// }

w(t) {
	solveB();
}

	return 0;
	
}