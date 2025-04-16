from sys import argv as entries

def mergepostfix(arr):

    post1 = post2 = ''
    if len(arr) > 2:
        post1 = mergepostfix(arr[0:len(arr) // 2])
        post2 = mergepostfix(arr[len(arr) // 2:])
    elif len(arr) == 2:
        post1, post2 = arr
    else: return arr[0]
    
    i = 1
    while post1[-i:] == post2[-i:] and len(post1) > i:
        i += 1
    i -= 1

    return post1[-i:] if i != 0 else ''

print(mergepostfix(entries[1].split()))