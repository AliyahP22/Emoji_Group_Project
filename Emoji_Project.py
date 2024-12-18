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
    canvas.draw_circle((width / 4, height / 4), width / 8 - 40, 10, "gold", "gold")
    canvas.draw_circle((width / 4 - 30, height / 4 - 40), 20, 2, "black", "white")
    canvas.draw_circle((width / 4 + 30, height / 4 - 40), 20, 2, "white", "white")
    canvas.draw_circle((width / 4 - 30, height / 4 - 40), 10, 2, "Black", "White")
    canvas.draw_circle((width / 4 + 30, height / 4 - 40), 10, 2, "black", "black")
    canvas.draw_circle((width / 4 - 30, height / 4 - 40), 10, 2, "Black", "black")
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


def draw_rohaan(canvas):
    # Center of the bottom-left quadrant
    center_x = width / 4
    center_y = height * 3 / 4
    face_radius = min(width, height) / 8 - 20
    canvas.draw_circle((center_x, center_y), face_radius, 2, "green", "green")

    # Draw eyes
    eye_radius = face_radius / 5
    pupil_radius = eye_radius / 3
    eye_offset_x = face_radius / 2
    eye_offset_y = face_radius / 3

    # Left eye
    canvas.draw_circle((center_x - eye_offset_x, center_y - eye_offset_y), eye_radius, 2, "white", "white")
    canvas.draw_circle((center_x - eye_offset_x, center_y - eye_offset_y), pupil_radius, 2, "black", "blue")

    # Right eye
    canvas.draw_circle((center_x + eye_offset_x, center_y - eye_offset_y), eye_radius, 2, "white", "white")
    canvas.draw_circle((center_x + eye_offset_x, center_y - eye_offset_y), pupil_radius, 2, "black", "blue")

  
    mouth_width = face_radius / 3.5
    mouth_height = face_radius / 5
    mouth_points = [
        (center_x - mouth_width / 2, center_y + mouth_height / 2),
        (center_x, center_y + mouth_height),
        (center_x + mouth_width / 2, center_y + mouth_height / 2)
    ]
    canvas.draw_polyline(mouth_points, 5, "black")

    # Draw eyebrows
    eyebrow_width = face_radius / 2
    eyebrow_height = face_radius / 4
    canvas.draw_line(
        (center_x - eyebrow_width / 2.6, center_y - eye_offset_y - eyebrow_height),
        (center_x - eye_offset_x, center_y - eye_offset_y - eyebrow_height * 2.6),
        5, "black"
    )  # Left eyebrow
    canvas.draw_line(
        (center_x + eyebrow_width / 2.6, center_y - eye_offset_y - eyebrow_height),
        (center_x + eye_offset_x, center_y - eye_offset_y - eyebrow_height * 2.6),
        5, "black"
    )  # Right eyebrow

    
# Rafael's emoji
def draw_rafael(canvas):
    canvas.draw_circle((width * 3 / 4, height * 3 / 4), width / 8 - 20, 2, "yellow", "yellow")
    canvas.draw_circle((width * 3 / 4 - 30, height * 3 / 4 - 40), 20, 2, "black", "white")
    canvas.draw_circle((width * 3 / 4 + 30, height * 3 / 4 - 40), 20, 2, "Black", "White")
    canvas.draw_circle((width * 3 / 4 - 30, height * 3 / 4 - 40), 10, 2, "Black", "White")
    canvas.draw_circle((width * 3 / 4 + 30, height * 3 / 4 - 40), 10, 2, "black", "black")
    canvas.draw_circle((width * 3 / 4 - 30, height * 3 / 4 - 40), 10, 2, "Black", "White")
    canvas.draw_circle((width * 3 / 4 + 30, height * 3 / 4 - 40), 10, 2, "black", "black")    
    canvas.draw_circle((width * 3 / 4 - 30, height * 3 / 4 - 40), 10, 2, "Black", "Black")
    canvas.draw_circle((width * 3 / 4 + 20, height * 3 / 4 + 30), 20, 2, "black", "Red")


    

# Combine emojis
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




