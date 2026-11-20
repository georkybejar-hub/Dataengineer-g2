from rich.console import Console
from modulo_externo import data
from rich.table import Table
def show_table(users):
    console= Console()
    for user in data:
            print(user)

def main ():
    pass
    
if __name__ =='__main__':
    main()