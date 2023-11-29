#include <stdio.h>
#include <stdlib.h>

int cmpnum(const int *a, const int *b)
{
    return *a - *b;
}

int main(){
    int n,m;
    scanf("%d %d",&n,&m);
    int a[n],b[m],c[n+m];
    for(int i=0;i<n;i++){
        scanf("%d",&a[i]);
        c[i]=a[i];
    }
    for(int j=0;j<m;j++){
        scanf("%d",&b[j]);
        c[n+j]=b[j];
    }
    qsort(c,n+m,sizeof(int),cmpnum);
    int j;
    int k=-1;
    for(int i=0;i<n;i++){
        printf("**\n");
        j=k+1;
        printf("%d\n",j);
        while(j<k+m){
            if(a[i]==c[j]){
            printf("%d* ",j+1);
            k=j;
            break;
            }
            j++;
        }
    }
    printf("\n");
    k=-1;
    for(int i=0;i<m;i++){
        j=k+1;
        while(j<k+m){
            if(b[i]==c[j]){
            //printf("%d ",j+1);
            k=j;
            break;
            }
            j++;
        }
    }

    return 0;
}