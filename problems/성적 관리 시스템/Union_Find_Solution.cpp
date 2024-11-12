#include <bits/stdc++.h>
#include <ext/rope>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;
#define ordered_set tree<int, null_type, less<int>, rb_tree_tag,tree_order_statistics_node_update>
#define fastio cin.tie(0), cout.tie(0), ios::sync_with_stdio(0);
#define all(x) (x).begin(), (x).end()
#define x first 
#define y second
using namespace std; typedef long long ll;
using ld = long double;
using ull = unsigned long long;
using pll = pair<ll, ll>; using tll = tuple<ll, ll, ll>;
ll n, m, k, t; string s;

constexpr ll INF = 0x3f3f3f3f3f3f3f3f;
constexpr ll MAX = 101010;
constexpr ll MOD = 998244353;
ll num[5], cnt[5];
ll arr[MAX];
char c[5] = { 'F', 'D', 'C', 'B', 'A' };

class _uf { 
public:
    ll n; vector <int> p, si;
    
    _uf(){}
    _uf(ll n) { 
        this->n = n;
        p.resize(n + 1); si.resize(n + 1);
        fill(all(p), -1);
        fill(all(si), 1);
    }

    ll find(ll num) { 
        if (p[num] == -1) return num;
        return p[num] = find(p[num]);
    }

    void merge(ll a, ll b) {
        a = find(a); b = find(b);
        if (a == b) return;
        if (size(a) < size(b)) swap(a, b);
        p[b] = a, si[a] += si[b];
    }

    ll size(ll num){
        return si[find(num)];
    }

    ll same(ll a, ll b) {
        if (find(a) == find(b)) return 1;
        return 0;
    }
};

ll find(ll n){
    for(int i = 0;i < 5;i++){
        if(num[i] == n) return i;
    }
    return -1;
}

int main() {
    fastio;

    cin >> n >> m; ll seq = 1; _uf uf(2 * m);
    memset(num, -1, sizeof(num));

    num[3] = 1;
    for(int i = 1;i <= n;i++) arr[i] = 1, cnt[3]++;

    while(m--){
        string com; cin >> com;
        if(com == "SET"){
            ll idx, val; cin >> idx >> val;
            ll org = uf.find(arr[idx]);
            if(find(org) != -1) cnt[find(org)]--;
        
            if(num[val] == -1) num[val] = ++seq;
            arr[idx] = num[val]; cnt[val]++;
        }
        else if(com == "ADD"){
            ll sc, val; cin >> sc >> val;
            ll org = num[sc];
            if(org == -1) continue;
            
            ll nxt = sc + val;
            nxt = min(nxt, 4ll); nxt = max(nxt, 0ll);
            if(sc == nxt) continue;

            if(num[nxt] == -1) num[nxt] = ++seq;
            uf.merge(num[nxt], num[sc]);
            num[nxt] = uf.find(num[nxt]);

            num[sc] = -1; 
            cnt[nxt] += cnt[sc]; cnt[sc] = 0;
        }
        else if(com == "PRN"){
            ll idx; cin >> idx;
            ll ret = find(uf.find(arr[idx]));
            cout << c[ret] << "\n";
        }
        else{
            ll val; cin >> val;
            cout << cnt[val] << "\n";
        }
    }


    return 0;
}
