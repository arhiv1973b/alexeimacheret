import matplotlib.pyplot as plt
import networkx as nx

G = nx.DiGraph()

# Узлы-принципы
G.add_node("Non_neutrality_against_False_Law", color='red')
G.add_node("Truth_as_Objective_Law", color='orange')
G.add_node("Equality_as_JusCogens", color='green')

# Узлы-искажения
G.add_node("Immunity_above_jus_cogens")
G.add_node("Procedure_over_substance")
G.add_node("Victim_rights_subordinated")

# Узлы-следствия
G.add_node("Legalized_Impunity")
G.add_node("Aggression_Unpunished")
G.add_node("Geopolitical_Disbalance")

# Связи
G.add_edges_from([
    ("Non_neutrality_against_False_Law", "Immunity_above_jus_cogens"),
    ("Immunity_above_jus_cogens", "Legalized_Impunity"),
    ("Truth_as_Objective_Law", "Procedure_over_substance"),
    ("Procedure_over_substance", "Aggression_Unpunished"),
    ("Equality_as_JusCogens", "Victim_rights_subordinated"),
    ("Victim_rights_subordinated", "Geopolitical_Disbalance")
])

colors = [G.nodes[n].get('color', 'lightblue') for n in G.nodes]
plt.figure(figsize=(10,7))
nx.draw(G, with_labels=True, node_color=colors, edge_color='gray', node_size=2000, font_size=9, arrows=True)
plt.title("TI-ULA: Деконструкция Лживого Закона через паттерны jus cogens")
plt.tight_layout()
plt.show()
