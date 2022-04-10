import heapq

# heapq는 우선순위 큐 관련 문제 사용하면 좋음. heap에 push 하는 것만으로도 바로 정렬이 됨.(오름 차순임)
# pop하면 제일 작은 값이 pop 결과로 나옴,


# 가끔 pop할때 제일 큰 값이 먼저 나오는 자료 구조를 원할 수 있음.
# 그럴 때는 push pop 하는 값에 -1를 곱하면 된다.


# 아래는 간단한 예제이다.
#
# heap = []
# x = []
# item = 1
# heapq.heappop(heap)
# heapq.heapify(x)
# heapq.heappush(heap, item)


# heap에서 가장 작은 항목을 팝하고 반환하며, 새로운 item도 푸시합니다. 힙 크기는 변경되지 않습니다. 힙이 비어 있으면, IndexError가 발생합니다.
# 이 한 단계 연산은 heappop()한 다음 heappush()하는 것보다 더 효율적이며 고정 크기 힙을 사용할 때 더 적합 할 수 있습니다.
# 팝/푸시 조합은 항상 힙에서 요소를 반환하고 그것을 item으로 대체합니다.
# heapq.heapreplace(heap, item)



n = 3

a = [4,5,2,1,3,7,6,8,9]

# iterable에 의해 정의된 데이터 집합에서 n 개의 가장 큰 요소로 구성된 리스트를 반환합니다.
large = heapq.nlargest(n, a, key=None)


# iterable에 의해 정의된 데이터 집합에서 n 개의 가장 작은 요소로 구성된 리스트를 반환합니다.
# key가 제공되면 iterable의 각 요소에서 비교 키를 추출하는 데 사용되는 단일 인자 함수를 지정합니다
small = heapq.nsmallest(n, a, key=None)


# 위 두 함수는 n이 너무 크면 안좋음. 작을때 사용하자.

print(large,small)

# heapq.heappushpop(heap, item)







# heapq.merge(*iterables, key=None, reverse=False) 아직 x