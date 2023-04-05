#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_result = []
    for i in range(list_length):
        try:
            prc = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            prc = 0
        except TypeError:
            print("wrong type")
            prc = 0
        except IndexError:
            print("out of range")
            prc = 0
        finally:
            new_result.append(prc)

    return (new_result)
