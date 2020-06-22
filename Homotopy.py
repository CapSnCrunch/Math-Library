from CalculusModule import function
from TrigModule import sin, cos, tan, cot, sec, csc
import pygame


width = 600
height = 600
scale = [10,10]
resolution = 100

win = pygame.display.set_mode((width, height))
pygame.display.set_caption('Homotopy Visualizer')

f1 = 'x'
f2 = 'x**2'
f3 = 'x**3'
f4 = '-abs((16 - x**2)**(1/2))'
f5 = 'abs((16 - x**2)**(1/2))'

F1, F2, = f1, f3

def draw_function(f, t):
    points = []
    for x in range(int(-resolution/2), int(resolution/2 + 1)):
        points.append([width/2 + x*width/resolution, height/2 - eval(f.replace('x', '('+str(x*scale[0]/resolution)+')').replace('t', str(t)))*height/scale[1]])
    for i in range(len(points)-1):
        pygame.draw.line(win, (0,0,0), (points[i]), (points[i+1]))

def redraw_window(win, t):

    win.fill((255, 255, 255))
    draw_function('(1-t)*' + F1 + ' + t*' + F2, t)
    pygame.display.update()

def main():

    run = True
    clock = pygame.time.Clock()
    t = 0

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        
        redraw_window(win, t)
        if t < 1:
            t += 0.01
    
main()