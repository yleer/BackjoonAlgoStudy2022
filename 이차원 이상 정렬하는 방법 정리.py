# 정렬의 중요성 https://leedakyeong.tistory.com/entry/python-%ED%8A%9C%ED%94%8C-%EC%A0%95%EB%A0%AC%ED%95%98%EA%B8%B0%EB%91%90-%EB%B2%88%EC%A7%B8-%EC%9B%90%EC%86%8C%EB%A1%9C-%EC%A0%95%EB%A0%AC%ED%95%98%EA%B8%B0-tuple-sorting-in-python

# 정렬할때 lambda 사용하면 더 자유롭게 정렬 가능.


# 이차원 배열일 때


array = [[100,4], [12,2],[2,3]]
# 첫번째 원소로 정렬 하기

# 람다 사용할때 x[0] -> 0번째 원소로 정렬
#  x[1] -> 1번쨰 원소로 정렬
# -x[0] -> 0번쨰 원소로 반대로 정렬
# -x[1] -> 0번쨰 원소로 반대로 정렬
array.sort(key = lambda x:x[0])

print(array)

array.sort(key = lambda x:(x[0], x[1]))
print(array)
array.sort(key = lambda x:(x[1], x[0]))

print(array)



array.sort(key = lambda x:(-x[0], x[1]))
print(array)
array.sort(key = lambda x:(x[0], -x[1]))

print(array)

 # {
 #     1: [[1, 5]],
 #     2: [[0, 4, 5], [2, 3]],
 #     3: [[0, 1, 5], [2, 4]]
 #  }