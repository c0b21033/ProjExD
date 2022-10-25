import pygame as pg
import sys

def main():
    pg.display.set_caption("逃げろこうかとん")
    scrn_sfc = pg.display.set_mode((1200, 600))

    bg_sfc = pg.image.load("ex04/fig/pg_bg.jpg")
    bg_rct = bg_sfc.get_rect()
    clock = pg.time.Clock()

    tori_sfc = pg.image.load("ex04/fig/6.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400

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
        pg.display.update()
        
if __name__ == "__main__":
    pg.init()
    main()
    sys.exit()
    pg.quit()