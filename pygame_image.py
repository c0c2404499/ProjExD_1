import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg") #背景画像を挿入
    bg_img2 = pg.transform.flip(bg_img, True, False) #反転
    kokaton_img = pg.image.load("fig/3.png")
    kokaton_img = pg.transform.flip(kokaton_img, True, False)
    kokaton_rect = kokaton_img.get_rect() #rectを取得
    kokaton_rect.center = 300, 200 #中心座標を設定
    
    
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_lst = pg.key.get_pressed() #キーの押下状態のリストを取得
        if key_lst[pg.K_UP]: #上矢印キーが押されたとき
            hor = -1
            ver = -1
            #kokaton_rect.move_ip((0, -1)) #横に0、縦に―1移動させる
        elif key_lst[pg.K_DOWN]:
            hor = -1
            ver = 1
            #kokaton_rect.move_ip(0, +1)
        elif key_lst[pg.K_RIGHT]:
            hor = 2
            ver = 0 
            #kokaton_rect.move_ip(+1, 0)
        else:
            hor = -2
            ver = 0
            #kokaton_rect.move_ip(-1, 0) #演習課題1
        
        kokaton_rect.move_ip(hor, ver)

        x = tmr % 3200
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img2, [-x + 1600, 0])
        screen.blit(bg_img, [-x + 3200, 0])
        screen.blit(kokaton_img, kokaton_rect) #画像をrectに従って貼り付け
        pg.display.update()
        tmr += 1
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()