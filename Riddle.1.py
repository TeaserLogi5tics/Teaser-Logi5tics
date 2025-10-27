import tkinter as tk
from tkinter import messagebox

riddles = [
    {"question": "I speak without a mouth and hear without ears. What am I?", "answer": "echo"},
    {"question": "What has keys but can't open locks?", "answer": "piano"},
    {"question": "I’m not alive, but I can grow. I don’t have lungs, but I need air. What am I?", "answer": "fire"},
    {"question": "What has a head and a tail but no body?", "answer": "coin"},
    {"question": "What comes once in a minute, twice in a moment, but never in a thousand years?", "answer": "m"},
    {"question": "I’m tall when I’m young and short when I’m old. What am I?", "answer": "candle"},
    {"question": "The more you take, the more you leave behind. What are they?", "answer": "footsteps"},
]


current_riddle = 0
score = 0
time_left = 20
timer_running = False


def show_riddle():
    global time_left, timer_running
    question_label.config(text=riddles[current_riddle]["question"])
    answer_entry.delete(0, tk.END)
    result_label.config(text="")
    next_button.config(state="disabled")
    submit_button.config(state="normal")
    time_left = 20
    timer_label.config(text=f"Time: {time_left}")
    timer_running = True
    countdown()


def check_answer():
    global score
    user_input = answer_entry.get().strip().lower()
    correct_answer = riddles[current_riddle]["answer"].lower()


    if user_input == correct_answer:
        score += 1
        result_label.config(text="Correct!", fg="green")
        score_label.config(text=f"Score: {score}")
    else:
        result_label.config(text=f"Wrong! The answer was '{correct_answer}'", fg="red")


    next_button.config(state="normal")
    submit_button.config(state="disabled")


def next_riddle():
    global current_riddle
    current_riddle += 1

    if current_riddle < len(riddles):
        show_riddle()
    else:
        messagebox.showinfo("Game Over", f"You finished the game! Final score: {score}/{len(riddles)}")
        window.destroy()

def end_game():
    global timer_running
    timer_running = False
    messagebox.showinfo("Ooops! Out of TIME", f"You finished the game!\nFinal Score: {score}/{len(riddles)}")
    question_label.config(text=f"Game Over! Final Score: {score}/{len(riddles)}")
    submit_button.config(state="disabled")
    next_button.config(state="disabled")
    restart_button.pack(pady=10)

def countdown():
    global time_left, timer_running
    if timer_running and time_left > 0:
        timer_label.config(text=f"Time: {time_left}")
        time_left -= 1
        window.after(1000, countdown)
    elif time_left == 0 and timer_running:
        result_label.config(text="Time’s up!", fg="red")
        next_button.config(state="normal")
        submit_button.config(state="disabled")

def restart_game():
    global score, current_riddle
    score = 0
    current_riddle = 0
    score_label.config(text=f"Score: {score}")
    restart_button.pack_forget()
    show_riddle()

window = tk.Tk()
window.title("Teaser Logi5tics")
window.geometry("1080x720")
window.config(bg="#C6A488")

icon = tk.PhotoImage(file="logo1.png")
window.iconphoto(False, icon)

question_label = tk.Label(window, text="", wraplength=600, font=("Verdana", 15, "bold"))
question_label.pack(pady=20, padx=10)

result_label = tk.Label(window, text="", font=("Times New Roman",13), bg="#f5f5f5")
result_label.pack(pady=5, padx=10)

answer_entry = tk.Entry(window, font=("Times New Roman", 20))
answer_entry.pack()

timer_label = tk.Label(window, text="Time: 20", bg="#C5B5A6", fg="black",font=("Arial", 10, "bold"))
timer_label.pack(pady=5, padx=10)

score_label = tk.Label(window, text="Score: 0", bg="#C5B5A6", font=("Times New Roman", 9, "bold"), relief="ridge")
score_label.pack(pady=10, padx=10)

submit_button = tk.Button(window, text="Submit Answer", command=check_answer,font=("Verdana",12, "bold"), relief="ridge", bg="#C5B5A6", fg="black", height=3, width=15)
submit_button.pack(pady=10,padx=10)

next_button = tk.Button(window, text="Next Riddle", command=next_riddle, state="disabled", font=("Verdana",12, "bold"), relief="ridge", bg="#C5B5A6", fg="black", height=2, width=12)
next_button.pack(side = "bottom",pady=10, padx=10)

restart_button = tk.Button(window, text="Restart Game", command=restart_game, bg="#C5B5A6", fg="black", font=("Arial", 10, "bold"))
restart_button.pack_forget()

show_riddle()
window.mainloop()
