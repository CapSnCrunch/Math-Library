from ComplexModule import Complex
from CalculusModule import function
from TrigModule import sin, cos, tan, cot, sec, csc
import pygame

width = 600
height = 600
scale = 75
grid_size = 2
win = pygame.display.set_mode((width, height))
pygame.display.set_caption('Complex Grapher')

f1 = 'z*z' # Sprials with a circle
f2 = 'z*z / 2'
f3 = 'sin(z, terms = 3)' # Mandelbrot Set!
f4 = 'sin(z, terms = 3) ** 2' # Weird fractal
f5 = 'Complex(1,1) / z'
f6 = 'csc(z)'
f7 = "Complex(cos(t, 'deg'), sin(t, 'deg')) * z" # Cool Polygons

t = 30
f = f3

def draw_iterations(win, z0, n = 10):

    points = [z0]
    
    for i in range(n-1):
        try:
            points.append(eval(f.replace('z', str(points[-1]))))
        except:
            break

    for i in range(len(points) - 1):
        if -width/2 <= points[i].a <= width/2 and -height/2 <= points[i].b <= height/2:
            try:
                pygame.draw.line(win, (0,0,0), (int(points[i].a * scale + width/2), int(height/2 - points[i].b * scale)), (int(points[i+1].a * scale + width/2), int(height/2 - points[i+1].b * scale)))
                pygame.draw.circle(win, (0,0,0), (int(points[i].a * scale + width/2), int(height/2 - points[i].b * scale)), 3)
            except:
                pass

def draw_grid(n = 10):

    rectangles = []

    for i in range(int(width / grid_size)):
        for j in range(int(width / grid_size)):
            #pygame.draw.rect(win, (255 * i * grid_size / width, 0, 255 * j * grid_size / width), (i*grid_size, j*grid_size, grid_size, grid_size))
            point = Complex(i*grid_size - width/2, height/2 - j*grid_size) / scale
            try:
                for iter in range(n):
                    point = eval(f.replace('z', str(point)))
                magnitude = (point.a **2 + point.b **2) ** (1/2)
                if magnitude <= 1:
                    #color = (255 * i * grid_size / width, 0, 255 * j * grid_size / width)
                    #color = (0, 255 * i * grid_size / width, 255 * j * grid_size / width)
                    color = (255*magnitude, 255*magnitude, 255*magnitude)
                    rectangles.append([color, (i*grid_size, j*grid_size, grid_size, grid_size)])
            except:
                pass
    return rectangles

def redraw_window(win, rectangles):

    win.fill((255, 255, 255))

    a,b = pygame.mouse.get_pos()
    z0 = Complex(a - width/2, height/2 - b) / scale

    for rect in rectangles:
        pygame.draw.rect(win, rect[0], rect[1])

    pygame.draw.circle(win, (0,0,0), (int(width / 2), int(height / 2)), scale, 1)

    draw_iterations(win, z0, 15)
    
    pygame.draw.line(win, (0,0,0), (width/2, 0), (width/2, height))
    pygame.draw.line(win, (0,0,0), (0, height/2), (width, height/2))
    pygame.display.update()

def main():

    rectangles = draw_grid(15)

    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        
        redraw_window(win, rectangles)
    
main()

