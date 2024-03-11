import sys
import pygame
import setting

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((setting.WIDTH, setting.HEIGHT))
image = pygame.image.load(setting.SHIP_IMAGE_PATH) #이미지 있는 폴더명/이미지 이름
#rect 크기 정보와 좌표 정보를 가지고 있음 > image에 부여?

# rect = image.get_rect()

#rect 위치 옮기기
ship_rect = image.get_rect()
screen_rect = screen.get_rect()
ship_rect.midbottom = screen_rect.midbottom

#총알 만들기
def create_bullet(ship_rect):
    bullet = pygame.Rect(0, 0, 5, 50)
    bullet.midtop = ship_rect.midtop
    return bullet

bullets = []
# bullet = create_bullet(ship_rect)
bullets.append(create_bullet(ship_rect))

# bullet = create_bullet(ship_rect)

while True: #무한루프
    # Process player inputs.
    #1. 키보드 or 마우스 이벤트 ex) 방향키 입력
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit() # raise SystemExit 보다는
            
            #방향키 입력 시 움직이게 하기
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship_rect.right += setting.SHIP_SPEED
            elif event.key == pygame.K_LEFT:
                ship_rect.left -= setting.SHIP_SPEED
            elif event.key == pygame.K_UP:
                ship_rect.top -= setting.SHIP_SPEED    
            elif event.key == pygame.K_DOWN:
                ship_rect.top += setting.SHIP_SPEED
            elif event.key == pygame.K_SPACE:
                b = create_bullet(ship_rect)
                bullets.append(b)

    # 2. Do logical updates here.
    # ...
    new_bullet = []
    for bullet in bullets:
        if screen_rect.top < bullet.top:
            bullet.top -= 1
            new_bullet.append(bullet)       

    screen.fill("purple")  # Fill the display with a solid color

    # 3. Render the graphics here. render = 그리다. 
    # ...
    #rect 사각형으로 인식하고 그 안에 그려넣겠다?
    # screen.blit(image, rect)
    screen.blit(image, ship_rect) #이미지 표면 픽셀을 스크린 표면에 복사하는 함수 blit
    for bullet in bullets:
        pygame.draw.rect(screen, setting.BULLET_COLOR, bullet)

    pygame.display.flip()  # 4. Refresh on-screen display 화면 업데이트
    clock.tick(setting.FPS)         # 5. wait until next frame (at 60 FPS)