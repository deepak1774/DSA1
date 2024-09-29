import tkinter as tk
from tkinter import messagebox

# List of Python-related questions, options, and correct answers
questions = [
    {"question": "Which keyword is used to define a function in Python?",
     "options": ["def", "func", "define", "lambda"], "answer": "def"},

    {"question": "What is the correct syntax to output 'Hello World' in Python?",
     "options": ["echo 'Hello World'", "p('Hello World')", "print('Hello World')", "printf('Hello World')"],
     "answer": "print('Hello World')"},

    {"question": "Which of the following is a mutable data type in Python?",
     "options": ["tuple", "list", "int", "str"], "answer": "list"},

    {"question": "How do you insert comments in Python code?",
     "options": ["// This is a comment", "# This is a comment", "/* This is a comment */", "-- This is a comment"],
     "answer": "# This is a comment"},

    {"question": "What does the len() function do?",
     "options": ["Returns the number of characters in a string", "Returns the number of items in a list",
                 "Returns the size of an object", "All of the above"],
     "answer": "All of the above"}
]

# Variables to keep track of current question, score, and time
current_question = 0
score = 0
time_left = 20  # Update to 20 seconds
timer_running = False  # Prevent multiple pop-ups


# Function to display the next question
def show_question():
    global current_question, time_left, timer_running
    timer_running = False  # Stop the timer for the previous question
    if current_question < len(questions):
        time_left = 20  # Reset the timer to 20 seconds
        timer_label.config(text=f"Time left: {time_left} seconds")
        timer_running = True  # Set the timer to start running again
        update_timer()

        # Update the question and options
        question_label.config(text=questions[current_question]["question"])
        option1.config(text=questions[current_question]["options"][0])
        option2.config(text=questions[current_question]["options"][1])
        option3.config(text=questions[current_question]["options"][2])
        option4.config(text=questions[current_question]["options"][3])
    else:
        # Quiz finished, show the final score
        messagebox.showinfo("Quiz Finished", f"Your score is: {score}")
        root.quit()  # Close the game window


# Function to update the timer
def update_timer():
    global time_left, timer_running
    if time_left > 0 and timer_running:
        time_left -= 1
        timer_label.config(text=f"Time left: {time_left} seconds")
        root.after(1000, update_timer)  # Update timer every second
    elif time_left == 0 and timer_running:
        timer_running = False  # Prevent multiple pop-ups
        messagebox.showinfo("Time's up!", "You ran out of time!")
        check_answer(None)  # If time runs out, move to the next question


# Function to check the selected answer
def check_answer(selected_option):
    global current_question, score

    correct_answer = questions[current_question]["answer"]

    if selected_option == correct_answer:
        score += 1  # Add to score if correct

    current_question += 1
    show_question()  # Move to the next question


# Function to toggle full-screen mode
def toggle_fullscreen(event=None):
    root.attributes("-fullscreen", True)


# Function to exit full-screen mode
def end_fullscreen(event=None):
    root.attributes("-fullscreen", False)


# Set up the main window
root = tk.Tk()
root.title("Quiz Game")
root.iconbitmap("icon1.ico")

# Set the background color of the main window
root.configure(bg='#1e1e2e')

# Set the window to full-screen mode by default
root.attributes("-fullscreen", True)

# Get screen width and height for placing elements
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Bind the "F11" key to toggle full-screen mode and "Escape" to exit full-screen
root.bind("<F11>", toggle_fullscreen)
root.bind("<Escape>", end_fullscreen)

# Create and place the question label with a color theme
question_label = tk.Label(root, text="", wraplength=screen_width - 100, font=('Arial', 24), bg='#1e1e2e', fg='#f4f4f4')
question_label.pack(pady=50)

# Button colors for a more attractive look
button_bg_color = '#ff6b6b'
button_fg_color = '#ffffff'
button_active_bg = '#ff8787'

# Create and place the option buttons
option1 = tk.Button(root, text="", font=('Arial', 20), command=lambda: check_answer(option1.cget("text")),
                    bg=button_bg_color, fg=button_fg_color, activebackground=button_active_bg)
option1.pack(pady=10)

option2 = tk.Button(root, text="", font=('Arial', 20), command=lambda: check_answer(option2.cget("text")),
                    bg=button_bg_color, fg=button_fg_color, activebackground=button_active_bg)
option2.pack(pady=10)

option3 = tk.Button(root, text="", font=('Arial', 20), command=lambda: check_answer(option3.cget("text")),
                    bg=button_bg_color, fg=button_fg_color, activebackground=button_active_bg)
option3.pack(pady=10)

option4 = tk.Button(root, text="", font=('Arial', 20), command=lambda: check_answer(option4.cget("text")),
                    bg=button_bg_color, fg=button_fg_color, activebackground=button_active_bg)
option4.pack(pady=10)

# Create and place the timer label with a different color
timer_label = tk.Label(root, text=f"Time left: {time_left} seconds", font=('Arial', 20), bg='#1e1e2e', fg='#8be9fd')
timer_label.pack(pady=20)

# Show the first question
show_question()

# Start the main loop for the window
root.mainloop()
