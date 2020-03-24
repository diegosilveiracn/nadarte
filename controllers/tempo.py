# -*- coding: utf-8 -*-
# try something like

@auth.requires_login()
def index():
    query = ((db.tempos.estilo == db.estilos.id) & 
             (db.tempos.nadador == db.auth_user.id))
    fields = [db.tempos.id,
              db.tempos.data_treino,
              db.auth_user.first_name,
              db.auth_user.last_name,
              db.estilos.descricao,
              db.tempos.distancia,
              db.tempos.tempo,
              db.tempos.nadadeira,
              db.tempos.palmar,
              db.tempos.pubol]
    grid = SQLFORM.grid(query=query,fields=fields,user_signature=False)
    return dict(grid=grid)
