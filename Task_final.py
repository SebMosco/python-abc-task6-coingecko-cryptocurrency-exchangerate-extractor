# ***************************************************************************
# *   copyright       : (C) 2026 by SebMosco                                *
# *                                                                         *
# *   It is a final homework for a Python course                            *
# *                                                                         *
# *   This program is free software; you can redistribute it and/or modify  *
# *   it under the terms of the GNU General Public License as published by  *
# *   the Free Software Foundation; either version 3 of the License, or     *
# *   (at your option) any later version.                                   *
# *                                                                         *
# ***************************************************************************

import tkinter as tk
from tkinter import messagebox, ttk

import requests
from requests.exceptions import ConnectionError, HTTPError, Timeout

currency_list = {}
currency_list_for_cmb = []


# Получаем все доступные валюты с сайта
def get_currency_list():
    global currency_list
    global currency_list_for_cmb
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd"

    # Try to get cryptocurrency rates
    try:
        response = requests.get(url)

        response.raise_for_status()
    
    except HTTPError as e:
        messagebox.showerror('Ошибка', f'Ошибка запроса по HTTP: {e}')
    except ConnectionError as e:
        messagebox.showerror('Ошибка', f"Нет подключения к Интернет: {e}")
    except Timeout as e:
        messagebox.showerror('Ошибка', f"Сайт coingecko.com не доступен: {e}")
    except Exception as e:
        messagebox.showerror('Ошибка', f'{e}')
        
    coins = response.json()
    
    # Save only "symbol" and "name"

    keys_to_keep = {"id", "symbol", "name", "current_price"}

    # Фильтрация ключей в словаре и удаление данных которые не требуются
    currency_list = [{key: d[key] for key in keys_to_keep if key in d} for d in coins]

    # currency_list = {i['symbol']: i['name'] for i in coins}
    currency_list_for_cmb = [i['symbol'] for i in coins]
    currency_list_for_cmb.sort()
  
    # Update combobox dropdown lists
    cmb_base_currency_1['values'] = currency_list_for_cmb
    cmb_base_currency_2['values'] = currency_list_for_cmb
    cmb_target_currency['values'] = currency_list_for_cmb


# Update a corresponding lable on_select in combobox
def on_select_cmb(event):
    dd= [d['name'] for d in currency_list if d['symbol'] == event.widget.get()][0]


    match event.widget.winfo_name():
        case "cmb_base_currency_1":
            lbl_base_currency_1.config(text=dd)
        case "cmb_base_currency_2":
            lbl_base_currency_2.config(text=dd)
        case "cmb_target_currency":
            lbl_target_currency.config(text=dd)

    if cmb_base_currency_1.get() and cmb_base_currency_2.get() and cmb_target_currency.get():
        btt_calc.state(['!disabled'])

def show_exchange_rate():
    popup_win = tk.Toplevel(root)
    popup_win.title("Курсы выбранных криптовалют")
    
    # Place popup window at the center of the screen
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    center_x = int(screen_width / 2 - 500 / 2)
    center_y = int(screen_height / 2 - 250 / 2)
    popup_win.geometry(f"500x250+{center_x}+{center_y}")

    # Made popup window modal
    popup_win.transient(root)
    popup_win.grab_set()

    # Create pop up windows header
    frm_top = ttk.Frame(popup_win, padding="10 10 10 10", borderwidth=2, relief="flat")
    frm_top.pack(side=tk.TOP)   
    label = ttk.Label(frm_top, text="Курсы выбранных криптовалют по отношению к \nUSD\n(доллару США)", justify="center")
    label.pack()

    frm_center = ttk.Frame(popup_win, padding="10 10 10 10", borderwidth=2, relief="flat")
    frm_center.pack(side=tk.TOP)
    frm_center.columnconfigure(0, minsize=150)
    frm_center.columnconfigure(1, minsize=150)
    frm_center.columnconfigure(2, minsize=150)

    # Create a currency exchange table header
    label = ttk.Label(frm_center, text="Символ", font=("Arial", 12, "bold"))
    label.grid(column=0, row=0)
    label = ttk.Label(frm_center, text="Название", font=("Arial", 12, "bold"))
    label.grid(column=1, row=0)
    label = ttk.Label(frm_center, text="Курс", font=("Arial", 12, "bold"))
    label.grid(column=2, row=0)

    # Create table for currencies
    lbl_curr1_exch_rate = ttk.Label(frm_center, text=get_line_cur_exch_rate(cmb_base_currency_1)[0], anchor="w", justify="left")
    lbl_curr1_exch_rate.grid(column=0, row=1)
    lbl_curr1_exch_rate = ttk.Label(frm_center, text=get_line_cur_exch_rate(cmb_base_currency_1)[1], anchor="w", justify="left")
    lbl_curr1_exch_rate.grid(column=1, row=1)
    lbl_curr1_exch_rate = ttk.Label(frm_center, text=get_line_cur_exch_rate(cmb_base_currency_1)[2], anchor="w", justify="left")
    lbl_curr1_exch_rate.grid(column=2, row=1)
 
    lbl_curr2_exch_rate = ttk.Label(frm_center, text=get_line_cur_exch_rate(cmb_base_currency_2)[0], anchor="w", justify="left")
    lbl_curr2_exch_rate.grid(column=0, row=2)
    lbl_curr2_exch_rate = ttk.Label(frm_center, text=get_line_cur_exch_rate(cmb_base_currency_2)[1], anchor="w", justify="left")
    lbl_curr2_exch_rate.grid(column=1, row=2)
    lbl_curr2_exch_rate = ttk.Label(frm_center, text=get_line_cur_exch_rate(cmb_base_currency_2)[2], anchor="w", justify="left")
    lbl_curr2_exch_rate.grid(column=2, row=2)
      
    lbl_curr3_exch_rate = ttk.Label(frm_center, text=get_line_cur_exch_rate(cmb_target_currency)[0], anchor="w", justify="left")
    lbl_curr3_exch_rate.grid(column=0, row=3)
    lbl_curr3_exch_rate = ttk.Label(frm_center, text=get_line_cur_exch_rate(cmb_target_currency)[1], anchor="w", justify="left")
    lbl_curr3_exch_rate.grid(column=1, row=3)
    lbl_curr3_exch_rate = ttk.Label(frm_center, text=get_line_cur_exch_rate(cmb_target_currency)[2], anchor="w", justify="left")
    lbl_curr3_exch_rate.grid(column=2, row=3)

    # Place a close button at a pop up window footer
    frm_bottom = ttk.Frame(popup_win, padding="10 10 10 10", borderwidth=2, relief="flat")
    frm_bottom.pack(side=tk.TOP)
    close_btn = ttk.Button(frm_bottom, text="Закрыть", command=popup_win.destroy)
    close_btn.pack()

    # Start a pop up window loop
    root.wait_window(popup_win)

# Take a link to combobox and return data for a table
def get_line_cur_exch_rate(name: ttk.Combobox) -> str:
    i=0
    # Get ID for the selected currency in combobox
    for item in currency_list:
        if item.get('symbol') == name.get():
            break
        i += 1   

    s = currency_list[i]['symbol']
    n1 = currency_list[i]['name']
    cp = currency_list[i]['current_price']
    
    return s, n1, cp
 

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
cmb_base_currency_1.bind("<<ComboboxSelected>>", on_select_cmb)
cmb_base_currency_1.pack()
lbl_base_currency_1 = ttk.Label(frm_base_currency_1, text="")
lbl_base_currency_1.pack()

# create frame for the 2nd currency
frm_base_currency_2 = ttk.Frame(frm_base_currency, padding="10 10 10 10", borderwidth=2, relief="flat")
frm_base_currency_2.pack(side=tk.LEFT)
lbl_base_currency_2 = ttk.Label(frm_base_currency_2, text="Вторая криптовалюта")
lbl_base_currency_2.pack()
cmb_base_currency_2 = ttk.Combobox(frm_base_currency_2, name="cmb_base_currency_2", values=[], state="readonly")
cmb_base_currency_2.bind("<<ComboboxSelected>>", on_select_cmb)
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
cmb_target_currency.bind("<<ComboboxSelected>>", on_select_cmb)
cmb_target_currency.pack()
lbl_target_currency = ttk.Label(frm_target_currency, text="")
lbl_target_currency.pack()

# Button to calculate exchange rate and show popup window
frm_calc = ttk.Frame(root, padding="10 10 10 10", borderwidth=2, relief="flat")
frm_calc.pack(side=tk.TOP)
# The button will be active when three currecies are selected
btt_calc = ttk.Button(frm_calc, text="Получить курс обмена", command=show_exchange_rate, state=tk.DISABLED)
btt_calc.pack()

get_currency_list()
root.mainloop()