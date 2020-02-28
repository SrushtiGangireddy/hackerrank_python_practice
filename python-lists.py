if __name__ == '__main__':
    N = int(raw_input())
    result = []
    for n in range(N):
        query = raw_input()
        q = query.split(' ')
        if q[0] == 'insert':
            result.insert(int(q[1]),int(q[2])) 
        elif q[0] == 'print':
            print result
        elif q[0] == 'remove':
            result.remove(int(q[1]))
        elif q[0] == 'append':
            result.append(int(q[1]))
        elif q[0] == 'sort':
            result.sort()
        elif q[0] == 'pop':
            result.pop()
        elif q[0] == 'reverse':
            result.reverse()
