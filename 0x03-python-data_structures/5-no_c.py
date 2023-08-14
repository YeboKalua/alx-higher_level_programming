def no_c(my_string):
    rem = 'cC'
    new_string = "".join(ch for ch in my_string if ch not in rem)
    return new_string
