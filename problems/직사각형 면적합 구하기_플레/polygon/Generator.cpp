#include "testlib.h"
#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define fastio cin.tie(0), cout.tie(0), ios::sync_with_stdio(0);
constexpr ll MAX = 30000;

int main(int argc, char* argv[]) {
    fastio;
    registerGen(argc, argv, 1);

    ll mx = stoll(argv[1]);
    ll xmx = stoll(argv[2]);
    ll ymx = stoll(argv[3]);

    ll t = 10;
    cout << t << endl;
    while(t--){
        cout << mx << endl;
        for(int i = 1;i <= mx;i++){
            ll x1 = rnd.next(0ll, xmx - 1);
            ll y1 = rnd.next(0ll, ymx - 1);
            ll x2 = rnd.next(x1 + 1, xmx);
            ll y2 = rnd.next(y1 + 1, ymx);
            
            cout << x1 << " " << y1 << " " << x2 << " " << y2 << endl;
        }
    }

    return 0;
}
