import tkinter as tk
from tkinter import messagebox, ttk

import requests
from requests.exceptions import ConnectionError, HTTPError, Timeout

currency_list = {}
currency_list_for_cmb = []


root = tk.Tk()
root.title("Курсы обмена криптовалют")

# Place a main windows in the center of the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width / 2 - 400 / 2)
center_y = int(screen_height / 2 - 400 / 2)
root.geometry(f"400x300+{center_x}+{center_y}")

# create frame for the 1st currency
frm_base_currency = ttk.Frame(root, padding="10 10 10 10", borderwidth=2, relief="flat")
frm_base_currency.pack(side=tk.TOP)
frm_base_currency_1 = ttk.Frame(frm_base_currency, padding="10 10 10 10", borderwidth=2, relief="flat")
frm_base_currency_1.pack(side=tk.LEFT)
lbl_base_currency_1 = ttk.Label(frm_base_currency_1, text="Первая криптовалюта")
lbl_base_currency_1.pack()
cmb_base_currency_1 = ttk.Combobox(frm_base_currency_1, name="cmb_base_currency_1", values=[], state="readonly")
cmb_base_currency_1.pack()
lbl_base_currency_1 = ttk.Label(frm_base_currency_1, text="")
lbl_base_currency_1.pack()

# create frame for the 2nd currency
frm_base_currency_2 = ttk.Frame(frm_base_currency, padding="10 10 10 10", borderwidth=2, relief="flat")
frm_base_currency_2.pack(side=tk.LEFT)
lbl_base_currency_2 = ttk.Label(frm_base_currency_2, text="Вторая криптовалюта")
lbl_base_currency_2.pack()
cmb_base_currency_2 = ttk.Combobox(frm_base_currency_2, name="cmb_base_currency_2", values=[], state="readonly")
cmb_base_currency_2.pack()
lbl_base_currency_2 = ttk.Label(frm_base_currency_2, text="")
lbl_base_currency_2.pack()

# create frame for the 3d currency
frm_target_currency = ttk.Frame(root, padding="10 10 10 10", borderwidth=2, relief="flat")
frm_target_currency.pack(side=tk.TOP)
frm_target_currency = ttk.Frame(frm_target_currency, padding="10 10 10 10", borderwidth=2, relief="flat")
frm_target_currency.pack(side=tk.LEFT)
lbl_target_currency = ttk.Label(frm_target_currency, text="Третья криптовалюта")
lbl_target_currency.pack()
cmb_target_currency = ttk.Combobox(frm_target_currency, name="cmb_target_currency", values=[], state="readonly")
cmb_target_currency.pack()
lbl_target_currency = ttk.Label(frm_target_currency, text="")
lbl_target_currency.pack()

# Button to calculate exchange rate and show popup window
frm_calc = ttk.Frame(root, padding="10 10 10 10", borderwidth=2, relief="flat")
frm_calc.pack(side=tk.TOP)
# The button will be active when three currecies are selected
btt_calc = ttk.Button(frm_calc, text="Получить курс обмена", state=tk.DISABLED)
btt_calc.pack()

root.mainloop()
