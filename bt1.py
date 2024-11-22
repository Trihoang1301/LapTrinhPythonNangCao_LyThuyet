import tkinter as tk
from tkinter import ttk, messagebox
import math

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Tính toán")
        master.geometry("230x180")
        master.resizable(False, False)

        # Tạo menu
        self.menu = tk.Menu(master)
        master.config(menu=self.menu)

        # Tạo file menu
        self.file_menu = tk.Menu(self.menu, tearoff=0)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Exit", command=self.exit)
        self.menu.add_cascade(label="File", menu=self.file_menu)

        # Tạo help menu
        self.help_menu = tk.Menu(self.menu, tearoff=0)
        self.help_menu.add_command(label="About", command=self.show_about)
        self.menu.add_cascade(label="Help", menu=self.help_menu)

        # Tạo tab
        self.notebook = ttk.Notebook(master)
        self.notebook.pack(fill="both", expand=True)

        #Tạo tab Standard
        self.standard_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.standard_tab, text="Standard")

        # Tạo tab Scientific
        self.scientific_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.scientific_tab, text="Scientific")

        # tạo ô nhập
        self.entry_field = tk.Entry(self.standard_tab, width=30)
        self.entry_field.grid(row=0, column=0, columnspan=4)
        self.entry_field.focus()

        # Tạo phím số 
        buttons = [
            '7', '8', '9', '÷',
            '4', '5', '6', 'x',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        row_val = 1
        col_val = 0
        for button in buttons:
            tk.Button(self.standard_tab, text=button, width=5, command=lambda button=button: self.click_button(button)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Tạo phím Clear
        tk.Button(self.standard_tab, text="Clear", width=30, command=self.clear_entry).grid(row=row_val, column=0, columnspan=4)

        # Tạo các phím  cho tab Scientific
        scientific_buttons = [
            'sin', 'cos', 'tan', 'log',
            'exp', 'sqrt', 'pow', 'abs',
            'pi', 'e', 'deg', 'rad'
        ]

        row_val = 1
        col_val = 0
        for button in scientific_buttons:
            tk.Button(self.scientific_tab, text=button, width=5, command=lambda button=button: self.click_scientific_button(button)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def click_button(self, button):
        if button == '=':
            try:
                result = eval(self.entry_field.get())
                self.entry_field.delete(0, tk.END)
                self.entry_field.insert(tk.END, result)
            except Exception as e:
                self.entry_field.delete(0, tk.END)
                self.entry_field.insert(tk.END, "Error")
        else:
            self.entry_field.insert(tk.END, button)

    def clear_entry(self):
        self.entry_field.delete(0, tk.END)

    def save_file(self):
        messagebox.showinfo("Save", "File đã lưu thành công!")

    def new_file(self):
        messagebox.showinfo("New", "File đã tạo mới thành công!")  
    def show_about(self):
        about_window = tk.Toplevel(self.master)
        about_window.title("About")
        tk.Label(about_window, text="Calculator v1.0").pack()
        tk.Button(about_window, text="OK", command=about_window.destroy).pack()

    def exit(self):
        if messagebox.askyesno("Exit", "Bạn có muốn thoát ứng dụng không?"):
            self.master.destroy()
    def click_scientific_button(self, button):
        if button == 'sin':
            try:
                result = math.sin(math.radians(float(self.entry_field.get())))
                self.entry_field.delete(0, tk.END)
                self.entry_field.insert(tk.END, result)
            except Exception as e:
                self.entry_field.delete(0, tk.END)
                self.entry_field.insert(tk.END, "Error")
        elif button == 'cos':
            try:
                result = math.cos(math.radians(float(self.entry_field.get())))
                self.entry_field.delete(0, tk.END)
                self.entry_field.insert(tk.END, result)
            except Exception as e:
                self.entry_field.delete(0, tk.END)
                self.entry_field.insert(tk.END, "Error")
        elif button == 'tan':
            try:
                result = math.tan(math.radians(float(self.entry_field.get())))
                self.entry_field.delete(0, tk.END)
                self.entry_field.insert(tk.END, result)
            except Exception as e:
                self.entry_field.delete(0, tk.END)
                self.entry_field.insert(tk.END, "Error")
        elif button == 'log':
            try:
                result = math.log10(float(self.entry_field.get()))
                self.entry_field.delete(0, tk.END)
                self.entry_field.insert(tk.END, result)
            except Exception as e:
                self.entry_field.delete(0, tk.END)
                self.entry_field.insert(tk.END, "Error")
        elif button == 'exp':
            try:
                result = math.exp(float(self.entry_field.get()))
                self.entry_field.delete(0, tk.END)
                self.entry_field.insert(tk.END, result)
            except Exception as e:
                self.entry_field.delete(0, tk.END)
                self.entry_field.insert(tk.END, "Error")
        elif button == 'sqrt':
            try:
                result = math.sqrt(float(self.entry_field.get()))
                self.entry_field.delete(0, tk.END)
                self.entry_field.insert(tk.END, result)
            except Exception as e:
                self.entry_field.delete(0, tk.END)
                self.entry_field.insert(tk.END, "Error")
        elif button == 'pow':
            try:
                result = float(self.entry_field.get()) ** 2
                self.entry_field.delete(0, tk.END)
                self.entry_field.insert(tk.END, result)
            except Exception as e:
                self.entry_field.delete(0, tk.END)
                self.entry_field.insert(tk.END, "Error")
        elif button == 'abs':
            try:
                result = abs(float(self.entry_field.get()))
                self.entry_field.delete(0, tk.END)
                self.entry_field.insert(tk.END, result)
            except Exception as e:
                self.entry_field.delete(0, tk.END)
                self.entry_field.insert(tk.END, "Error")
        elif button == 'pi':
            self.entry_field.delete(0, tk.END)
            self.entry_field.insert(tk.END, math.pi)
        elif button == 'e':
            self.entry_field.delete(0, tk.END)
            self.entry_field.insert(tk.END, math.e)
        elif button == 'deg':
            try:
                result = math.degrees(float(self.entry_field.get()))
                self.entry_field.delete(0, tk.END)
                self.entry_field.insert(tk.END, result)
            except Exception as e:
                self.entry_field.delete(0, tk.END)
                self.entry_field.insert(tk.END, "Error")
        elif button == 'rad':
            try:
                result = math.radians(float(self.entry_field.get()))
                self.entry_field.delete(0, tk.END)
                self.entry_field.insert(tk.END, result)
            except Exception as e:
                self.entry_field.delete(0, tk.END)
                self.entry_field.insert(tk.END, "Error")

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
