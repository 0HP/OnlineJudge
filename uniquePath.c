#include<stdio.h>
#include<stdlib.h>
int uniquePaths(int m, int n){
  int **a;
  a=(int**)malloc(sizeof(int*)*n);
  for(int i=0;i<n;++i)
  {
    a[i]=(int*)malloc(sizeof(int)*m);
  }
  for(int i=0;i<m;++i)
  {a[0][i]=1;}
  for(int j=0;j<n;++j)
  {a[j][0]=1;}
  for(int x=1;x<n;++x)
  {
    for(int y=1;y<m;++y)
    {a[x][y]=a[x-1][y]+a[x][y-1];}
  }
  return a[n-1][m-1];
}
