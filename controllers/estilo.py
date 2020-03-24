# -*- coding: utf-8 -*-
# try something like

@auth.requires_login()
def index():
    grid = SQLFORM.grid(Estilo,user_signature=False)
    return dict(grid=grid)
