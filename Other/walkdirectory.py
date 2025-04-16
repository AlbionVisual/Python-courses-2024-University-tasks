import sys, os

def sort(arr):
    for i in range(len(arr)):
        isSorted = True
        for j in range(len(arr) - i - 1):
            if arr[j][0] < arr[j+1][0]:
                isSorted = False
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if isSorted: break
    return arr

def walkdirectory(path):

    res = []

    def unpackFolder(path):
        current = os.listdir(path)
        for el in current:
            # if os.path.isdir(path + el):
            #     unpackFolder(path + el + '/')
            # elif os.path.isfile(path + el):
                res.append([os.stat(path + el).st_size, path + el])

    unpackFolder(path + '/' if path[-1] != '/' else path)

    res = sort(res)

    return res

res =  walkdirectory(sys.argv[1])
print('Files: ' + str(len(res)))
for el in res:
    [size, path] = el
    size, type = (size / 1024, 'KB') if size < 1024**2 else (size / 1024**2, 'MB') if size < 1024**3 else (size / 1024**3, 'GB')
    print("{:7.2f}".format(size) + ' ' + type + ' ' + path)