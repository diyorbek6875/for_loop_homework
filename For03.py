def main(k,n):
    """
    Repeat the number k n times and return to the list view.
    Args:
        k: int
        n: int
    Returns:
        list: return  answer
    """
    list1=[k]
    return list1 * n
k=int(input(""))
n=int(input(""))
print(main(k,n))