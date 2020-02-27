if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    arr.sort(reverse=True)
    winner = arr[0]
    for r in arr:
        if r != winner:
            print(r)
            break
