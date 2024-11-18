import pyfiglet
from rich.console import Console
from rich.traceback import install

console = Console()
install()

user = input('Enter the text here to convert to ASCII text: ')
result = pyfiglet.figlet_format(user, font='gothic')

console.print(result)