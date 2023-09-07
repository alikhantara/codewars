def solution(a):
    word_lenght=len(a)
    res = [(i, i + 1)
        for i in range(len(a))]
    print(res)
solution("abcdefgh")