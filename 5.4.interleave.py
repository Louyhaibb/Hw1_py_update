def interleave(*it_s):
    iterators = [iter(x) for x in it_s]
    res = []
    while True:
        current = []
        for i in iterators:
            try:
                current.append(next(i))
            except StopIteration:
                continue
        if not current:
            break
        res.extend(current)
    return res
def interleave_generator(*it_s):
    ite_s = [iter(x) for x in it_s]
    while True:
        current = []
        for it in ite_s:
            try:
                yield next(it)
            except StopIteration:
                continue
        if not current:
            break


if __name__ == '__main__':
    inter_list = interleave('abc', [1, 2, 3], ('!', '@', '#'))
    print(inter_list)
    generator_res = list(interleave_generator('abc', [1, 2, 3], ('!', '@', '#')))
    print(generator_res)
# in this code i use (stack overflow+ geeksforgeeks+ gpt)