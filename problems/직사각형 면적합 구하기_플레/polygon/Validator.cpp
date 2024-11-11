#include "testlib.h"
#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define fastio cin.tie(0), cout.tie(0), ios::sync_with_stdio(0);
constexpr ll MAX = 30000;

int main(int argc, char* argv[]) {
    fastio;
    registerValidation(argc, argv);

    ll t = inf.readLong(1ll, 10ll, "t");
    inf.readEoln();

    while(t--){
        ll mx = inf.readLong(1ll, 30000ll, "n");
        inf.readEoln();

        for(int i = 1;i <= mx;i++){
            ll x1 = inf.readLong(0, MAX, "x1");
            inf.readSpace();

            ll y1 = inf.readLong(0, MAX, "y1");
            inf.readSpace();

            ll x2 = inf.readLong(0, MAX, "x2");
            inf.readSpace();

            ll y2 = inf.readLong(0, MAX, "y2");
            ensuref(x1 < x2, "x1 must lower then x2");
            ensuref(y1 < y2, "y1 must lower then y2");
            inf.readEoln();
        }
    }

    inf.readEof();


    return 0;
}
