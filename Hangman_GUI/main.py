from tkinter import *
from PIL import ImageTk, Image
import random
from tkinter import messagebox
from hangman_words import word_list_en, word_list_ro
import easygui


class Hangman:

    def __init__(self, window):
        self.window = window
        window.title("Hangman")
        window.geometry('1200x800')
        window.config(bg='#1D6F42')
        self.chosen_word = None
        self.lives = None
        self.not_guess = None
        self.stages = None
        self.display_list = None
        self.guess_input = None
        self.show_stage = None
        self.show_word = None
        self.game()

    def game(self):

        if self.select_language():

            self.not_guess = ''
            self.lives = 6

            self.display_list = []
            for _ in range(len(self.chosen_word)):
                self.display_list += '_'

            self.guess_input = Entry(self.window)
            self.guess_input.place(x=500, y=650, width=200, height=45)
            self.guess_input.insert(0, "Enter a letter...")

            self.show_word = Label(self.window, font=('Arial', 32, 'bold'), bg='#1D6F42', fg='white')
            self.show_word.place(x=300, y=70, width=600, height=85)
            self.show_word["text"] = len(self.chosen_word) * " _ "

            image_size = (400, 400)
            img0 = ImageTk.PhotoImage(Image.open("stages/0.png").resize(image_size))
            img1 = ImageTk.PhotoImage(Image.open("stages/1.png").resize(image_size))
            img2 = ImageTk.PhotoImage(Image.open("stages/2.png").resize(image_size))
            img3 = ImageTk.PhotoImage(Image.open("stages/3.png").resize(image_size))
            img4 = ImageTk.PhotoImage(Image.open("stages/4.png").resize(image_size))
            img5 = ImageTk.PhotoImage(Image.open("stages/5.png").resize(image_size))
            img6 = ImageTk.PhotoImage(Image.open("stages/6.png").resize(image_size))

            self.stages = [img0, img1, img2, img3, img4, img5, img6]

            self.show_stage = Label(self.window, font=('Arial', 32, 'bold'), bg='#1D6F42', fg='white')
            self.show_stage.place(x=300, y=200, width=600, height=400)
            self.show_stage['image'] = self.stages[-1]

            self.guess_input.bind("<Return>", self.play)
            submit_button = Button(self.window, text="Guess")
            submit_button.bind("<Button>", self.play)
            submit_button.place(x=450, y=700, width=300, height=45)

            self.guess_input.bind("<FocusIn>", self.clear_guess_input)
        else:
            self.window.destroy()

    def select_language(self):
        options = ["Romanian", "English"]
        selected_button = easygui.buttonbox("Select language you want to play in..", "Language", choices=options)
        if selected_button == "Romanian":
            self.chosen_word = random.choice(word_list_ro)
            return True
        elif selected_button == "English":
            self.chosen_word = random.choice(word_list_en)
            return True

    def clear_guess_input(self, _event):
        if self.guess_input.get() == "Enter a letter...":
            self.guess_input.delete(0, END)

    def play(self, _event):

        guess = self.guess_input.get().lower()

        if guess in self.display_list:
            messagebox.showinfo("Try another letter!", f"You have already guessed letter: {guess.upper()} ")

        for position in range(len(self.chosen_word)):
            letter = self.chosen_word[position]
            if letter == guess:
                self.display_list[position] = letter

        if guess not in self.chosen_word:
            if guess in self.not_guess:
                messagebox.showinfo("",
                                    f" You have already try  letter: {guess.upper()}  Please make a different choice.")
            else:
                self.lives -= 1
                self.not_guess += guess

        if self.lives:
            self.show_stage['image'] = self.stages[self.lives]
        elif self.lives == 0:
            self.show_stage['image'] = self.stages[0]
            messagebox.showinfo("", f"GAME OVER! YOU LOST!\nThe word was: {self.chosen_word}")
            self.play_again()

        display_word_part = '  '.join(self.display_list)

        if '_' not in self.display_list:
            self.show_word['text'] = self.chosen_word
            messagebox.showinfo("Good job!", f"Congratulations! YOU WON!")
            self.play_again()
        else:
            self.show_word['text'] = f'{display_word_part}'
        self.guess_input.delete(0, END)

    def play_again(self):
        play_again = messagebox.askyesno("Play again?")
        if play_again:
            self.game()
        else:
            self.window.quit()


root = Tk()
game = Hangman(root)
root.mainloop()
