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
constexpr ll MAX = 30101;
constexpr ll MOD = 998244353;
ll arr[MAX];

class node{
public:
    ll x, y1, y2, num;
    bool operator<(node& ot){
        return x < ot.x;
    }
};
vector <node> query; 

int main() {
    fastio;

    cin >> t;
    while(t--){
        cin >> n; query.clear();
        memset(arr, 0, sizeof(arr));
        
        while(n--){
            ll x1, y1, x2, y2; 
            cin >> x1 >> y1 >> x2 >> y2; y2--;
            query.push_back({x1, y1, y2, 1});
            query.push_back({x2, y1, y2, -1});
        }
        sort(all(query));

        ll result = 0, cnt = 0, la = 0;
        for(auto& i : query){
            auto[x, y1, y2, num] = i;
            result += cnt * (x - la); la = x;

            for(int i = y1;i <= y2;i++){
                arr[i] += num;
                if(arr[i] == 1 && num == 1) cnt++;
                else if(!arr[i] && num == -1) cnt--;
            }
        }

        cout << result << "\n";
    }
    
    
    return 0;
}
