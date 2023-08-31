# by Ahmed shokry 
from operator import add, sub, mul, truediv as div 
from random import randint, seed, choice

typer = Typer()

class Crossword:

    ops = {
            -1: add,
            -2: sub,
            -3: mul,
            -4: div
        }

  '''
  + -1
  - -2
  × -3
  ÷ -4
  = -5
  '''
    
    def __init__(self):
        self.dims = 15 
        self.target = 20
      
    def generate(self,):
        
        trials = 0
        counter = 0
        target = self.target
        while counter<target:
            trials = 0
            counter = 0
            arr = [[0 for i in range(self.dims)] for j in range(self.dims)]
            xhis = set([(1,1)])
            yhis = set()
            used = set()
            history = []
            traces = []
            while counter<target:
                trials += 1
                if trials==1000:
                    break
                #print(xhis, yhis,counter%2!=0)
                
                try:
                    xy = choice(list(xhis)) if counter%2==0 else choice(list(yhis))
                except:
                    continue
                if xy[1]+5>self.dims-1:continue
            
                que = arr[xy[0]][xy[1]:xy[1]+5]
                sol = self.question(que)
                if sol==False:
                    if counter%2==0:
                        xhis.remove(xy)
                    else:
                        yhis.remove(xy)

                if all([
                    sol,
                    # equal rules
                    (xy[0]-1>=0 and arr[xy[0]-1][xy[1]+3]==0),
                    (xy[0]+1<=self.dims-1 and arr[xy[0]+1][xy[1]+3]==0),
                    not arr[xy[0]-1][xy[1]+3]>0,
                    # rules of first no.
                    (xy[0]-1>=0 and not arr[xy[0]-1][xy[1]]>0),
                    (xy[0]+1<=self.dims-1 and not arr[xy[0]+1][xy[1]]>0),
                    not (xy[0]+1<=self.dims-1 and xy[0]-1>=0 and arr[xy[0]-1][xy[1]]==-5 and arr[xy[0]-1][xy[1]-1]>0 and arr[xy[0]-1][xy[1]+1]>0),
                    not (xy[0]+1<=self.dims-1 and xy[0]-1>=0 and arr[xy[0]+1][xy[1]]==-5 and arr[xy[0]+1][xy[1]-1]>0 and arr[xy[0]+1][xy[1]+1]>0),

                    arr[xy[0]][xy[1]-1]==0,
                    # rules of seond no.
                    (xy[0]-1>=0 and not arr[xy[0]-1][xy[1]+2]>0),
                    (xy[0]+1<=self.dims-1 and not arr[xy[0]+1][xy[1]+2]>0),
                    arr[xy[0]][xy[1]+5]==0,

                    # rules of third no.
                    (xy[0]-1>=0 and not arr[xy[0]-1][xy[1]+4]>0),
                    (xy[0]+1<=self.dims-1 and not arr[xy[0]+1][xy[1]+4]>0),
                    sol not in history
                ]):
                    if counter%2!=0:
                        xhis = xhis.union({(xy[1], xy[0]),(xy[1]+2, xy[0]),(xy[1], xy[0])}.union({(xy[1]+2, xy[0]-4), (xy[1], xy[0]-4), (xy[1]+4, xy[0]-4),(xy[1]+4, xy[0]-2)}))-used
                        
                        traces.append([(xy[1], xy[0]),(xy[1]+2, xy[0]),(xy[1], xy[0])])
                        
                    else:
                        yhis = yhis.union({(xy[1], xy[0]),(xy[1]+2, xy[0]),(xy[1], xy[0])}.union({(xy[1]+2, xy[0]-4), (xy[1], xy[0]-4),(xy[1]+4, xy[0]-4),(xy[1]+4, xy[0]-2)}))-used
                        traces.append([(xy[0], xy[1],),(xy[0], xy[1]+2),(xy[0], xy[1])])
                    

                    arr[xy[0]][xy[1]:xy[1]+5] = sol
                    used.add(xy)
                    history.append(sol)
                    counter += 1
                    if counter%2!=0:
                        xhis.remove(xy) 
                    else:
                        yhis.remove(xy) 

                    arr = list(map(list,zip(*arr)))


        for trace in traces:
            xy = choice(trace)
            arr[xy[0]][xy[1]] = 999
      
        return arr

    def question(self, arr):
        if not arr:return False
        if arr[3] not in [0,-5] or arr[1]*arr[3]<0:
            return False
        elif arr[0]*arr[2]<0:
            return False
        elif arr[1]==-5 or arr[1]>0 or arr[0]<0 or arr[2]<0:
            return False
        
        arr[3] = -5
        c = 0
        while c<10000:
            arr2 = arr.copy()
            c+=1
            if arr[0]==0:
                arr2[0] = randint(2,50)
            if arr[1]==0:
                arr2[1] = -randint(1,4)
            if arr[2]==0:
                arr2[2] = randint(2,50)
            if arr[4]==0:
                arr2[4] = self.ops[arr2[1]](arr2[0],arr2[2])
                if not (arr2[4]/1).is_integer() or arr2[4]<=0 or arr2[4]>99:
                    continue
                arr2[4] = int(arr2[4])
                break
            elif self.ops[arr2[1]](arr2[0],arr2[2]) != arr2[4]:
                continue
            break
        if c!=10000: 
            return arr2
        else:
            return False
 
        

if __name__=='__main__':
    for i in range(50):
    crossword = Crossword()
    arr = crossword.generate()
    print(arr)
