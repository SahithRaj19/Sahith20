import tkinter as tk
from tkinter import messagebox

class HotelManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management and Billing System")
        
        self.room_prices = {
            "Single": 100,
            "Double": 150,
            "Suite": 250
        }
        
        self.guests = []
        
        self.create_widgets()
        
    def create_widgets(self):
        # Room Type
        self.room_label = tk.Label(self.root, text="Select Room Type:")
        self.room_label.pack()
        
        self.room_var = tk.StringVar()
        self.room_var.set("Single")
        
        self.room_menu = tk.OptionMenu(self.root, self.room_var, *self.room_prices.keys())
        self.room_menu.pack()
        
        # Guest Name
        self.name_label = tk.Label(self.root, text="Guest Name:")
        self.name_label.pack()
        
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack()
        
        # Number of Nights
        self.nights_label = tk.Label(self.root, text="Number of Nights:")
        self.nights_label.pack()
        
        self.nights_entry = tk.Entry(self.root)
        self.nights_entry.pack()
        
        # Calculate Button
        self.calculate_button = tk.Button(self.root, text="Calculate Total", command=self.calculate_total)
        self.calculate_button.pack()
        
        # Total Amount
        self.total_label = tk.Label(self.root, text="Total Amount:")
        self.total_label.pack()
        
        self.total_var = tk.StringVar()
        self.total_label_value = tk.Label(self.root, textvariable=self.total_var)
        self.total_label_value.pack()
        
    def calculate_total(self):
        room_type = self.room_var.get()
        nights = int(self.nights_entry.get())
        
        if room_type in self.room_prices:
            room_price = self.room_prices[room_type]
            total_amount = room_price * nights
            self.total_var.set(f"${total_amount}")
            
            guest_name = self.name_entry.get()
            self.guests.append({"name": guest_name, "room_type": room_type, "nights": nights, "total_amount": total_amount})
        else:
            messagebox.showerror("Error", "Invalid room type.")
        
        self.clear_entries()
        
    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.nights_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = HotelManagementApp(root)
    root.mainloop()
