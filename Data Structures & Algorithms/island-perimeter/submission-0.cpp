class Solution {
public:
    int islandPerimeter(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();

        int p = 0;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    p += 4;

                    // check right
                    if (j + 1 < n && grid[i][j + 1] == 1) {
                        p -= 2;
                    }

                    // check down
                    if (i + 1 < m && grid[i + 1][j] == 1) {
                        p -= 2;
                    }
                }
            }
        }

        return p;
    }
};