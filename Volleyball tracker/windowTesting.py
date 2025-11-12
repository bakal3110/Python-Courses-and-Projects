import customtkinter as ctk

def increase_team1_points():
    global team1_points
    team1_points += 1
    update_labels()

def increase_team2_points():
    global team2_points
    team2_points += 1
    update_labels()

def increase_team1_sets():
    global team1_sets
    team1_sets += 1
    update_labels()

def increase_team2_sets():
    global team2_sets
    team2_sets += 1
    update_labels()

def update_labels():
    team1_points_label.configure(text=str(team1_points))
    team2_points_label.configure(text=str(team2_points))
    sets_label.configure(text=f"{team1_sets}:{team2_sets}")

app = ctk.CTk()
app.title("Volleyball Points Tracker")

team1_points = 14
team2_points = 21
team1_sets = 0
team2_sets = 1

# Layout
court_frame = ctk.CTkFrame(app, width=400, height=200, border_width=2)
court_frame.place(relx=0.5, rely=0.5, anchor="center")

team1_label = ctk.CTkLabel(app, text="Team 1")
team1_label.place(relx=0.3, rely=0.2, anchor="center")

team2_label = ctk.CTkLabel(app, text="Team 2")
team2_label.place(relx=0.7, rely=0.2, anchor="center")

team1_points_label = ctk.CTkLabel(app, text=str(team1_points), text_color="red")
team1_points_label.place(relx=0.3, rely=0.3, anchor="center")

team2_points_label = ctk.CTkLabel(app, text=str(team2_points), text_color="red")
team2_points_label.place(relx=0.7, rely=0.3, anchor="center")

sets_label = ctk.CTkLabel(app, text=f"{team1_sets}:{team2_sets}")
sets_label.place(relx=0.5, rely=0.2, anchor="center")

increase_team1_points_button = ctk.CTkButton(app, text="Increase Team 1 Points", command=increase_team1_points)
increase_team1_points_button.place(relx=0.3, rely=0.4, anchor="center")

increase_team2_points_button = ctk.CTkButton(app, text="Increase Team 2 Points", command=increase_team2_points)
increase_team2_points_button.place(relx=0.7, rely=0.4, anchor="center")

increase_team1_sets_button = ctk.CTkButton(app, text="Increase Team 1 Sets", command=increase_team1_sets)
increase_team1_sets_button.place(relx=0.3, rely=0.5, anchor="center")

increase_team2_sets_button = ctk.CTkButton(app, text="Increase Team 2 Sets", command=increase_team2_sets)
increase_team2_sets_button.place(relx=0.7, rely=0.5, anchor="center")

app.mainloop()
