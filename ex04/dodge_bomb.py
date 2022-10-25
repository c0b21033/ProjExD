import pygame as pg
import sys
from random import randint

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1200, 600))
    screen_rct = screen.get_rect()
    w, h = screen_rct.width, screen_rct.height
    tori = pg.image.load("ex04/fig/6.png") #こうかとん作成
    tori = pg.transform.rotozoom(tori, 0, 2.0)
    tori_rect = tori.get_rect()
    tori_rect.center = 900, 400

    background = pg.image.load("ex04/fig/pg_bg.jpg")

    vx, vy = randint(0, w), randint(0, h) #弾の座標１
    vx2, vy2 = randint(0, w), randint(0, h) #弾の座標２
    vx3, vy3 = randint(0, w), randint(0, h) #弾の座標３
    xspeed, yspeed = 1, 1 #１個目の弾のスピード
    xspeed2, yspeed2 = 1, 1 #２個目の弾のスピード
    xspeed3, yspeed3 = 1, 1  #３個目の弾のスピード
    lis_pos = [[vx, vy], [vx2, vy2], [vx3, vy3]] #弾の座標をまとめたリスト
    lis_speed = [[xspeed, yspeed], [xspeed2, yspeed2], [xspeed3, yspeed3]] #弾のスピードをまとめたリスト
    maxspeed = 10 #弾のスピードの最大値
    tori_life = 100 #こうかとんの体力
    tori_direction = 0 #向いている方向0右 1左 2上 3下を表す
    
    fonto = pg.font.Font(None, 80)
    txt = fonto.render("LIFE", True, "BLACK")
    
    while True:
        #それぞれ向いている方向ごとのシールドの描写位置を格納
        shield_pos = [[(tori_rect.centerx-60, tori_rect.centery-70), (tori_rect.centerx-60, tori_rect.centery+70)],
                  [(tori_rect.centerx+60, tori_rect.centery-70), (tori_rect.centerx+60, tori_rect.centery+70)],
                  [(tori_rect.centerx-70, tori_rect.centery-60), (tori_rect.centerx+70, tori_rect.centery-60)],
                  [(tori_rect.centerx-70, tori_rect.centery+60), (tori_rect.centerx+70, tori_rect.centery+60)]]
        
        #こうかとんの当たり判定
        tori_circle = pg.draw.circle(screen, (0, 0, 0), (tori_rect.centerx+10, tori_rect.centery), 40)
        screen.blit(background, (0, 0))
        screen.blit(txt, (930, 10))
        screen.blit(tori, tori_rect)

        #弾３つの描写
        circle = pg.draw.circle(screen, (255, 0, 0), (lis_pos[0][0], lis_pos[0][1]), 10)
        circle2 = pg.draw.circle(screen, (255, 0, 0), (lis_pos[1][0], lis_pos[1][1]), 10)
        circle3 = pg.draw.circle(screen, (255, 0, 0), (lis_pos[2][0], lis_pos[2][1]), 10)

        #弾３つを格納したリスト
        lis_circle = [circle, circle2, circle3]

        #こうかとんのLIFEの四角形を描写
        pg.draw.rect(screen, (0, 255, 0), (1080, 20, tori_life, 30))

        #盾の描写
        shield = pg.draw.line(screen, (255, 128, 0), shield_pos[tori_direction][0], shield_pos[tori_direction][1], )
        
        #３つの弾を動かす
        for i, j in zip(lis_pos, lis_speed):#iは場所[vx, vy],jはスピード[xspeed, yspeed]
            i[0] += j[0]
            i[1] += j[1]
            if i[0] < 0 or i[0] > w:#弾が画面外にでたら(x軸)
                j[0] *= -1
                if j[0] < maxspeed:#スピード制限でなければ
                    j[0] *= 1.1
            if  i[1]< 0 or i[1] > h:#弾が画面外にでたら(y軸)
                j[1] *= -1
                if abs(j[1]) < maxspeed:#スピード制限でなければ
                    j[1] *= 1.1

        #こうかとんが画面外に出ないための処理
        if tori_rect.left < 0:
            tori_rect.left = 0
        if tori_rect.right > w:
            tori_rect.right = w
        if tori_rect.top < 0:
            tori_rect.top = 0
        if tori_rect.bottom > h:
            tori_rect.bottom = h

        for i, j in zip(lis_circle, lis_speed):
            #こうかとんの体力を減らす
            if tori_circle.colliderect(i):
                tori_life -= 1
            #シールドと弾の当たり判定
            if shield.colliderect(i):
                if tori_direction == 0 or tori_direction == 1:#右か左を向いていたら
                    j[0] *= -1 #xspeedを反転
                else:
                    j[1] *= -1

        if tori_life == 0:
            return    
        
        for event in pg.event.get():
            if event.type == pg.QUIT: return
            
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_LEFT]:
            tori_rect.move_ip(-1, 0)
            tori_direction = 0 #向きを右に設定
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