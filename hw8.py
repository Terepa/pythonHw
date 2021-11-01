#1.

def get_char_count(s):
    result = {}
    for i in s:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result

print (get_char_count('hubba bubba'))


#2.
def replace_item(d, bad_val, good_val):
    for key, val in d.items():
        if val==bad_val:
            d[key] = good_val
    return d

my_dict= {'a': 5, 'b': 6, 'c': 5}
print(my_dict)
new_dict=replace_item(my_dict, 5, 12)
print(new_dict)
print(my_dict)

# 3.a
def clean_dict_value (d, bad_val):
    backup=d.copy()
    for key, value in d.copy().items():
        if value==bad_val:
            del d[key]
    return(d)

new_dict=clean_dict_value({'a': 5, 'b': 6, 'c': 5}, 5)
print(new_dict)

# 3.b
def clean_dict_value (d, v_list):
    backup=d.copy()
    for key, value in d.copy().items():
        for i in v_list:
            if value==i:
                del d[key]
    return(d)

new_dict=clean_dict_value({'a': 5, 'b': 6, 'c': 5, 'd':3}, [3,4,5])
print(new_dict)