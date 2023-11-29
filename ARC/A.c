#include <stdio.h>

long long gcd(long long a,long long b){
   if(b==0)return a;
   else return gcd(b,a%b);
}

long long min(long long a,long long b){
    if(a>b)
    return b;
    else
    return a;
}

void gcdsub(long long a,long long b){
    long long count=0;
     while(a>0&&b>0){
        long long g=gcd(a,b);
       
        a=a-g;
        b=b-g;
        long long g2=gcd(a,b);
        if(g==g2&&(b-a==g)){
            count=count+(min(a,b)+g)/g;
             printf("%lld\n",count);
             return;
        }
        count++;
    }
    printf("%lld\n",count);
}

int main(){
    long long a,b;
    scanf("%lld %lld",&a,&b);
    gcdsub(a,b);
    return 0;
}