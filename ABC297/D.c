#include <stdio.h>
long long ab(long long a,long long b){
    if(a>b){
        return a/b-1;
    }
   
    return b/a-1;
    
}
int main(){
    long long a,b;
    long long count=0;
    scanf("%lld %lld",&a,&b);
    while(a!=b){
        if(a>b){
             if(ab(a,b)==0){
            count++;
            a=a-b;
             }
            else{
            count+=ab(a,b);
            a=a-b*ab(a,b);
            }
        }
        if(a<b){
             if(ab(a,b)==0){
            count++;
            b=b-a;
             }
            else{
            count+=ab(a,b);
            b=b-a*ab(a,b);
            }
        }
    }
    printf("%lld\n",count);
    return 0;
}