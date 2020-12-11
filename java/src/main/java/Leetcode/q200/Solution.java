package main.java.Leetcode.q200;

public class Solution {
    private int m, n;
    private boolean[][] v;
    void dfs(char[][] grid, int r, int l) {
        if(r>m || l>n || r<0 || l< 0 || !v[r][l] || grid[r][l] == '0')
            return;

        this.v[r][l] = false;
        dfs(grid, r-1, l);
        dfs(grid, r+1, l);
        dfs(grid, r, l-1);
        dfs(grid, r, l+1);
    }

    public int numIslands(char[][] grid) {
        if(grid == null || grid.length == 0){
            return 0;
        }
        int result = 0;
        this.m = grid.length;
        this.n = grid[0].length;
        this.v = new boolean[m][n];
        for(int i=0; i<grid.length; i++){
            for(int j=0; j<grid[0].length; j++){
                if(grid[i][j] == '1'){
                    this.v[i][j] = true;
                }
                else{
                    this.v[i][j] = false;
                }
            }
        }
        for(int i=0; i<grid.length; i++){
            for(int j=0; j<grid[0].length; j++){
                if(grid[i][j] == '1' && this.v[i][j]){
                    dfs(grid, i, j);
                    ++result;
                }
            }
        }
        return result;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        char[][] grid = grid = new char[][]{
                {'1', '1', '1', '1', '0'},
                {'1', '1', '0', '1', '0'},
                {'1', '1', '0', '0', '0'},
                {'0', '0', '0', '0', '0'}
        };
        int result = solution.numIslands(grid);
        System.out.println(result);
    }
}
