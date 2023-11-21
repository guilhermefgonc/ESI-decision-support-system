import customtkinter as ctk
import tkinter
import tkintermapview
from data_reading import CROPS_LIST, CITIES_LIST, TIME_LIST
from data.dictionary import DATA

# function to search city in map
def search():
    map_widget.set_address(entry_widget.get())

# function to get details of the selectedc crop
def on_crops_option_selected(*args):
    selected_crop = crops_var.get()
    if selected_crop in DATA["Crops"]:
        time = DATA["Crops"][selected_crop]["Time"]
        cities = ", ".join(DATA["Crops"][selected_crop]["Cities"])
        result_label.configure(text=f"Cultura: {selected_crop}\nTempo de Plantio: {time}\nCidades: {cities}")
    else:
        result_label.configure(text="Cultura não encontrada.")

# formatting lists
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
tabs.add("Mapa")
tabs.add("Culturas")
tabs.add("Cidades")
tabs.tab("Menu").grid_columnconfigure(0, weight=1)
tabs.tab("Mapa").grid_columnconfigure(0, weight=1)
tabs.tab("Cidades").grid_columnconfigure(0, weight=1)
tabs.tab("Culturas").grid_columnconfigure(0, weight=1)

# adding elements in tab view
text_crops = ctk.CTkLabel(tabs.tab("Culturas"), text=CROPS_LIST, font=("Arial", 20))
text_crops.pack()

text_cities = ctk.CTkLabel(tabs.tab("Cidades"), text=CITIES_LIST, font=("Arial", 20))
text_cities.pack()

# menu option to select crops
crops_label = ctk.CTkLabel(master=tabs.tab("Menu"), text="Digite a cultura que deseja plantar:", font=("Arial", 20))
crops_label.pack()

crops_values = CROPS_LIST.split("\n")
crops_values.insert(0, "Selecione uma cultura...")

crops_var = ctk.StringVar(value="Selecione uma cultura...")

crops_option = ctk.CTkOptionMenu(master=tabs.tab("Menu"), variable=crops_var, values=crops_values)
crops_option.pack()

# label to show selected crop info
result_label = ctk.CTkLabel(master=tabs.tab("Menu"), text="", font=("Arial", 16))
result_label.pack()

crops_var.trace_add("write", on_crops_option_selected)

# user input and search button
entry_widget = ctk.CTkEntry(master=tabs.tab("Mapa"), placeholder_text="Digite uma cidade...")
entry_widget.grid(row=0, column=0, padx=(10, 0), sticky="ew")

button_search = ctk.CTkButton(master=tabs.tab("Mapa"), text="Pesquisar", width=100, height=26, command=search)
button_search.grid(row=0, column=1, padx=(10, 0))

# setting map view
map_widget = tkintermapview.TkinterMapView(master=tabs.tab("Mapa"), width=1000, height=800, corner_radius=0)
map_widget.grid(row=1, column=0, columnspan=2, pady=30) 
map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=20)
map_widget.set_position(-22.320545, -49.071004) # bauru
map_widget.set_zoom(15)

main_window.mainloop()