import pygame as pg
import sys
from random import randint
def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1200, 600))

    tori = pg.image.load("ex04/fig/6.png") #こうかとん作成
    tori = pg.transform.rotozoom(tori, 0, 2.0)
    tori_rect = tori.get_rect()
    tori_rect.center = 900, 400

    background = pg.image.load("ex04/fig/pg_bg.jpg")
    vx, vy = randint(0, 1200), randint(0, 600) #弾の座標
    vx2, vy2 = randint(0, 1200), randint(0, 600)
    vx3, vy3 = randint(0, 1200), randint(0, 600)
    xspeed, yspeed = 1, 1
    xspeed2, yspeed2 = 1, 1
    xspeed3, yspeed3 = 1, 1
    lis_pos = [[vx, vy], [vx2, vy2], [vx3, vy3]] 
    lis_speed = [[xspeed, yspeed], [xspeed2, yspeed2], [xspeed3, yspeed3]]
    maxspeed = 10
    tori_life = 100
    tori_direction = 0 #0右 1左 2上 3下
    
    fonto = pg.font.Font(None, 80)
    txt = fonto.render("LIFE", True, "BLACK")
    
    while True:
        shield_pos = [[(tori_rect.centerx-60, tori_rect.centery-70), (tori_rect.centerx-60, tori_rect.centery+70)],
                  [(tori_rect.centerx+60, tori_rect.centery-70), (tori_rect.centerx+60, tori_rect.centery+70)],
                  [(tori_rect.centerx-70, tori_rect.centery-60), (tori_rect.centerx+70, tori_rect.centery-60)],
                  [(tori_rect.centerx-70, tori_rect.centery+60), (tori_rect.centerx+70, tori_rect.centery+60)]]
        #こうかとんの当たり判定
        tori_circle = pg.draw.circle(screen, (0, 0, 0), (tori_rect.centerx+10, tori_rect.centery), 40)
        screen.blit(background, (0, 0))
        screen.blit(txt, (930, 10))
        screen.blit(tori, tori_rect)
        circle = pg.draw.circle(screen, (255, 0, 0), (lis_pos[0][0], lis_pos[0][1]), 10)
        circle2 = pg.draw.circle(screen, (255, 0, 0), (lis_pos[1][0], lis_pos[1][1]), 10)
        circle3 = pg.draw.circle(screen, (255, 0, 0), (lis_pos[2][0], lis_pos[2][1]), 10)
        lis_circle = [circle, circle2, circle3]
        pg.draw.rect(screen, (0, 255, 0), (1080, 20, tori_life, 30))
        shield = pg.draw.line(screen, (255, 128, 0), shield_pos[tori_direction][0], shield_pos[tori_direction][1], )
        
        for i, j in zip(lis_pos, lis_speed):#iは場所,jはスピード
            i[0] += j[0]
            i[1] += j[1]
            if i[0] < 0 or i[0] > 1200:
                j[0] *= -1
                if j[0] < maxspeed:
                    j[0] *= 1.1
            if  i[1]< 0 or i[1] > 600:
                j[1] *= -1
                if abs(j[1]) < maxspeed:
                    j[1] *= 1.1

        if tori_rect.left < 0:
            tori_rect.left = 0
        if tori_rect.right > 1200:
            tori_rect.right = 1200
        if tori_rect.top < 0:
            tori_rect.top = 0
        if tori_rect.bottom > 600:
            tori_rect.bottom = 600

        for i, j in zip(lis_circle, lis_speed):
            if tori_circle.colliderect(i):
                tori_life -= 1

            if shield.colliderect(i):
                if tori_direction == 0 or tori_direction == 1:
                    j[0] *= -1
                else:
                    j[1] *= -1


        if tori_life == 0:
            return
            
        for event in pg.event.get():
            if event.type == pg.QUIT: return
            # if event.type == pg.KEYDOWN and event.key == pg.K_F1:
            #     screen = pg.display.set_mode((800, 600), pg.FULLSCREEN)
            # if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            #     screen = pg.display.set_mode((800, 600))
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_LEFT]:
            tori_rect.move_ip(-1, 0)
            tori_direction = 0
        if key_lst[pg.K_RIGHT]:
            tori_rect.move_ip(1, 0)
            tori_direction = 1
        if key_lst[pg.K_UP]:
            tori_rect.move_ip(0, -1)
            tori_direction = 2
        if key_lst[pg.K_DOWN]:
            tori_rect.move_ip(0, 1)
            tori_direction = 3
        pg.display.update()
        clock = pg.time.Clock()
        clock.tick(1000)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()