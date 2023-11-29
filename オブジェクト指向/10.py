class Exercise:
    data=[]
    def add_data(self,lst):
        self.data.append(lst)
#"共通の"クラス変数であるdataリストに値を追加
e1=Exercise()
e1.add_data('value1')
e2=Exercise()
e2.add_data('value2')

for value in e1.data:
    print(f'{value} ',end='')