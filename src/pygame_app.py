import pygame
from intro_scene import IntroScene
from play_scene import PlayScene

class PygameApp():
    def __init__(self):
        self.running = True
        self.fps = 60
        self.active_scene = None
        self.width = 800
        self.height = 600
        self.init_pygame()

    def init_pygame(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.load_assets()
        self.active_scene=IntroScene(self)
        self.scenes = {'intro': IntroScene(self), 'play': PlayScene(self)}
        self.change_scene('intro')
        
        

    def change_scene(self, scene_name):
        if self.active_scene is not None:
            self.active_scene.exit()
        self.active_scene = self.scenes[scene_name]
        self.active_scene.start()
        


    def load_assets(self):
        pass


    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running=False
            self.active_scene.process_events(event)

    def update(self):
        self.active_scene.update()

    def draw(self):
        self.active_scene.draw()
        pygame.display.flip()

    def run (self):
        while self.running:
            self.clock.tick(60)
            self.process_events()
            self.update()
            self.draw()

app = PygameApp()
app.run()
pygame.quit()



