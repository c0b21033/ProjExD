import pygame as pg
import sys
from random import randint


class Screen:
    def __init__(self, title, scr_size, background):
        self.title = title
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode((scr_size))
        self.rct = self.sfc.get_rect()
        self.back = pg.image.load(background)
        self.back_rct = self.back.get_rect()

    def blit(self):
        return self.sfc.blit(self.back, self.back_rct)

class Bird:
    key_delta = {
    pg.K_UP:    [0, -1],
    pg.K_DOWN:  [0, +1],
    pg.K_LEFT:  [-1, 0],
    pg.K_RIGHT: [+1, 0],}
    dif1 = 60
    dif2 = 70
    
    def __init__(self, file, zoom, pos, hp):
        self.sfc = pg.image.load(file)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, zoom)
        self.rct = self.sfc.get_rect()
        self.rct.center = pos
        self.life = hp
        self.shield_pos = [[(self.rct.centerx-self.dif1, self.rct.centery-self.dif2), (self.rct.centerx-self.dif1, self.rct.centery+self.dif2)],
                           [(self.rct.centerx+self.dif1, self.rct.centery-self.dif2), (self.rct.centerx+self.dif1, self.rct.centery+self.dif2)],
                           [(self.rct.centerx-self.dif2, self.rct.centery-self.dif1), (self.rct.centerx+self.dif2, self.rct.centery-self.dif1)],
                           [(self.rct.centerx-self.dif2, self.rct.centery+self.dif1), (self.rct.centerx+self.dif2, self.rct.centery+self.dif1)]]

    def draw_life(self, screen):
        fonto = pg.font.Font(None, 80)
        txt = fonto.render("LIFE", True, "BLACK")
        screen.sfc.blit(txt, (930, 10))
        pg.draw.rect(screen.sfc, (0, 255, 0), (1080, 20, self.life, 30))

    def blit(self, sfc:Screen):
        return sfc.blit(self.sfc, self.rct)

    def update(self, screen:Screen):
        key_states = pg.key.get_pressed()
        for key, delta in self.key_delta.items():
            if key_states[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]
                # 練習7
                if check_bound(self.rct, screen.rct) != (+1, +1):
                    self.rct.centerx -= delta[0]
                    self.rct.centery -= delta[1]
        self.draw_life(screen)
        screen.sfc.blit(self.sfc, self.rct)
        #shield = pg.draw.line(screen, (255, 128, 0), self.shield_pos[tori_direction][0], self.shield_pos[tori_direction][1], )

        # if shield.colliderect(i):
        #         if tori_direction == 0 or tori_direction == 1:#右か左を向いていたら
        #             j[0] *= -1 #xspeedを反転
        #         else:
        #             j[1] *= -1
        


class Bomb:
    def __init__(self, color, radius, speed, screen):
        self.sfc = pg.Surface((radius*2, radius*2)) # 空のSurface
        self.sfc.set_colorkey((0, 0, 0)) # 四隅の黒い部分を透過させる
        self.rct = self.sfc.get_rect()
        pg.draw.circle(self.sfc, color, (self.rct.width//2, self.rct.height//2), radius) # 爆弾用の円を描く
        self.rct.centerx = randint(self.rct.width, screen.rct.width//2-self.rct.width)
        self.rct.centery = randint(self.rct.height, screen.rct.height//2-self.rct.height)
        self.vx, self.vy = +speed[0], +speed[1] # 練習6

    def blit(self, screen):
        return screen.sfc.blit(self.sfc, self.rct)

    def update(self, screen):
        yoko, tate = check_bound(self.rct, screen.rct)
        self.vx *= yoko
        self.vy *= tate
        self.rct.move_ip(self.vx, self.vy)
        screen.sfc.blit(self.sfc, self.rct)

def check_bound(obj_rct, scr_rct):
    """
    obj_rct：こうかとんrct，または，爆弾rct
    scr_rct：スクリーンrct
    領域内：+1／領域外：-1
    """
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right: 
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom: 
        tate = -1
    return yoko, tate


def main():
    screen = Screen("逃げろこうかとん",(1200, 600), "ex05/fig/pg_bg.jpg")
    tori = Bird("ex05/fig/6.png", 2.0, (900, 400), 100)
    bomb = Bomb((255, 0, 0), 10, (1, 1), screen)
    bomb2 = Bomb((0, 255, 0), 5, (2, 2), screen)
    clock = pg.time.Clock()

    while True:
        screen.blit()
        
        for event in pg.event.get(): 
            if event.type == pg.QUIT:
                return

        tori.update(screen)

        bomb.update(screen)
        bomb2.update(screen)

        if (tori.rct.colliderect(bomb.rct) 
            or tori.rct.colliderect(bomb2.rct)): # こうかとんrctが爆弾rctと重なったら
            tori.life -= 1
            
        if tori.life == 0:
            return

        pg.display.update() #練習2
        clock.tick(1000)


if __name__ == "__main__":
    pg.init() # 初期化
    main()    # ゲームの本体
    pg.quit() # 初期化の解除
    sys.exit()
