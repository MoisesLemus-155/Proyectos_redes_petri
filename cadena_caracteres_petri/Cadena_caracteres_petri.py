from graphviz import Digraph
import time
import re

# -------------------------------------------- CODIGO EN ESTATICO -------------------------------------------
# def create_petri_red():
#     dot = Digraph(format='png')
#     dot.attr(size='8,8')
    
#     # Plazas
#     plazas = ["P_Inicio", "P_Filtrado", "P_Aceptado", "P_Error", "P_Final"]
#     for plaza in plazas:
#         dot.node(plaza, shape='circle', style='filled', fillcolor='lightgray')
    
#     # Transiciones
#     transitions = ["T_Filtrar", "T_Validar", "T_Error", "T_Completar"]
#     for trans in transitions:
#         dot.node(trans, shape='box', style='filled', fillcolor='black', fontcolor='white')
    
#     # Arcos entre plazas y transiciones
#     edges = [
#         ("P_Inicio", "T_Filtrar"), ("T_Filtrar", "P_Filtrado"),
#         ("P_Filtrado", "T_Validar"), ("T_Validar", "P_Aceptado"),
#         ("P_Filtrado", "T_Error"), ("T_Error", "P_Error"),
#         ("P_Aceptado", "T_Completar"), ("T_Completar", "P_Final")
#     ]
#     for edge in edges:
#         dot.edge(edge[0], edge[1])
    
#     return dot

# def simular_petri_red(input_string):
#     string_filtrado = re.sub(r'[^A-Za-z]', '', input_string).lower()
#     output_esperado = "aprobado"
    
#     states = []
#     current_state = {"P_Inicio": 1, "P_Filtrado": 0, "P_Aceptado": 0, "P_Error": 0, "P_Final": 0}
#     states.append(current_state.copy())
    
#     # Paso 1: Filtrar números
#     current_state["P_Inicio"] = 0
#     current_state["P_Filtrado"] = 1
#     states.append(current_state.copy())
    
#     # Paso 2: Validar cadena
#     current_state["P_Filtrado"] = 0
#     if string_filtrado == output_esperado:
#         current_state["P_Aceptado"] = 1
#         states.append(current_state.copy())
        
#         # Paso 3: Completar proceso
#         current_state["P_Aceptado"] = 0
#         current_state["P_Final"] = 1
#     else:
#         current_state["P_Error"] = 1
#     states.append(current_state.copy())
    
#     for i, state in enumerate(states):
#         dot = create_petri_red()
#         for place, active in state.items():
#             if active:
#                 dot.node(place, shape='circle', style='filled', fillcolor='red')
        
#         filename = f'step_{i}'
#         dot.render(filename)
#         print(f'Generado: {filename}.png')
#         time.sleep(1)

# if __name__ == "__main__":
#     input_string = "A1P2R3O4B5A6D7O8"
#     simular_petri_red(input_string)


# ------------------------------------------- CODIGO EN DINAMICO -------------------------------------------

def create_petri_red(active_places=[]):
    dot = Digraph(format='png')
    dot.attr(size='8,8')
    
    # Plazas
    plazas = ["P_Inicio", "P_Filtrado", "P_Aceptado", "P_Final"]
    for plaza in plazas:
        color = 'red' if plaza in active_places else 'lightgray'
        dot.node(plaza, shape='circle', style='filled', fillcolor=color)
    
    # Transiciones
    transitions = ["T_Filtrar", "T_Validar", "T_Completar"]
    for trans in transitions:
        dot.node(trans, shape='box', style='filled', fillcolor='black', fontcolor='white')
    
    # Arcos entre plazas y transiciones
    edges = [
        ("P_Inicio", "T_Filtrar"), ("T_Filtrar", "P_Filtrado"),
        ("P_Filtrado", "T_Validar"), ("T_Validar", "P_Aceptado"),
        ("P_Aceptado", "T_Completar"), ("T_Completar", "P_Final")
    ]
    for edge in edges:
        dot.edge(edge[0], edge[1])
    
    return dot

def simular_petri_red(input_string):
    string_filtrado = re.sub(r'[^A-Za-z]', '', input_string).lower()
    
    print(f"Entrada: {input_string}")
    print(f"Cadena filtrada: {string_filtrado}")
    print("Salida: La cadena ha sido procesada correctamente")
    
    states = [
        ["P_Inicio"],
        ["P_Filtrado"],
        ["P_Aceptado"],
        ["P_Final"]
    ]
    
    for i, active_plazas in enumerate(states):
        dot = create_petri_red(active_plazas)
        filename = f'step_{i}'
        dot.render(filename)
        print(f'Generado: {filename}.png')
        time.sleep(1)
    
if __name__ == "__main__":
    input_string = input("Ingrese una cadena de caracteres: ")
    simular_petri_red(input_string)