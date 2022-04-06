# Key를 기준으로 정렬 하기

my_dict = {'c': 3, 'a': 1, 'b': 2, 'e': 1, 'd': 2}

sorted_dict = sorted(my_dict.items())
print(sorted_dict)



# Value를 기준으로 정렬 하기
sorted_dict = sorted(my_dict.items(), key = lambda item: item[1])
print(sorted_dict)

sorted_dict2 = sorted(my_dict.items(), key = lambda item: item[1], reverse=True)
print(sorted_dict2)





#   https://codechacha.com/ko/python-sorting-dict/