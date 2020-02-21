import turtle
import random
colores = ['red','lightblue','black','green','blue','yellow',]
numeros = [50,100,150,200,250,300]
red=0
lb=0
black=0
green=0
blue=0
yellow=0
contador = 0


try:
    while True:
        v = turtle.Turtle()
        v.color(random.choice(colores))
        v.speed(random.randrange(1,10))
        v.pensize(5)
        v.shape('turtle')
        v.right(random.randrange(0,350))
        v.forward(random.randrange(100,250))

        if random.randrange(100,150)==125:
            v.begin_fill()
            v.circle(25)
            v.end_fill()
            if v.color()==('red','red'):
                red+=1
            if v.color()==('lightblue','lightblue'):
                lb+=1
            if v.color()==('black','black'):
                black+=1
            if v.color()==('green','green'):
                green+=1
            if v.color()==('blue','blue'):
                blue+=1
            if v.color()==('yellow','yellow'):
                yellow+=1

        contador+=1

        if contador % 5 == 0:
            print("ROJO: {} ".format(red))
            print("CELESTE: {} ".format(lb))
            print("NEGRO: {} ".format(black))
            print("VERDE: {} ".format(green))
            print("AZUL: {} ".format(blue))
            print("AMARILLO: {} \n".format(yellow))

        if red == 3:
            ganador = 'ROJO'
            break
        elif lb == 3:
            ganador = 'CELESTE'
            break
        elif black == 3:
            ganador = 'NEGRO'
            break
        elif green == 3:
            ganador = 'VERDE'
            break
        elif blue == 3:
            ganador = 'AZUL'
            break
        elif yellow == 3:
            ganador = 'AMARILLO'
            break

except:
    print("")
finally:
    print("El ganador fue {}".format(ganador))
#while True:
#    v = turtle.Turtle()
#    v.setx(-30)
#    v.sety(30)
#    v.color('red')
#    v.pensize(5)
#    v.shape('turtle')
#    v.right(100)
#    v.forward(100)

#turtle.getscreen()._root.mainloop()