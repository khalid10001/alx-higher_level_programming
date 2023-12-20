#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    listn = []

    for n in range(list_length):
        try:
            listn.append(my_list_1[n] / my_list_2[n])
        except ZeroDivisionError:
            listn.append(0)
            print("division by 0")
            continue
        except IndexError:
            listn.append(0)
            print("out of range")
            continue
        except TypeError:
            listn.append(0)
            print("wrong type")
            continue
        finally:
            pass
    return listn
