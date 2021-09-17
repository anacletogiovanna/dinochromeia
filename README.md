# Dinochromeia
Projeto de um agente inteligente para o jogo Dino do Chrome 

![teste](https://user-images.githubusercontent.com/33101169/133177957-08292e22-b35c-443e-9185-b39c2f7cc708.gif)

#### Tecnologias utilizadas:
Para a criação do agente inteligente, utilizamos as seguintes bibliotecas:
- [NEAT-Python](https://neat-python.readthedocs.io/en/latest/): Biblioteca Python que implementa um algoritmo evolucionario onde cria-se redes neurais artificiais (NeuroEvolution of Augmenting Topologies). Essa biblioteca é responsável por gerar as populações e gerações responsáveis por aprimorar o agente inteligente.
- [PyGame](https://www.pygame.org/news): Responsável pela criação de jogos, escrevendo elementos em tela e realizando animações utilizando a linguagem python, com ele é possível recriar jogos como o do Dino Chrome.

#### Estrutura do projeto:

```bash
├── dinochromeia                      # Diretório principal
│   ├── Assets                        # Diretório com as imagens dos obstáculos, dinossauros
│   ├── Characters                    # Diretório com as classes dos personagens
│   |   ├── bird.py                   # Arquivo da classe Bird, tipo de personagem-obstáculo do jogo
│   |   ├── cactus.py                 # Arquivo da classe Cactus, tipo de personagem-obstáculo do jogo
│   |   ├── cloud.py                  # Arquivo da classe Cloud, compõe o cenário pre-histórico do jogo
│   |   ├── dinosaur.py               # Arquivo da classe Dinosaur, personagem principal do jogo
│   |   ├── obstacle.py               # Arquivo da classe Obstacle, demais obstáculos herdam desta.
│   ├── Const                         # Diretório com a classe das constantes utlizadas
│   |   ├── constants.py              # Script de constantes utilizadas no código
│   ├── config.txt                    # Arquivo de configuração do NEAT-Python 
│   ├── main.py                       # Script principal 
│   ├── output_Dino.txt               # Arquivo com logs/reports 
│   ├── requirements.txt              # Arquivos de bibliotecas utilizadas no projeto
│   ├── supportFunction.py            # Arquivo com funções de apoio
│   ├── supportFunctionNeat.py        # Arquivo com funções de apoio relativas ao uso para o NEAT

```

Este projeto foi baseado nos tutoriais:
[Chrome Dinosaur in Python & Pygame](https://youtu.be/KOBKkPWGP-g) e 
[Python A.I Tutorial with NEAT](https://www.youtube.com/watch?v=lcC-jiCuDnQ&t=33s)
