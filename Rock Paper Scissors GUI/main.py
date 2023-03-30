import random
from tkinter import *
from PIL import ImageTk, Image

WINDOW = Tk()
WINDOW.title('Rock Paper Scissors ')
WINDOW.geometry('1500x750')
WINDOW.resizable(width=False, height=False)
WINDOW.configure(background="black")

label_player_choice = Label(WINDOW, font=('Arial', 60, 'bold'), bg='black', fg='grey')
label_player_choice.place(x=800, y=0, width=600, height=350)
label_player_choice['text'] = '?'
label_player = Label(WINDOW, font=('Arial', 20, 'bold'), bg='black', fg='grey')
label_player.place(x=1020, y=300, width=150, height=50)
label_player['text'] = 'You'

label_computer_choice = Label(WINDOW, font=('Arial', 60, 'bold'), bg='black', fg='grey')
label_computer_choice.place(x=90, y=0, width=600, height=350)
label_computer_choice['text'] = '?'
label_computer = Label(WINDOW, font=('Arial', 20, 'bold'), bg='black', fg='grey')
label_computer.place(x=300, y=300, width=150, height=50)
label_computer['text'] = 'Computer'

label_result = Label(WINDOW, font=('Arial', 30, 'bold'), bg='black', fg='white')
label_result.place(x=450, y=350, width=600, height=100)

label_score = Label(WINDOW, font=('Arial', 30, 'bold'), bg='black', fg='grey')
label_score.place(x=670, y=50, width=150, height=150)
label_score['text'] = f'score'

PAPER_SIGN_PIC = ImageTk.PhotoImage(Image.open('pictures/paper.png'))
ROCK_SIGN_PIC = ImageTk.PhotoImage(Image.open('pictures/rock.png'))
SCISSORS_SIGN_PIC = ImageTk.PhotoImage(Image.open('pictures/scissors.png'))

options = ('Rock', 'Paper', 'Scissors')
computer_choice = None
player_choice = None
computer_score = 0
player_score = 0


def computer():
    global computer_choice
    computer_choice = random.choice(options)
    match computer_choice:
        case 'Rock':
            label_computer_choice['image'] = ROCK_SIGN_PIC
        case 'Paper':
            label_computer_choice['image'] = PAPER_SIGN_PIC
        case 'Scissors':
            label_computer_choice['image'] = SCISSORS_SIGN_PIC
    return computer_choice


def player_choose_rock():
    global player_choice
    player_choice = options[0]
    label_player_choice['image'] = ROCK_SIGN_PIC
    computer()
    play_game()
    decide_winner()
    return player_choice


def player_choose_paper():
    global player_choice
    player_choice = options[1]
    label_player_choice['image'] = PAPER_SIGN_PIC
    computer()
    play_game()
    decide_winner()
    return player_choice


def player_choose_scissors():
    global player_choice
    player_choice = options[2]
    label_player_choice['image'] = SCISSORS_SIGN_PIC
    computer()
    play_game()
    decide_winner()
    return player_choice


def play_game():
    global computer_score
    global player_score

    if (computer_choice == 'Rock' and player_choice == 'Scissors') or (
            computer_choice == 'Paper' and player_choice == 'Rock') or (
            computer_choice == 'Scissors' and player_choice == 'Paper'):
        computer_score += 1
        label_result['fg'] = '#a11e15'
        label_result['text'] = f'COMPUTER WINS!'
        label_score['text'] = f'{computer_score} : {player_score}'

    elif (computer_choice == 'Scissors' and player_choice == 'Rock') or (
            computer_choice == 'Rock' and player_choice == 'Paper') or (
            computer_choice == 'Paper' and player_choice == 'Scissors'):
        player_score += 1
        label_result['fg'] = '#126b2a'
        label_result['text'] = f'YOU WIN!'
        label_score['text'] = f'{computer_score} : {player_score}'

    else:
        label_result['fg'] = 'orange'
        label_result['text'] = f'Tie!'
        label_score['text'] = f'{computer_score} : {player_score}'


def reset_game():
    global computer_score
    global player_score
    player_score = 0
    computer_score = 0
    label_score['text'] = f'{computer_score} : {player_score}'


def decide_winner():
    global computer_score
    global player_score
    if computer_score == 3 or player_score == 3:
        if computer_score > player_score:
            label_result['text'] = f'Game over! Computer wins!\nscore {computer_score} : {player_score}'
            reset_game()
        elif computer_score < player_score:
            label_result['text'] = f'Game over! You win!\nscore {computer_score} : {player_score}'
            reset_game()


button_player_pick_rock = Button(
    text='Rock',
    width=15,
    height=3,
    font=('Arial', 15, 'bold'),
    bg='yellow',
    fg='black',
    borderwidth=0,
    command=player_choose_rock
)
button_player_pick_rock.place(x=400, y=500)

button_player_pick_paper = Button(
    text='Paper',
    width=15,
    height=3,
    font=('Arial', 15, 'bold'),
    bg='green',
    fg='black',
    borderwidth=0,
    command=player_choose_paper)
button_player_pick_paper.place(x=650, y=500)

button_player_pick_scissors = Button(
    text='Scissors',
    width=15,
    height=3,
    font=('Arial', 15, 'bold'),
    bg='#cfa242',
    fg='black',
    borderwidth=0,
    command=player_choose_scissors)
button_player_pick_scissors.place(x=900, y=500)

WINDOW.mainloop()
