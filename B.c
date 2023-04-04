#include <stdio.h>
int main(){
    char s[8][8];
    int i=0;
    while(i<8){
        scanf("%s",s[i]);
        i++;
    }
    i=0;
    int j;
    while(i<8){
        j=0;
        while(j<8){
            if(s[i][j]=='*'){
                char c='a';
            printf("%c",c+j);
            printf("%d\n",8-i);
            return 0;
            }
            j++;
        }
        i++;
    }
    return 0;
}