#include <stdio.h>
int main(){
    int n,d;
    scanf("%d %d",&n,&d);
    int t[n];
    int i;
    for(i=0;i<n;i++){
        scanf("%d",&t[i]);
    }
    for(i=0;i<n-1;i++){
        if(t[i]+d>=t[i+1]){
            printf("%d\n",t[i+1]);
            return 0;
        }
    }
    printf("-1\n");
    return 0;
}