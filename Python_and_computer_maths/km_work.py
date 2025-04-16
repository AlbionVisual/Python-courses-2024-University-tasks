

def flatten_list(nested_obj):
    res = []
    if isinstance(nested_obj, list):
        assert nested_obj not in nested_obj, "syclic object"
        for i in nested_obj:
            res += flatten_list(i)
    else: return [nested_obj]
    return res


lst = [1,2,3,4, [1,6,8,4], [13,5,[1,4]]]
print(lst)
print(flatten_list(lst))

lst[3] = lst
print(lst)
print(flatten_list(lst))