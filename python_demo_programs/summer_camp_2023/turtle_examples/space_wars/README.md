# SpaceWars
A simple game made using Turtle Library in python.

**Screenshot** of the game is given below

<img src="https://user-images.githubusercontent.com/27866638/54981382-27bbff00-4fce-11e9-9694-983f2c00b0d0.png" width="500">
<img src="https://user-images.githubusercontent.com/27866638/55740118-105a2880-5a48-11e9-92c5-6ef52506541f.png" width="500">
<img src="https://user-images.githubusercontent.com/27866638/55740223-3da6d680-5a48-11e9-8614-d984f024afe3.png" width= "500">

This is just an Intro to Python project. Made using Turtle Library in Python

**Libraries used:**

 - [Turtle](https://docs.python.org/3.1/library/turtle.html) for animations.
 - [Math](https://docs.python.org/3.7/library/math.html) for Mathematical operations to govern the motion of the player and enemy. 
 - [Random](https://docs.python.org/3/library/random.html) for random spawn of enemies when they are hit.
 - [Winsound](https://docs.python.org/2/library/winsound.html) for sound effects like collision sound and missile sound.

**Note:** *This game is made for windows only, if you are using in other platforms `import winsound` in line4 of [SpaceWars.py](https://github.com/madhavambati/SpaceWars/blob/master/SpaceWars.py) gives an error.*
## About Turtle Library

**Turtle graphics** is a popular way for introducing programming to kids. It was part of the original Logo programming language developed by Wally Feurzig and Seymour Papert in 1966. “Turtle” is a Python feature like a drawing board, which lets us command a turtle to draw all over it! We can use functions like turtle.forward(…) and turtle.right(…) which can move the turtle around. The turtle module provides turtle graphics primitives, in both object-oriented and procedure-oriented ways. Because it uses `tkinter` for the underlying graphics, it needs a version of Python installed with Tk support. It just works like a paint app and is efficient and very easy to use.

**Some of the animations created in Turltle library are shown below:**

<img src="https://3.bp.blogspot.com/-STgFumygvXA/WAHu1iTia3I/AAAAAAAAAtk/Ym_vWmzlr7wrPjeq4h1F_ZV6Zwi1CZCigCLcB/s1600/900px-Turtle_Graphics_Spiral.svg.png" width="375"><img src="https://ianwitham.files.wordpress.com/2010/04/screenshot-python-turtle-graphics2.png" width="700">

### Important links: 
 To dive deep into Turtle Library/Animations check out the links below. 
 - [Documentation](https://docs.python.org/3.1/library/turtle.html)
 - [Tutorials](https://www.geeksforgeeks.org/turtle-programming-python/)
 - [Video tutorials](https://www.youtube.com/watch?v=uRtCq6MBp1I)
 
 ### Installation:
 You can clone it and run **SpaceWars.py**. Use the following commands to get a copy from Github
     
    git clone https://github.com/madhavambati/SpaceWars.git
 change the directory to SpaceWars    
     
    cd SpaceWars
 Launch the game 
 
    python SpaceWars.py
 
### How To Play:
Move the player accordingly to a position to shoot the enemy. Each kill gains 10 points. When the enemy closes the player the *"Game is over."*

`Left key` to move the player left.

`right key` to move the player right.

`spacebar` to shoot the missile.

### References:
 - https://docs.python.org/3/library/turtle.html
 - https://www.youtube.com/channel/UC2vm-0XX5RkWCXWwtBZGOXg
 - https://leerob.io/blog/space-invaders-with-python
