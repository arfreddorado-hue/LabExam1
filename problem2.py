def towerHnaoi(n, source, auxiliary, target):
        if n==1:
            print("Move disls 1 from rod " + source + "to rod" + target)
            return
        towerHnaoi