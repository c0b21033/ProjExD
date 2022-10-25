import pygame as pg
import sys
from random import randint
def main():
    pg.display.set_caption("逃げろこうかとん")
    scrn_sfc = pg.display.set_mode((1200, 600))
    scrn_rct = scrn_sfc.get_rect()
    bg_sfc = pg.image.load("ex04/fig/pg_bg.jpg")
    bg_rct = bg_sfc.get_rect()
    clock = pg.time.Clock()
    vx, vy = 1, 1

    tori_sfc = pg.image.load("ex04/fig/6.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400

    bomb_sfc = pg.Surface((20, 20))
    bomb_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb_sfc, (255, 0, 0), (10, 10), 10)
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx, bomb_rct.centery = randint(0, scrn_rct.width), randint(0, scrn_rct.height)
    while True:
        scrn_sfc.blit(bg_sfc, bg_rct)
        clock.tick(1000)
        for event in pg.event.get():
            if event.type == pg.QUIT:return
        key_states = pg.key.get_pressed()
        if key_states[pg.K_UP]:
            tori_rct.centery-=1
        if key_states[pg.K_DOWN]:
            tori_rct.centery+=1
        if key_states[pg.K_LEFT]:
            tori_rct.centerx-=1
        if key_states[pg.K_RIGHT]:
            tori_rct.centerx+=1
        scrn_sfc.blit(tori_sfc, tori_rct)
        bomb_rct.move_ip(vx, vy)
        scrn_sfc.blit(bomb_sfc, bomb_rct)
        
        
        pg.display.update()

        
if __name__ == "__main__":
    pg.init()
    main()
    sys.exit()
    pg.quit()