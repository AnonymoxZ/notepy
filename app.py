# Bloco de Notas - v0.0
# Date-time: 10-03-25 / 17:26
# Author: Sr.Stoner
# Programmers: {your name}
# ***************************

import bloco


class blocoNotas:
    def __init__(self,title,content,date_time):
        self.title = title
        self.content = content
        self.date_time = date_time

    # structure CRUD
    def _create_note(self):
        with open(f'notas_local/{self.title}.txt', 'a') as bd:
            bd.write(bloco.note(self.title,self.content,self.date_time))
    
    
    def _delete_note(self):
       pass
    
    
    def _edit_note(self):
        pass


nota = blocoNotas('Pythonic','Love and snakes',bloco.logtime())

'''
ATRIBUTTES
print(nota.title)
print(nota.content)
print(nota.datetime)
'''


'''
METHOD CREATE NOTES
'''
nota._create_note()
