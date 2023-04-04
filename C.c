#include <stdio.h>
#include <stdlib.h>
int cmpnum(const void * n1, const void * n2)
{
	if (*(long *)n1 > *(long *)n2)
	{
		return 1;
	}
	else if (*(long *)n1 < *(long *)n2)
	{
		return -1;
	}
	else
	{
		return 0;
	}
}

int main(){
    int n,x;
    scanf("%d %d",&n,&x);
    if(x==0){
        printf("Yes\n");
        return 0;
    }
    int a[n];
    int b[n];
    scanf("%d",a);
qsort(a,sizeof(a)/sizeof(a[0]),sizeof(int),cmpnum);
int i=0;
while(i<n-1){
    b[i]=a[i+1]-a[i];
    i++;
}
qsort(b,sizeof(b)/sizeof(b[0]),sizeof(int),cmpnum);
i=0;
while(i<n-1){
    if(b[i]==x){
    printf("Yes\n");
    return 0;
    }
    i++;
}
printf("No\n");

    return 0;
}