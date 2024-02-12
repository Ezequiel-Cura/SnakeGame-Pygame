import pygame as py

class Config:
    def __init__(self, size, FPS, caption = "Title", icon = ""):
        self.running = True
        #fondos
        self.list_fondos = []
        self.fondo = None
        
        self.size = size
        self.SCREEN = py.display.set_mode(self.size)
        self.FPS = FPS
        self.clock = py.time.Clock()

        py.mixer.init()

        if icon != "":
            self.set_icon(icon)
            
        self.set_caption(caption)
        


    def set_caption(self, caption):
        #Settear el titulo del juego
        py.display.set_caption(caption)

    def set_icon(self, icon):
        py.display.set_icon(icon)

    def set_fps(self, FPS):
        self.FPS = FPS

    def set_music(self, music):
        self.music = py.mixer.Sound(music)
        self.music.set_volume(0.2)
        self.play_music()
        
    def set_volume(self, volume):
        self.music.set_volume(volume)

    def play_music(self):
        self.music.play()

    def stop_music(self):
        self.music.stop()

    def set_background_image(self, background, list_bg = False):
        if list_bg == True:
            for img in background:
                img_cargada = py.image.load(img)
                img_rescalada = py.transform.scale(img_cargada, self.size)
                self.list_fondos.append(img_rescalada)
        else:
            self.background_image = py.image.load(background)
            self.background_image = py.transform.scale(self.background_image, self.size)

    def set_fuente(self):
        pass

    def fill_screen(self, color=None):
        if color != None:
            self.SCREEN.fill(color)
        else:
            self.SCREEN.fill((0, 0,0))