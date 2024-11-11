#include "testlib.h"
#include <bits/stdc++.h>
using namespace std;
using ll = long long;
constexpr ll MAX = 30100 * 30100;

int main(int argc, char* argv[]) {
    setName("checker");
    registerTestlibCmd(argc, argv);
    
    ll cnt = 0;
    while(!ans.seekEof() && !ouf.seekEof()){
        cnt++;

        ll ret = ans.readLong(0ll, MAX, "ret");
        ll out = ouf.readLong(0ll, MAX, "out");
        if(ret != out){
            quitf(_wa, "%d%s%s numbers diff - expected: %s, found: %s"
            , cnt, englishEnding(cnt).c_str(), vtos(ret).c_str(), vtos(out).c_str());
        }
    }

    ll extans = 0, extouf = 0;
    while(!ouf.seekEof()){
        ouf.readLong(0ll, MAX, "out");
        extouf++;
    }

    while(!ans.seekEof()){
        ans.readLong(0ll, MAX, "ret");
        extans++;
    }

    if(extans){
        quitf(_wa, "less Output");
    }
    else if(extouf){
        quitf(_wa, "Exceed Ouput");
    }
    quitf(_ok, "");

    return 0;
}
