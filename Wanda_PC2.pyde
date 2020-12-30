clusterList = []
clusterPos = PVector(0,0)
removeNr = 0

def setup():
   #size(800,600, P2D)
    fullScreen(P2D,1)
    noCursor()
    background(0)
def draw():  
   # fill(0,0,0,10)
   # rect(0,0,width,height)  
    background(0)
    noStroke()
    removeItem = False
    for i in range(len(clusterList)):
        clusterList[i].display()
        for j in range(len(clusterList[i].off)):
            if clusterList[i].off[j].y > 2*height:
                removeItem = True
                removeNr = i
    if removeItem:
        del clusterList[removeNr]
       # print('removed!')
        
def keyPressed():
    clusterPos = PVector(random(width),random(height))
    mkCluster(clusterPos)

def mouseClicked():
    clusterPos = PVector(mouseX, mouseY)
    mkCluster(clusterPos)

def mkCluster(pos):
    cluster = Cluster(pos)
    clusterList.append(cluster)

class Cluster(object):
    def __init__(self, input):
        self.scl = random(1, 3)*((width/800)*2)
        self.n = int(random(5, 30))
        self.col = color(random(255),random(255),random(255))
        self.pos = input
        self.s = []
        self.off = []
        self.g = []
        for i in range(self.n):
            self.s.append(random(5,50)*self.scl)
            self.off.append(PVector(random(3*self.scl*self.n), random(3*self.scl*self.n)))
            self.g.append(PVector(5,random(0.1,2)))
        
    def display(self):
        fill(self.col)
        for i in range(self.n):
          #  self.off[i].x 
            self.off[i].y += self.g[i].y
            self.g[i].y += 0.1
            ellipse(self.pos.x + self.off[i].x ,self.pos.y + self.off[i].y, self.s[i], self.s[i])
