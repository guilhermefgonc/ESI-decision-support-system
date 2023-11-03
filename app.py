import customtkinter as ctk
from data_reading import CROPS_LIST, CITIES_LIST, TIME_LIST

def on_crops_option_selected(*args):
    selected_crop = crops_var.get()
    selected_index = crops_var.trace_vinfo()[1]
    
    print(selected_crop, selected_index)

# formatting the lists
CROPS_LIST = '\n'.join(CROPS_LIST)
CITIES_LIST = '\n'.join(CITIES_LIST)
TIME_LIST = '\n'.join(TIME_LIST)    
        
# setting the main window
main_window = ctk.CTk()
main_window.title("Sistema de Apoio à Decisão")
main_window.geometry("1100x800")
main_window.minsize(width=1000, height=700)
main_label = ctk.CTkLabel(master=main_window, text="Sistema de Apoio à Decisão", font=("arial bold", 30))
main_label.pack(pady=20, padx=5)

# setting tab view
tabs = ctk.CTkTabview(master=main_window, width=400)
tabs.pack()
tabs.add("Menu")
tabs.add("Culturas")
tabs.add("Cidades")
tabs.tab("Menu").grid_columnconfigure(0, weight=1)
tabs.tab("Cidades").grid_columnconfigure(0, weight=1)
tabs.tab("Culturas").grid_columnconfigure(0, weight=1)

# adding elements in tabs
text_crops = ctk.CTkLabel(tabs.tab("Culturas"), text=CROPS_LIST, font=("Arial", 20))
text_crops.pack()

text_cities = ctk.CTkLabel(tabs.tab("Cidades"), text=CITIES_LIST, font=("Arial", 20))
text_cities.pack()

# option menu
crops_label = ctk.CTkLabel(master=tabs.tab("Menu"), text="Digite a cultura que deseja plantar:", font=("Arial", 20))
crops_label.pack()

crops_values = CROPS_LIST.split("\n")
crops_values.insert(0, "Selecione uma cultura...")

crops_var = ctk.StringVar(value="Selecione uma cultura...")

crops_option = ctk.CTkOptionMenu(master=tabs.tab("Menu"), variable=crops_var, values=crops_values)
crops_option.pack()

crops_var.trace_add("write", on_crops_option_selected)

main_window.mainloop()