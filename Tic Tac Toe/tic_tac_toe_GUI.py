from tkinter import Tk
from tkinter import Button
from tkinter import messagebox

pressed_button = False
clicked_buttons = 0


class Game:

    def __init__(self, window):
        self.window = window
        window.title("Tic Tac Toe")
        self.create_gui()

    def click(self, btn):
        global pressed_button, clicked_buttons
        if btn['text'] == '' and not pressed_button:
            btn['fg'] = 'green'
            btn['text'] = "X"
            pressed_button = True
            clicked_buttons += 1
        elif btn['text'] == '' and pressed_button:
            btn['fg'] = 'red'
            btn['text'] = "O"
            pressed_button = False
            clicked_buttons += 1
        self.check_winner()

    def create_gui(self):
        global btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, clicked_buttons
        btn1 = Button(self.window, height=5, width=10, font=("Arial", 12, "bold"), text='',
                      command=lambda: self.click(btn1))
        btn1.grid(row=1, column=0, padx=5, pady=5)
        btn2 = Button(self.window, height=5, width=10, font=("Arial", 12, "bold"), text='',
                      command=lambda: self.click(btn2))
        btn2.grid(row=1, column=1, padx=5, pady=5)
        btn3 = Button(self.window, height=5, width=10, font=("Arial", 12, "bold"), text='',
                      command=lambda: self.click(btn3))
        btn3.grid(row=1, column=2, padx=5, pady=5)
        btn4 = Button(self.window, height=5, width=10, font=("Arial", 12, "bold"), text='',
                      command=lambda: self.click(btn4))
        btn4.grid(row=2, column=0, padx=5, pady=5)
        btn5 = Button(self.window, height=5, width=10, font=("Arial", 12, "bold"), text='',
                      command=lambda: self.click(btn5))
        btn5.grid(row=2, column=1, padx=5, pady=5)
        btn6 = Button(self.window, height=5, width=10, font=("Arial", 12, "bold"), text='',
                      command=lambda: self.click(btn6))
        btn6.grid(row=2, column=2, padx=5, pady=5)
        btn7 = Button(self.window, height=5, width=10, font=("Arial", 12, "bold"), text='',
                      command=lambda: self.click(btn7))
        btn7.grid(row=3, column=0, padx=5, pady=5)
        btn8 = Button(self.window, height=5, width=10, font=("Arial", 12, "bold"), text='',
                      command=lambda: self.click(btn8))
        btn8.grid(row=3, column=1, padx=5, pady=5)
        btn9 = Button(self.window, height=5, width=10, font=("Arial", 12, "bold"), text='',
                      command=lambda: self.click(btn9))
        btn9.grid(row=3, column=2, padx=5, pady=5)
        clicked_buttons = 0

    def play_again(self):
        decision = messagebox.askokcancel('Game over', 'Do you want to play again?')
        if decision:
            self.create_gui()
        else:
            self.window.quit()

    def set_winner_line(self, b1, b2, b3):
        b1.config(bg='green', fg='black')
        b2.config(bg='green', fg='black')
        b3.config(bg='green', fg='black')
        if b1['text'] == b2['text'] == b3['text'] == 'X':
            messagebox.showinfo("", "X wins!")
        else:
            messagebox.showinfo("", "O wins!")
        self.play_again()

    def check_winner(self):
        if btn1['text'] == btn2['text'] == btn3['text'] != '':
            self.set_winner_line(btn1, btn2, btn3)

        elif btn4['text'] == btn5['text'] == btn6['text'] != '':
            self.set_winner_line(btn4, btn5, btn6)

        elif btn7['text'] == btn8['text'] == btn9['text'] != '':
            self.set_winner_line(btn7, btn8, btn9)

        elif btn1['text'] == btn4['text'] == btn7['text'] != '':
            self.set_winner_line(btn1, btn4, btn7)

        elif btn2['text'] == btn5['text'] == btn8['text'] != '':
            self.set_winner_line(btn2, btn5, btn8)

        elif btn3['text'] == btn6['text'] == btn9['text'] != '':
            self.set_winner_line(btn3, btn6, btn9)

        elif btn1['text'] == btn5['text'] == btn9['text'] != '':
            self.set_winner_line(btn1, btn5, btn9)

        elif btn3['text'] == btn5['text'] == btn7['text'] != '':
            self.set_winner_line(btn3, btn5, btn7)

        elif clicked_buttons == 9:
            messagebox.showinfo("", "It's tie!")
            self.play_again()


root = Tk()
game = Game(root)
root.mainloop()
