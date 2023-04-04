#include <stdio.h>
int main(){
    int n;
    char s[100];
    scanf("%d",&n);
    scanf("%s",s);
   
    int i=0;
    while(i<n){
        if(s[i]==s[i+1]){
        printf("No\n");
        return 0;
        }
        i++;
        
    }
    printf("Yes\n");
    return 0;
}