N=int(input());S=[[0]for i in range(N+9)]
for i in range(N):k,v=map(int,input().split());S[i+k]+=[max(sum(S[:i+1],[]))+v]
print(max(sum(S[:N+1],[])))