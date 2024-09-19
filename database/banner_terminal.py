# Banner Terminal

try:
    import os, sys, urllib
    from rich.panel import Panel
    from rich.console import Console
except(Exception, KeyboardInterrupt) as e:
    try:
        from urllib.parse import quote
        __import__('os').system(f'xdg-open https://wa.me/6283140199711?text=BANNER%20ERROR%20%3A%20{quote(str(e))}')
        exit()
    except(Exception, KeyboardInterrupt) as e:
        from urllib.parse import quote
        __import__('os').system(f'xdg-open https://wa.me/6283140199711?text=BANNER%20ERROR%20%3A%20{quote(str(e))}')
        exit()

class Terminal:
    def __init__(self) -> None:
        pass
        
    def clear_terminal_size(self):
        os.system('clear' if 'linux' in sys.platform.lower() else 'cls')
        
    def banner_instagram(self):
        self.clear_terminal_size()
        Console(width = 50, style = "bold grey50").print(Panel("""[bold purple]       
 ┳        ┏┓     ┓
 ┃┏┓┏╋┏┓  ┏┛┏┓┏┓┏┫
 ┻┛┗┛┗┗┻  ┗┛┗┛┛ ┗┻
 [bold white]Author : [bold green]Zora Dev                
""", title = "[bold white]• Insta Zord •"), justify="center")
        return (True)
        
            
