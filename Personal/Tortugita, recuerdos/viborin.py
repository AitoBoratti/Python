import turtle as t


class fragmento:
    
    
    def __init__(self,x,y,forma="square",color="green",tamaño=0.9):
        self.fragmento = t.Turtle()
        self.fragmento.color(color)
        self.fragmento.left(90.0)
        self.fragmento.penup()
        self.fragmento.goto(int(x)-20,int(y))
        self.fragmento.shapesize(tamaño)
        self.fragmento.shape(forma)
    
    # Movimiento --------------------
    def arriba(self):
        self.fragmento.forward(20)
    def abajo(self):
        self.fragmento.left(180.0)
        self.fragmento.forward(20)
        self.fragmento.left(180.0)
    def derecha(self):
        self.fragmento.right(90.0)
        self.fragmento.forward(20)
        self.fragmento.left(90.0)
    def izquierda(self):
        self.fragmento.left(90.0)
        self.fragmento.forward(20)
        self.fragmento.right(90.0)
    
    def getX(self):
        return self.fragmento.xcor()
    def getY(self):
        return self.fragmento.ycor()
    
    
    def check_colision(self, aux):
        if (self.fragmento.distance(aux.fragmento) <= 1):
            return True
        return False    
        
class serpiente:
    def __init__(self):
        self.fragmentos = []
        self.fragmentos.append(fragmento(20,20))
        self.fragmentos.append(fragmento(20,20))
        self.cabeza = self.fragmentos[0]
    
    def añadirFragmento(self):
        self.fragmentos.append(fragmento(self.fragmentos[len(self.fragmentos)-1].getX(),self.fragmentos[len(self.fragmentos)-1].getY()))
    
    def getPosicion(self):
        return self.cabeza.getX(), self.cabeza.getY()
    
    
    def mover_cuerpo(self):
        for i in range(len(self.fragmentos) - 1, 0, -1):
            actX = self.fragmentos[i - 1].getX()
            actY = self.fragmentos[i - 1].getY()
            self.fragmentos[i].fragmento.goto(actX, actY)
            
        if self.fragmentos:  # Verifica que haya fragmentos
            self.fragmentos[0].fragmento.goto(self.cabeza.xcor(), self.cabeza.ycor())
    
    def arriba(self):
        self.cabeza.arriba()
        self.mover_cuerpo()        
                
    def abajo(self):
        self.cabeza.abajo()
        self.mover_cuerpo()
            
    def derecha(self):
        self.cabeza.derecha()
        self.mover_cuerpo()
            
    def izquierda(self):
        self.cabeza.izquierda()
        self.mover_cuerpo()
    
    
    
    
    
    def colision(self):
        for i in range(2,len(self.fragmentos)-1,1):
            if (self.cabeza.check_colision(self.fragmentos[i])):
                return True
        return False


class cabezon(fragmento):
    
    
    def __init__ (self,x,y):
        super().__init__(x,y)
        self.fragmentos = []
        self.fragmentos.append(self.fragmento)
        self.dibujar_cara()
        
    def dibujar_cara(self):
        # Ojos
        ojo_izq = fragmento(self.fragmentos[0].xcor() , self.fragmentos[0].ycor() , forma="circle", color="white", tamaño=0.3)
        self.fragmentos.append(ojo_izq)

        ojo_der = fragmento(self.fragmentos[0].xcor() , self.fragmentos[0].ycor() , forma="circle", color="white", tamaño=0.3)
        self.fragmentos.append(ojo_der)

        # Pupilas
        pupila_izq = fragmento(ojo_izq.getX(), ojo_izq.getY(), forma="circle", color="black", tamaño=0.1)
        self.fragmentos.append(pupila_izq)

        pupila_der = fragmento(ojo_der.getX(), ojo_der.getY(), forma="circle", color="black", tamaño=0.1)
        self.fragmentos.append(pupila_der)
        
        
        
    def mover_rostro(self):
        self.fragmentos[1].fragmento.goto(self.fragmento.xcor() - 10, self.fragmento.ycor() + 10)
        self.fragmentos[2].fragmento.goto(self.fragmento.xcor() + 10, self.fragmento.ycor() - 10)
        self.fragmentos[3].fragmento.goto(self.fragmentos[1].xcor(), self.fragmentos[1].ycor())
        self.fragmentos[4].fragmento.goto(self.fragmentos[2].xcor(), self.fragmentos[2].ycor())
        
        
        
        
        
    def arriba(self):
        self.fragmentos[0]
        self.mover_rostro()
    def abajo(self):
        self.fragmentos[0].left(180.0)
        self.fragmentos[0].forward(20)
        self.fragmentos[0].left(180.0)
        self.mover_rostro()
    def derecha(self):
        self.fragmentos[0].right(90.0)
        self.fragmentos[0].forward(20)
        self.fragmentos[0].left(90.0)
        self.mover_rostro()
    def izquierda(self):
        self.fragmentos[0].left(90.0)
        self.fragmentos[0].forward(20)
        self.fragmentos[0].right(90.0)
        self.mover_rostro()