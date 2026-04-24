
'''
Each person needs about 20 bushels of food
Buying land increases future production potential
More land requires more workers to farm
more workers means more mouths to feed
Planting land requires 1 person per ~10 acres & 2 bushels of grain per acre to seed
'''
import random
import tkinter as tk
from tkinter import messagebox


class HamurabiGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hamurabi")
        self.root.geometry("760x560")

        ### State Variables
        self.year = 1
        self.population = 95
        self.bushels_in_store = 2800
        self.acres_owned = 1000
        self.bushels_eaten_by_rats = 200
        self.harvest_per_acre = random.randint(25,45)
        self.acres_per_person = self.acres_owned / self.population
        self.new_immigrants = 5
        self.user_input = 1
        self.total_number_starved = 0
        self.percent_of_population_that_starved = 0.0
        self.number_starved = 0
        self.land_price = random.randint(17, 26)
        self.bushels_to_feed = 0
        self.acres_to_plant = 0

        self.step = "buy"

        self.build_gui()
        self.start_year()

    def build_gui(self):
        self.title_label = tk.Label(self.root, text="HAMURABI", font=("Arial", 18, "bold"))
        self.title_label.pack(pady=10)

        self.output = tk.Text(self.root, height=22, width=88, wrap="word", state="disabled")
        self.output.pack(padx=10, pady=10)

        self.prompt_label = tk.Label(self.root, text="", font=("Arial", 11))
        self.prompt_label.pack(pady=(5, 2))

        self.entry = tk.Entry(self.root, width=20, font=("Arial", 12))
        self.entry.pack()
        self.entry.bind("<Return>", lambda event: self.submit_input())

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)

        self.submit_button = tk.Button(self.button_frame, text="Submit", width=12, command=self.submit_input)
        self.submit_button.grid(row=0, column=0, padx=5)

        self.quit_button = tk.Button(self.button_frame, text="Quit", width=12, command=self.root.destroy)
        self.quit_button.grid(row=0, column=1, padx=5)

    def write_output(self, text):
        self.output.config(state="normal")
        self.output.insert("end", text + "\n")
        self.output.see("end")
        self.output.config(state="disabled")

    def clear_entry(self):
        self.entry.delete(0, "end")
        self.entry.focus()

    def start_year(self):
        if self.year > 10:
            self.end_game()
            return

        self.acres_per_person = self.acres_owned / self.population

        self.write_output(
            f"\nHAMURABI: I BEG TO REPORT TO YOU, IN YEAR {self.year}, "
            f"{self.number_starved} PEOPLE STARVED, {self.new_immigrants} CAME TO THE CITY."
        )

        self.population += self.new_immigrants

        if random.randint(1, 100) <= 15:
            self.population = self.population // 2
            self.write_output("A HORRIBLE PLAGUE STRUCK! HALF THE PEOPLE DIED.")

        self.write_output(f"POPULATION IS NOW {self.population}")
        self.write_output(f"THE CITY NOW OWNS {self.acres_owned} ACRES.")
        self.write_output(f"THAT IS {self.acres_per_person:.2f} ACRES PER PERSON.")
        self.write_output(f"YOU HARVESTED {self.harvest_per_acre} BUSHELS PER ACRE.")
        self.write_output(f"THE RATS ATE {self.bushels_eaten_by_rats} BUSHELS.")
        self.write_output(f"YOU NOW HAVE {self.bushels_in_store} BUSHELS IN STORE.\n")

        self.land_price = random.randint(17, 26)
        self.write_output(f"LAND IS TRADING AT {self.land_price} BUSHELS PER ACRE.")

        self.step = "buy"
        self.prompt_label.config(text="HOW MANY ACRES DO YOU WISH TO BUY?")
        self.clear_entry()

    def submit_input(self):
        raw_value = self.entry.get().strip()

        try:
            self.user_input = int(raw_value)
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a whole number.")
            self.clear_entry()
            return

        if self.user_input < 0:
            self.root.destroy()
            return

        if self.step == "buy":
            self.handle_buy()
        elif self.step == "sell":
            self.handle_sell()
        elif self.step == "feed":
            self.handle_feed()
        elif self.step == "plant":
            self.handle_plant()

    def handle_buy(self):
        if self.user_input * self.land_price > self.bushels_in_store:
            self.write_output("HAMURABI: THINK AGAIN. YOU DON'T HAVE ENOUGH BUSHELS.")
            self.clear_entry()
            return

        self.acres_owned += self.user_input
        self.bushels_in_store -= self.user_input * self.land_price

        self.step = "sell"
        self.prompt_label.config(text="HOW MANY ACRES DO YOU WISH TO SELL?")
        self.clear_entry()

    def handle_sell(self):
        if self.user_input > self.acres_owned:
            self.write_output("HAMURABI: THINK AGAIN. YOU CAN'T SELL MORE ACRES THAN YOU OWN.")
            self.clear_entry()
            return

        self.acres_owned -= self.user_input
        self.bushels_in_store += self.user_input * self.land_price

        self.step = "feed"
        self.prompt_label.config(text="HOW MANY BUSHELS DO YOU WISH TO FEED YOUR PEOPLE?")
        self.clear_entry()

    def handle_feed(self):
        if self.user_input > self.bushels_in_store:
            self.write_output("HAMURABI: THINK AGAIN. YOU DON'T HAVE ENOUGH BUSHELS.")
            self.clear_entry()
            return

        self.bushels_to_feed = self.user_input
        self.bushels_in_store -= self.bushels_to_feed

        self.step = "plant"
        self.prompt_label.config(text="HOW MANY ACRES DO YOU WISH TO PLANT WITH SEED?")
        self.clear_entry()

    def handle_plant(self):
        self.acres_to_plant = self.user_input

        if self.acres_to_plant > self.acres_owned:
            self.write_output("HAMURABI: THINK AGAIN. YOU CAN'T PLANT MORE ACRES THAN YOU OWN.")
            self.clear_entry()
            return

        if self.acres_to_plant > 10 * self.population:
            self.write_output(f"BUT YOU HAVE ONLY {self.population} PEOPLE TO TEND THE FIELDS! NOW THEN,")
            self.clear_entry()
            return

        if self.acres_to_plant // 2 > self.bushels_in_store:
            self.write_output("HAMURABI: THINK AGAIN. YOU DON'T HAVE ENOUGH BUSHELS FOR SEED.")
            self.clear_entry()
            return

        self.bushels_in_store -= self.acres_to_plant // 2

        random_variable = random.randint(1, 6)
        self.harvest_per_acre = random_variable
        self.bushels_in_store += self.acres_to_plant * self.harvest_per_acre

        self.bushels_eaten_by_rats = 0
        random_variable = random.randint(5, 10)
        if random_variable % 2 == 0:
            self.bushels_eaten_by_rats = self.bushels_in_store // random_variable
            self.bushels_in_store -= self.bushels_eaten_by_rats

        people_fed = self.bushels_to_feed // 20
        self.number_starved = self.population - people_fed
        if self.number_starved < 0:
            self.number_starved = 0

        if self.number_starved > 0.45 * self.population:
            self.write_output(f"YOU STARVED {self.number_starved} PEOPLE IN ONE YEAR!!!")
            self.write_output("DUE TO THIS EXTREME MISMANAGEMENT YOU HAVE NOT ONLY")
            self.write_output("BEEN IMPEACHED AND THROWN OUT OF OFFICE BUT YOU HAVE")
            self.write_output("ALSO BEEN DECLARED NATIONAL FINK!!!!")
            messagebox.showinfo("Game Over", "You have been removed from office.")
            self.root.destroy()
            return

        self.total_number_starved += self.number_starved

        self.percent_of_population_that_starved = (
            ((self.year - 1) * self.percent_of_population_that_starved)
            + (self.number_starved * 100 / self.population)
        ) / self.year

        self.population -= self.number_starved

        if self.number_starved == 0 and self.population > 0:
            self.new_immigrants = int((20 * self.acres_owned + self.bushels_in_store) / self.population / 100 + 1)
        else:
            self.new_immigrants = 0

        self.year += 1
        self.start_year()

    def end_game(self):
        sustainability = self.acres_owned / self.population if self.population > 0 else 0

        self.write_output(
            f"\nIN YOUR 10-YEAR TERM OF OFFICE, {self.percent_of_population_that_starved:.2f} PERCENT OF THE POPULATION STARVED PER YEAR ON AVERAGE, A TOTAL OF {self.total_number_starved} PEOPLE DIED!!"
        )
        self.write_output(
            f"YOU STARTED WITH 10 ACRES PER PERSON AND ENDED WITH {sustainability:.2f} ACRES PER PERSON.\n"
        )

        if self.percent_of_population_that_starved > 33 or sustainability < 7:
            self.write_output("YOUR RULE WAS A DISASTER!")
        elif self.percent_of_population_that_starved > 10 or sustainability < 9:
            self.write_output("YOUR RULE WAS MEDIOCRE.")
        elif self.percent_of_population_that_starved > 3 or sustainability < 10:
            self.write_output("YOUR RULE WAS FAIRLY GOOD.")
        else:
            self.write_output("A FANTASTIC PERFORMANCE!!!")

        self.write_output("SO LONG FOR NOW.")
        self.prompt_label.config(text="GAME OVER")
        self.entry.config(state="disabled")
        self.submit_button.config(state="disabled")


root = tk.Tk()
game = HamurabiGame(root)
root.mainloop()
