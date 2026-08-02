import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import os

def browse_csv():
    file = filedialog.askopenfilename(title = "Select CSV file", filetypes = [("CSV files", "*.csv")])

    if file:
        csv_path.set(file)

def browse_folder():
    folder = filedialog.askdirectory(title = "select output folder")

    if folder:
        output_path.set(folder)

def convert_files():
    csv_file = csv_path.get()
    output_folder = output_path.get()

    if not csv_file:
        messagebox.showerror("Error", "Please selec a csv file.")
        return

    if not output_folder:
        messagebox.showerror("Error", "Please select a output folder")
        return

    
    try:
        df = pd.read_csv(csv_file)

        file_name = os.path.splitext(os.path.basename(csv_file))[0]
        excel_file = os.path.join(output_folder, file_name + ".xlsx")

        df.to_excel(excel_file, index = False)

        messagebox.showinfo("Success", f"Excel file saved successfully!\n\n{excel_file}")

    except Exception as e:
        messagebox.showerror("Error", str(e))


##Gui

root = tk.Tk()
root.title("CSV to Excel Converter")
root.geometry("600x250")
root.resizable(False, False)

csv_path = tk.StringVar()
output_path = tk.StringVar()

##csv
tk.Label(root, text = "CSV file").pack(pady = (15,5))
tk.Entry(root, textvariable = csv_path, width = 60).pack()
tk.Button(root, text = "Browse CSV", command = browse_csv).pack(pady =5)
##output

tk.Label(root, text = "Output Folder").pack(pady = (10,5))
tk.Entry(root, textvariable=output_path, width=60).pack()
tk.Button(root, text = "Browse Folder", command = browse_folder).pack(pady = 5)

tk.Button(root, text="Convert", width = 20, height =2, command = convert_files).pack(pady =20)

root.mainloop()

