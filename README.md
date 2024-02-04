# project-f
Folders Game

# Template de Jogo de Texto em Python

Este projeto é um jogo onde a interface é feita no sistema de pastas do computador, além de uma interface em linha de comando.

## Funcionalidades

- **Interface do Usuário:** Utiliza a biblioteca `curses` para criar uma interface baseada em texto, permitindo interações através de comandos de texto.
- **Lógica do Jogo:** Inclui uma classe `GameLogic` como um placeholder para implementar a lógica específica do jogo, como enigmas e progressão da história.
- **Gerenciamento de Metadados:** A classe `MetadataManager` é responsável pelo gerenciamento do estado e informações do jogo, permitindo persistência do progresso.
- **Monitoramento do Sistema de Arquivos:** A classe `FileWatcher` observa mudanças no sistema de arquivos para atualizar o conteúdo do jogo dinamicamente.
- **Gerenciamento de Cenas:** Propõe a implementação de um sistema de gerenciamento de contextos para criar e gerenciar níveis de jogo de forma independente, semelhante ao gerenciamento de cenas do Unity.

## Estrutura do Projeto

- `main.py`: Script principal onde a execução do jogo começa.
- `game_logic.py`: Define a lógica básica do jogo e o processamento de comandos do usuário.
- `ui_manager.py`: Gerencia a interface do usuário baseada em texto usando a biblioteca `curses`.
- `metadata_manager.py`: Responsável por gerenciar e persistir o estado do jogo.
- `file_watcher.py`: Monitora mudanças no sistema de arquivos para atualizações dinâmicas de conteúdo.
- `scene_manager.py`: (Proposta) Gerencia diferentes cenas do jogo, como níveis ou menus.

## Como Usar

1. **Configuração do Ambiente:**
   Certifique-se de que o Python está instalado em sua máquina. Este projeto foi desenvolvido usando Python 3.8 ou superior.

2. **Instalação das Dependências:**
   Algumas funcionalidades podem requerer bibliotecas externas. Instale-as usando o comando:
   ```
   pip install -r requirements.txt
   ```

3. **Executando o Jogo:**
   Para iniciar o jogo, execute o script principal através do comando:
   ```
   python main.py
   ```

4. **Expandindo o Jogo:**
   - Para adicionar novas cenas ou níveis, crie classes que herdem de `Scene` e implementem os métodos abstratos.
   - Registre novas cenas no `SceneManager` e controle a transição entre elas conforme necessário.

## Exemplo de Nível de Jogo

O projeto inclui um exemplo de nível chamado "Read the Secret", onde o jogador precisa encontrar e ler um documento secreto. A lógica para criar e interagir com este nível está implementada na classe `ReadTheSecretScene`.
