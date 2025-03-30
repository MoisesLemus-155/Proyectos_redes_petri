from graphviz import Digraph
import time
import os

def create_petri_red():
    dot = Digraph(format='png')
    dot.attr(size='8,8')
    
    # Plazas
    plazas = ['P_R1', 'P_G1', 'P_Y1', 'P_R2', 'P_G2', 'P_Y2']
    for plaza in plazas:
        dot.node(plaza, shape='circle', style='filled', fillcolor='lightgray')
    
    # Transiciones
    transitions = ['T_1', 'T_2', 'T_3', 'T_4', 'T_5', 'T_6']
    for trans in transitions:
        dot.node(trans, shape='box', style='filled', fillcolor='black', fontcolor='white')
    
    # Arcos entre plazas y transiciones
    edges = [
        ('P_R1', 'T_1'), ('T_1', 'P_G1'),
        ('P_G1', 'T_2'), ('T_2', 'P_Y1'),
        ('P_Y1', 'T_3'), ('T_3', 'P_R1'),
        ('P_R2', 'T_4'), ('T_4', 'P_G2'),
        ('P_G2', 'T_5'), ('T_5', 'P_Y2'),
        ('P_Y2', 'T_6'), ('T_6', 'P_R2'),
    ]
    for edge in edges:
        dot.edge(edge[0], edge[1])
    
    return dot

def simular_petri_red():
    states = [
        {"P_R1": 1, "P_G1": 0, "P_Y1": 0, "P_R2": 0, "P_G2": 1, "P_Y2": 0},  # Estado inicial
        {"P_R1": 0, "P_G1": 1, "P_Y1": 0, "P_R2": 1, "P_G2": 0, "P_Y2": 0},  # Verde principal, Rojo secundario
        {"P_R1": 0, "P_G1": 0, "P_Y1": 1, "P_R2": 1, "P_G2": 0, "P_Y2": 0},  # Amarillo principal
        {"P_R1": 1, "P_G1": 0, "P_Y1": 0, "P_R2": 0, "P_G2": 1, "P_Y2": 0},  # Rojo principal, Verde secundario
        {"P_R1": 1, "P_G1": 0, "P_Y1": 0, "P_R2": 0, "P_G2": 0, "P_Y2": 1},  # Amarillo secundario
        {"P_R1": 1, "P_G1": 0, "P_Y1": 0, "P_R2": 1, "P_G2": 0, "P_Y2": 0}   # Rojo secundario
    ]
    
    for i, state in enumerate(states):
        dot = create_petri_red()
        for plaza, active in state.items():
            if active:
                dot.node(plaza, shape='circle', style='filled', fillcolor='red')
        
        filename = f'step_{i}'
        dot.render(filename)
        print(f'Generado: {filename}.png')
        time.sleep(1)

if __name__ == "__main__":
    simular_petri_red()