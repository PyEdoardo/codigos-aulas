import customtkinter as ctk
import requests
from PIL import Image, ImageTk
from io import BytesIO

# Função para buscar informações do Pokémon
def get_pokemon_info(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        pokemon_info = {
            "name": data['name'].capitalize(),
            "image_url": data['sprites']['front_default'],
            "types": [type_info['type']['name'].capitalize() for type_info in data['types']],
            "moves": [move['move']['name'].capitalize() for move in data['moves']]
        }
        return pokemon_info
    else:
        return None

# Função para mostrar informações do Pokémon na interface gráfica
def show_pokemon_info():
    pokemon_name = entry.get()
    pokemon_info = get_pokemon_info(pokemon_name)
    
    if pokemon_info:
        name_label.configure(text=f"Name: {pokemon_info['name']}")
        types_label.configure(text=f"Type: {', '.join(pokemon_info['types'])}")
        moves_label.configure(text=f"Moves: {', '.join(pokemon_info['moves'][:5])}...")  # Mostra os primeiros 5 movimentos
        
        response = requests.get(pokemon_info['image_url'])
        image_data = response.content
        image = Image.open(BytesIO(image_data))
        image = ImageTk.PhotoImage(image)
        image_label.configure(image=image)
        image_label.image = image
    else:
        name_label.configure(text="Pokémon não encontrado!")
        types_label.configure(text="")
        moves_label.configure(text="")
        image_label.configure(image="")
        image_label.image = None

# Configurações da interface gráfica
app = ctk.CTk()
app.geometry("400x600")
app.title("Pokémon Info")

frame = ctk.CTkFrame(master=app)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = ctk.CTkLabel(master=frame, text="Digite o nome do Pokémon")
label.pack(pady=12, padx=10)

entry = ctk.CTkEntry(master=frame, placeholder_text="Nome do Pokémon")
entry.pack(pady=12, padx=10)

button = ctk.CTkButton(master=frame, text="Buscar", command=show_pokemon_info)
button.pack(pady=12, padx=10)

name_label = ctk.CTkLabel(master=frame, text="")
name_label.pack(pady=12, padx=10)

types_label = ctk.CTkLabel(master=frame, text="")
types_label.pack(pady=12, padx=10)

moves_label = ctk.CTkLabel(master=frame, text="")
moves_label.pack(pady=12, padx=10)

image_label = ctk.CTkLabel(master=frame, text="")
image_label.pack(pady=12, padx=10)

app.mainloop()