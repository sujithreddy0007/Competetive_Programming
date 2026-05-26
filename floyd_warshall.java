java.util.*;
class Solution {
    public void shortestDistance(int[][] mat) {
        int n=mat.length;
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<n;j++)
            {
                if(mat[i][j]==-1)
                {
                    mat[i][j]=Integer.MAX_VALUE;
                }
                if(i==j)
                mat[i][j]=0;
            }
        }
        for(int k=0;k<n;k++)
        {
            for(int i=0;i<n;i++)
            {
                for(int j=0;j<n;j++)
                {
                    if(mat[i][k]!=Integer.MAX_VALUE && mat[k][j]!=Integer.MAX_VALUE)
                    mat[i][j]=Math.min(mat[i][j],mat[i][k]+mat[k][j]);
                }
            }
        }
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<n;j++)
            {
                if(mat[i][j]==Integer.MAX_VALUE)
                {
                    mat[i][j]=-1;
                }
            }
        }
        return;
    }
}