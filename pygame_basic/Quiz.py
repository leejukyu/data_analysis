import random
import pygame
###############################################################
# 기본 초기화 (반드시 해야 하는 것들)
pygame.init() # 초기화(반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("똥 피하기") # 게임이름

# FPS
clock = pygame.time.Clock()
###############################################################

# 1. 사용자 게임 초기화 (배경화면, 게임이미지, 좌표, 폰트 등)

background = pygame.image.load("C:/data_analysis/pygame_basic/background_quiz.png")

character = pygame.image.load("C:/data_analysis/pygame_basic/pet.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width - character_width) / 2
character_y_pos = screen_height - character_height

to_x = 0

character_speed = 10

enemy = pygame.image.load("C:/data_analysis/pygame_basic/dog-poop.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_hieght = enemy_size[1]
enemy_x_pos = random.randint(0, screen_width - enemy_width)
enemy_y_pos = 0
enemy_speed = 10

game_font = pygame.font.Font(None, 40)

total_time = 60

start_ticks = pygame.time.get_ticks()

running = True 
while running:
    dt = clock.tick(30) 

# 2. 이벤트 처리(키보드, 마우스 등)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 

        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_LEFT:
                to_x -= character.speed
            elif event.type == pygame.K_RIGHT:
                to_x += character_speed

        if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    character_x_pos += to_x*dt

# 3. 게임 캐릭터 위치 정의
    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    enemy_y_pos += enemy_speed

    if enemy_y_pos > screen_height:
        enemy_y_pos = 0
        enemy_x_pos = random.randint(0, screen_width - enemy_width)

# 4. 충돌 체크

    # 충돌 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos
    
    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running=False

# 5. 화면에 그리기
    screen.blit(background, (0,0)) # 배경 그리기
    
    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기

    screen.blit(enemy, (enemy_x_pos,enemy_y_pos)) # 적 그리기
    pygame.display.update() 

# pygame 종료
pygame.quit()