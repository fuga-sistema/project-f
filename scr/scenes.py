import os
import random
from scene_manager import Scene


class ReadTheSecretScene(Scene):
    def __init__(self, metadata_manager, ui_manager, secret_path='secrets'):
        super().__init__(metadata_manager, ui_manager)
        self.secret_path = secret_path
        self.secret_file = os.path.join(self.secret_path, 'secret.txt')

    def enter(self):
        # Verifica se o diretório 'secrets' existe, senão cria
        if not os.path.exists(self.secret_path):
            os.makedirs(self.secret_path)

        # Cria um segredo aleatório e o salva em 'secret.txt'
        secret = str(random.randint(100, 999))
        with open(self.secret_file, 'w') as f:
            f.write(f"The secret is: {secret}")
        self.ui_manager.display_message("A secret has been hidden...")

    def process_input(self, input):
        # Processa a entrada do usuário para ler ou usar o segredo
        if input == 'read secret':
            with open(self.secret_file, 'r') as f:
                secret_message = f.read()
            self.ui_manager.display_message(secret_message)
        elif input == 'use secret':
            self.ui_manager.display_message("You used the secret to unlock the next level!")
            # Aqui você pode implementar a lógica para transição para o próximo nível

    def update(self):
        # Aqui você pode atualizar qualquer estado do jogo necessário para este nível
        pass

    def render(self):
        # Atualiza a UI se necessário para este nível
        pass

    def exit(self):
        # Lógica de limpeza ao sair deste nível
        pass
