#include <stdio.h>
int main(){
    char s[8];
    int sum=0;
    int count=0;
    int flag=0;
    scanf("%s",s);
    for(int i=0;i<8;i++){
        if(s[i]=='B'){
            sum+=i;
        }
        if(s[i]=='R'){
            count++;
        }
        if(count==1&&s[i]=='K'){
            flag=1;
        }
    }
    if(sum%2==1&&flag==1){
        printf("Yes\n");
        return 0;
    }
    printf("No\n");
    return 0;
}