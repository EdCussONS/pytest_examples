

def add(a, b):
    # if not all([isinstance(a, (int, float)), isinstance(b, (int, float))]):
    #     raise TypeError(f"add expects [int, int] got [{type(a)}, {type(b)}]") 
    return a + b


def add_to_list(inp_list, addition):
    inp_list.append(addition)
    return inp_list


def divide(a, b):
    if not all([isinstance(a, (int, float)), isinstance(b, (int, float))]):
        raise TypeError(f"add expects [int, int] got [{type(a)}, {type(b)}]") 
    try:
        return a / b
    except ZeroDivisionError as e:
        print(e)
        