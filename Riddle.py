import tkinter as tk
from tkinter import messagebox

#Answer Checker
def check_answer():
    global score
    user_input = answer_entry.get()
    correct_answer = riddles[current_riddle]["answer"]

    if user_input == correct_answer:
        result_label.config(text="Correct!", fg="green")
        score_label.config(text=f"Score: {score + 1}")
        next_button.config(state="normal")
        submit_button.config(state="disabled")
        score += 1
    else:
        result_label.config(text="Wrong!", fg="red")

#Next riddle
def next_riddle():
    global current_riddle
    current_riddle += 1

    if current_riddle < len(riddles):
        show_riddle()
    else:
        messagebox.showinfo("Game Over", f"You finished the game! Final score: {score}/{len(riddles)}")
        window.destroy()

def show_riddle():
    question_label.config(text=riddles[current_riddle]["question"])
    answer_entry.delete(0, tk.END)
    result_label.config(text="")
    next_button.config(state="disabled")
    submit_button.config(state="normal")

# def restart_game():
#     submit_button.config(state="normal")
#     restart_game()


window = tk.Tk()
window.title("Teaser Logi5tics")
window.geometry("400x300")
window.config(bg="#CCCCCC")

#Icon
icon= tk.PhotoImage(file="logo1.png")
window.iconphoto(icon, icon)

question_label = tk.Label(window, text="", wraplength=250, font=("Verdana", 11), bg="#CCCCCC")
question_label.pack(pady=20)

answer_entry = tk.Entry(window, font=("Arial", 10))
answer_entry.pack()

submit_button = tk.Button(window, text="Submit Answer", command=check_answer, relief="ridge", bg = "gray", fg="white" )
submit_button.pack(pady=20)
submit_button.pack(pady=10)

result_label = tk.Label(window, text="", font=("Arial", 7), bg="#f5f5f5")
result_label.pack()

next_button = tk.Button(window, text="Next Riddle", command=next_riddle, state="disabled", relief="ridge")
next_button.pack(pady=10)

score_label = tk.Label(window, text="Score: 0", bg="#f5f5f5", font=("Arial", 7), relief="ridge")
score_label.pack(side="bottom", pady=10, padx=10)

# restart_game_button = tk.Button(window, text="Restart Game", command=restart_game)
# restart_game_button.pack(pady=10)

riddles = [
    {"question": "I speak without a mouth and hear without ears. What am I?", "answer": "echo"},
    {"question": "What has keys but can't open locks?", "answer": "piano"},
    {"question": "I’m not alive, but I can grow. I don’t have lungs, but I need air. What am I?", "answer": "fire"},
    {"question": "What has a head and a tail but no body?", "answer": "coin"},
    {"question": "What comes once in a minute, twice in a moment, but never in a thousand years?", "answer": "m"},
    {"question": "I’m tall when I’m young and short when I’m old. What am I?", "answer": "candle"},
    {"question": "The more you take, the more you leave behind. What are they?", "answer": "footsteps"},
    {"question": "The more you take, the more you leave behind. What are they?", "answer": "stamp"},
]

current_riddle = 0
score = 0

show_riddle()

window.mainloop()
