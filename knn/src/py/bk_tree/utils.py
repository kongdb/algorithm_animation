#-*- coding:utf-8 -*-


def edit_distance(s1, s2):
    row1 = [i for i in range(len(s2) + 1)]
    row2 = [0 for i in range(len(s2) + 1)]
    for i in range(len(s1)):
        row2[0] = i + 1
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                row2[j+1] = row1[j]
            else:
                row2[j+1] = min(row2[j], row1[j], row1[j+1]) + 1
        row1, row2 = row2, row1
    return row1[-1]


if __name__ == '__main__':
    print(edit_distance("ab", "bbb"))
    print(edit_distance("abc", "bc"))
    print(edit_distance("abc", "abc"))
    print(edit_distance("c", "abc"))
