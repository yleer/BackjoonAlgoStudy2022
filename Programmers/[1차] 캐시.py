
import collections

cacheSize = 2
cities = ["Jeju", "Pangyo", "NewYork", "newyork"]


caches = collections.deque()
result = 0ㅂ

for city in cities:
    a = city.lower()
    if a not in caches: 
        if len(caches) < cacheSize:
            caches.append(a)
            result += 5
        else:
            if caches:
                caches.popleft()
            if cacheSize > 0:
                caches.append(a)
            result += 5

    else:
        caches.remove(a)
        caches.append(a)
        result += 1




print(result)
