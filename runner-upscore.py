if __name__ == '__main__':
    n = int(input())
    arr =  input()
    numb = list(map(int, arr.split(' ')))
    numb.sort(reverse=True)
    lar  = max(numb)
    i = 0 
    while (i<n):
        if lar == max(numb):
         numb.remove(max(numb))
        i+=1
     
    print(max(numb))

