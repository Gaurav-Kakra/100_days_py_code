import turtle
import pandas

screen = turtle.Screen() ##Creating the screen
t = turtle.Turtle() ##Creating a turtle
correct_guesses_list = [] ##Creating the list of correct guesses
screen.title("U.S. States Game") ##Screen Title
image = ("blank_states_img.gif") #Writing the path of the image
screen.addshape(image) ##displaying the screen with the image
turtle.shape(image) ##displaying the screen with the image

data = pandas.read_csv("50_states.csv") ##Reading the states data

data_dict = data.to_dict() #converting them into dictionary

while len(correct_guesses_list) != 50: #while we don't guess all the correct states
    a = len(correct_guesses_list) ##creating the length of the correct_guesses_list to put it in the prompt box
    answer_state = screen.textinput(title=f"Guess the State {a}/50",prompt="What's the next US State?").title() ##Converting the response into title case
    if answer_state == "Exit":
        break
    for index, state in data_dict['state'].items(): ##MAIN LINE, here we are looping through index and state items like alabama, ohio so on..
        if answer_state == state: ##checking if the response is present in data states
            t.goto(data_dict['x'][index], data_dict['y'][index]) ##Turtle going to location where the index of x,y is captured for the state in data
            t.write(answer_state, align='center',font=("Arial",9,"normal")) ##writing them into that location
            correct_guesses_list.append(answer_state) ##Appending the correct_guesses_list with the correct answer response


states = data['state'].to_list()

# Create a new list containing elements that are in states but not in corrected_guesses_states
missed_states = [item for item in states if item not in correct_guesses_list]

missed_states_dict = {"Missed_States":missed_states}

pandas.DataFrame(missed_states_dict).to_csv("missed_states.csv")



