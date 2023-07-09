# 내 쓰레기 코드..^^ 최악의 경우 시간복잡도가 O(N)이 될..코드
def function1(n, k):
    count = 0
    while (n != 1):
        if n % k == 0:
            n = devision(n,k)
            count += 1
        else:
            while(n % k != 0):
                if n == 1:
                    break
                else:
                    n = minus(n)
                    count += 1
    return print("최소 횟수",count)
def minus(n):
    return (n - 1)

def devision(n, k):
    return (n // k)

function1(25, 3)

# GPT가 효율성 높게 수정한 코드
# def function1(n, k):
#     count = 0
#     while n != 1:
#         if n % k == 0:
#             n //= k
#             count += 1
#         else:
#             remain = n % k
#             n -= remain
#             count += remain
#
#     return count
#
# print("최소 횟수", function1(25, 3))