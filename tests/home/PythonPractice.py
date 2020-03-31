def div(a, b):
    print(a / b)


def smart_div(fun):

    def inn(a, b):
        if a < b:
            a, b = b, a
        return fun(a, b)

    return inn


# div = smart_div(div)

div(2, 4)
