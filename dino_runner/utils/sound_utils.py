import pygame

def play_sound_effect(sound):
    pygame.mixer.music.load(sound)
    pygame.mixer.music.stop()
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume == 40