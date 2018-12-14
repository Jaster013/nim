import tkinter
import tkinter.messagebox

import Spel


class Gui:
    def __init__(self):
        self.main_window = tkinter.Tk()

        # Variables
        name = ''
        self.stack1 = Spel.Stack
        self.stack2 = Spel.Stack
        self.stack3 = Spel.Stack
        self.ai = Spel.AI
        self.human = Spel.Human(name)

        # Frames
        self.frame1 = tkinter.Frame(self.main_window)
        self.frame2 = tkinter.Frame(self.main_window)
        self.frame3 = tkinter.Frame(self.main_window)

        # First frame
        self.empty_frame = tkinter.Label(self.frame1, text='')
        self.label_player = tkinter.Label(self.frame2, text='Speler')
        self.label_AI = tkinter.Label(self.frame3, text='AI')

        self.empty_frame.pack(side='top')
        self.label_player.pack(side='top')
        self.label_AI.pack(side='top')

        # Name frame
        self.label_name = tkinter.Label(self.frame1, text='Naam:')
        self.player_name = tkinter.Entry(self.frame2, textvariable=self.human.getName)
        self.AI_name = tkinter.Entry(self.frame3, textvariable=self.ai.getName)

        self.label_name.pack(side='top')
        self.player_name.pack(side='top')
        self.AI_name.pack(side='top')

        # Move frame
        self.moves_label = tkinter.Label(self.frame1, text='Aantal zetten:')
        self.player_moves = tkinter.Entry(self.frame2, textvariable=self.human.getMoves)
        self.AI_moves = tkinter.Entry(self.frame3, textvariable=self.ai.getMoves)

        self.moves_label.pack(side='top')
        self.player_moves.pack(side='top')
        self.AI_moves.pack(side='top')

        # Stack frame
        self.stack1_label = tkinter.Label(self.frame1, text='Stapel 1')
        self.stack2_label = tkinter.Label(self.frame2, text='Stapel 2')
        self.stack3_label = tkinter.Label(self.frame3, text='Stapel 3')

        self.stack1_label.pack(side='top')
        self.stack2_label.pack(side='top')
        self.stack3_label.pack(side='top')

        # Balls left frame
        self.stack1_balls = tkinter.Entry(self.frame1, textvariable=self.stack1.getStack)
        self.stack2_balls = tkinter.Entry(self.frame2, textvariable=self.stack2.getStack)
        self.stack3_balls = tkinter.Entry(self.frame3, textvariable=self.stack3.getStack)

        self.stack1_balls.pack(side='top')
        self.stack2_balls.pack(side='top')
        self.stack3_balls.pack(side='top')

        # Balls taken frame
        self.balls_taken1 = tkinter.Entry(self.frame1)
        self.balls_taken2 = tkinter.Entry(self.frame2)
        self.balls_taken3 = tkinter.Entry(self.frame3)

        self.balls_taken1.pack(side='top')
        self.balls_taken2.pack(side='top')
        self.balls_taken3.pack(side='top')

        # Button frame
        self.set_button = tkinter.Button(self.frame1, text='Zet', command=self.Set)
        self.new_button = tkinter.Button(self.frame2, text='Nieuw', command=self.New)
        self.quit_button = tkinter.Button(self.frame3, text='Stop', command=self.main_window.destroy)

        self.set_button.pack(side='top')
        self.new_button.pack(side='top')
        self.quit_button.pack(side='top')

        # Pack frames
        self.frame1.pack(side='left')
        self.frame2.pack(side='left')
        self.frame3.pack(side='left')

        tkinter.mainloop()

    def New(self):
        pass

    def Set(self):
        pass


if __name__ == "__main__":
    gui = Gui()
