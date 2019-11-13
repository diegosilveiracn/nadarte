# -*- coding: utf-8 -*-
# try something like

def index():
    grid = SQLFORM.grid(Estilo,user_signature=False)
    return dict(grid=grid)
