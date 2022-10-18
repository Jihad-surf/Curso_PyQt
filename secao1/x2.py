
dados = {
    "Joao": ["Sao Paulo", 25, "Engenheiro"],
    "Pedro": ["Rio de Janeiro", 30, "Enfermeiro"],
    "Maria": ["Minas gerais", 45, "Professora"],
    "Fernanda": ["Porto Alegre", 22, "Estudante"],
    "Gabriel": ["Sao Paulo", 28, "Entregador"]
}

for chave in dados:
    print(f'Chave: {chave} ---- valor:{dados[chave]} --- primeiro valor: {dados[chave][0]}')