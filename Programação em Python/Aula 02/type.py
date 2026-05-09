#Douglas Rafael Assis Mendes
curso = "Programação em Python"
carga_horaria = 60
media_esperada = 8.5
status = True

print(f"""
--- Informações do Curso ---
Nome do Curso: {curso} {type(curso)}

--- Detalhes Numéricos ---
Carga Horária Total (horas): {carga_horaria} {type(carga_horaria)}
Nota Média Esperada: {media_esperada} {type(media_esperada)}

--- Status do Curso ---
O curso já foi iniciado? {status} {type(status)}

--- Informações gerais do curso: ---

Resumo:
O curso '{curso}' tem nota média esperada {media_esperada}
Status de início: {status}.
Carga horária: {carga_horaria}h.

--- FIM ---""")