import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

def get_mouse_click_coor(x,y):
    print(x,y)
    
    
answer_state = screen.textinput(title="Guess the State", prompt="Whats another state's name?")
turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()
