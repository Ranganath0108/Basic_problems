// 5
// 54
// 543
// 5432
// 54321
#include<stdio.h>
int main(int argc, char const *argv[])
{
    int row,col,n=5;
    for(row=1;row<=n;row++){
        for(col=1;col<=row;col++)
        {
            printf("%d",5-col+1);

        }
        printf("\n");
    }




    return 0;
}


