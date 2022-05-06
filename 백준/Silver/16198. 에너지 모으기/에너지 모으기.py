def dfs(tmp):
    global ans
    if len(a)==2:
        ans=max(ans,tmp)
        return
    for i in range(1,len(a)-1):
        k=a[i]
        del a[i]
        dfs(tmp+a[i-1]*a[i])
        a.insert(i,k)
N,a=int(input()),list(map(int,input().split()))
ans=0
dfs(0)
print(ans)