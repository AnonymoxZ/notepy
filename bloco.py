# functions app nota
from os import system
from time import strftime



def logtime():
    return f"{strftime('%d/%m/%y - %H:%M')}"


def note(title,content,datetime):
    '''
    ---------------------------------------------------------------------------
    Title: {title}

    Content...

    dd/mm/yy - H:M
    ---------------------------------------------------------------------------
    '''
    return f"{75*'-'}\nTitle: {title}\n\n{content}\n\n{datetime}\n{75*'-'}\n\n"
