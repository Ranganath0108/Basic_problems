#include<stdio.h>

int fact(int n){
    if (n == 0 || n == 1)
    return 1;
    else
    return n*fact(n-1);
    }

int combination (int n ,int r){
    int nCr;
    nCr=fact(n)/(fact(n-r)*fact(r));
    return nCr;
}
int main(int argc, char const *argv[])
{
int row,col,space,n;
printf("Enter the number of rows to print \n");
scanf("%d",&n);
for(row=0;row<=n;row++){
    for (space = 1; space <= n+1-row; space++)
        printf(" ");
    for(col=0;col<=row;col++)
        printf("%d ",combination(row,col));

    printf("\n");
    
}
}

