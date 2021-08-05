w,h = 1200, 1200

#w = int(random(500,1000))
colors = [[(53, 206, 183), (128, 219, 178,), (92, 217, 133), (221, 122, 68)],
[(53, 206, 183), (128, 219, 178,), (92, 217, 133), (221, 122, 68)],
[(53, 206, 183), (128, 219, 178,), (92, 217, 133), (221, 122, 68)],
[(53, 206, 183,int(random(0,256))), (128, 219, 178,int(random(0,256))), (92, 217, 133,int(random(0,256))), (221, 122, 68,int(random(0,256)))], #Sorbet Palette
[(57,28,98), (95,46,146), (135,245,180), (255,105,104),(225,53,73)],
[(57,28,98), (95,46,146), (135,245,180), (255,105,104),(225,53,73)],
[(57,28,98), (95,46,146), (135,245,180), (255,105,104),(225,53,73)],
[(57,28,98, int(random(0,256))), (95,46,146, int(random(0,256))), (135,245,180, int(random(0,256))), (255,105,104, int(random(0,256))),(225,53,73, int(random(0,256)))], # El tropico palette
[(242,146,236), (23,18,147), (64,24,54),(196,166,220), (249,235,40)],
[(242,146,236,int(random(0,256))), (23,18,147,int(random(0,256))), (64,24,54,int(random(0,256))),(196,166,220,int(random(0,256))), (249,235,40,int(random(0,256)))], # Cyberpunk palette
[(248,201,215),(255,186,190),(255,217,186),(255,252,186),(224,255,186)],
[(248,201,215),(255,186,190),(255,217,186),(255,252,186),(224,255,186)],
[(248,201,215,int(random(0,256))),(255,186,190,int(random(0,256))),(255,217,186,int(random(0,256))),(255,252,186,int(random(0,256))),(224,255,186,int(random(0,256)))], #pastel cream palete
[(0,128,128), (36,158,160), (141,229,219),(27,154,140),(255,175,66),(253,86,2)],
[(0,128,128), (36,158,160), (141,229,219),(27,154,140),(255,175,66),(253,86,2)],
[(0,128,128), (36,158,160), (141,229,219),(27,154,140),(255,175,66),(253,86,2)],
[(0,128,128,int(random(0,256))), (36,158,160,int(random(0,256))), (141,229,219,int(random(0,256))),(27,154,140,int(random(0,256))),(255,175,66,int(random(0,256))),(253,86,2,int(random(0,256)))], #aqua heat 
[(195,151,20), (127,67,17), (54,31,0),(192,192,192),(123,144,149)], #chrome palette
[(int(random(0,256)),int(random(0,256)),int(random(0,256)),int(random(0,256))), (int(random(0,256)),int(random(0,256)),int(random(0,256)),int(random(0,256))), (int(random(0,256)),int(random(0,256)),int(random(0,256)),int(random(0,256))),(int(random(0,256)),int(random(0,256)),int(random(0,256)),int(random(0,256))),(int(random(0,256)),int(random(0,256)),int(random(0,256)),int(random(0,256)))], #random palette palette
[(0,0,0),(255,255,255,int(random(0,256))),(255,255,255)]] #B&W

random_colors = int(random(20)) #choose a random palette from the color dictionary

def get_random_element(l):
    return l[int(random(len(l)))]


def deformed_circle(x, y, r, random_colors):
    pushMatrix()
    translate(x, y)
    
    points = []
    for i in range(0, 360, 15):
        points.append((r/2.2*sin(radians(i)), r/2.2*cos(radians(i))))
        
    # Create a circle
    final = []
    for p in points:
        x_change = p[0] / int(random(25, 45)) 
        y_change = p[1] / int(random(25,45))
        
        change = random(-10, 10)
        p = (p[0] + x_change * change, p[1] + y_change * change)
        final.append(p)
        
    # Create outline and morph shape

    fill(*get_random_element(colors[random_colors]))
    strokeWeight(2)
    beginShape()
    for p in final:
        curveVertex(*p)
    curveVertex(*final[0])
    curveVertex(*final[1])
    curveVertex(*final[2])
    endShape()
    
    
    popMatrix()
    
def setup():
    size(w, h)
    pixelDensity(1)
   

def draw():

    random_colors = int(random(20))
    background(*get_random_element(colors[random_colors]))
    strokeWeight(2)
    noFill()
    shrinkit = int(random(5, 110)) #shrink amount between layer randomizer
    current_size = 900
    while (current_size >= 0):
        deformed_circle(w/2, h/2, current_size, random_colors)
  
        current_size -= shrinkit #sets the shrink amount between layers
        #noLoop()
    print([random_colors, shrinkit])    
    #save("Name Test/" +str("####") + ".png")
    saveFrame("Final3/" + "Perpetual Petals ###"+".png")#folder destination + file name

        
