#!/usr/bin/python3
def uniq_add(my_list=[]):
    already = []
    plu = 0
    if my_list:
        for x in my_list:
            if x not in already:
                plu += x
                already.append(x)
    return plu
