#include<iostream>
using namespace std;
int main(int argc, char const *argv[])
{
int row,symbol,space,n=5;
for(row=1;row<=n;row++){
    // print spaces
    for(space=1;space<=n-row;space++)
    cout<<" ";
    // print symbol
    for(symbol=1;symbol<=2*row-1;symbol++)
    cout<<"*";

cout<<"\n";}
    return 0;
}


