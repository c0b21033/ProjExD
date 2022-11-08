import pygame as pg
import sys
from random import randint

#画面を作成するクラス
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

#プレイヤーのこうかとんのクラス
class Bird:
    def __init__(self, file, zoom, pos, hp, weapon, weapon_zoom):
        self.sfc = pg.image.load(file)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, zoom)
        self.rct = self.sfc.get_rect()
        self.rct.center = pos
        self.speed_y = 0 #y方向へのスピード
        self.jump_power = 0 #どのくらい跳ぶか　ボタンを押した分だけ数値が大きくなる
        self.charge = False #jump_powerをためているかどうか
        self.sky = True #こうかとんが空中にいるか

    def blit(self, sfc:Screen):
        return sfc.sfc.blit(self.sfc, self.rct)

    def update(self, screen:Screen):
        #左右移動
        key_lst = pg.key.get_pressed()
        if self.sky == True:
            if key_lst[pg.K_LEFT]:
                self.rct.move_ip(-1, 0)
            if key_lst[pg.K_RIGHT]:
                self.rct.move_ip(1, 0)
        
        #壁との判定
        self.wall_bound()
        self.blit(screen)

        #スピード制限
        if self.speed_y < 1:
            self.speed_y += 0.005

        #y軸に動かす
        self.rct.centery += self.speed_y

    #壁と天井の判定
    def wall_bound(self):
        if self.rct.left < 0:
            self.rct.left = 0
        if self.rct.right > 600:
            self.rct.right = 600
        if self.rct.top < 0:
            self.rct.top = 0
    
    #溜めジャンプする関数
    def jump(self, event):
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_SPACE]:
            #スピード制限
            if self.jump_power > -3:
                self.jump_power -= 0.1
                self.charge = True

        #spacekeyを離したら跳ぶ
        if self.charge == True and event.type == pg.KEYUP:
            #少しの溜めでは跳ばない
            if self.jump_power > -1 :
                self.jump_power = 0
            else:
                self.speed_y += self.jump_power
                self.jump_power = 0

    #def draw_charge(self, screen):
    #    pg.draw.rect(screen.sfc, (255,0,0), (self.rct.right+10,self.rct.top,10,self.jump_power))

#足場のクラス
class Floor:
    def __init__(self, screen):
        self.x = randint(0, 500)
        self.width = randint(20, 100)
        self.sfc = pg.Surface((self.width, 20))
        self.rct = pg.draw.rect(self.sfc, (255, 0, 0), (self.x, 900, 10, 10))
        

    def update(self, tori, screen):
        self.rct.centery -= 1
        print(self.rct.center, tori.rct.center)
        if self.rct.top < tori.rct.bottom and self.rct.bottom > tori.rct.top and self.rct.left+10 < tori.rct.right and self.rct.right+7 > tori.rct.left:
            tori.rct.bottom = self.rct.top
            
        if self.rct.centery < 0:
            self.rct.centery = 900
            self.rct.centerx = randint(0, 500)
        self.blit(screen)
        
    def blit(self, sfc:Screen):
        return sfc.sfc.blit(self.sfc, self.rct)

def main():
    screen = Screen("跳ねろこうかとん",(600, 900), "ex06/fig/pg_bg.jpg")
    tori = Bird("ex05/fig/6.png", 2.0, (300, 550), 100, "ex05/fig/sword-2.png", 0.3)
    clock = pg.time.Clock()
    floor1 = Floor(screen)
    floor2 = Floor(screen)
    floor3 = Floor(screen)
    while True:
        for event in pg.event.get(): 
            if event.type == pg.QUIT:
                return
            tori.jump(event)

        screen.blit()
        floor1.update(tori, screen)
        floor2.update(tori, screen)
        floor3.update(tori, screen)

        #最初の足場を描写
        first_box = pg.draw.rect(screen.sfc, (255,255,255), (0,880,600,10))
        #最初の足場と鳥
        if first_box.top < tori.rct.bottom and tori.rct.colliderect(first_box):
            tori.rct.bottom = first_box.top
            tori.sky = False
        tori.update(screen)
        tori.sky = True
        pg.display.update() 
        clock.tick(1000)

if __name__ == "__main__":
    pg.init() # 初期化
    main()    # ゲームの本体
    pg.quit() # 初期化の解除
    sys.exit()
