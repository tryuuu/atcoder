#include <stdio.h>
#include <stdlib.h>

int cmpnum(const int *a, const int *b)
{
    return *a - *b;
}

int count2(int count){
    count++;
   return count/2;
}

int main(){
    int n;
    scanf("%d",&n);
    int a[n+1];
    int i=0;
    while(i<n){
        scanf("%d",&a[i]);
        i++;
    }
    a[n]=-1;
    //printf("%d*\n",count2(3));
    qsort(a,n,sizeof(int),cmpnum);
    i=1;
    int count=0;
    int result=0;
    while(i<=n){
        if(a[i]==a[i-1]){
            count++;
        }else{
             result+=count2(count);
             count=0;
        }
        i++;
    }
    printf("%d\n",result);
    return 0;
}