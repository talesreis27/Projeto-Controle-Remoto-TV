# 📺 Controle Remoto de TV em Python

Simulação de um **controle remoto de televisão** desenvolvida em Python com Programação Orientada a Objetos (POO) e interface visual no terminal usando a biblioteca **Rich**. Projeto baseado no Mundo 4 de Python do canal [Curso em Vídeo](https://www.youtube.com/@CursoemVideo).

---

## 📋 Sobre o Projeto

O projeto simula o funcionamento de um controle remoto básico de TV diretamente no terminal, com painéis coloridos, barra de volume animada e lista de canais com destaque para o canal atual. Foi desenvolvido para praticar os conceitos de POO em Python, além do uso da biblioteca `rich` para uma saída visual mais rica.

---

## 🗂️ Estrutura do Código

### Dicionário `NOME_CANAIS`
Mapeamento dos canais disponíveis:

| Número | Canal |
|--------|-------|
| 1 | Globo |
| 2 | SBT |
| 3 | Record |
| 4 | Animal Planet |
| 5 | Discovery Channel |

---

### Funções auxiliares

**`barra_volume(volume, maximo, largura)`**  
Gera uma barra visual de volume com cores dinâmicas:
- ⬛ Cinza — volume zerado
- 🟢 Verde — volume até 30%
- 🟡 Amarelo — volume de 31% a 69%
- 🔴 Vermelho — volume 70% ou acima

**`lista_canais(canal_atual, canal_minimo, canal_maximo)`**  
Exibe a lista de canais disponíveis, destacando o canal atualmente selecionado com uma seta `->`.

**`painel_hud(canal_atual, volume, canal_minimo, canal_maximo)`**  
Renderiza o painel principal da TV no terminal, combinando a barra de volume e a lista de canais dentro de um `Panel` estilizado com `rich`.

---

### `class Controle`

Representa o controle remoto com todos os seus estados e comportamentos.

**Atributos:**
- `ligado` — estado da TV (`True`/`False`)
- `volume` — volume atual (padrão: `0`)
- `canal` — canal atual (padrão: `1`)
- `volume_maximo` / `volume_minimo` — limites de volume (`100` / `0`)
- `canal_maximo` / `canal_minimo` — limites de canal (`5` / `1`)

**Métodos:**

| Método | Descrição |
|--------|-----------|
| `ligar()` | Liga a TV; exibe aviso se já estiver ligada |
| `desligar()` | Desliga a TV; exibe aviso se já estiver desligada |
| `aumenta_volume()` | Aumenta o volume em 10; respeita o limite máximo |
| `diminui_volume()` | Diminui o volume em 10; respeita o limite mínimo |
| `next_chanel()` | Avança para o próximo canal; volta ao mínimo ao ultrapassar o máximo |
| `back_chanel()` | Volta para o canal anterior; vai ao máximo ao ficar abaixo do mínimo |

> Todos os métodos verificam se a TV está ligada antes de executar a ação, exibindo um painel de erro caso contrário.

---

## 🖥️ Exemplo de Saída no Terminal

```
╭─────────── LIGAR ───────────╮
│                             │
│  ✔ TV LIGADA!               │
│  CANAL: 1                   │
│  VOLUME: 0%                 │
│                             │
╰─────────────────────────────╯

╭──────────── TV ─────────────╮
│  VOLUME                     │
│  ██████░░░░░░░░░░░░░░  30%  │
│                             │
│  CANAIS                     │
│  1 Globo                    │
│  2 SBT                      │
│ -> 3 Record                 │
│  4 Animal Planet            │
│  5 Discovery Channel        │
╰─────────────────────────────╯
```

---

## ▶️ Como Executar

### Pré-requisitos

- Python 3.x instalado
- Biblioteca `rich` instalada

### Instalação da dependência

```bash
pip install rich
```

### Passos

```bash
# Clone o repositório
git clone https://github.com/talesreis27/Projeto-Controle-Remoto-TV.git

# Acesse a pasta do projeto
cd Projeto-Controle-Remoto-TV

# Execute o script
python controle_remoto.py
```

---

## 📁 Arquivos do Repositório

```
Projeto-Controle-Remoto-TV/
├── controle_remoto.py   # Código-fonte principal
├── LICENSE              # Licença MIT
└── README.md            # Este arquivo
```

---

## 🛠️ Tecnologias Utilizadas

- **Python 3** — linguagem principal
- **[Rich](https://github.com/Textualize/rich)** — biblioteca para saída estilizada no terminal (`Panel`, cores, formatação)

---

## 💡 Conceitos Praticados

- Programação Orientada a Objetos (POO)
- Encapsulamento de estado com atributos de instância
- Validação de estados antes de executar ações
- Uso de bibliotecas externas para UI no terminal
- Funções auxiliares para geração de componentes visuais

---

## 📄 Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE) — sinta-se livre para usar, modificar e distribuir.

---

## 👤 Autor

**Tales Reis e Silva**  
GitHub: [@talesreis27](https://github.com/talesreis27)

---

## 🙏 Referência

Projeto inspirado no **Mundo 4 de Python** do canal [Curso em Vídeo](https://www.youtube.com/@CursoemVideo) — um dos maiores canais de ensino de programação em português.
