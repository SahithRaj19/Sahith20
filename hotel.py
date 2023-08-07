import tkinter as tk

class HotelApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hotel Menu")
        self.geometry("450x550")

        self.item_names = ["IDLI", "PUNDI", "BAJIL", "PATHRODE", "SAJJIGE", "CHAI", "KALI"]
        self.item_rates = [100, 70, 60, 150, 50, 70, 250]
        self.item_quantities = [tk.IntVar() for _ in range(7)]

        self.create_widgets()

    def calculate_total(self):
        total_amount = 0
        for i, quantity in enumerate(self.item_quantities):
            total_amount += self.item_rates[i] * quantity.get()

        self.total_label.config(text=f"Total Amount: {total_amount}")

    def create_widgets(self):
        self.menu_label = tk.Label(self, text="MENU:")
        self.menu_label.pack()

        for i, item in enumerate(self.item_names, 1):
            item_label = tk.Label(self, text=f"{i}. {item} - Rs. {self.item_rates[i-1]}")
            item_label.pack()

            quantity_label = tk.Label(self, text="Quantity:")
            quantity_label.pack()

            quantity_entry = tk.Entry(self, textvariable=self.item_quantities[i-1])
            quantity_entry.pack()

        self.calculate_button = tk.Button(self, text="Calculate Total", command=self.calculate_total)
        self.calculate_button.pack()

        self.total_label = tk.Label(self, text="Total Amount: 0")
        self.total_label.pack()

if __name__ == "__main__":
    app = HotelApp()
    app.mainloop()
