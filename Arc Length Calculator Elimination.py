'''
Equation: (h1*h1) - (h2*h2) - 2*h1*x + 2*h2*x + (k1*k1) - (k2*k2) - 2*k2*y + 2*k2*y = (r1*r1) - (r2*r2)
Simplified: h = h1- h2, k = k1-k2, r = r1 - r2
Equation: h^2 - 2*h1*x + 2*h2*x + k^2 - 2*k1*y + 2*k2*y = r^2
Equation: -2*k1*y + 2*k2*y = r^2 - h^2 + 2*h1*x - 2*h2*x - k^2
Equation: k2*y - k1*y = (r^2 - h^2 + 2*h1*x - 2*h2*x - k^2)/2
Equation: (k2-k1)*y = (r^2 - h^2 + 2*h1*x - 2*h2*x - k^2)/2
Y-Equation: y = (r^2 - h^2 + 2*h1*x - 2*h2*x - k^2)/(2*(k2-k1))
X-Equation: x = (r^2 - h^2 + 2*k1*y - 2*k2*y - k^2)/(2*(h2-h1))
Substitution: y = (r^2 - h^2 + 2*h1*((r^2 - h^2 + 2*k1*y - 2*k2*y - k^2)/(2*(h2-h1))) - 2*h2*((r^2 - h^2 + 2*k1*y - 2*k2*y - k^2)/(2*(h2-h1))) - k^2)/(2*(k2-k1)
Substitution: y = (r*r - h*h + 2*h1*((r*r - h*h + 2*k1*y - 2*k2*y - k*k)/(2*(h2-h1))) - 2*h2*((r*r - h*h + 2*k1*y - 2*k2*y - k*k)/(2*(h2-h1))) - k*k)/(2*(k2-k1))
'''
def solveCircleSystem(h1, k1, h2, k2, r1, r2):
    h = h1 - h2
    k = k1 - k2
    r = r1 - r2
    y = (r*r - h*h + 2*h1*((r*r - h*h + 2*k1*y - 2*k2*y - k*k)/(2*(h2-h1))) - 2*h2*((r*r - h*h + 2*k1*y - 2*k2*y - k*k)/(2*(h2-h1))) - k*k)/(2*(k2-k1))
    x = (r*r - h*h + 2*k1*y - 2*k2*y - k*k)/(2*(h2-h1))
    print("%s, %s")
    
solveCircleSystem(0, 0, 1, 0, 1, 1)
