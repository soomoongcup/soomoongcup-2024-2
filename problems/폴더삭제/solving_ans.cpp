// 왼쪽 위에서 오른쪽 아래로 드래그 해서 파일을 지워야함 -> 단, 가장 적은 범위 안에서
// 가장 왼쪽의 y, 위쪽의 x, 밑쪽의 x, 오른쪽의 y 를 구하면 된다.

#include <iostream>
#include <string>
#include <vector>

using namespace std;

const int INF = 0x3f3f3f3f;
int n, m;
vector<string> v;


void func(vector<string> wallpaper) {
    
    vector<int> answer;
    
    int left = INF;
    int up = INF;
    int bottom = -1;
    int right = -1;
    int row = wallpaper.size();
    int col = wallpaper[0].size();
    
    for(int i = 0; i < row; i++) {
        for(int j = 0; j < col; j++) {
            if(wallpaper[i][j] == 'D') {
                if(j < left) left = j;
                if(i < up) up = i;
                if(i > bottom) bottom = i;
                if(j > right) right = j;
            }
        }
    }

    cout << up << ' ' << left << ' ' << bottom+1 << ' ' << right+1 << '\n';
}

int main(void) {
    
    cin >> n >> m;

    for(int i = 0; i < n; i++) {
        string str; cin >> str;
        v.push_back(str);
    }

    func(v);

    return 0;
}