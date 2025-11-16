class Criatura: 
    def __init__(self, nombre, energia, ataque):
        self.nombre = nombre
        self.energia = energia
        self.ataque = ataque
        self.viva = True

    def __str__(self): #imprimible con la información del personaje
        return f"Tu personaje: {self.nombre} (Energía:{self.energia}), (Ataque:{self.ataque} )."
    
    def __sub__(self, otro): #Ataque. Self se enfrenta a otro
        otro.energia -= self.ataque
        print(f"{self.nombre} ha atacado a {otro.nombre} por {self.ataque}E. {otro.nombre} tiene {otro.energia}E")

    
    def __add__(self, cantidad): #se curan
        self.energia += cantidad
        print(f"{self.nombre} recupera {cantidad} de energía. Ahora tiene {self.energia}E")  

    def __mul__(self, mejora):
        self.ataque = self.ataque * mejora
        print(f"{self.nombre} se entrena (x{mejora}). Ahora su ataque es de {self.ataque}")

    
    def esta_viva(self): 
       if self.energia >0.0:
           return True
       else:
           return False
    
class Druida(Criatura):
    def __init__(self, nombre, energia, ataque, bonus):
        self.nombre = nombre
        self.energia = energia
        self.ataque = ataque
        self.viva = True
        self.bonus = bonus

    def __str__(self):
        return f"Tu personaje: {self.nombre} y es de clase Druida. (Energía:{self.energia}), (Ataque:{self.ataque})."
    
    def __add__(self, cantidad):
        self.energia = self.energia +  cantidad * self.bonus
        print(f"{self.nombre} se recupera con bonus x{self.bonus}. Ahora tiene {self.energia} E")

    
   
class Barbaro(Criatura): 
    def __init__(self, nombre, energia, ataque):
        self.nombre = nombre
        self.energia = energia
        self.viva = True
        self.ataque = ataque 
    
    def __str__(self):
        return f"Tu personaje: {self.nombre} y es de clase Bárbaro. (Energía:{self.energia}), (Ataque:{self.ataque})."
    
    def __sub__(self, otro):
        # Solo puede atacar si su energía es mayor de 10
        if self.energia > 10:
            self.energia -=  10
            otro.energia -= self.ataque
            print(f"{self.nombre} ha atacado a {otro.nombre} por {self.ataque}E. {otro.nombre} tiene {otro.energia}E")
        else:
            print(f"{self.nombre} está demasiado débil para atacar!")


class Guerrero(Criatura): 
    def __init__(self, nombre, energia, ataque, weapon):
        self.nombre = nombre
        self.energia = energia
        self.ataque = ataque 
        self.viva = True
        self.weapon = weapon
    
    def __str__(self):
        return f"Tu personaje: {self.nombre} y es de clase Guerero. (energia:{self.energia}), (Ataque:{self.ataque})."
    
    def __sub__(self, otro):
        otro.energia = otro.energia - self.ataque
        print(f"{self.nombre} ha atacado a {otro.nombre} por {self.ataque}E. {otro.nombre} tiene {otro.energia}E")

            

    def arma (self): # Puede elegir distintas armas para atacar
        if self.weapon == "espada":
            self.ataque += 15
            self.energia -=  10
        elif self.weapon == "lanza":
            self.ataque += 10
            self.energia -=  5 
        elif self.weapon == "arco": 
            self.ataque += 5
            self.energia -= 2    
        
 
class Clerigo(Criatura):
    def __init__(self, nombre, energia, ataque, espiritu):
        self.nombre = nombre
        self.energia = energia
        self.ataque = ataque
        self.viva = True
        self.espiritu = espiritu

    def __sub__(self, otro):
        # Puede invocar espíritus amigos para aumentar su fuerza 
        if self.espiritu == 1:
            self.ataque += 5
            otro.energia -= self.ataque
        elif self.espiritu == 2:
            self.ataque += 10
            otro.energia -= self.ataque
        print(f"{self.nombre} ha atacado a {otro.nombre} por {self.ataque}E. {otro.nombre} tiene {otro.energia}E")

 #Instanciamos las criaturas: Un Druida, un Bábaro, un Guerrero, un Clérigo. 
druid = Druida("Druid", 60, 30, 1.5)
barbarian = Barbaro("Barbarian", 50, 45)
fighter = Guerrero("Fighter", 60, 30, "espada")
cleric = Clerigo("Cleric", 70, 30, 1)

print("\n ESTADO INICIAL")
print(druid)
print(barbarian)
print(fighter)
print(cleric)

#montamos dos partidas
print("\n BATALLA: DRUID VS BARBARIAN")
ronda = 1
while druid.esta_viva() and barbarian.esta_viva() and ronda <20:
    print(f"\nRonda {ronda}:")
    if druid.esta_viva():
        druid - barbarian
    else: 
        print(f"{druid.nombre} ha sido derrotado.")
       
    if barbarian.esta_viva():
         barbarian - druid
    else: 
        print(f"{barbarian.nombre} ha sido derrotado.")
    ronda += 1
    if ronda > 20:
            print("Empate técnico (demasiadas rondas).")

print(" \n ESTADO FINAL")
print(druid)
print(barbarian)
print(fighter)
print(cleric)


print("\n BATALLA: FIGHTER VS CLERIC")
ronda = 1
while fighter.esta_viva() and cleric.esta_viva() and ronda <20:
    print(f"\n Ronda {ronda}:")
    if fighter.esta_viva():
        fighter - cleric
    else: 
        print(f"{fighter.nombre} ha sido derrotado.")
        
    if cleric.esta_viva():
        cleric - fighter
    else:
        print(f"{cleric.nombre} ha sido derrotado.")
    ronda += 1
    if ronda > 20:
        print("Empate técnico (demasiadas rondas).")

fighter.energia = 60
barbarian.energia = 50
print("\n BATALLA: FIGHTER VS BARBARIAN")
ronda = 1
while fighter.esta_viva() and barbarian.esta_viva() and ronda <20:
    print(f"\n Ronda {ronda}:")
    if fighter.esta_viva():
            fighter - barbarian
    else: 
        print(f"{barbarian.nombre} ha sido derrotado.")
        
    if barbarian.esta_viva():
        barbarian - fighter
    else:
        print(f"{barbarian.nombre} ha sido derrotado.")
    ronda += 1
    if ronda > 20:
        print("Empate técnico (demasiadas rondas).")

druid.energia = 60
cleric.energia = 70
print("\n BATALLA: DRUID VS CLERIC")
ronda = 1
while druid.esta_viva() and cleric.esta_viva() and ronda <20:
    print(f"\n Ronda {ronda}:")
    if druid.esta_viva():
            druid- cleric
    else: 
        print(f"{fighter.nombre} ha sido derrotado.")
        
    if druid.esta_viva():
        cleric - druid
    else:
        print(f"{cleric.nombre} ha sido derrotado.")
    ronda += 1
    if ronda > 20:
        print("Empate técnico (demasiadas rondas).")

fighter.energia = 60
cleric.energia = 70
print("\n BATALLA: FIGHTER VS CLERIC")
ronda = 1
while fighter.esta_viva() and cleric.esta_viva() and ronda <20:
    print(f"\n Ronda {ronda}:")
    if fighter.esta_viva():
            fighter - cleric
    else: 
        print(f"{fighter.nombre} ha sido derrotado.")
        
    if cleric.esta_viva():
        cleric - fighter
    else:
        print(f"{cleric.nombre} ha sido derrotado.")
    ronda += 1
    if ronda > 20:
        print("Empate técnico (demasiadas rondas).")

fighter.energia = 60
druid.energia = 60
print("\n BATALLA: FIGHTER VS DRUID")
ronda = 1
while fighter.esta_viva() and druid.esta_viva() and ronda <20:
    print(f"\n Ronda {ronda}:")
    if fighter.esta_viva():
            fighter - druid
    else: 
        print(f"{fighter.nombre} ha sido derrotado.")
        
    if druid.esta_viva():
        druid - fighter
    else:
        print(f"{druid.nombre} ha sido derrotado.")
    ronda += 1
    if ronda > 20:
        print("Empate técnico (demasiadas rondas).")


barbarian.energia = 50
cleric.energia = 70
print("\n BATALLA: BARBARIAN VS CLERIC")
ronda = 1
while barbarian.esta_viva() and cleric.esta_viva() and ronda <20:
    print(f"\n Ronda {ronda}:")
    if barbarian.esta_viva():
            barbarian - cleric
    else: 
        print(f"{barbarian.nombre} ha sido derrotado.")
        
    if cleric.esta_viva():
        cleric - barbarian
    else:
        print(f"{cleric.nombre} ha sido derrotado.")
    ronda += 1
    if ronda > 20:
        print("Empate técnico (demasiadas rondas).")
      

print("\n ESTADO FINAL")
print(druid)
print(barbarian)
print(fighter)
print(cleric)
