if __name__ == '__main__':
    arr= []
    scorelist = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr+= [[name, score]]
        scorelist+= [score]
    scorelist = list(dict.fromkeys(scorelist))
    b = sorted(scorelist)[1]
    for a, c in sorted(arr):
        if c==b:
            print(a)
    
