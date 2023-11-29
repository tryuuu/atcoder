n, m = map(int, input().split())
a = list(map(int, input().split()))
sorted_a=sorted(a)
s = [input() for _ in range(n)]
score = [0]*n
def min_questions_to_exceed(test_data, current_score, desired_score):
    if current_score >= desired_score:
        return 0

    diff = desired_score - current_score
    sorted_tests = sorted(test_data, key=lambda x: x[0],reverse=True)  # 昇順に変更
    total = 0
    count = 0
    for score, result in sorted_tests:
        if result == 'x':  
            total += score
            count += 1
            if total >= diff:
                return count
    return -1

for i in range(n):
    score[i]=i+1
    for j in range(m):
        if s[i][j] == 'o':
            score[i]+=a[j]
sorted_score=sorted(score)
other_list=[[] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i!=j:
            other_list[i].append(score[j])
max_list=[]
for i in range(n):
    max_list.append(max(other_list[i]))

for i in range(n):
    data=list(zip(a,s[i]))
    sorted_data_asc = sorted(data, key=lambda x: x[0])
    print(min_questions_to_exceed(sorted_data_asc,score[i],max_list[i]))
