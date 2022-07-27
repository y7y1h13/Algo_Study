N=int(input())
card=list(map(int,input().split()))
card=sorted(card)
M=int(input())
target_list=list(map(int,input().split()))

def BS(array, target, start, end):
  if start > end:
    return 0
  mid=(start+end)//2
  if array[mid]==target:
    return 1
  elif array[mid]>target:
    return BS(array, target, start, mid-1)
  else:
    return BS(array, target, mid+1, end)

for target in target_list:
  print(BS(card, target, 0, N-1), end=' ')