# -*- coding: utf-8 -*-
# try something like
def index():
    grid = SQLFORM.grid(Atleta,user_signature=False)
    return dict(grid=grid)
