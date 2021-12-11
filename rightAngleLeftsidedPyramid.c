// 
//        *
//       **
//      ***
//     ****
//    *****
//   ******
//  *******
// ********
#include<stdio.h>
int main(int argc, char const *argv[])
{
    int row,symbol,space,n=10;
    for(row=1;row<=n;row++){
        for(space=1;space<=n-row;space++)
        printf(" ");
        for (symbol=1;symbol<=row;symbol++)
        printf("*");
        printf("\n");
    }
    return 0;}