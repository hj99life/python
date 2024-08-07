# pip install pygame
import random
import pygame

####################################################################################
#### 기본 초기화 
pygame.init() #초기화 (반드시 필요)

# 화면 크기 설정 
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기 
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정 
pygame.display.set_caption("QUIZ") #게임 이름 

#FPS
clock = pygame.time.Clock()

####################################################################################
# 1. 사용자 게임 초기화 ( 배경화면, 게임 이미지, 좌표, 속도, 폰트 등)

#배경 만들기
background = pygame.image.load(".//python2//pygame_basic//background.png")

# 캐릭터 만들기 
character = pygame.image.load(".//python2//pygame_basic//character.png")
character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0] # 가로 크기
character_height = character_size[1] # 세로 크기
character_x_pos = screen_width / 2 - character_width / 2 # 화면 가로의 절반 크기에 해당하는 곳에 위치 
character_y_pos = screen_height - character_height # 화면 세로 크기 가장 아래

# 이동할 좌표 
to_x = 0

# 이동 속도 
character_speed = 5


# 똥 만들기 
ddong = pygame.image.load(".//python2//pygame_basic//enemy.png")
ddong_size = ddong.get_rect().size # 이미지의 크기를 구해옴
ddong_width = ddong_size[0] # 가로 크기
ddong_height = ddong_size[1] # 세로 크기
ddong_x_pos = random.randint(0, screen_width - ddong_width)
ddong_y_pos = 0
ddong_speed = 5

running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(60) # 게임화면의 초당 프레임 수를 설정 
    
    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False 
            
        if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:
                to_x -= character_speed 
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed 
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0    
            
    # 3. 게임 캐릭터 위치 정의 
    character_x_pos += to_x 
    
    if character_x_pos < 0:
        character_x_pos = 0 
    elif character_x_pos > screen_width - character_width: 
        character_x_pos = screen_width - character_width 
    
    ddong_y_pos += ddong_speed 
    
    if ddong_y_pos > screen_height:
        ddong_y_pos = 0 
        ddong_x_pos = random.randint(0, screen_width - ddong_width)
        
    
    # 4. 충돌 처리    
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
    
    ddong_rect = ddong.get_rect()
    ddong_rect.left = ddong_x_pos
    ddong_rect.top = ddong_y_pos
    
    if character_rect.colliderect(ddong_rect):
        print("충돌했어요")
        running = False
        
        
    # 5. 화면에 그리기 
    screen.blit(background, (0, 0))
    
    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기 
    
    screen.blit(ddong, (ddong_x_pos, ddong_y_pos))
     
    pygame.display.update() # 게임 화면을 다시 그리기!
 
# pygame 종료
pygame.quit()