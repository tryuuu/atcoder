#include <stdio.h>
#include <stdlib.h>
int	N;
int	L;
int	K;
int	A[100000 + 1];

void binary_search(a,b){
    int mid=10;
    int *sum = malloc(sizeof(int) * (N + 1));
    sum[0]=0;
    int j=0;
    for(int i=0;i<N;i++){
        if(sum[j]<mid){
            sum[j]+=A[i];
            printf("%d\n",sum[j]);
        }else{
            sum[j]=0;
            j++;
            sum[j]+=A[i];
        }
    }
    // while(j>=0){
    //     if(sum[j]<mid){
    //         mid=(a+mid)/2;
    //         free(sum);
    //        return binary_search(a,mid);
    //     }
    //     j--;
    // }
    // free(sum);
    // return mid;
}
 
int	main(void)
{
	scanf("%d %d", &N, &L);
	scanf("%d", &K);
	for (int i = 0; i < N; i++)
		scanf("%d", &A[i]);
	A[N] = L;
    binary_search(1,L);
	//printf("%d\n", binary_search(1, L));
}

