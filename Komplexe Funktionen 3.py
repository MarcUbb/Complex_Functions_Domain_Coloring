import matplotlib.pyplot as plt
import cmath
import math

def function(z):
    return ((complex(0,1)*z+2)*(z**z-complex(0,1)))/(pow(z,3)-3)



#interesting functions:
#((complex(0,1)*z+2)*(z**z-complex(0,1)))/(pow(z,3)-3)

#Riemann Zeta-Funktion:
#depth = 50
#i = 1
#summe = 0
#while(i< depth):
#    summe += 1/i**z
#    i += 1
#return summe

#Mandelbrot Werte
#depth = 10
#c = z
#i = 0
#while (i < depth):
#    z = z * z + c
#    if (abs(z) > 2):
#        return 0
#    i += 1
#return z


res = 1000
pos_x = 0.0
pos_y = 0.0
zoom = 0.1

depth_brightness = 72
depth_color = 72

x = []
y = []
val = []

x_s = [[[]for _ in range(0,depth_color)]for _ in range(0,depth_brightness)]
y_s = [[[]for _ in range(0,depth_color)]for _ in range(0,depth_brightness)]

brightness_x = [[]for _ in range(0,depth_brightness)]
brightness_y = [[]for _ in range(0,depth_brightness)]


print 'creating x and y array...'
i = 0
while(i < res):
    j = 0
    while(j < res):
        z = complex((i*(1/zoom)/res)-0.5*(1/zoom)+pos_x, (j*(1/zoom)/res)-0.5*(1/zoom)+pos_y)
        w = function(z)
        x.append(z)
        y.append(w)
        val.append(abs(w))
        j += 1
    i += 1
max_val = max(val)
print 'created x and y array!'

print 'creating brightness arrays...'
k = 0
while k < len(y):
    l = 0
    while l < len(brightness_y):
        if abs(y[k]) >= l*(max_val/depth_brightness) and abs(y[k]) <= (l+1)*(max_val/depth_brightness):
            brightness_y[l].append(y[k])
            brightness_x[l].append(x[k])
        l += 1
    k += 1
print 'created brightness arrays!'

print 'creating sorted arrays for x and y...'
m = 0
while m < len(brightness_y):
    n = 0
    while n < len(brightness_y[m]):
        o = 0
        while o < len(y_s[m]):
            if (cmath.pi+cmath.phase(brightness_y[m][n]))*180/cmath.pi >= o*(360/depth_color) and (cmath.pi + cmath.phase(brightness_y[m][n]))*180/cmath.pi <= (o+1)*(360/depth_color):
                y_s[m][o].append(brightness_y[m][n])
                x_s[m][o].append(brightness_x[m][n])
            o += 1
        n += 1
    m += 1
print 'created sorted arrays for x and y!'


def color(z):
    angle = (cmath.phase(z)+cmath.pi)*180/cmath.pi
    value = abs(z)

    if(angle >= 300 or angle <= 60):
        red = 255
        if(angle >= 300):
            green = 0
            blue = ((360.0-angle)*255)/60
        elif(angle <= 60):
            green = (angle*255)/60
            blue = 0

    elif(angle >= 60 and angle <= 180):
        green = 255
        if(angle <= 120):
            red = ((120.0-angle)*255)/60
            blue = 0
        elif(angle > 120):
            red = 0
            blue = ((120.0-angle)*-255)/60

    elif (angle >= 180 and angle <= 300):
        blue = 255
        if (angle <= 240):
            green = ((240.0 - angle) * 255) / 60
            red = 0
        elif (angle > 120):
            green = 0
            red = ((240.0 - angle) * -255) / 60


    red = red + (value * 511)/max_val - 255
    green = green + (value * 511)/max_val - 255
    blue = blue + (value * 511)/max_val - 255

    if(red < 0):
        red = 0
    if (green < 0):
        green = 0
    if (blue < 0):
        blue = 0
    if (red > 255):
        red = 255
    if (green > 255):
        green = 255
    if (blue > 255):
        blue = 255

    red = hex(int(round(red,0)))
    green = hex(int(round(green,0)))
    blue = hex(int(round(blue,0)))

    red = list(str(red))
    green = list(str(green))
    blue = list(str(blue))

    del (red[0], green[0], blue[0], red[0], green[0], blue[0])
    if (len(red) == 1):
        red.append(0)
        red[1] = red[0]
        red[0] = 0

    if (len(green) == 1):
        green.append(0)
        green[1] = green[0]
        green[0] = 0

    if (len(blue) == 1):
        blue.append(0)
        blue[1] = blue[0]
        blue[0] = 0


    color = list('#'+str(red[0])+str(red[1])+str(green[0])+str(green[1])+str(blue[0])+str(blue[1]))
    colorcode = "".join(color)
    return colorcode

real = [[[]for _ in range(0,depth_color)]for _ in range(0,depth_brightness)]
imag = [[[]for _ in range(0,depth_color)]for _ in range(0,depth_brightness)]

print 'seperating real and imaginary part of sorted x array...'
p = 0
while p < len(x_s):
    q = 0
    while q < len(x_s[p]):
        r = 0
        while r < len(x_s[p][q]):
            real[p][q].append(x_s[p][q][r].real)
            imag[p][q].append(x_s[p][q][r].imag)
            r += 1
        q += 1
    p += 1
print 'finished creating real and imaginary array!...'

s = 0
while s < len(y_s):
    t = 0
    while t < len(y_s[s]):
        if(len(y_s[s][t]) > 0):
            colour = color(y_s[s][t][0])
            plt.scatter(real[s][t],imag[s][t],s = 0.25,c = colour)
        t += 1
    print 'finished plotting brightness',s+1,'/',depth_brightness
    s += 1
print 'finished!'

plt.show()

