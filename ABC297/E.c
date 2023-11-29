#include <stdio.h>

typedef struct List {
	struct List *next;
	long long v;
} list;

#define HASH 1000003
const int H_Mod = HASH;

typedef struct {
	long long key;//値段の候補が入る
	int id;
} data;

typedef struct {
	data obj[10000001];
	int size;
} min_heap;

void push(min_heap* h, data x)
{
    /*最小ヒープの末尾に要素を追加するために、
    ヒープのsizeを1増やし、要素を末尾に格納する*/
	int i = ++(h->size);
    int  j = i >> 1;//iを右に1ビットシフトすることでiの半分を格納
    //jはiの親ノードのインデックス(補足2参照)
	data tmp;
	h->obj[i] = x;

//ヒープが最小ヒープの性質(値が最小)を満たすように、要素の位置を再配置するためにループを繰り返す。
	while (j > 0) {
        //親ノード(j)が子ノード(i)より大きければswap
		if (h->obj[i].key < h->obj[j].key) {
			tmp = h->obj[j];
			h->obj[j] = h->obj[i];
			h->obj[i] = tmp;
            //再度その親ノードの親ノードとの比較を行う
			i = j;
			j >>= 1;
		} else break;
	}
}

data pop(min_heap* h)//ヒープ木から最小値を取り出す
{
	int i = 1, j = 2;
	data output = h->obj[1];//最小値を格納
    data tmp;
	h->obj[1] = h->obj[(h->size)--];//ヒープ木のサイズを1減らす
    //ヒープ木の再構築(jはiの左のノードのインデックス)
	while (j <= h->size) {
        //j^=1はjの最下位ビットを反転
		if (j < h->size && h->obj[j^1].key < h->obj[j].key) j ^= 1;
        //iのキー値よりjのキー値が小さければswap
		if (h->obj[j].key < h->obj[i].key) {
			tmp = h->obj[j];
			h->obj[j] = h->obj[i];
			h->obj[i] = tmp;
            //iをjに更新に更新,jを子節点に
			i = j;
			j <<= 1;
		} else break;
	}
	return output;//最小値を返す
}

int main()
{
	int i, N, K, A[11];
	scanf("%d %d", &N, &K);
	for (i = 1; i <= N; i++) scanf("%d", &(A[i]));
	
	int h, k, hn = 0;
	long long x, y;
	static list *hash[HASH] = {}, hd[10000001], *hp;
	data d;
	static min_heap he;
	he.size = 0;
	d.key = 0;
	push(&he, d);
	while (K--) {//K回ループを回す
		d = pop(&he);//ヒープ木から最小値のdataを取り出している
        //printf("%d**\n",d.id);
		x = d.key;//値段の候補
        printf("%lld*\n",x);
		for (i = 1; i <= N; i++) {
			y = x + A[i];//補足参照,yは金額の候補
			h = y % H_Mod;
            //ハッシュテーブルにyがなければ最小ヒープ,ハッシュテーブルに追加する
			for (hp = hash[h]; hp != NULL; hp = hp->next) if (hp->v == y) break;
			if (hp == NULL) {//yに対応するノードがないので追加する
				hd[hn].v = y;
				hd[hn].next = hash[h];
                //hashはhdの各要素のポインタが格納されている
				hash[h] = &(hd[hn++]);//ハッシュ表に追加
				d.key = y;//ヒープ木に追加
				push(&he, d);
			}
		}
	}
	printf("%lld\n", he.obj[1].key);//最小ヒープであるheの根の要素のkey値(値が最小値)
	fflush(stdout);
	return 0;
}