# 51. 두 정수(a, b)를 입력받아 a의 값이 b의 값과 서로 다르면 True 를, 같으면 False 를 출력하는 프로그램을 작성해보자.
# a,b = input().split()
# print(a!=b)
#######################################################
# 52. 정수가 입력되었을 때, True/False 로 평가해주는 프로그램을 작성해보자.
# print(bool(int(input())))
#######################################################
# 53. 정수값이 입력될 때, 그 불 값을 반대로 출력하는 프로그램을 작성해보자.
# print(not bool(int(input())))
#######################################################
# 54. 2개의 정수값이 입력될 때, 그 불 값이 모두 True 일 때에만 True 를 출력하는 프로그램을 작성해보자.
# a, b = map(bool, map(int, input().split()))
# print(a and b)
#######################################################
# 55. 2개의 정수값이 입력될 때, 그 불 값이 하나라도 True 일 때에만 True 를 출력하는 프로그램을 작성해보자.
# a, b = map(bool, map(int, input().split()))
# print(a or b)
#######################################################
# 56.2개의 정수값이 입력될 때, 그 불 값(True/False) 이 서로 다를 때에만 True 를 출력하는 프로그램을 작성해보자.
# a, b = map(bool, map(int, input().split()))
# print(not(a == b))
#######################################################
# 57. 2개의 정수값이 입력될 때, 그 불 값(True/False) 이 서로 같을 때에만 True 를 출력하는 프로그램을 작성해보자.
# a, b = map(bool, map(int, input().split()))
# print(a == b)
#######################################################
# 58. 두 값의 True / False 값이 모두 False 일 때만 True 를 출력하고, 그 외의 경우에는 False 를 출력한다.
# a, b = map(bool, map(int, input().split()))
# print(not(a or b))
#######################################################
# 63. 입력된 두 정수(a, b) 중 큰 값을 출력하는 프로그램을 작성해보자. 단, 3항 연산을 사용한다.
# a, b = map(int, input().split())
# print(a if (a > b) else b)
#######################################################
# 64. 입력된 세 정수 a, b, c 중 가장 작은 값을 출력하는 프로그램을 작성해보자. 단, 3항 연산을 사용한다.
# a,b,c = map(int, input().split())
# k = a if a<b else b
# print(k if k<c else c)
#######################################################
# 65. 3개의 정수(a, b, c)가 입력되었을 때, 짝수만 출력해보자.
# for i in list(map(int, input().split())):
#     if i %2 == 0:
#         print(i)
#######################################################
# 66. 3개의 정수(a, b, c)가 입력되었을 때, 짝(even)/홀(odd)을 출력해보자.
# for i in list(map(int, input().split())):
#     if i % 2 == 0:
#         print('even')
#     else:
#         print('odd')
#######################################################
# 67. 0이 아닌 정수 1개가 입력되었을 때, 음(-)/양(+)과 짝(even)/홀(odd)을 구분해 분류해보자.
# for i in list(map(int, input().split())):
#     if i < 0 and i % 2 == 0:
#         print('A')
#     elif i<0 and not(i%2==0):
#         print('B')
#     elif i>0 and i%2==0:
#         print('C')
#     else:
#         print('D')
#
#######################################################
# 69. 평가를 문자(A, B, C, D, ...)로 입력받아 내용을 다르게 출력해보자.
# a = input()
# if a == 'A':
#     print('best!!!')
# elif a == 'B':
#     print('good!!')
# elif a == 'C':
#     print('run!')
# elif a == 'D':
#     print('slowly~')
# else:
#     print('what?')
#######################################################
# 70. 월이 입력될 때 계절 이름이 출력되도록 해보자.
# a = int(input())
# if a // 3 == 1:
#     print('spring')
# elif a//3 == 2:
#     print('summer')
# elif a//3 == 3:
#     print('fall')
# else:
#     print('winter')
#######################################################
# 71. 0이 아니면 입력된 정수를 출력하고, 0이 입력되면 출력을 중단해보자.
# while True:
#     a = int(input())
#     if a == 0:
#         break
#     else:
#         print(a)
#######################################################
# 72. 정수(1 ~ 100) 1개가 입력되었을 때 카운트다운을 출력해보자.
# a = int(input())
# while True:
#     if a == 0:
#         break
#     print(a)
#     a -= 1
#######################################################
# 73. 1만큼씩 줄이면서 카운트다운 수가 0이 될 때까지 한 줄에 1개씩 출력한다.
# a = int(input())
# while True:
#     a -= 1
#     print(a)
#     if a == 0:
#         break
#######################################################
# 74. 영문 소문자(a ~ z) 1개가 입력되었을 때, a부터 그 문자까지의 알파벳을 순서대로 출력해보자.
# for i in range(ord('a'), ord(input())+1): print(chr(i),end=' ')
#######################################################
# 75. 정수(0 ~ 100) 1개를 입력받아 0부터 그 수까지 순서대로 출력해보자.
#######################################################
# for i in range(int(input())+1):
#     print(i)
#######################################################
# 76. 정수(0 ~ 100) 1개를 입력받아 0부터 그 수까지 순서대로 출력해보자.
# for i in range(int(input())+1):
#     print(i)
#######################################################
# 77. 정수(1 ~ 100) 1개를 입력받아 1부터 그 수까지 짝수의 합을 구해보자.


#######################################################

#######################################################

#######################################################

#######################################################

#######################################################

#######################################################

#######################################################

#######################################################

#######################################################

#######################################################

#######################################################

#######################################################

#######################################################
#######################################################

#######################################################

#######################################################

#######################################################

#######################################################

#######################################################
#######################################################

#######################################################

#######################################################

#######################################################

#######################################################

#######################################################