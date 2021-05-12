def muerte():
  print('''
           _,.---,---.._
     ,-';     `.      ''-.
   ,' -<        )         `.
  ;    |`.     '|     .     :
 ,     |  \     |      `._,' .  
,'.    |        u      -'|  .',
; ;    U .           .   |  ; |
| ;    _____       _____ u  ; |
|  ',""     "" . ""     "".'  |
'. ~  ,-~~~^~, | ,~^~~~-,  ~ .'
 |   |._,-.'  }:{  `,-.  |   |
 |   l  `-'. / | \ ,`-'_,!   |
 .~  (__,|--" .^. "--|,__)  ~.
 |    ---+;' / . \ `;+--+    |
  \__.   U   \/^\/   |  |.__/
   V| \         |    u  | |V
    | |T"-..____U__..-"T| |
    | |`IIII_I_I_I_IIII'U |
    | |   (  ( U )  )   | |
    | |    `_ _ _ _'    | |
    |  \,III I I I III,/  |
     \   `~~~~,~~~~~'|   /
      `.   .  |    . | ,'
        `-._  |^   _.+'
            '"|^'"'  |        
              u      |        
                     U

,-.    .---.    .---.          .-. .-.,---.  ,---.  _______  .---.    .---.   
| |   / .-. )  ( .-._) |\    /|| | | || .-'  | .-.\|__   __|/ .-. )  ( .-._)  
| |   | | |(_)(_) \    |(\  / || | | || `-.  | `-'/  )| |   | | |(_)(_) \     
| |   | | | | _  \ \   (_)\/  || | | || .-'  |   (  (_) |   | | | | _  \ \    
| `--.\ `-' /( `-'  )  | \  / || `-')||  `--.| |\ \   | |   \ `-' /( `-'  )   
|( __.')---'  `----'   | |\/| |`---(_)/( __.'|_| \)\  `-'    )---'  `----'    
(_)   (_)              '-'  '-'      (__)        (__)       (_)               



 .-. .-. .---.     ,--,  .-. .-.,---.  .-. .-. _______  .--.  .-. .-. 
 |  \| |/ .-. )  .' .')  | | | || .-'  |  \| ||__   __|/ /\ \ |  \| | 
 |   | || | |(_) |  |(_) | | | || `-.  |   | |  )| |  / /__\ \|   | | 
 | |\  || | | |  \  \    | | | || .-'  | |\  | (_) |  |  __  || |\  | 
 | | |)|\ `-' /   \  `-. | `-')||  `--.| | |)|   | |  | |  |)|| | |)| 
 /(  (_) )---'     \____\`---(_)/( __.'/(  (_)   `-'  |_|  (_)/(  (_) 
(__)    (_)                    (__)   (__)                   (__)     



  ,--,  .-. .-.,---.  .-. .-. _______  .---.    .---. 
.' .')  | | | || .-'  |  \| ||__   __|/ .-. )  ( .-._)
|  |(_) | | | || `-.  |   | |  )| |   | | |(_)(_) \   
\  \    | | | || .-'  | |\  | (_) |   | | | | _  \ \  
 \  `-. | `-')||  `--.| | |)|   | |   \ `-' /( `-'  ) 
  \____\`---(_)/( __.'/(  (_)   `-'    )---'  `----'  
              (__)   (__)             (_)             

  ''')


print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Bienvenid@ a la Isla del Tesoro.")
print("Tu misión es encontrar el cofre del tesoro.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

print("Te encuentras caminando por el Pantano Maldito, pero de repente el camino se divide.")
respuesta1 = input("¿Cuál de los dos senderos escoges?: Izquierda | Derecha\n").lower()

if respuesta1 == "derecha":
  print("El sendero te lleva a la orilla de un río.")
  respuesta2 = input("¿Qué haces?: Esperar | Nadar\n").lower()
  if respuesta2 == "esperar":
    print("Una barca aparece, te subes y alcanzas el otro lado de la orilla")
    respuesta3 = input("De repente te encuentras frente a tres puertas de colores\
    , ¿cuál de ellas escoges?: Roja, Amarilla, Azul").lower()
    if respuesta3 == "amarilla":
      print("¡Enhorabuena, has encontrado el Tesoro!")
    elif respuesta3 == "roja":
      print("La habitación está en llamas, nada puedes hacer por salvarte")
      muerte()
    elif respuesta3 == "azul":
      print("Las bestias de la Isla se lanzan a por ti y desgarran tu carne")
      muerte()
    else:
      muerte()
  elif respuesta2 == "nadar":
    print("Rápidamente te conviertes en pasto para los cocodrilos")
    muerte()
  else:
    muerte()
elif respuesta1 == "izquierda":
  print("Caes en un oscuro agujero, ahora tu vida está en manos del tiempo")
  muerte()
else:
  muerte()