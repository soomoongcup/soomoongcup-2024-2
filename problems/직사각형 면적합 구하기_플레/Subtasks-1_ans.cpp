#include <bits/stdc++.h>

using namespace std;

int board[1020][1020];
int cnt;

int main() {
    int x1, y1, x2, y2, n;
    cin >> n;
    
    for (int i = 0; i < n; i++) {
        cin >> x1 >> y1 >> x2 >> y2;
        for (int j = x1; j < x2; j++) {
            for (int k = y1; k < y2; k++) {
                if (board[j][k]) continue;
                board[j][k] = 1;
                cnt++;
            }
        }
    }

    cout << cnt << '\n';

}
