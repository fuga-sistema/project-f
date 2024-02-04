from abc import ABC, abstractmethod


class Scene(ABC):
    def __init__(self, metadata_manager, ui_manager):
        self.metadata_manager = metadata_manager
        self.ui_manager = ui_manager

    @abstractmethod
    def enter(self):
        # Código para executar quando a cena é carregada
        pass

    @abstractmethod
    def process_input(self, input):
        # Código para processar a entrada do usuário nesta cena
        pass

    @abstractmethod
    def update(self):
        # Código para atualizar o estado da cena
        pass

    @abstractmethod
    def render(self):
        # Código para renderizar a cena na interface do usuário
        pass

    @abstractmethod
    def exit(self):
        # Código para executar quando a cena está sendo descarregada/saída
        pass


class SceneManager:
    def __init__(self):
        self.scenes = {}
        self.current_scene = None

    def add_scene(self, name, scene):
        self.scenes[name] = scene

    def go_to_scene(self, name):
        if self.current_scene:
            self.current_scene.exit()
        self.current_scene = self.scenes[name]
        self.current_scene.enter()

    def process_input(self, input):
        if self.current_scene:
            self.current_scene.process_input(input)

    def update(self):
        if self.current_scene:
            self.current_scene.update()

    def render(self):
        if self.current_scene:
            self.current_scene.render()
