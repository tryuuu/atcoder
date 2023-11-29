#include <stdio.h>

int main(){
  int h,w;
  scanf("%d %d",&h,&w);
  char s[h][w+1];
  for(int i=0;i<h;i++){
    scanf("%s",s[i]);
  }
for(int i=0;i<h;i++){
    int j=0;
    while(j<w-1){
        if(s[i][j]=='T'&&s[i][j+1]=='T'){
            s[i][j]='P';
            s[i][j+1]='C';
            j+=2;
        }else
        j++;
    }
}
for(int i=0;i<h;i++){
    for(int j=0;j<w;j++){
        printf("%c",s[i][j]);
    }
    printf("\n");
}

    return 0;
}
//文字列sはNULL終端を含めるためw+1だけ取っておくことに注意