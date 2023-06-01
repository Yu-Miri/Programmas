def solution(cacheSize, cities):
    time = 0
    cities = list(map(lambda x:x.lower(), cities))
    if cacheSize==0:
        return len(cities)*5
    else:
        cache = []
        for city in cities:
            if city not in cache:
                cache.append(city)
                time += 5
                if len(cache) > cacheSize:
                    del cache[0]
            elif city in cache:
                city_idx = cache.index(city)
                cache.pop(city_idx)
                cache.append(city)
                time+=1
    return time