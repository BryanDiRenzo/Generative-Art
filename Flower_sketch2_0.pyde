w,h = 1000, 1000

#w = int(random(500,1000))
colors = [[(53, 206, 183), (128, 219, 178,), (92, 217, 133), (221, 122, 68)],
[(57,28,98), (95,46,146), (135,245,180), (255,105,104),(225,53,73)],
[(242,146,236), (23,18,147), (64,24,54),(196,166,220), (249,235,40)],
[(248,201,215),(255,186,190),(255,217,186),(255,252,186),(224,255,186)],
[(0,128,128), (36,158,160), (141,229,219),(27,154,140),(255,175,66),(253,86,2)]]

random_colors = int(random(5)) #set the variable random_colors to an integer between 0 and 3 (excluding 4)

def get_random_element(l):
    return l[int(random(len(l)))]


def deformed_circle(x, y, r, random_colors):
    pushMatrix()
    translate(x, y)
    
    points = []
    for i in range(0, 360, 15):
        points.append((r/2.5*sin(radians(i)), r/2.5*cos(radians(i))))
        
    # Create the deformed circle
    final = []
    for p in points:
        x_change = p[0] / int(random(20, 40)) #normally 25, not random fill
        y_change = p[1] / int(random(20,40))
        
        change = random(-10, 10)
        p = (p[0] + x_change * change, p[1] + y_change * change)
        final.append(p)
        
    # Create outline and deformed shape

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

    random_colors = int(random(5))
    background(*get_random_element(colors[random_colors]))
    strokeWeight(2)
    noFill()
    shrinkit = int(random(5, 100)) #shrink amount between layer randomizer
    current_size = 900
    while (current_size >= 0):
        deformed_circle(w/2, h/2, current_size, random_colors)
  
        current_size -= shrinkit #sets the shrink amount between layers
        noLoop()
        
    #save("Name Test/" +str("####") + ".png")
    saveFrame("Name Test/" + "Circle of Life ###.png")#folder destination + file name

        
