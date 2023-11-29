#include <stdio.h>
#include <string.h>

#define MAX_N 100009
#define MAX_S 26

char S[MAX_N];
int N,K;
int nex[MAX_N][MAX_S];

int main() {
    // Step #1. 入力
    scanf("%d %d", &N, &K);
    scanf("%s", S);

    // Step #2. 前計算
    for (int i = 0; i < MAX_S; i++) nex[strlen(S)][i] = strlen(S);
    for (int i = (int)strlen(S) - 1; i >= 0; i--) {
        for (int j = 0; j < MAX_S; j++) {
            if ((int)(S[i] - 'a') == j) {
                nex[i][j] = i;
            }
            else {
                nex[i][j] = nex[i + 1][j];
            }
        }
    }

    // Step #3. 一文字ずつ貪欲に決める
    char Answer[MAX_N];
    int CurrentPos = 0;
    for (int i = 1; i <= K; i++) {
        for (int j = 0; j < MAX_S; j++) {
            int NexPos = nex[CurrentPos][j];
            int MaxPossibleLength = (int)(strlen(S) - NexPos - 1) + i;
            if (MaxPossibleLength >= K) {
                Answer[i - 1] = (char)('a' + j);
                CurrentPos = NexPos + 1;
                break;
            }
        }
    }
    Answer[K] = '\0';

    // Step #4. 出力
    printf("%s\n", Answer);
    return 0;
}
