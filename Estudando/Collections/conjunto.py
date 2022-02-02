usuarios_data_science = [15, 23, 45, 65]
usuarios_machine_learning = [12, 23, 43, 2]


assistiram = usuarios_data_science.copy()
assistiram.extend(usuarios_machine_learning)
# Criando conjunto com set(), e não existe posição
print(set(assistiram), "\nTamanho:", len(set(assistiram)))
