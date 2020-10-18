# -*- coding: utf-8 -*-
# try something like
def index():
    query = ((db.tempos.estilo == db.estilos.id) &
             (db.tempos.atleta == db.atletas.id))
    fields = [db.tempos.id,
              db.tempos.data_treino,
              db.atletas.nome,
              db.estilos.descricao,
              db.tempos.distancia,
              db.tempos.tempo,
              db.tempos.nadadeira,
              db.tempos.palmar,
              db.tempos.pubol]
    grid = SQLFORM.grid(query=query,fields=fields,user_signature=False)
    return dict(grid=grid)
