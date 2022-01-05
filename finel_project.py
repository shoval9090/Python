import graphics

big=0
med=0
small=0

def draw3Circles (n1,n2,n3):
    # func to check how is the biggest from the all n's
    # i will make a sort for them , and put them into variables

     if n1 > n2 and n1 > n3:
         big = n1
         if n2 > n3:
             med = n2
             small = n3
         else:
             med = n3
             small = n2
     if n2 > n1 and n2 > n3:
         big = n2
         if n1 > n3:
             med =n1
             small = n3
         else:
             med = n3
             small = n1
     if n3 > n1 and n3 > n2:
         big = n3
         if n2 > n1:
             med = n2
             small = n1
         else:
             med = n1
             small = n2
     win = graphics.GraphWin("Graphics Window",400,400)
# print the Circles in the right size
     circle1 = graphics.Circle(graphics.Point(200,200),big)
     circle1.draw(win)
     circle1.setFill("green")

     circle2 = graphics.Circle(graphics.Point(200, 200), med)
     circle2.draw(win)
     circle2.setFill("yellow")

     circle3 = graphics.Circle(graphics.Point(200, 200), small)
     circle3.draw(win)
     circle3.setFill("red")

     win.getMouse()



draw3Circles(35,55,85)

# function to get a single digit from two or more digit
def sumOfNum(m):
    theSum = 0
    while m > 0:
        digit = m % 10
        theSum = theSum + digit
        m = m // 10
    return theSum

# func with "for" loop to run over all the numbers until the "n" and the result will be "M"

def PrintNum(n,m):
    for i in range(n):
        if sumOfNum(i) == m:
            print(i)

# call to the functions
PrintNum(100,5)


# func to make a face and print them

def drawface(eye1,eye2,mouth,noise):
    win = graphics.GraphWin("Graphics Window",400,400)

    eye1 = graphics.Circle(graphics.Point(100,100),eye1)
    eye1.draw(win)
    eye1.setFill("green")

    eye2 = graphics.Circle(graphics.Point(300,100),eye2)
    eye2.draw(win)
    eye2.setFill("green")

    mouth = graphics.Line(graphics.Point(200-mouth/2,300),graphics.Point(200+mouth/2,300))
    mouth.draw(win)
    mouth.setFill("green")

    noise = graphics.Rectangle(graphics.Point(200-noise/2,200-noise/4),graphics.Point(200+noise/2,200+noise/4))
    noise.draw(win)
    noise.setFill("blue")


    win.getMouse()

# call to the func
drawface(30,30,80,100)

