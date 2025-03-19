def even_sqrt(lst:list[int, float]) -> list:
    def sqrt():
        return sum([i**2 for i in lst if i%2==0])
    return sqrt
res = even_sqrt([1, 2, 3, 4, 5, 6, 7, 8])
print(res())