import py_compile


def main(n):
    """
    Return numbers from zero to n in a list view.
    Args:
        n: int
    Returns:
        list: return  answer
    """

    list1=list(range(n))
    return list1
n=int(input())
print(main(n))