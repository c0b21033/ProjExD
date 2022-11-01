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
    
    def __init__(self, file, zoom, pos, hp, weapon, weapon_zoom):
        self.sfc = pg.image.load(file)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, zoom)
        self.rct = self.sfc.get_rect()
        self.rct.center = pos
        self.life = hp
        self.weapon = pg.image.load(weapon)
        self.weapon = pg.transform.rotozoom(self.weapon, 0, weapon_zoom)
        self.weapon_rct = self.sfc.get_rect()

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
        self.weapon_rct.center = (self.rct.centerx+50, self.rct.centery-40)
        screen.sfc.blit(self.sfc, self.rct)
        screen.sfc.blit(self.weapon, self.weapon_rct)
        

class Bomb(pg.sprite.Sprite):
    def __init__(self, color, radius, speed, screen, file, zoom):
        self.sfc = pg.image.load(file)
        self.rct = self.sfc.get_rect()
        pg.draw.circle(self.sfc, color, (self.rct.width//2, self.rct.height//2), radius) # 爆弾用の円を描く
        self.sfc = pg.transform.rotozoom(self.sfc, 0, zoom)
        self.sfc.set_colorkey((255, 255, 255)) # 四隅の黒い部分を透過させる
        self.rct = self.sfc.get_rect()
        self.rct.centerx = randint(self.rct.width, screen.rct.width//2-self.rct.width)
        self.rct.centery = randint(self.rct.height, screen.rct.height-self.rct.height)
        self.vx, self.vy = +speed[0], +speed[1] # 練習6
        self.flag = True

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

class Item:
    def __init__(self, file, pos, zoom):
        self.sfc = pg.image.load(file)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, zoom)
        self.rct = self.sfc.get_rect()
        self.rct.center = pos
        self.sfc.set_colorkey((255, 255, 255))
    
    def blit(self, screen):
        return screen.sfc.blit(self.sfc, self.rct)

def main():
    x, y = 0, 0
    screen = Screen("逃げろこうかとん",(1200, 600), "ex05/fig/pg_bg.jpg")
    tori = Bird("ex05/fig/6.png", 2.0, (900, 400), 50, "ex05/fig/sword-2.png", 0.3)
    bomb = Bomb((255, 0, 0), 10, (1, 1), screen, "ex05/fig/enemy.png", 0.12)
    bomb2 = Bomb((0, 255, 0), 5, (2, 2), screen, "ex05/fig/enemy.png", 0.05)
    clock = pg.time.Clock()
    item = Item("ex05/fig/Item.png", (x, y), 0.5)

    while True:
        screen.blit()
        
        for event in pg.event.get(): 
            if event.type == pg.QUIT:
                return

        tori.update(screen)
        if bomb.flag == True:
            bomb.update(screen)
        if bomb2.flag == True:
            bomb2.update(screen)

        #if tori.shiled:


        if tori.rct.colliderect(bomb.rct) and bomb.flag == True:
            tori.life -= 1  
        if tori.rct.colliderect(bomb2.rct) and bomb2.flag == True: # こうかとんrctが爆弾rctと重なったら
            tori.life -= 1

        if tori.life == 0:
            return

        now = pg.time.get_ticks()
        if now % 1000 == 0:
            x = randint(screen.rct.left, screen.rct.right)
            y = randint(screen.rct.top, screen.rct.bottom)
            item = Item("ex05/fig/Item.png", (x, y), 0.5)
        item.blit(screen)

        if tori.rct.colliderect(item.rct):
            print("Itemとぶつかってしまいました")
            clock.tick(2)
            return

        if tori.weapon_rct.colliderect(bomb.rct):
            bomb.flag = False

        if tori.weapon_rct.colliderect(bomb2.rct):
            bomb2.flag = False


        pg.display.update() #練習2
        clock.tick(1000)
        
if __name__ == "__main__":
    pg.init() # 初期化
    main()    # ゲームの本体
    pg.quit() # 初期化の解除
    sys.exit()
