
import random
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from Crypto.Cipher import AES
import base64
import requests
import json

class FitnessApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Space Fitness Tracker")
        self.master.geometry("600x500")
        self.master.configure(bg='#2C3E50')
        self.master.option_add('*TButton*highlightBackground', '#2C3E50')
        self.master.option_add('*TButton*highlightColor', '#2C3E50')
        self.master.option_add('*TButton*background', '#3498DB')
        self.master.option_add('*TButton*foreground', 'white')

        self.inspirational_quotes = [
            "The only bad workout is the one that didn't happen.",
            "Don't stop until you're proud.",
            "Your only limit is you.","The only way to do great work is to love what you do. - Steve Jobs",

   "Your time is limited, so don't waste it living someone else's life. - Steve Jobs",

   "The best and most beautiful things in the world cannot be seen or even touched - they must be felt with the heart. - Helen Keller",

   "The only thing that stands between you and your dream is the will to try and the belief that it is actually possible. - Joel Brown",

   "The difference between ordinary and extraordinary is that little extra. - Jimmy Johnson",

   "The best revenge is massive success. - Frank Sinatra",

   "Don't be afraid to give up the good to go for the great. - John D. Rockefeller",

   "I have not failed. I've just found 10,000 ways that won't work. - Thomas A. Edison",

   "If you can dream it, you can do it. - Walt Disney",

   "The only person you are destined to become is the person you decide to be. - Ralph Waldo Emerson",

   "Believe you can and you're halfway there. - Theodore Roosevelt",

   "The journey of a thousand miles begins with a single step. - Lao Tzu",

   "Everything you've ever wanted is on the other side of fear. - George Addair",

   "Life is not about finding yourself. Life is about creating yourself. - George Bernard Shaw",

   "The best time to plant a tree was 20 years ago. The second best time is now. - Chinese Proverb",

   "The best and most beautiful things in the world cannot be seen or even touched - they must be felt with the heart. - Helen Keller",

   "Every day may not be good, but there is something good in every day. - Alice Morse Earle",

   "The only way to do great work is to love what you do. - Steve Jobs",

   "If you can dream it, you can do it. - Walt Disney",

   "The only person you are destined to become is the person you decide to be. - Ralph Waldo Emerson",

   "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",

   "The only way to do great work is to love what you do. - Steve Jobs",

   "The only thing that stands between you and your dream is the will to try and the belief that it is actually possible. - Joel Brown",

   "The difference between ordinary and extraordinary is that little extra. - Jimmy Johnson",

   "The best revenge is massive success. - Frank Sinatra",

   "Don't be afraid to give up the good to go for the great. - John D. Rockefeller",

   "I have not failed. I've just found 10,000 ways that won't work. - Thomas A. Edison",

   "If you can dream it, you can do it. - Walt Disney",

   "The only person you are destined to become is the person you decide to be. - Ralph Waldo Emerson",

   "Believe you can and you're halfway there. - Theodore Roosevelt",

   "The journey of a thousand miles begins with a single step. - Lao Tzu",

   "Everything you've ever wanted is on the other side of fear. - George Addair",

   "Life is not about finding yourself. Life is about creating yourself. - George Bernard Shaw",

   "The best time to plant a tree was 20 years ago. The second best time is now. - Chinese Proverb",

   "The best and most beautiful things in the world cannot be seen or even touched - they must be felt with the heart. - Helen Keller",

   "Every day may not be good, but there is something good in every day. - Alice Morse Earle",

   "The only way to do great work is to love what you do. - Steve Jobs",

   "If you can dream it, you can do it. - Walt Disney",

   "The only person you are destined to become is the person you decide to be. - Ralph Waldo Emerson",

   "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",

   "It is never too late to be what you might have been. - George Eliot",

   "The best and most beautiful things in the world cannot be seen or even touched - they must be felt with the heart. - Helen Keller",

   "The only way to do great work is to love what you do. - Steve Jobs"
            
        ]

        self.exercise_types = ["Space Walk", "Zero Gravity Yoga", "Astronaut Training", "Weightlifting", "Cardio"]

        self.current_quote = tk.StringVar()
        self.current_quote.set(random.choice(self.inspirational_quotes))

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="Exercise Type:", bg='#2C3E50', fg='white').pack()
        self.exercise_type_var = tk.StringVar(value=self.exercise_types[0])
        exercise_type_combobox = ttk.Combobox(self.master, textvariable=self.exercise_type_var, values=self.exercise_types, state="readonly")
        exercise_type_combobox.pack()

        tk.Label(self.master, text="Exercise Name:", bg='#2C3E50', fg='white').pack()
        self.exercise_name_entry = tk.Entry(self.master)
        self.exercise_name_entry.pack()

        tk.Label(self.master, text="Duration (min):", bg='#2C3E50', fg='white').pack()
        self.duration_entry = tk.Entry(self.master)
        self.duration_entry.pack()

        tk.Label(self.master, text="Weight (kg):", bg='#2C3E50', fg='white').pack()
        self.weight_entry = tk.Entry(self.master)
        self.weight_entry.pack()

        tk.Label(self.master, text="Height (cm):", bg='#2C3E50', fg='white').pack()
        self.height_entry = tk.Entry(self.master)
        self.height_entry.pack()

        tk.Label(self.master, text="Mass (kg):", bg='#2C3E50', fg='white').pack()
        self.mass_entry = tk.Entry(self.master)
        self.mass_entry.pack()

        tk.Label(self.master, text="Oxygen Saturation (%):", bg='#2C3E50', fg='white').pack()
        self.oxygen_saturation_entry = tk.Entry(self.master)
        self.oxygen_saturation_entry.pack()

        tk.Label(self.master, text="BPM:", bg='#2C3E50', fg='white').pack()
        self.bpm_entry = tk.Entry(self.master)
        self.bpm_entry.pack()

        tk.Button(self.master, text="Submit", command=self.submit_entry).pack()

        tk.Label(self.master, text="Inspirational Quote:", bg='#2C3E50', fg='white').pack()
        tk.Label(self.master, textvariable=self.current_quote, bg='#2C3E50', fg='white').pack()

        tk.Button(self.master, text="Next Quote", command=self.next_quote).pack()

        tk.Button(self.master, text="Share Progress", command=self.share_progress).pack()
        tk.Button(self.master, text="Show Exercise Examples", command=self.show_exercise_examples).pack()

    def submit_entry(self):
        exercise_type = self.exercise_type_var.get()
        exercise_name = self.exercise_name_entry.get()
        duration = self.duration_entry.get()
        weight = self.weight_entry.get()
        height = self.height_entry.get()
        mass = self.mass_entry.get()
        oxygen_saturation = self.oxygen_saturation_entry.get()
        bpm = self.bpm_entry.get()

        if exercise_name and duration and weight and height and mass and oxygen_saturation and bpm:
            message = f"Exercise Type: {exercise_type}\nExercise Name: {exercise_name}\nDuration: {duration} min\nWeight: {weight} kg\nHeight: {height} cm\nMass: {mass} kg\nOxygen Saturation: {oxygen_saturation}%\nBPM: {bpm}"
            messagebox.showinfo("Exercise Entry", message)
        else:
            messagebox.showwarning("Incomplete Entry", "Please fill in all fields.")

    def next_quote(self):
        self.current_quote.set(random.choice(self.inspirational_quotes))



    def share_progress(self):
        exercise_type = self.exercise_type_var.get()
        exercise_name = self.exercise_name_entry.get()
        duration = self.duration_entry.get()
        weight = self.weight_entry.get()
        height = self.height_entry.get()
        mass = self.mass_entry.get()
        oxygen_saturation = self.oxygen_saturation_entry.get()
        bpm = self.bpm_entry.get()

        if exercise_name and duration and weight and height and mass and oxygen_saturation and bpm:
            progress_data = {
                "exercise_type": exercise_type,
                "exercise_name": exercise_name,
                "duration": duration,
                "weight": weight,
                "height": height,
                "mass": mass,
                "oxygen_saturation": oxygen_saturation,
                "bpm": bpm,
            }

            try:
                response = requests.post('https://xvy7vm-5000.csb.app/share_progress', json={'progress': progress_data})
                if response.status_code == 200:
                    code = response.json().get('code')
                    url = f'https://xvy7vm-5000.csb.app/get_progress/{code}'
                    
                    messagebox.showinfo("Share Progress", f"Progress shared successfully!\nShare this code:\n{code}")
                else:
                    messagebox.showerror("Share Progress", "Failed to share progress. Please try again.")
            except Exception as e:
                messagebox.showerror("Share Progress", f"An error occurred: {str(e)}")
        else:
            messagebox.showwarning("Incomplete Entry", "Please fill in all fields.")

    
        import webbrowser
        webbrowser.open(f'https://xvy7vm-5000.csb.app/get_progress/{code}')


    def show_exercise_examples(self):
        examples_window = tk.Toplevel(self.master)
        examples_window.title("Exercise API Examples")
        examples_window.geometry("800x400")

        scroll_frame = ttk.Frame(examples_window)
        scroll_frame.pack(fill='both', expand=True)

        scrollbar = ttk.Scrollbar(scroll_frame, orient='vertical')
        example_text = scrolledtext.ScrolledText(scroll_frame, wrap='word', yscrollcommand=

scrollbar.set)
        example_text.insert(tk.END, json.dumps(exercise_examples, indent=2))
        example_text.config(state='disabled')
        scrollbar.config(command=example_text.yview)

        example_text.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')

exercise_examples = []
   

if __name__ == "__main__":
    root = tk.Tk()
    app = FitnessApp(root)
    root.mainloop()
