# Memory by Brenton Wright 2020
# A Mini-Project for Week 6 of "Introduction to Interactive Programming in Python (Part 2)"
# Run code here: https://py2.codeskulptor.org/

import simplegui
import random

WIDTH = 800
HEIGHT = 100
CARD_WIDTH = 50
CARD_HEIGHT = 100
card_list1 = range(8) # uses Range function to create incrementing elements between 0 and <8
card_list2 = range(8)
cards_all_list = card_list1 + card_list2
cards_exposed = []
random.shuffle(cards_all_list)
width_offset = CARD_WIDTH / 4
height_offset = (CARD_HEIGHT * 0.7)
card_index = -1
state = 0
card_1_index = 0
card_2_index = 0
turns = 0
isGameOver = "False"
game_completed_text = "Game Complete in"
number_of_turns_text = str(turns) + " Turns"

def hide_all_cards():
    """Hides all cards on starting a New Game."""
    global cards_exposed
    counter = 0
    
    # If no list is built, builds a list called CARDS_EXPOSED and makes all elements FALSE
    if len(cards_exposed) == 0:
        for c in cards_all_list:
            cards_exposed.append("False")
    # If list elements exist, list is already built, so increment through list and 
    # Checks if there are ANY cards already exposed and SET elements to FALSE"
    else:
        if len(cards_exposed) > 0:
            counter = 0
            while counter < len(cards_exposed):
                cards_exposed[counter] = "False"
                counter +=1

def new_game():
    global state, turns, isGameOver
    # Rsetting card_index, turns, state to 0
    card_index = 0
    turns = 0
    label.set_text("Turns = " + str(turns))
    state = 0
    random.shuffle(cards_all_list)
    hide_all_cards()
    isGameOver = "False"
     
def mouseclick(pos):
    global cards_exposed, state, card_1_index, card_2_index, turns
    # Detects pos of mouseclick and determines which card was clicked
    # Assigns a card_index value to card_index
    card_index = pos[0] /CARD_WIDTH
    # Exposes cards clicked on. 
    # Only accepts clicks on Non-exposed cards(ie: card_exposed = False)
    # clicking on an exposed card DOES NOTHING 
    if cards_exposed[card_index] == "False":
        cards_exposed[card_index] = "True"
        if state == 0:
            state = 1
            card_1_index = card_index
        elif state == 1:
            state = 2
            state2clicked = "True"
            card_2_index = card_index
            # Increments Turn
            turns += 1
            # Updates Frame label
            label.set_text("Turns = " + str(turns)) 
            test_if_game_complete()
        else:
            compare_card_indexes()
            state = 1
            card_1_index = card_index

def test_if_game_complete():
    """Keeps track of number of cards exposed by counting them. If ALL are True, 
    function generates Number Of Turns text string, and changes isGameOver bool to True.
    When Draw sees isGameOver bool = True, it loads the Game Complete screen."""
    global isGameOver, number_of_turns_text
    if cards_exposed !=[]:
        cards_exposed_counter = 0
        for c in cards_exposed:
            if c == "True":
                cards_exposed_counter +=1
                if cards_exposed_counter == len(cards_exposed):
                    number_of_turns_text = str(turns) + " Turns"
                    isGameOver = "True"

def compare_card_indexes():
    """Compares the indexes of the first and second card clicked to determine 
    If they are equal, cards MATCH - so leave them exposed, else NO-MATCH so hide cards"""
    if cards_all_list[card_2_index] == cards_all_list[card_1_index]:
        cards_exposed[card_1_index] = "True"
        cards_exposed[card_2_index] = "True"
    else:
        cards_exposed[card_1_index] = "False"
        cards_exposed[card_2_index] = "False"

def draw(canvas):
    if isGameOver == "True":
        canvas.draw_text(game_completed_text,[WIDTH/2 - game_complete_text_width /2, 45], 52, 'White')
        canvas.draw_text(number_of_turns_text,[WIDTH/2 - number_of_turns_text_width/2, 90], 52, 'White')
    else:
        # Draws each value of each element of the cards_all_list to CANVAS  
        for i in range(len(cards_all_list)):
                if cards_exposed[i] == "True":
                    # Displays CARD VALUE
                    canvas.draw_text(str(cards_all_list[i]),[i * CARD_WIDTH + width_offset, height_offset], 52, 'White')
                else:
                    # Displays GREEN RECTANGLE 50x100 pixels in size to represent card. 
                    canvas.draw_polygon([(0 + CARD_WIDTH * i, 0), 
                                         (CARD_WIDTH + (CARD_WIDTH  * i), 0),
                                         (CARD_WIDTH + (CARD_WIDTH  * i), CARD_HEIGHT),
                                         (0 + CARD_WIDTH * i, CARD_HEIGHT)],
                                        1, 'Black', 'Brown')

frame = simplegui.create_frame("Memory", WIDTH, HEIGHT)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = " + str(turns))
game_complete_text_width = frame.get_canvas_textwidth(game_completed_text, 52)
number_of_turns_text_width = frame.get_canvas_textwidth(number_of_turns_text, 52)
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

new_game()
frame.start()
