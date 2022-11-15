import pygame as pg
import sys                    
from random import randint

sky = 0 #空中

def collide(rct1, rct2, bird): # 土台のRect、上に乗る鳥のRect、x速度、y速度
    global sky
    if rct1.top < rct2.bottom and rct1.centery > rct2.bottom and rct1.colliderect(rct2):
        sky = 1 #地面
        rct2.bottom = rct1.top

    elif rct1.centery < rct2.top and rct1.bottom > rct2.top and rct1.left < rct2.centerx and rct1.right > rct2.centerx:
        rct2.centery = rct2.bottom+10
        bird.speed_y = 0


class Screen:
    
    def __init__(self, title, wh, bg_file):
        pg.display.set_caption(title)
        self.wh = (wh[0], wh[1])
        self.sfc = pg.display.set_mode(self.wh)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(bg_file)
        self.bgi_rct = self.bgi_sfc.get_rect()
        self.bgi_sfc2 = pg.image.load(bg_file)
        self.bgi_rct2 = self.bgi_sfc2.get_rect()

    def blit(self, bird):
        if bird.speed_y < 0:
            self.bgi_rct.centery = bird.rct.centery+200         
            self.bgi_rct2.centery = bird.rct.centery-400
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)
        self.sfc.blit(self.bgi_sfc, self.bgi_rct2)
        return 


class Bird:


    def __init__(self, bird_path, zup, default):
        self.sfc = pg.image.load(bird_path)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, zup)
        self.rct = self.sfc.get_rect()
        self.rct.center = default[0], default[1]
        self.vx = 0    #横方向の移動のための変数（着地したら0になる）
        self.vy = 0    #上方向にどのくらいいけるかを溜める溜めに使う変数

        self.jump_power = 0
        self.speed_y = 0
    
    def blit(self, scr :Screen):
        return scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr :Screen):
        global sky

        key_lst = pg.key.get_pressed()
        if sky == 0:
            if key_lst[pg.K_LEFT]:
                self.rct.move_ip(-1, 0)
            if key_lst[pg.K_RIGHT]:
                self.rct.move_ip(+1, 0)
        self.blit(scr)
        self.wall_bound()   
        sky = 0    
        if self.speed_y < 2:
            self.speed_y += 0.02
        self.rct.centery += self.speed_y
        pg.draw.rect(scr.sfc, (255, 0, 0), (self.rct.right, self.rct.centery, 20, 63))
        pg.draw.rect(scr.sfc, (255, 255, 255), (self.rct.right, self.rct.centery, 20, 63-self.jump_power*-10))


    def wall_bound(self):
        if self.rct.left < 0:
            self.rct.left = 0
        if self.rct.right > 600:
            self.rct.right = 600

    def jump(self, event):
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_SPACE]:
            #スピード制限
            if self.jump_power > -6:
                self.jump_power -= 0.3
          
                
        #spacekeyを離したら跳ぶ
        if event.type == pg.KEYUP and key_lst[pg.K_SPACE] == False:
            #少しの溜めでは跳ばない
            if self.jump_power > -1 :
                self.jump_power = 0
            else:
                self.speed_y += self.jump_power
                self.jump_power = 0
    
class FootFold:

    def __init__(self, y, scr :Screen):
        self.sfc = pg.Surface((100, 20))
        self.sfc.set_colorkey((0, 0, 0))
        pg.draw.rect(self.sfc,(255, 0, 0),(10, 10, 100, 10))
        self.rct = self.sfc.get_rect()
        self.y = y
        self.rct.centerx = randint(0, scr.rct.width)
        self.rct.centery = self.y

    def blit(self, scr :Screen):
        return scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr :Screen):
        self.rct.move_ip(0, 1)
        if self.rct.bottom > 900:
            self.rct.centerx = randint(0, scr.rct.width)
            self.rct.bottom = 0
        self.blit(scr)

def draw_score(scr, time):
    fonto = pg.font.Font(None, 80)
    score = time // 1000
    txt = fonto.render(f"Score:{score}", True, "BLACK")
    scr.sfc.blit(txt, (10, 10))

def main():
    scr = Screen("飛べ！こうかとん", (600, 800), "ProjExD-1/fig/background.jpg")
    bird = Bird("ProjExD-1/fig/1.png", 2.0, (300, 100))
    foot = FootFold(100, scr)
    foot1 = FootFold(400, scr)
    foot2 = FootFold(700, scr)
    clock = pg.time.Clock()
    starttime = True

    while (1):
        scr.blit(bird)
        if starttime == True:
            first_box = pg.draw.rect(scr.sfc, (255,255,255), (0,780,600,10))
            collide(first_box, bird.rct, bird)

        collide(foot.rct, bird.rct, bird)
        collide(foot1.rct, bird.rct, bird)
        collide(foot2.rct, bird.rct, bird)
        

        bird.update(scr)
        foot.update(scr)
        foot1.update(scr)
        foot2.update(scr)
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            bird.jump(event)
       
        time = pg.time.get_ticks()
        draw_score(scr, time)
        pg.display.update() 
        clock.tick(300)
        if time >= 5000:
            starttime = False
        if bird.rct.top > 900:
            return


if __name__ == "__main__":
    pg.init() # 初期化
    main()
    pg.quit()
    sys.exit()