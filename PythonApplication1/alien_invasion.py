import sys
from settings import Settings
import pygame
from ship import Ship
def run_game():
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship=Ship(screen)
    while True:
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        for event in pygame.event.get():#监视键盘和鼠标事件
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.flip()#让最近绘制的屏幕可见
run_game()