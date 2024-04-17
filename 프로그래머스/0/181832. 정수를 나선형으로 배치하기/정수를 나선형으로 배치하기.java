class Solution {
    public int[][] solution(int n) {
        int[][] spiral = new int[n][n];
        int[] dx = {0, 1, 0, -1};
        int[] dy = {1, 0, -1, 0};
        int num = 1;
        int direction = 0;
        int x = 0;
        int y = 0;
        
        for (int i = 0; i < n * n; i++){
            spiral[x][y] = num++;
            int nx = x + dx[direction];
            int ny = y + dy[direction];
            
            if (nx >= 0 && nx < n && ny >= 0 && ny < n && spiral[nx][ny] == 0) {
                x = nx;
                y = ny;
            } else {
                direction = (direction + 1) % 4;
                x += dx[direction];
                y += dy[direction];
            }
        }
        
        return spiral;
    }
}