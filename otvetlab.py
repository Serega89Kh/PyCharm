def main(*args):
    return sorted(args)
    
print(main(3, 2, 1, 49, 0))
if __name__ == '__main__':
    assert main(3, 2, 1, 49, 0) == [0, 1, 2, 3, 49], "Сортировка не удалась"
    assert main(5, 4, 3, 2, 1) == [1, 2, 3, 4, 5], "Сортировка не удалась"
