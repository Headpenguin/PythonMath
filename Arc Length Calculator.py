'''
This program only calulates lengths that are 90 degrees or less in the upper-right quadrant.
'''
import math
pi = 3.1415926535
p = 100
intersections = []
p2 = 10
#a is point a on a quarter circle, b is point b on a quarter circle, r is the radius of the full circle corresponding to the quarter circle
def arcLength(a, b, r):
    global intersections
    #c is the circumference of a whole circle
    c = 2*pi*r
    #d is the distance between point a and b 
    d = math.sqrt((a[0] - b[0])*(a[0] - b[0])+(a[1] - b[1])*(a[1] - b[1]))
    print(d)
    xcoords = []
    ycoords = []
    xcoords2 = []
    ycoords2 = []
    length = 0
    intersections = [a, b]
    success = True
    stop = False
    stopInner = False
    currentCoords = b
    while(not stop):
        xcoords = []
        ycoords = []
        xcoords2 = []
        ycoords2 = []		
        success = True
        for x in range(0, round(d*p)):
            xcoords.append(x/p+currentCoords[0])
            ycoords.append(math.sqrt(d*d-(x/p)*(x/p))+currentCoords[1])
        length = len(xcoords)
        for i in range(0, length):
            xcoords.append(-xcoords[i] + 2*currentCoords[0])
            ycoords.append(ycoords[i])
        for i in range(0, length):
            xcoords.append(xcoords[i])
            ycoords.append(-ycoords[i] + 2*currentCoords[1])
        for i in range(0, length):
            xcoords.append(-xcoords[i] + 2 * currentCoords[0])
            ycoords.append(-ycoords[i] + 2 * currentCoords[1])
        for y in range(0, round(d*p)):
            ycoords2.append(y/p+currentCoords[1])
            xcoords2.append(math.sqrt(d*d-(y/p)*(y/p))+currentCoords[0])
        length = len(ycoords2)
        for i in range(0, length):
            xcoords2.append(-xcoords2[i] + 2*currentCoords[0])
            ycoords2.append(ycoords2[i])
        for i in range(0, length):
            xcoords2.append(xcoords2[i])
            ycoords2.append(-ycoords2[i] + 2*currentCoords[1])
        for i in range(0, length):
            xcoords2.append(-xcoords2[i] + 2 * currentCoords[0])
            ycoords2.append(-ycoords2[i] + 2 * currentCoords[1])
        for i in range(0, len(xcoords)):
            if stopInner:
                break
            if xcoords[i]*xcoords[i]+ycoords[i]*ycoords[i] <= (r+p/(p*p))*(r+p/(p*p)) and xcoords[i]*xcoords[i]+ycoords[i]*ycoords[i] >= (r-p/(p*p))*(r-p/(p*p)):
                stop = True
                for n in intersections:
                    if xcoords[i] <= n[0]+.1 and ycoords[i] <= n[1]+.1 and xcoords[i] >= n[0]-.1 and ycoords[i] >= n[1]-.1:
                        if n[0] >= intersections[0][0] - 1/p2 and n[0] <= intersections[0][0] + 1/p2 and n[1] >= intersections[0][1] - 1/p2 and n[1] <= intersections[0][1] + 1/p2 and len(intersections) != 2:
                            stopInner = True
                        success = False
                if success == True:
                    if xcoords2[i] >= a[0] and xcoords2[i] <= b[0] and ycoords2[i] <= a[1] and ycoords2[i] >= b[1]:
                        print("STOP!!!!!!!!!")
                        stopInner = True
                    else:
                        intersections.append([xcoords[i], ycoords[i]])
                        currentCoords = intersections[len(intersections) - 1]
                        stop = False
                        break
            success = True
            if xcoords2[i]*xcoords2[i]+ycoords2[i]*ycoords2[i] <= (r+p/(p*p))*(r+p/(p*p)) and xcoords2[i]*xcoords2[i]+ycoords2[i]*ycoords2[i] >= (r-p/(p*p))*(r-p/(p*p)):
                stop = True
                for n in intersections:
                    if xcoords2[i] <= n[0]+.4 and ycoords2[i] <= n[1]+.4 and xcoords2[i] >= n[0]-.4 and ycoords2[i] >= n[1]-.4:
                        if n == intersections[0] and len(intersections) > 2:
                            stopInner = True
                        success = False
                if success == True:
                    if xcoords2[i] >= a[0] and xcoords2[i] <= b[0] and ycoords2[i] <= a[1] and ycoords2[i] >= b[1]:
                        print("STOP2!!!!!!!!!")
                        stopInner = True
                    else:
                        intersections.append([xcoords2[i], ycoords2[i]])
                        currentCoords = intersections[len(intersections) - 1]
                        stop = False
                        break
        print(intersections)
arcLength([0, 5], [3, 4],  5)

    
            

    
