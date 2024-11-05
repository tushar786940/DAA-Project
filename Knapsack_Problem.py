import tkinter as tk
from tkinter import messagebox

def knapsack_dynamic_programming(weights, values, capacity):
    n = len(values)   # i.e. number of items
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]  # 2D list with {(capacity+1) columns} and {(n+1) rows}

    for i in range(1, n + 1):    # Iterate over items
        for w in range(1, capacity + 1):    # Iterate over capacities from 1 to capacity to calculate the best achievable value for each weight limit.
            if weights[i - 1] <= w: # Check if the current item weight (weights[i - 1]) can fit in the knapsack (weights[i - 1] <= w)
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])  # Options (not include, include)
            else:
                dp[i][w] = dp[i - 1][w] #  If the item’s weight is more than the current capacity

    return dp[n][capacity] # Holds the maximum value achievable with n items and the given capacity


class KnapsackSolver:
    def __init__(self, master):
        self.master = master
        self.master.title("Knapsack Problem Solver")

        self.create_widgets() # Initializes all widgets (input fields, buttons, etc.) in a separate method

    def create_widgets(self):
        frame = tk.Frame(self.master)
        frame.pack()

        tk.Label(frame, text="Weights (comma-separated):").grid(row=0, column=0)
        self.weights_entry = tk.Entry(frame)
        self.weights_entry.grid(row=0, column=1)

        tk.Label(frame, text="Values (comma-separated):").grid(row=1, column=0)
        self.values_entry = tk.Entry(frame)
        self.values_entry.grid(row=1, column=1)

        tk.Label(frame, text="Capacity:").grid(row=2, column=0)
        self.capacity_entry = tk.Entry(frame)
        self.capacity_entry.grid(row=2, column=1)

        self.solve_button = tk.Button(frame, text="Solve Knapsack Problem", command=self.solve_knapsack)
        self.solve_button.grid(row=3, columnspan=2)

    def solve_knapsack(self):
        try:
            weights = list(map(int, self.weights_entry.get().split(',')))
            values = list(map(int, self.values_entry.get().split(',')))
            capacity = int(self.capacity_entry.get())

            if len(weights) != len(values):
                raise ValueError("Weights and values must have the same length.")

            max_value = knapsack_dynamic_programming(weights, values, capacity)

            messagebox.showinfo("Knapsack Result", f"Maximum Value: {max_value}")

        except Exception as e:
            messagebox.showerror("Input Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    solver = KnapsackSolver(root)
    root.mainloop()
