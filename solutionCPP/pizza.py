class Slice():

    def __init__(self,pizza,x,y):
        self.pizza = pizza
        self.x=x
        self.y=y
            self.shape= pizza.maxArea * (pizza.maxArea - 1) + 1



    def setArea(self):
        while True:
            self.shape-=1
            if(self.shape == 0)
                return False
            self.height= (self.shape // self.pizza.maxArea) + 1
            self.width= (self.shape % self.pizza.maxArea) + 1
            if(self.evaluate())
                self.populate()
                return True



    def populate(self,fill=True):
        value = 10
        if(!fill)
            value = -10

        for x in range(0,self.width):
            for y in range(0,self.height):
                self.pizza.setPos(x,y,value)




    def evaluate(self):
        ingredients = [0,0]

        if(self.width * self.height > self.pizza.maxArea)
            return False

        for x in range(0,self.width):
            for y in range(0,self.height):
                val = self.pizza.getPos(x+self.x,y + self.y)
                if(val // 10 == 1):
                    return False
                ingredients[val % 10]+=1


        return (ingredients[0] >= pizza.minIngre and ingredients[1] >= pizza.minIngre)





class Pizza():
    def __init__(self,pizza,r,c,l,h):
        self.pizza=pizza
        self.rows=r
        self.columns=c
        self.minIngre=l
        self.maxArea=h

    def getPos(self,x,y):
        return self.pizza[x+self.columns*y]

    def setPos(self,x,y,val):
        return self.pizza[x+self.columns*y] +=val


def solvePizza():
    pizzaValues=[  0,1,1,1,0,0,0,
                   1,1,1,1,0,1,1,
                   0,0,1,0,0,1,0,
                   0,1,1,0,1,1,1,
                   0,0,0,0,0,0,1,
                   0,0,0,0,0,0,1];

    pizza = Pizza(pizzaValues,6,7,1,5)
    slices = []
    firstSlice = Slice(pizza,0,0)
    slices.append(firstSlice)
    positions=[]

    while True:
        currSlice = slices[-1]
        succeded = currSlice.setArea()
        if(succeded)
            slices.append(Slice(pizza,positions[-1][0],positions[-1][1]))
            slices.remove(positions[-1])




    def getNeighbours(slice):

        neighbours= tup(slice.x + slice.width, slice.y)
        if(checkInBounds(slice.pizza,neighbours))
            positions.append(neighbours)

        neighbours= tup(slice.x,slice.y + slice.height)
        if(checkInBounds(slice.pizza,neighbours))
            positions.append(neighbours)



    def checkInBounds(pizza,pos):
        return (pos[0] < pizza.columns and pos[1] < pizza.rows)
