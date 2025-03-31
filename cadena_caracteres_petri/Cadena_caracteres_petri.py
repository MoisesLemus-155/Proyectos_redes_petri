from graphviz import Digraph
import time
import re

# -------------------------------------------- CODIGO EN ESTATICO -------------------------------------------

def create_petri_red(state):
    dot = Digraph(format='png')
    dot.attr(size='8,8')
    
    # Plazas
    plazas = ["Inicio", "Letra", "Error", "A", "P", "R", "O", "B", "D", "Fin"]
    for plaza in plazas:
        color = 'red' if state.get(plaza, 0) else 'lightgray'
        dot.node(plaza, shape='circle', style='filled', fillcolor=color)
    
    # Transiciones
    transitions = ["T_1", "T_2", "T_3", "T_4", "T_5", "T_6", "T_7", "T_8", "T_9", "T_10"]
    for trans in transitions:
        dot.node(trans, shape='box', style='filled', fillcolor='black', fontcolor='white')
    
    # Arcos entre plazas y transiciones
    edges = [
        ("Inicio", "T_1"), ("T_1", "Letra"),
        ("Letra", "T_2"), ("T_2", "A"),
        ("A", "T_3"), ("T_3", "P"),
        ("P", "T_4"), ("T_4", "R"),
        ("R", "T_5"), ("T_5", "O"),
        ("O", "T_6"), ("T_6", "B"),
        ("B", "T_7"), ("T_7", "Fin"),
        ("A", "T_8"), ("T_8", "D"),
        ("D", "T_9"), ("T_9", "O"),
        ("O", "T_10"), ("T_10", "Fin"),
        ("Letra", "Error")
    ]
    for edge in edges:
        dot.edge(edge[0], edge[1])
    
    return dot

def simular_petri_red(input_string):
    string_filtrado = re.sub(r'[^A-Za-z]', '', input_string).upper()
    output_esperado = "APROBADO"
    estados = []
    
    current_state = {"Inicio": 1}
    estados.append(current_state.copy())
    
    for letra in input_string:
        if letra in output_esperado:
            current_state = {letra: 1}
        else:
            current_state = {"Error": 1}
        estados.append(current_state.copy())
    
    if string_filtrado == output_esperado:
        current_state = {"Fin": 1}
    estados.append(current_state.copy())
    
    for i, state in enumerate(estados):
        dot = create_petri_red(state)
        filename = f'step_{i}'
        dot.render(filename)
        print(f'Generado: {filename}.png')
        time.sleep(1)

if __name__ == "__main__":
    input_string = "A1P2R3O4B5A6D7O8"
    simular_petri_red(input_string)

# ------------------------------------------- CODIGO EN DINAMICO -------------------------------------------

# def create_petri_red(active_places=[]):
#     dot = Digraph(format='png')
#     dot.attr(size='8,8')
    
#     # Plazas
#     plazas = ["P_Inicio", "P_Filtrado", "P_Aceptado", "P_Final"]
#     for plaza in plazas:
#         color = 'red' if plaza in active_places else 'lightgray'
#         dot.node(plaza, shape='circle', style='filled', fillcolor=color)
    
#     # Transiciones
#     transitions = ["T_Filtrar", "T_Validar", "T_Completar"]
#     for trans in transitions:
#         dot.node(trans, shape='box', style='filled', fillcolor='black', fontcolor='white')
    
#     # Arcos entre plazas y transiciones
#     edges = [
#         ("P_Inicio", "T_Filtrar"), ("T_Filtrar", "P_Filtrado"),
#         ("P_Filtrado", "T_Validar"), ("T_Validar", "P_Aceptado"),
#         ("P_Aceptado", "T_Completar"), ("T_Completar", "P_Final")
#     ]
#     for edge in edges:
#         dot.edge(edge[0], edge[1])
    
#     return dot

# def simular_petri_red(input_string):
#     string_filtrado = re.sub(r'[^A-Za-z]', '', input_string).lower()
    
#     print(f"Entrada: {input_string}")
#     print(f"Cadena filtrada: {string_filtrado}")
#     print("Salida: La cadena ha sido procesada correctamente")
    
#     states = [
#         ["P_Inicio"],
#         ["P_Filtrado"],
#         ["P_Aceptado"],
#         ["P_Final"]
#     ]
    
#     for i, active_plazas in enumerate(states):
#         dot = create_petri_red(active_plazas)
#         filename = f'step_{i}'
#         dot.render(filename)
#         print(f'Generado: {filename}.png')
#         time.sleep(1)
    
# if __name__ == "__main__":
#     input_string = input("Ingrese una cadena de caracteres: ")
#     simular_petri_red(input_string)