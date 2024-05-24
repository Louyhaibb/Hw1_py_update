def join(*lists, sep='-'):
    if not lists:
        return None

    list = []
    for i, curr_list in enumerate(lists):
        if i > 0:
            list.append(sep)
        list.extend(curr_list)
    return list

if __name__ == '__main__':
    print(join([1, 2], [8], [9, 5, 6], sep='@'))
    print(join([1, 2], [8], [9, 5, 6]))
    print(join([1]))
    print(join())
