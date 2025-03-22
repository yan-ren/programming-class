# Flora Charbonneau
# Emily Chen
# Katrina Pelcha
# Anissa Djaffri


import random
# pour la couleur des fleurs
import turtle

# créez un écran
ecran = turtle.Screen()
largeur = 1200
longueur = 1200
ecran.setup(largeur, longueur)
ecran.bgcolor("#ADD8E6")  # Couleur du ciel qui est bleu pâle
tortue = turtle.Turtle("classic")
tortue.speed(20)  # Pour que le dessin se crée rapidement!


def dessin_rectangle(largeur, hauteur, couleur, x, y):
    """Fonction qui permet de dessiner un rectangle"""

    tortue.penup()
    tortue.goto(x, y)
    tortue.pendown()
    tortue.pencolor("black")
    tortue.fillcolor(couleur)
    tortue.begin_fill()

    for i in range(2):
        tortue.forward(largeur)
        tortue.left(90)
        tortue.forward(hauteur)
        tortue.left(90)
    tortue.end_fill()


# Le gazon! C'est un rectangle vert!
dessin_rectangle(1200, 300, "green", -600, -400)


# Le lac!
def lac(x, y):
    """Cette fonction assemble d'autres fonctions soit le cercle et un rectangle
    afin de créer le lac"""

    tortue.penup()
    tortue.goto(x, y)
    tortue.pendown()
    tortue.pencolor("black")
    tortue.fillcolor("blue")
    tortue.begin_fill()

    for i in range(2):
        tortue.forward(150)
        tortue.circle(80, 180)
    tortue.end_fill()


lac(200, -300)


def fruit_feuillage(x, y):
    """Fonction qui dessine des fruits rouges """
    tortue.penup()  # Relever le stylo pour ne pas tracer en se déplaçant
    tortue.goto(x, y)  # Déplacer la tortue aux coordonnées spécifiées
    tortue.pendown()  # Abaisser le stylo pour commencer à dessiner
    tortue.fillcolor("red")  # Définir la couleur de remplissage du feuillage
    tortue.begin_fill()  # Démarrer le remplissage du cercle
    tortue.circle(4, 360)  # Dessiner un cercle de rayon 4
    tortue.end_fill()  # Terminer le remplissage du cercle


def feuillage(x, y):
    """Fonction qui dessine le feuillage d'un arbre en vert et les fruits"""
    tortue.penup()  # Relever le stylo pour ne pas tracer en se déplaçant
    tortue.goto(x, y)  # Déplacer la tortue aux coordonnées spécifiées
    tortue.pendown()  # Abaisser le stylo pour commencer à dessiner
    tortue.fillcolor("darkgreen")  # Définir la couleur de remplissage du feuillage
    tortue.begin_fill()  # Commencer à remplir la forme
    for i in range(9):  # Répéter 9 fois pour créer un feuillage en forme arrondie
        tortue.circle(12, 180)  # Dessiner un demi-cercle de rayon 12
        tortue.right(140)  # Ajuster l'angle pour connecter les demi-cercles
    tortue.end_fill()  # Terminer le remplissage de la forme
    # Ajouter des fruits après avoir dessiné le feuillage
    fruit_feuillage(x - 50, y + 5)  # Fruit à gauche
    fruit_feuillage(x - 20, y + 25)  # Fruit en haut à droite
    fruit_feuillage(x - 14, y - 10)  # Fruit en bas à droite


# feuillage(0,0)


def tronc_arbre(x, y):
    """Fonction qui dessine le tronc d'un arbre sous forme de rectangle."""
    dessin_rectangle(15, 50, "maroon", x, y)  # Dessiner un rectangle brun pour représenter le tronc


def arbre(x, y):
    """Fonction qui dessine un arbre complet en combinant tronc et feuillage."""
    tronc_arbre(x - 40, y - 68)  # Dessiner le tronc légèrement décalé pour centrer l'arbre
    feuillage(x, y)# Dessiner le feuillage au-dessus du tronc les 4 arbres


position_arbre_x = 160  # Définition de la position initiale du premier arbre sur l'axe X
# Dessiner 4 arbres en les espaçant régulièrement sur l'axe X
for i in range(4):
    arbre(position_arbre_x, -60)  # Placer chaque arbre au bon endroit sur l'axe Y
    position_arbre_x += 90  # Déplacer la position X pour le prochain arbre


def soleil(x, y):
    """Fonction qui dessine un soleil"""
    tortue.penup()  # Relever le stylo pour ne pas tracer en se déplaçant
    tortue.goto(x, y)  # Déplacer la tortue aux coordonnées spécifiées
    tortue.pendown()  # Abaisser le stylo pour commencer à dessiner
    tortue.fillcolor("orange")  # Définir la couleur de remplissage du fond de soleil
    tortue.pencolor("")
    tortue.begin_fill()  # Commencer à remplir la forme
    for i in range(18):  # Répéter 18 fois pour créer un soleil avec une forme de pic autour
        tortue.penup()
        tortue.forward(60)
        tortue.pendown()
        tortue.setheading(tortue.heading() + 45)
        for _ in range(3):
            tortue.forward(40)
            tortue.left(120)
        tortue.setheading(tortue.heading() - 45)
        tortue.penup()
        tortue.backward(60)
        tortue.right(20)
    tortue.end_fill()  # Terminer le remplissage de la forme
    tortue.penup()

    # large orange circle
    tortue.goto(x, y - 75)
    tortue.begin_fill()
    tortue.circle(75)
    tortue.end_fill()

    tortue.pencolor("black")
    # smaller yellow circle
    tortue.goto(x, y - 60)
    tortue.fillcolor("yellow")
    tortue.begin_fill()
    tortue.circle(60)
    tortue.end_fill()


soleil(250, 220)

def draw_x(size = 10):
    tortue.pendown()
    tortue.pencolor(random.choice(["red", "blue", "yellow", "gray", "brown"]))

    tortue.width(2)
    tortue.setheading(45)
    tortue.forward(size)
    tortue.backward(size * 2)
    tortue.forward(size)

    tortue.setheading(-45)
    tortue.forward(size)
    tortue.backward(size * 2)
    tortue.forward(size)

    tortue.penup()


def draw_x_grid(x, y, rows=9, cols=7, spacing=40):

    start_x = x -((cols - 1) * spacing) // 2  # Center horizontally
    start_y = y + ((rows - 1) * spacing) // 2  # Center vertically

    for row in range(rows):
        for col in range(cols):
            tortue.goto(x + start_x + col * spacing, y + start_y - row * spacing)
            draw_x()


draw_x_grid(0, -150)

turtle.done()
