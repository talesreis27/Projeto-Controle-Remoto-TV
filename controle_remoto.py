from rich import print
from rich.panel import Panel
from rich.text import Text

NOME_CANAIS= {
    1:'Globo',
    2:'SBT',
    3:'Record',
    4:'Animal Planet',
    5:'Discovery Chanel'
}

def barra_volume(volume, maximo=100, largura=20):
    preenchido = int((volume / maximo) * largura)
    vazio = largura - preenchido

    if volume == 0:
        cor = 'bright_black'
    elif volume <= 30:
        cor = 'green'
    elif volume < 70:
        cor = 'yellow'
    else:
        cor = 'red'
    barra  = f"[{cor}]{'█' * preenchido}[/{cor}][bright_black]{'▒'* vazio}[/bright_black]"
    return barra
def lista_canais(canal_atual, canal_minimo, canal_maximo):
    linhas = []
    for c in range(canal_minimo, canal_maximo + 1):
        nome = NOME_CANAIS.get(c, f"canal{c}")
        if c == canal_atual:
            linhas.append(f"[bold black on white] -> {c} {nome:<8}[/bold black on white]")
        else:
            linhas.append(f"[bold black on white] {c} {nome:<8}[/bold black on white]")
    return "\n".join(linhas)

def painel_hud(canal_atual,volume, canal_minimo, canal_maximo):
    barra = barra_volume(volume)
    canais = lista_canais(canal_atual, canal_minimo, canal_maximo)

    conteudo = (
        f"[cyan]  VOLUME[/cyan]\n"
        f"{barra}\n\n"
        f"[cyan]  CANAIS[/cyan]"
        f"{canais}"
        )

    print(Panel(
        conteudo,
        title='[cyan] TV[/cyan]',
        border_style= 'cyan'
        ))


class Controle:
    def __init__(self):
        self.ligado = False
        self.volume = 0
        self.canal = 1
        self.volume_maximo = 100
        self.volume_minimo = 0
        self.canal_maximo = 5
        self.canal_minimo = 1

    def ligar(self):
        if self.ligado:
            print(Panel(
            '[red]X A TV ja esta ligada![/red]',
            title = '[bold blue]AVISO[/bold blue]',
            border_style = 'red'
            ))
        else:
            self.ligado = True
            print(Panel(
            '[bold green]V TV LIGADA![/bold green]\n'
            f'[cyan]CANAL:[/cyan][bold yellow]{self.canal}[/bold yellow]\n'
            f'[cyan]VOLUME:[/cyan][bold yellow]{self.volume}%[/bold yellow]',
            title = '[green]LIGAR[/green]',
            border_style = 'green',
            padding=(1, 2)
            ))

    def desligar(self):
        if not self.ligado:
            print(Panel(
                '[red]X A TV ja esta desligada![/red]',
                  title='[bold blue]AVISO![/bold blue]',
                  border_style='red'
                  ))
        else:
            self.ligado = False
            painel = Panel(
                "[bold red]X TV DESLIGADA![/bold red]",
                title = '[bold red]DESLIGAR[/bold red]',
                border_style = 'red',
                padding=(1, 2)
            )
            print(painel)

    def aumenta_volume(self):
        if not self.ligado:
            print(Panel(
                '[red] A TV esta desligada... Ligue-a para aumentar o volume![/red]',
                title='[bold red] ERRO [/bold red]',
                border_style='red'
            ))

            return

        novo_volume = self.volume + 10

        if novo_volume > self.volume_maximo:
            novo_volume = self.volume_maximo
            self.volume = novo_volume
            print(Panel(
                f'[green]VOLUME MAXIMO ATINGIDO...[/green][bold yellow]{self.volume}[/bold yellow]',
                title='[bold yellow]AVISO[/bold yellow]',
                border_style = 'yellow'
            ))
        else:
            self.volume = novo_volume


    def diminui_volume(self):
        if not self.ligado:
            print(Panel(
            '[red] A TV esta desligada... Ligue-a para aumentar o volume![/red]',
            title='[bold red] ERRO [/bold red]',
            border_style = 'red'
            ))
            return

        novo_volume = self.volume - 10

        if novo_volume < self.volume_minimo:
            novo_volume = self.volume_minimo
            self.volume = novo_volume

            print(Panel(
                f"[green]VOLUME MINIMO ATINGIDO...[/green][bold yellow]{self.volume}[/bold yellow]",
                title='[bold yellow]AVISO[/bold yellow]',
                border_style='yellow'
            ))
        else:
            novo_volume= self.volume - 10
            self.volume = novo_volume

    def next_chanel(self):
        if not self.ligado:
            print(Panel(
            '[red]A TV esta desligada... Ligue-a para passar o canal[/red]',
            title='[bold red] ERRO [/bold red]',
            border_style = 'red'
            ))
            return

        if self.canal >= self.canal_maximo:
            self.canal = self.canal_minimo


        else:
            self.canal += 1

    def back_chanel(self):
        if not self.ligado:
            print(Panel(
            '[red]A TV esta desligada... Ligue-a para passar o canal[/red]',
            title='[bold red] ERRO [/bold red]',
            border_style = 'red'
            ))
            return
        if self.canal < self.canal_minimo:
            self.canal = self.canal_maximo
        else:
            self.canal -= 1


tv = Controle()

# Testa ligar
tv.ligar()

# Testa volume
tv.aumenta_volume()
tv.aumenta_volume()
tv.aumenta_volume()

# Testa canais
tv.next_chanel()
tv.next_chanel()

# Mostra o HUD
painel_hud(tv.canal, tv.volume, tv.canal_minimo, tv.canal_maximo)

# Testa desligar
tv.desligar()