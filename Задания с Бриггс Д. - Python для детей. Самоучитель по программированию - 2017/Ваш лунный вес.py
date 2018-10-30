import sys
def moon_weght(weight, wag, year):
    print ("Ваш земной вес")
    weight=float(sys.stdin.readline())
    print ("Прирост веса")
    wag=float(sys.stdin.readline())
    print ("Годы")
    year=int(sys.stdin.readline())
    year=year+1
    for year in range(1,year):
        
        
