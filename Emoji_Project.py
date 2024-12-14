#Aliyah Pargan
#David Muratov
#Rafael Perez
#Rohaan Mirza
#Michael Sookdeo

#12-9-2024
#Emoji project, where we would create 4 emojis

import simplegui
import math

# Global Variables

width = int(input("Initial width?"))
height = int(input("Initial Height?"))
face1 = False
face2 = False
face3 = False
face4 = False
face5 = False

# Event Handlers

def all_false():
    global face1
    global face2
    global face3
    global face4
    global face5
    face1 = False
    face2 = False
    face3 = False
    face4 = False
    face5 = False
    
def toggle_face1():
    all_false()
    global face1
    face1 = not face1
    
def toggle_face2():
    all_false()
    global face2
    face2 = not face2
      
def toggle_face3():
    all_false()
    global face3
    face3 = not face3
    
def toggle_face4():
    all_false()
    global face4
    face4 = not face4

def toggle_face5():
    all_false()
    global face5
    face5 = not face5

def draw(canvas):
    quandrant_width = width/2
    quandrant_height = height/2
    if face1:
        
        canvas.draw_circle((width/2, height/2), width/2 - 50, 10, "Yellow", "Yellow")
        canvas.draw_circle((200, 200), 30, 2, "Black", "White")
        canvas.draw_circle((400, 200), 30, 2, "Black", "White")
        canvas.draw_circle((200, 190), 15, 2, "Black", "Black")
        canvas.draw_circle((400, 190), 15, 2, "Black", "Black")
        canvas.draw_line((160, 180),(200, 150), 3, "Black")
        canvas.draw_line((200, 150),(240, 180), 3, "Black")
        canvas.draw_line((360, 180),(400, 150), 3, "Black")
        canvas.draw_line((400, 150),(440, 180), 3, "Black")
        canvas.draw_polygon([(width/2, height - height/4), (width/2 - 50, height - height/4 + -50), (width/2 - 10, height - height/4 - -30), (width/2 + 10, height - height/4 - -30), (width/2 + 50, height - height/4 + -25)],10, "Black", "White")
        canvas.draw_line((width/2 - 30, height - height/4 - 10), (width/2 + 30, height - height/4 - 10), 5, "Black")
    if face2:
        canvas.draw_circle((width/2, height/2), width/2 - 50, 10, "cyan", "cyan")
        canvas.draw_circle((200, 200), 30, 2, "Black", "White")
        canvas.draw_circle((400, 200), 30, 2, "Black", "White")
        canvas.draw_circle((200, 215), 15, 2, "Black", "Black")
        canvas.draw_circle((400, 215), 15, 2, "Black", "Black")
        canvas.draw_circle((200, 215), 4, 2, "White", "White")
        canvas.draw_circle((400, 215), 4, 2, "White", "White")
        canvas.draw_line((160, 180),(200, 150), 3, "Black")
        canvas.draw_line((400, 150),(440, 180), 3, "Black")
        canvas.draw_polygon([(width/2, height - height/4), (width/2 - 50, height - height/4 + 25), (width/2 - 10, height - height/4 - 30), (width/2 + 10, height - height/4 - 30), (width/2 + 50, height - height/4 + 25)],10, "Black", "White")
        canvas.draw_line((width/2 - 30, height - height/4 - 10), (width/2 + 30, height - height/4 - 10), 5, "Black")
        
        
    if face3:
        canvas.draw_circle((width/2, height/2), width/2 - 50, 10, "#FA8072", "#FA8072")
        canvas.draw_circle([width/2.75, height/2 - 100], 10 , 10, "Black", "White")
        canvas.draw_circle([width - width/2.75, height/2 - 100], 10 , 10, "Black", "White")
        canvas.draw_line((width/3, height/2 - 150),(width/3 + 50, height/2 - 125), 5, "Black")
        canvas.draw_line((width - width/3, height/2 - 150),(width - width/3 - 50, height/2 - 125), 5, "Black")
        canvas.draw_polygon([(width/2, height - height/4), (width/2 - 50, height - height/4 + 25), (width/2 - 10, height - height/4 - 30), (width/2 + 10, height - height/4 - 30), (width/2 + 50, height - height/4 + 25)],10, "Black", "White")
        canvas.draw_line((width/2 - 30, height - height/4 - 10), (width/2 + 30, height - height/4 - 10), 5, "Black")


    if face4:
        canvas.draw_circle((300, 300), 250, 10, "#FCF4A3", "#FCF4A3")
        canvas.draw_circle((200, 200), 30, 2, "Black", "White")
        canvas.draw_circle((400, 200), 30, 2, "Black", "White")
        canvas.draw_circle((200, 215), 15, 2, "Black", "Black")
        canvas.draw_circle((400, 215), 15, 2, "Black", "Black")
        canvas.draw_circle((200, 215), 4, 2, "White", "White")
        canvas.draw_circle((400, 215), 4, 2, "White", "White")
        canvas.draw_line((160, 180),(200, 150), 3, "Black")
        canvas.draw_line((200, 150),(240, 180), 3, "Black")
        canvas.draw_line((360, 180),(400, 150), 3, "Black")
        canvas.draw_line((400, 150),(440, 180), 3, "Black")
        canvas.draw_circle((300, 400), 30, 2, "Black", "Black")

    if face5:
        canvas.draw_circle((300, 300), 250, 10, "#90EE90", "#90EE90")
        canvas.draw_circle((200, 200), 30, 2, "Black", "White")
        canvas.draw_circle((400, 200), 30, 2, "Black", "White")
        canvas.draw_circle((200, 215), 15, 2, "Black", "Black")
        canvas.draw_circle((400, 215), 15, 2, "Black", "Black")
        canvas.draw_circle((200, 215), 4, 2, "White", "White")
        canvas.draw_circle((400, 215), 4, 2, "White", "White")
        canvas.draw_line((160, 180),(200, 150), 3, "Black")
        canvas.draw_line((200, 150),(240, 180), 3, "Black")
        canvas.draw_line((360, 180),(400, 150), 3, "Black")
        canvas.draw_line((400, 150),(440, 180), 3, "Black")
        canvas.draw_polygon([(width/2, height - height/4), (width/2 - 50, height - height/4 + 25), (width/2 - 10, height - height/4 - 30), (width/2 + 10, height - height/4 - 30), (width/2 + 50, height - height/4 + 25)],10, "Black", "White")
        canvas.draw_line((width/2 - 30, height - height/4 - 10), (width/2 + 30, height - height/4 - 10), 5, "Black")

        
frame = simplegui.create_frame("Emoji Project", width, height) 

frame.set_draw_handler(draw)
frame.add_button("Michael's Emoji", toggle_face1, 100)
frame.add_button("Aliyah's Emoji", toggle_face2, 100)
frame.add_button("David's Emoji", toggle_face3, 100)
frame.add_button("Rohaan's Emoji", toggle_face4, 100)
frame.add_button("Rafael's Emoji", toggle_face5, 100)

# Remember to start the frame
frame.start()





import simplegui
def canvas_size():
    global width, height
    width = int(input("Initial Width? "))
    height = int(input("Initial Height? "))

canvas_size()

# buttons for emojis
aliyah, david, rohaan, rafael,  = False, False, False, False,

# Aliyah's emoji
def draw_aliyah(canvas):
    canvas.draw_circle((width / 4, height / 4), width / 8 - 20, 10, "Gold", "Gold")
    canvas.draw_circle((width / 4, height / 4), width / 8 - 40, 10, "#FFE4B5", "#FFE4B5")
    canvas.draw_circle((width / 4 - 30, height / 4 - 30), 10, 2, "Red", "Red")
    canvas.draw_circle((width / 4 - 20, height / 4 - 30), 10, 2, "Red", "Red")
    canvas.draw_polygon([(width / 4 - 35, height / 4 - 30),
                         (width / 4 - 15, height / 4 - 30),
                         (width / 4 - 25, height / 4 - 10)],
                        2, "Red", "Red")
    canvas.draw_circle((width / 4 + 30, height / 4 - 30), 10, 2, "Red", "Red")
    canvas.draw_circle((width / 4 + 40, height / 4 - 30), 10, 2, "Red", "Red")
    canvas.draw_polygon([(width / 4 + 25, height / 4 - 30),
                         (width / 4 + 45, height / 4 - 30),
                         (width / 4 + 35, height / 4 - 10)],
                        2, "Red", "Red")
    mouth_points = [(width / 4 - 30, height / 4 + 30),
                    (width / 4 - 20, height / 4 + 40),
                    (width / 4, height / 4 + 30),
                    (width / 4 + 20, height / 4 + 40),
                    (width / 4 + 30, height / 4 + 30)]
    for i in range(len(mouth_points) - 1):
        canvas.draw_line(mouth_points[i], mouth_points[i + 1], 3, "Black")
   

#David's emoji
def draw_david(canvas):
    canvas.draw_circle((width * 3 / 4, height / 4), width / 8 - 20, 5, 'black', 'yellow')
    canvas.draw_polygon([(width * 3 / 4 - 30, height / 4 - 20),
                         (width * 3 / 4 - 20, height / 4 - 40),
                         (width * 3 / 4 - 10, height / 4 - 20)],
                        5, 'black', 'red')  # Left eye
    canvas.draw_polygon([(width * 3 / 4 + 10, height / 4 - 20),
                         (width * 3 / 4 + 20, height / 4 - 40),
                         (width * 3 / 4 + 30, height / 4 - 20)],
                        5, 'black', 'red')  # Right eye
    mouth_points = [(width * 3 / 4 - 30, height / 4 + 20),
                    (width * 3 / 4 - 20, height / 4 + 30),
                    (width * 3 / 4 - 10, height / 4 + 20),
                    (width * 3 / 4, height / 4 + 30),
                    (width * 3 / 4 + 10, height / 4 + 20)]
    canvas.draw_polyline(mouth_points, 5, 'black')

# Wendy's emoji
def draw_rohaan(canvas):
    # Center of the bottom-left quadrant
    center_x = width / 4
    center_y = height * 3 / 4

    # Draw face (yellow circle)
    face_radius = min(width, height) / 8 - 20
    canvas.draw_circle((center_x, center_y), face_radius, 2, "yellow", "yellow")

    # Draw eyes (white circles with black pupils)
    eye_radius = face_radius / 5
    pupil_radius = eye_radius / 3
    eye_offset_x = face_radius / 2
    eye_offset_y = face_radius / 3

    # Left eye
    canvas.draw_circle((center_x - eye_offset_x, center_y - eye_offset_y), eye_radius, 2, "white", "white")
    canvas.draw_circle((center_x - eye_offset_x, center_y - eye_offset_y), pupil_radius, 2, "black", "black")

    # Right eye
    canvas.draw_circle((center_x + eye_offset_x, center_y - eye_offset_y), eye_radius, 2, "white", "white")
    canvas.draw_circle((center_x + eye_offset_x, center_y - eye_offset_y), pupil_radius, 2, "black", "black")

    # Draw sad mouth (downward arc)
    mouth_width = face_radius / 1.5
    mouth_height = face_radius / 3
    mouth_points = [
        (center_x - mouth_width / 2, center_y + mouth_height / 2),
        (center_x, center_y + mouth_height),
        (center_x + mouth_width / 2, center_y + mouth_height / 2)
    ]
    canvas.draw_polyline(mouth_points, 5, "black")

    # Draw eyebrows (arched)
    eyebrow_width = face_radius / 2
    eyebrow_height = face_radius / 4
    canvas.draw_line(
        (center_x - eyebrow_width / 1.5, center_y - eye_offset_y - eyebrow_height),
        (center_x - eye_offset_x, center_y - eye_offset_y - eyebrow_height * 1.5),
        5, "black"
    )  # Left eyebrow
    canvas.draw_line(
        (center_x + eyebrow_width / 1.5, center_y - eye_offset_y - eyebrow_height),
        (center_x + eye_offset_x, center_y - eye_offset_y - eyebrow_height * 1.5),
        5, "black"
    )  # Right eyebrow

    
   

# Betsy's emoji
def draw_rafael(canvas):
    canvas.draw_circle((width * 3 / 4, height * 3 / 4), width / 8 - 20, 2, "yellow", "yellow")
    canvas.draw_circle((width * 3 / 4 - 30, height * 3 / 4 - 40), 20, 2, "white", "white")
    canvas.draw_circle((width * 3 / 4 + 30, height * 3 / 4 - 40), 20, 2, "white", "white")
    canvas.draw_circle((width * 3 / 4 - 30, height * 3 / 4 - 40), 10, 2, "black", "black")
    canvas.draw_circle((width * 3 / 4 + 30, height * 3 / 4 - 40), 10, 2, "black", "black")
    mouth_points = [(width * 3 / 4 - 30, height * 3 / 4 + 20),
                    (width * 3 / 4, height * 3 / 4 + 40),
                    (width * 3 / 4 + 30, height * 3 / 4 + 20)]
    canvas.draw_polyline(mouth_points, 5, "red")

# Render emojis
def draw(canvas):
    if aliyah:
        draw_aliyah(canvas)
    if david:
        draw_david(canvas)
    if rohaan:
        draw_rohaan(canvas)
    if rafael:
        draw_rafael(canvas)

# Button handlers
def show_aliyah():
    global aliyah,david,rohaan,rafael
    aliyah,david,rohaan,rafael = True, False, False, False

def show_david():
    global aliyah,david,rohaan,rafael
    aliyah,david,rohaan,rafael = False, True, False, False

def show_rohaan():
    global aliyah,david,rohaan,rafael
    aliyah,david,rohaan,rafael = False, False, True, False

def show_rafael():
    global aliyah,david,rohaan,rafael
    aliyah,david,rohaan,rafael = False, False, False, True

def show_all():
    global aliyah,david,rohaan,rafael
    aliyah,david,rohaan,rafael = True, True, True, True

# Frame initialization
frame = simplegui.create_frame("Emoji Project", width, height)
frame.set_draw_handler(draw)

frame.add_button("Aliyah's Emoji", show_aliyah, 150)
frame.add_button("David's Emoji", show_david, 150)
frame.add_button("Rohaan's Emoji", show_rohaan, 150)
frame.add_button("Rafael's Emoji", show_rafael, 150)
frame.add_button("Show All Emojis", show_all, 150)

frame.start()


