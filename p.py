from customtkinter import *

app = CTk()
app.geometry("700x400")
set_appearance_mode("dark")
app.title("North west corner")


supply_values = []
demand_values = []
set_default_color_theme("green")

def tab1():
    num_lignes = []
    supply_var = StringVar()
    demand_var = StringVar()
    supply_entries = []
    supply_entries1 = []
    demand_entries = []
    demand_entries1 = []
    
    back_btn = None
    global a, b, go_to_tab2_button, go_to_tab3_button, save_button, save_button1, num_colonne , label1 , label2 , label3

    def go_tab2():
        num_ligne = supply_var.get()
        num_colonne = demand_var.get()
        if num_ligne.isdigit() and num_colonne.isdigit() and int(num_ligne) > 0 and int(num_colonne) > 0:
            label1.configure(text="")
            entry_supply.destroy()
            entry_demand.destroy()
            go_to_tab2_button.destroy()
            label2.destroy()
            label3.destroy()
            scan_supply()
            scan_demand()
            
    def scan_supply():
        num_ligne = supply_var.get()

        if num_ligne.isdigit() and int(num_ligne) > 0:
            for i in range(int(num_ligne)):
                entry_label = CTkLabel(app, text=f'Supply Element {i + 1}:', font=('Bold', 12))
                entry_label.place(relx=0.1, rely=0.2 + i * 0.1, anchor="center")

                entry_supply_element = CTkEntry(app, font=('Bold', 12))
                entry_supply_element.place(relx=0.3, rely=0.2 + i * 0.1, anchor="center")
                supply_entries1.append(entry_label)
                supply_entries.append(entry_supply_element)
            global save_button, save_button1
            save_button1 = CTkButton(app, text='Save Supply Values', font=('Bold', 12), width=15, command=save_supply_values)
            save_button1.place(relx=0.4, rely=0.3 + i * 0.1, anchor="ne")
            label1.configure(text="Supply Vector Scanned Successfully!")
        else:
            label1.configure(text="Invalid Supply value. Please enter a positive integer.")

    def scan_demand():
        global num_colonne
        num_colonne = demand_var.get()

        if num_colonne.isdigit() and int(num_colonne) > 0:
            for i in range(int(num_colonne)):
                entry_label = CTkLabel(app, text=f'Demand Element {i + 1}:', font=('Bold', 12))
                entry_label.place(relx=0.6, rely=0.2 + i * 0.1, anchor="center")

                entry_demand_element = CTkEntry(app, font=('Bold', 12))
                entry_demand_element.place(relx=0.8, rely=0.2 + i * 0.1, anchor="center")
                demand_entries1.append(entry_label)
                demand_entries.append(entry_demand_element)
            global save_button, save_button1,label1
            save_button = CTkButton(app, text='Save Demand Values', font=('Bold', 12), width=15, command=save_demand_values)
            save_button.place(relx=0.7, rely=0.3 + i * 0.1, anchor="nw")
            label1.configure(text="Demand Vector Scanned Successfully!")

            global go_to_tab3_button , back1_button
            go_to_tab3_button = CTkButton(app, text='Next', font=('Bold', 12), width=15, command=go_tab3)
            go_to_tab3_button.place(relx=0.5, rely=0.8, anchor="center")
            back1_button = CTkButton(app, text='BACK', font=('Bold', 12), width=15, command=back_btn1)
            back1_button.place(relx=0.1, rely=0.8, anchor="w")

    def save_supply_values():
        global b, supply_values
        supply_values = []
        supply_values.extend(int(entry.get()) for entry in supply_entries)
        label1.configure(text="supply values saved" , text_color='green')       
        print("Supply Values:", supply_values)
        b = 1

    def save_demand_values():
       global a, demand_values
       demand_values=[]
       demand_values.extend(int(entry.get()) for entry in demand_entries)
       label1.configure(text="demand values saved" , text_color='green')      
       print("Demand Values:", demand_values)
       a = 1

    def go_tab3():
        global a, b, go_to_tab3_button, save_button, save_button1, entry_label, num_colonne, supply_values , label1 ,back2_button
        if a == 1 and b == 1:
            label1.configure(text="")
            back1_button.destroy()
            entry_supply.destroy()
            entry_demand.destroy()
            go_to_tab2_button.destroy()
            go_to_tab3_button.destroy()
            label1.configure(text="Put Matrix.")
            label1.pack()
            for entry_label in supply_entries1:
                entry_label.destroy()

            for entry_label in demand_entries1:
                entry_label.destroy()
            for entry in supply_entries:
                entry.destroy()
            for entry in demand_entries:
                entry.destroy()

            save_button.destroy()
            save_button1.destroy()
            show_matrix(supply_entries, demand_entries, supply_values, demand_values)

        else:
            label1.configure(text="Please complete the scanning in Tab 2 first.")
    def back_btn1():
        supply_values = None
        demand_values = None
        label1.destroy()
        back1_button.destroy()
        entry_supply.destroy()
        entry_demand.destroy()
        go_to_tab2_button.destroy()
        go_to_tab3_button.destroy()
        for entry_label in supply_entries1:
            entry_label.destroy()

        for entry_label in demand_entries1:
            entry_label.destroy()
        for entry in supply_entries:
            entry.destroy()
        for entry in demand_entries:
            entry.destroy()

        save_button.destroy()
        save_button1.destroy()
        tab1()
        

      
    label1 = CTkLabel(app, text='Scan Supply and Demand', font=('Bold', 14))
    label1.pack()

    label2 = CTkLabel(app, text='Put number Supply ', font=('Bold', 14))
    label2.place(relx=0.25, rely=0.4, anchor="center")
    

    label3 = CTkLabel(app, text='Put number Demand', font=('Bold', 14))
    label3.place(relx=0.75, rely=0.4, anchor="center")
    
    entry_supply = CTkEntry(app, textvariable=supply_var, font=('Bold', 12))
    entry_supply.place(relx=0.25, rely=0.5, anchor="center")

    entry_demand = CTkEntry(app, textvariable=demand_var, font=('Bold', 12))
    entry_demand.place(relx=0.75, rely=0.5, anchor="center")

    go_to_tab2_button = CTkButton(app, text='Next', font=('Bold', 12), width=15, command=go_tab2)
    go_to_tab2_button.place(relx=0.5, rely=0.8, anchor="center")


def show_matrix(supply_entries, demand_entries, supply_values, demand_values):
    global matrix_frame, num_colonne , matrix_label
    matrix_label = CTkLabel(app, text='Matrix:', font=('Bold', 20))
    matrix_label.pack()

    matrix_frame = CTkFrame(app)
    matrix_frame.pack()
    matrix = []

    for i in range(len(supply_entries)):
        row_entries = []
        for j in range(int(num_colonne)):
            entry = CTkEntry(matrix_frame, font=('Bold', 40), width=5)
            entry.grid(row=i, column=j, padx=5, pady=5)
            row_entries.append(entry)
        matrix.append(row_entries)

    confert_button = CTkButton(app, text='Confert', font=('Bold', 12), width=15, command=lambda: confert(matrix, supply_values, demand_values , label1))
    confert_button.place(relx=0.5, rely=0.8, anchor="center")
    

matrix = []


def scan_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            value = matrix[i][j].get()
            print(f"Matrix Element [{i + 1}, {j + 1}]: {value}")


def confert(matrix, supply_values, demand_values ,label1):
    scan_matrix(matrix)
    newtable = []
    for i in range(len(supply_values)):
        temp = []
        for j in range(len(demand_values)):
            temp.append(0)
        newtable.append(temp)
    i = 0
    j = 0
    while i < len(supply_values) and j < len(demand_values):
        x = min(int(supply_values[i]), int(demand_values[j]))
        supply_values[i] -= x
        demand_values[j] -= x
        newtable[i][j] = x
        if supply_values[i] == 0:
            i += 1
        if demand_values[j] == 0:
            j += 1
    Result = sum(newtable[i][j] * int(matrix[i][j].get()) for i in range(len(supply_values)) for j in range(len(demand_values)))
    print("Result:", Result)
    label1.configure(text="Result="+ str(Result) , fg_color='white', text_color='red')

tab1()
app.mainloop()
