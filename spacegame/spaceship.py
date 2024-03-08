import sys
import pygame

pygame.init()

screen = pygame.display.set_mode((1280,720))

clock = pygame.time.Clock()
image = pygame.image.load("spacegame/ship.bmp") #이미지 있는 폴더명/이미지 이름
#rect 크기 정보와 좌표 정보를 가지고 있음 > image에 부여?
rect = image.get_rect()

while True: #무한루프
    # Process player inputs.
    #1. 키보드 or 마우스 이벤트 ex) 방향키 입력
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit() # raise SystemExit 보다는

    # 2. Do logical updates here.
    # ...

    screen.fill("purple")  # Fill the display with a solid color

    # 3. Render the graphics here. render = 그리다. 
    # ...
    #rect 사각형으로 인식하고 그 안에 그려넣겠다?
    screen.blit(image, rect) #이미지 표면 픽셀을 스크린 표면에 복사하는 함수 blit

    pygame.display.flip()  # 4. Refresh on-screen display 화면 업데이트
    clock.tick(60)         # 5. wait until next frame (at 60 FPS)