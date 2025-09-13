import tkinter as tk
from tkinter import messagebox

# Login Credentials
USERNAME = "kbc24"
PASSWORD = "Jaat@123"

# Quiz Questions (Structured by Rounds)
rounds = {
    "Round 1": [
        {"question": "Q1. Who developed Python programming language?",
         "options": ["Wick van Rossum", "Rasmus Lerdorf", "Guido van Rossum", "Niene Stom"],
         "answer": "Guido van Rossum"},
        {"question": "Q2. Which keyword is used to define a function in Python?",
         "options": ["fun", "def", "function", "define"],
         "answer": "def"},
        {"question": "Q3. Which character is used to give single-line comments in Python?",
         "options": ["# (Pound)", "// (Slash)", "-- (Dash)", "/* (Asterisk)"],
         "answer": "# (Pound)"},
        {"question": "Q4. Which function is used to take input directly from user in python?",
         "options": ["print()", "INPUT()", "format()", "input()"],
         "answer": "input()"},
        {"question": "Q5. Is python code?",
         "options": ["Compiled", "Interpreted", "Both a and b", "None of these"],
         "answer": "Both a and b"}
    ],
    "Round 2": [
        {"question": "Q1. Giddha is the folk dance of which state in India?",
         "options": ["Assam", "West Bengal", "Odisha", "Punjab"],
         "answer": "Punjab"},
        {"question": "Q2. Highest dam of India is?",
         "options": ["Sardar Sarovar Dam", "Tehri Dam", "Bhakra Nangal Dam", "None of these"],
         "answer": "Tehri Dam"},
        {"question": "Q3. Who heads the RBI?",
         "options": ["Home Minister", "Governor", "President ", "Finance Minister"],
         "answer": "Governor"},
        {"question": "Q4. On which date and year did the Titanic sink?",
         "options": ["18-April-1912", "14-April-1907", "14-April-1912", "18-April-1907"],
         "answer": "14-April-1912"},
        {"question": "Q5. Who is known as The God of Cricket?",
         "options": ["Virat Kohli", "MS Dhoni", "Sachin Tendulkar", "Rohit Sharma"],
         "answer": "Sachin Tendulkar"}
    ],
    "Round 3": [
        {"question": "Q1. The first AI programming language was called:",
         "options": ["BASIC", "FORTRAN", "IPL", "LISP"],
         "answer": "LISP"},
        {"question": "Q2. What was the first iPhone model to feature a fingerprint sensor?",
         "options": ["iPhone 5", "iPhone 6", "iPhone 4s", "iPhone 5s"],
         "answer": "iPhone 5s"},
        {"question": "Q3. Which Of The Following Does Not Belong To Java?",
         "options": ["Switch", "Double", "Instance Of ", "Then "],
         "answer": "Then "},
        {"question": "Q4. Artificial Intelligence Introduce In?",
         "options": ["1970", "1978", "1956", "1965"],
         "answer": "1956"},
        {"question": "Q5. Which data structure is used to implement recursion?",
         "options": ["Queue", "Stack", "Linked list", "Tree"],
         "answer": "Stack"}
        ]
}

# Global variables
current_round = list(rounds.keys())[0]
current_question_index = 0
score = 0 # cumulative score
current_round_score = 0  # score in current round
round_scores={"Round 1": 0,"Round 2": 0,"Round 3": 0}

# Function to check login
def check_login():
    username = username_entry.get()
    password = password_entry.get()
    if username == USERNAME and password == PASSWORD:
        messagebox.showinfo("Login", "Login Successful! \nWelcome to KBC \nMade by SANDEEP JAAT")
        login_frame.pack_forget()
        quiz_frame.pack()
        load_question()
    else:
        messagebox.showerror("Login Failed", "Invalid Username or Password \nPlease try again.")

# Function to load questions
def load_question():
    global current_question_index, current_round
    
    if current_round in rounds and current_question_index < len(rounds[current_round]):
        q = rounds[current_round][current_question_index]
        question_label.config(text=f"{current_round}: {q['question']}")
        answer_var.set("")  # Reset selection
        selected_option_label.config(text="Selected Option: None")  # Reset displayed selection

        for i in range(len(q["options"])):
            options[i].config(text=q["options"][i], value=q["options"][i])
    else:
        end_of_round()

# Function to update selected option label
def show_selected():
    selected_option_label.config(text=f"Selected Option: {answer_var.get()}")

# Function to check the answer
def check_answer():
    global current_question_index, score , current_round_score
    
    selected = answer_var.get()
    if not selected:
        messagebox.showwarning("No Selection", "Please select an option before submitting!")
        return
    
    correct_answer = rounds[current_round][current_question_index]["answer"]
    if selected == correct_answer:
        score += 10
        current_round_score += 10
        messagebox.showinfo("Correct!", f"Your answer is correct!\nYour score: {score}")
    else:
        messagebox.showerror("Wrong!", f"Wrong answer!\nCorrect answer: {correct_answer}")
    
    current_question_index += 1
    load_question()

# Function called when round ends
def end_of_round():
    global round_scores, current_round_score
    round_scores[current_round] = current_round_score
    messagebox.showinfo("Round Over", f"{current_round} is over!\nYour score in this round: {round_scores[current_round]}\nTotal score: {score}")
    ask_next_round()


# Function to ask user whether to go to next round
def ask_next_round():
    global current_round, current_question_index, score,current_round_score

    round_keys = list(rounds.keys())
    current_index = round_keys.index(current_round)
    
    if current_index + 1 < len(round_keys):
        # Store the score of current round before moving to next
        previous_scores = {k: round_scores[k] for k in round_scores if round_scores[k] != 0}
        result = messagebox.askyesno("Next Round", "Do you want to go for the next round?")
        if result:
            current_round = round_keys[current_index + 1]
            current_question_index = 0
            current_round_score=0
            # Build message according to which round is coming next
            message = ""
            if current_round == "Round 2":
                message = f"Round 1 total score is {round_scores['Round 1']}\n"
            elif current_round == "Round 3":
                total_so_far = round_scores["Round 1"] + round_scores["Round 2"]
                message = (f"Round 1 score is {round_scores['Round 1']}\n"
                           f"Round 2 score is {round_scores['Round 2']}\n"
                           f"Total score till now is {total_so_far}\n")
            messagebox.showinfo("Starting Next Round",message )
            load_question()
        else:
            show_final_score()
    else:
        show_final_score()

# Function to show final score at the end
def show_final_score():
    total = round_scores["Round 1"] + round_scores["Round 2"] + round_scores["Round 3"]
    messagebox.showinfo("Game Over",
                        f"Final Scores:\n"
                        f"Round 1: {round_scores['Round 1']}\n"
                        f"Round 2: {round_scores['Round 2']}\n"
                        f"Round 3: {round_scores['Round 3']}\n\n"
                        f"Total Score: {total}"
                        f"\nThank you for playing KBC!")
    root.quit()

# GUI Setup
root = tk.Tk()
root.title("Kaun Banega Crorepati")
root.geometry("600x450")
root.configure(bg="black")

# Login Frame
login_frame = tk.Frame(root, bg="black")
tk.Label(login_frame, text="KBC LOGIN", fg="yellow", bg="black", font=("Arial", 16)).pack(pady=10)
tk.Label(login_frame, text="Username:", fg="white", bg="black").pack()
username_entry = tk.Entry(login_frame)
username_entry.pack()

tk.Label(login_frame, text="Password:", fg="white", bg="black").pack()
password_entry = tk.Entry(login_frame, show="*")
password_entry.pack()

tk.Button(login_frame, text="Login", command=check_login, fg="black", bg="yellow").pack(pady=10)
login_frame.pack()

# Quiz Frame
quiz_frame = tk.Frame(root, bg="black")
question_label = tk.Label(quiz_frame, text="", fg="yellow", bg="black", font=("Arial", 14), wraplength=500)
question_label.pack(pady=10)

answer_var = tk.StringVar()
options = []
for i in range(4):
    rb = tk.Radiobutton(quiz_frame, text="", variable=answer_var, value="", fg="white", bg="black", font=("Arial", 12), command=show_selected)
    rb.pack()
    options.append(rb)

selected_option_label = tk.Label(quiz_frame, text="Selected Option: None", fg="white", bg="black", font=("Arial", 12))
selected_option_label.pack(pady=5)

tk.Button(quiz_frame, text="Submit", command=check_answer, fg="black", bg="yellow").pack(pady=10)

root.mainloop()
