import pygame# ІМПОРТУЄМ ПАЙГЕЙМ
import math# ДОДАТКОВА БІБЛІОТЕКА
import random
import time
pygame.init()
walk_Up = True
walk_Down = True
walk_Right = True
walk_Left = True
size_player = (90, 90)
r = 0
s = 0
stop = 1
W, H = 1148, 644
D, P = 1148, 644
back = (255, 255, 255)
sc = pygame.display.set_mode((1280, 660))
pygame.display.set_caption("Boxes in one")
clock = pygame.time.Clock()
FPS = 40
center = (W//2, H//2)
marker2 = 0
playerX = -125
playerY = 200
mouse2 = (-1000, -1000)
mouse1 = (200, 500)
center_area = (574, 322)
right_angle_x = 1230
right_angle_y = 10
health_player = 5
marker3 = 0
function_time = False
table_time = False
istouch = False
animation_npc = False
stand_npc = False
dog_animation_walk = False
word_time = False
heart_double = True
stand_dog = True
inventory_time = False
box_game = True
game = False
settings_gol = False
key_blit = True
door_close = False
door_open = False
key_blit_inventory = False
message_game = True
player_time = True
count_animation_dog = -1
i = 0
count = 0
dog_speed = 10
count_start_npc = -1
speed = 6
marker = 0
message_count = 1
count_box = 1
win = random.randint(1, 3)
player_anim_count = 0

def start_words():
    global text
    font = pygame.font.SysFont('arial', 75)
    text = font.render('Том 1: Початок', 1, (0, 0, 0))


start_words()

def fences():
    global fence
    fence = pygame.transform.scale(pygame.image.load("images/fence.png"), (38, 250))
    global capth
    capth = pygame.transform.scale(pygame.image.load("images/fence.png"), (38, 250))

fences()
def playerr():
    global player_surf
    player_surf = pygame.image.load("images/player_up1.gif")
    global player_rect
    player_rect = player_surf.get_rect(center=(600, 190))
    player_surf = pygame.transform.scale(player_surf, (80, 80))


playerr()
def qvest():
    global table
    table = pygame.transform.scale(pygame.image.load("images/qvest.png"), (300, 100))
    global tree
    tree = pygame.transform.scale(pygame.image.load("images/trees.png"), (500, 500))



qvest()
def Area():
    global bg_surf
    bg_surf = pygame.image.load("images/polop.png").convert_alpha()
    bg_surf = pygame.transform.scale(bg_surf, (1000, 800))

Area()
def bullets():
    global bullet_surf
    bullet_surf = pygame.image.load("images/bullet #1.png").convert_alpha()
    bullet_surf = pygame.transform.scale(bullet_surf, (80, 60))
    bullet_rect = bullet_surf.get_rect(center=(0, 0))

bullets()
def hearts():
    global heart
    heart = pygame.image.load("images/heart.png"). convert_alpha()
    heart = pygame.transform.scale(heart, (43, 38.6))

hearts()
def menu():
    global start_menu
    start_menu = pygame.transform.scale(pygame.image.load("images/Знімок_екрана_2023-07-03_223128-removebg-preview.png"), (500, 200))

menu()
def inventory():
    global big_inventory
    big_inventory = pygame.transform.scale(pygame.image.load("images/inventory.jpg"), (550, 450))
    global small_inventory
    small_inventory = pygame.transform.scale(pygame.image.load("images/Small_inventory-removebg-preview.png").convert_alpha(), (70, 70))
inventory()
def boxes():
    global box1
    global box2
    global box3
    box1 = pygame.transform.scale(pygame.image.load("images/box.gif"), (60, 60))
    box2 = pygame.transform.scale(pygame.image.load("images/box.gif"), (60, 60))
    box3 = pygame.transform.scale(pygame.image.load("images/box.gif"), (60, 60))
    global rectangle
    rectangle = pygame.transform.scale(pygame.image.load("images/rectangle.png"), (60, 60))
    global key
    key = pygame.transform.scale(pygame.image.load("images/key.png"), (70, 70))


boxes()
def zombi_all():
    zombi  = pygame.image.load("images/0.gif")
    zombi_walk = [
        pygame.image.load("images/0.gif"),

        pygame.image.load("images/2.gif"),
        pygame.image.load("images/3.gif"),
        pygame.image.load("images/4.gif"),
        pygame.image.load("images/5.gif"),
        pygame.image.load("images/6.gif"),
        pygame.image.load("images/7.gif")
    ]

zombi_all()
def NPC():
    global start_npc
    start_npc = pygame.image.load("images/npc2.png").convert_alpha()
    start_npc = pygame.transform.scale(start_npc, (60, 80))
    global animation_start_npc
    animation_start_npc = [
        pygame.image.load("images/step_1npc.png"),
        pygame.image.load("images/step_2npc.png"),
        pygame.image.load("images/npc2.png")
    ]


NPC()
def dog_sharik():
    global dog
    dog = pygame.transform.scale(pygame.image.load("images/ziqpjxgukth21 (1).png"), (80, 68))
    global dog_house
    dog_house = pygame.transform.scale(pygame.image.load("images/dog house.jpg"), (113, 87))
    global true_animation_dog
    true_animation_dog = [
        pygame.image.load("images/ziqpjxgukth21 (2).png"),
        pygame.image.load("images/ziqpjxgukth21 (3).png"),
        pygame.image.load("images/ziqpjxgukth21 (2).png"),
        pygame.image.load("images/ziqpjxgukth21 (3).png"),
        pygame.image.load("images/ziqpjxgukth21 (2).png"),
        pygame.image.load("images/ziqpjxgukth21 (3).png"),
        pygame.image.load("images/ziqpjxgukth21 (2).png"),
        pygame.image.load("images/ziqpjxgukth21 (3).png"),
        pygame.image.load("images/ziqpjxgukth21 (2).png"),
        pygame.image.load("images/ziqpjxgukth21 (3).png"),
        pygame.image.load("images/ziqpjxgukth21 (2).png"),
        pygame.image.load("images/ziqpjxgukth21 (3).png"),
        pygame.image.load("images/ziqpjxgukth21 (2).png"),
        pygame.image.load("images/ziqpjxgukth21 (3).png"),
        pygame.image.load("images/ziqpjxgukth21 (2).png"),
        pygame.image.load("images/ziqpjxgukth21 (3).png"),
        pygame.image.load("images/ziqpjxgukth21 (2).png"),
        pygame.image.load("images/ziqpjxgukth21 (3).png"),
        pygame.image.load("images/ziqpjxgukth21 (1).png"),
        pygame.image.load("images/ziqpjxgukth21 (1).png")
    ]
    global reverse_animation_dog
    reverse_animation_dog = [
        pygame.image.load("images/dog 1.png"),
        pygame.image.load("images/dog 2.png"),
        pygame.image.load("images/dog 1.png"),
        pygame.image.load("images/dog 2.png"),
        pygame.image.load("images/dog 1.png"),
        pygame.image.load("images/dog 2.png"),
        pygame.image.load("images/dog 1.png"),
        pygame.image.load("images/dog 2.png"),
        pygame.image.load("images/dog 1.png"),
        pygame.image.load("images/dog 2.png"),
        pygame.image.load("images/dog 1.png"),
        pygame.image.load("images/dog 2.png"),
        pygame.image.load("images/dog 1.png"),
        pygame.image.load("images/dog 2.png"),
        pygame.image.load("images/dog 1.png"),
        pygame.image.load("images/dog 2.png"),
        pygame.image.load("images/dog 1.png"),
        pygame.image.load("images/dog.png"),
        pygame.image.load("images/dog.png")
    ]

dog_sharik()
def right_and_left():
    global player_up
    player_up = [
        pygame.transform.scale(pygame.image.load("images/player_up1.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_up1.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_up1.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_up1.gif"), (size_player)),

        pygame.transform.scale(pygame.image.load("images/player_up2.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_up2.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_up2.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_up2.gif"), (size_player)),

        pygame.transform.scale(pygame.image.load("images/player_up3.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_up3.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_up3.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_up3.gif"), (size_player)),

        pygame.transform.scale(pygame.image.load("images/player_up4.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_up4.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_up4.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_up4.gif"), (size_player)),

        pygame.transform.scale(pygame.image.load("images/player_up5.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_up5.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_up5.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_up5.gif"), (size_player)),

        pygame.transform.scale(pygame.image.load("images/player_up6.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_up6.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_up6.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_up6.gif"), (size_player)),

        pygame.transform.scale(pygame.image.load("images/player_up7.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_up7.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_up7.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_up7.gif"), (size_player)),
    ]
    global player_down
    player_down = [
        pygame.transform.scale(pygame.image.load("images/player_down1.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_down1.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_down1.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_down1.gif"), (size_player)),

        pygame.transform.scale(pygame.image.load("images/player_down2.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_down2.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_down2.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_down2.gif"), (size_player)),

        pygame.transform.scale(pygame.image.load("images/player_down3.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_down3.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_down3.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_down3.gif"), (size_player)),

        pygame.transform.scale(pygame.image.load("images/player_down4.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_down4.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_down4.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_down4.gif"), (size_player)),

        pygame.transform.scale(pygame.image.load("images/player_down5.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_down5.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_down5.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_down5.gif"), (size_player)),

        pygame.transform.scale(pygame.image.load("images/player_down6.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_down6.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_down6.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_down6.gif"), (size_player)),

        pygame.transform.scale(pygame.image.load("images/player_down7.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_down7.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_down7.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_down7.gif"), (size_player)),
    ]

    global player_left
    player_left = [
        pygame.transform.scale(pygame.image.load("images/player_left1.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_left1.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_left1.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_left1.gif"), (size_player)),

        pygame.transform.scale(pygame.image.load("images/player_left2.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_left2.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_left2.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_left2.gif"), (size_player)),

        pygame.transform.scale(pygame.image.load("images/player_left3.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_left3.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_left3.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_left3.gif"), (size_player)),

        pygame.transform.scale(pygame.image.load("images/player_left4.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_left4.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_left4.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_left4.gif"), (size_player)),

        pygame.transform.scale(pygame.image.load("images/player_left5.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_left5.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_left5.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_left5.gif"), (size_player)),

        pygame.transform.scale(pygame.image.load("images/player_left6.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_left6.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_left6.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_left6.gif"), (size_player)),

        pygame.transform.scale(pygame.image.load("images/player_left7.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_left7.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_left7.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_left7.gif"), (size_player))
    ]
    global player_right
    player_right = [
        pygame.transform.scale(pygame.image.load("images/player_right1.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_right1.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_right1.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_right1.gif"), (size_player)),

        pygame.transform.scale(pygame.image.load("images/player_right2.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_right2.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_right2.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_right2.gif"), (size_player)),

        pygame.transform.scale(pygame.image.load("images/player_right3.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_right3.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_right3.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_right3.gif"), (size_player)),

        pygame.transform.scale(pygame.image.load("images/player_right4.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_right4.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_right4.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_right4.gif"), (size_player)),

        pygame.transform.scale(pygame.image.load("images/player_right5.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_right5.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_right5.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_right5.gif"), (size_player)),

        pygame.transform.scale(pygame.image.load("images/player_right6.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_right6.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_right6.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_right6.gif"), (size_player)),

        pygame.transform.scale(pygame.image.load("images/player_right7.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_right7.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_right7.gif"), (size_player)),
        pygame.transform.scale(pygame.image.load("images/player_right7.gif"), (size_player)),
    ]
    global player_down_clone
    player_down_clone = pygame.transform.scale(pygame.image.load("images/player_down4.gif"), (size_player))
    global player_up_clone
    player_up_clone = pygame.transform.scale(pygame.image.load("images/player_up1.gif"), (size_player))
    global player_left_clone
    player_left_clone = pygame.transform.scale(pygame.image.load("images/player_left4.gif"), (size_player))
    global player_right_clone
    player_right_clone = pygame.transform.scale(pygame.image.load("images/player_right4.gif"), (size_player))
    global player
    player = player_up_clone

right_and_left()
def Doors():
    global door
    door = pygame.transform.scale(pygame.image.load("images/door.jpg"), (100, 150))
    global door2
    door2 = pygame.transform.scale(pygame.image.load("images/door2.jpg"), (100, 150))

Doors()
class Button_icon:
    def __init__(self, screen, pos=(0, 0), scale=(100, 100), rot=0, image="", image2="", image3="", image4="", image5=""):
        self.screen = screen
        self.pos = pos
        self.scale = scale
        self.image_npc = pygame.transform.scale(pygame.image.load("images/npc2.png"), (150, 200))
        self.rotate = rot
        self.image = pygame.image.load(image)
        self.image2 = pygame.image.load(image2)
        self.image3 = pygame.image.load(image3)
        self.image4 = pygame.image.load(image4)
        self.image5 = pygame.image.load(image5)
        self.message_count = 1

    def messaging_1(self):
        self.message1 = pygame.transform.scale(self.image, self.scale)
        self.message2 = pygame.transform.scale(self.image2, self.scale)
        self.message3 = pygame.transform.scale(self.image3, self.scale)
        self.message4 = pygame.transform.scale(self.image4, self.scale)
        self.message5 = pygame.transform.scale(self.image5, self.scale)

        if self.message_count == 1:
            self.screen.blit(self.message1, (300, 530))
            self.screen.blit(self.image_npc, (150, 530))
        if self.message_count == 2:
            self.screen.blit(self.message2, (300, 530))
            self.screen.blit(self.image_npc, (150, 530))
        if self.message_count == 3:
            self.screen.blit(self.message3, (300, 530))
            self.screen.blit(self.image_npc, (150, 530))
        if self.message_count == 4:
            self.screen.blit(self.message4, (300, 530))
            self.screen.blit(self.image_npc, (150, 530))
        if self.message_count == 5:
            self.screen.blit(self.message5, (300, 530))
            self.screen.blit(self.image_npc, (150, 530))
    def messaging_2(self):
        self.message6 = pygame.transform.scale(self.image, self.scale)
        self.message7 = pygame.transform.scale(self.image2, self.scale)
        self.message8 = pygame.transform.scale(self.image3, self.scale)
        self.message9 = pygame.transform.scale(self.image4, self.scale)
        self.message10 = pygame.transform.scale(self.image5, self.scale)
        if self.message_count == 6:
            self.screen.blit(self.message6, (300, 530))
            self.screen.blit(self.image_npc, (150, 530))
        if self.message_count == 7:
            self.screen.blit(self.message7, (300, 530))
            self.screen.blit(self.image_npc, (150, 530))
    def message_count_dodavannya(self):
        self.message_count += 1
    def message_count_vidnimannya(self):
        self.message_count -= 1
    def message_count_6(self):
        self.message_count = 6

message_all = Button_icon(sc, image="images/message 1.jpg", image2="images/message 2.jpg", image3="images/message 3.jpg", image4="images/message 4.jpg", image5="images/message 5.jpg", scale=(795.2, 288), pos=(300, 530))
message_all_2 = Button_icon(sc, image="images/message 6.jpg", image2="images/message 7.jpg", image3="images/message 8.jpg", image4="images/message 9.jpg", image5="images/message 10.jpg", scale=(795.2, 288), pos=(300, 530))
animation_dog = true_animation_dog
key_rect = key.get_rect(center=(-playerX + 370, -playerY + 180))
door_rect = door.get_rect(center=(-playerX + 370, -playerY + 180))

while 1:

    sc.fill(back)
    sc.blit(bg_surf, (-playerX, -playerY))
    if function_time:
        if message_game:
             pygame.draw.circle(sc, (65, 65, 65), mouse1, 100)
             pygame.draw.circle(sc, (255, 255, 255), mouse1, 95)
             pygame.draw.circle(sc, (65, 65, 65), mouse1, 50)
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sc = pygame.display.set_mode((1280, 660), pygame.FULLSCREEN)
            if event.key == pygame.K_F1:
                sc = pygame.display.set_mode((1280, 660))
            if event.key == pygame.K_RIGHT:
                if message_game == False:
                    message_all.message_count_dodavannya()
                    message_all_2.message_count_dodavannya()
                    message_count += 1
                if game:
                    count_box += 1
            if event.key == pygame.K_LEFT:
                if message_game == False:
                    message_all.message_count_vidnimannya()
                    message_all_2.message_count_vidnimannya()
                    message_count -= 1
                if game:
                    count_box -= 1
            if event.key == pygame.K_SPACE:
                if game:
                    box_game = False
                    if count_box != win:
                        dog_animation_walk = True
                        animation_dog == true_animation_dog
                        marker2 = 0
                        gamepad = False
                        player_time = False
                    if count_box == win:
                        dog_animation_walk = False
                        marker2 = 5


            if event.key == pygame.K_e:
                if inventory_time == False:
                    inventory_time = True
                elif inventory_time:
                    inventory_time = False
                    player_time = True

            if event.key == pygame.K_0:
                if function_time == False:
                    function_time = True
                elif function_time:
                    function_time = False
        pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            if function_time:
                if message_game:
                      istouch = True
            i += 1
            mouse2 = mouse
        elif event.type == pygame.MOUSEBUTTONUP:
            istouch = False
    if istouch:
        player = player_up
        sc.fill(back)
        sc.blit(bg_surf, (-playerX, -playerY))
        pygame.draw.circle(sc, (65, 65, 65), mouse2, 100)
        pygame.draw.circle(sc, (255, 255, 255), mouse2, 95)
        cur_mouse = mouse[0] - mouse2[0], mouse[1] - mouse2[1]
        angler = math.atan2(cur_mouse[0], cur_mouse[1])
        distance = math.sqrt(pow(cur_mouse[0], 2) + pow(cur_mouse[1], 2))
        joy_pos = mouse2
        if distance > 80:
            si = math.sin(angler)
            co = math.cos(angler)
            joy_pos = (math.degrees(si) * 1.4 + mouse2[0], math.degrees(co) * 1.4 + mouse2[1])
            distance = 90
        else:
            joy_pos = mouse
        pygame.draw.circle(sc, (65, 65, 65), joy_pos, 50)
        playerX += math.sin(angler) * distance / 20
        playerY += math.cos(angler) * distance / 20
    if heart_double:
        if health_player == 5:
            sc.blit(heart, (right_angle_x, right_angle_y))
            sc.blit(heart, (right_angle_x - 40, right_angle_y))
            sc.blit(heart, (right_angle_x - 80, right_angle_y))
            sc.blit(heart, (right_angle_x - 120, right_angle_y))
            sc.blit(heart, (right_angle_x - 160, right_angle_y))
        if health_player == 4:
            sc.blit(heart, (right_angle_x, right_angle_y))
            sc.blit(heart, (right_angle_x - 40, right_angle_y))
            sc.blit(heart, (right_angle_x - 80, right_angle_y))
            sc.blit(heart, (right_angle_x - 120, right_angle_y))
        if health_player == 3:
            sc.blit(heart, (right_angle_x, right_angle_y))
            sc.blit(heart, (right_angle_x - 40, right_angle_y))
            sc.blit(heart, (right_angle_x - 80, right_angle_y))
        if health_player == 2:
            sc.blit(heart, (right_angle_x, right_angle_y))
            sc.blit(heart, (right_angle_x - 40, right_angle_y))
        if health_player == 1:
            sc.blit(heart, (right_angle_x, right_angle_y))
    if player_rect.collidepoint(key_rect.center):
        key_blit = False
        key_blit_inventory = True
    if player_rect.collidepoint(door_rect.center):
        door_open = True
        door_close = False
    bt = pygame.key.get_pressed()


    if playerX < -575:
        walk_Left = False
    if playerX > 325:
        walk_Right = False
    if playerY < -370:
        walk_Up = False
    if playerY > 365:
        walk_Down = False
    if playerY < -68 and marker == 0:
        stand_npc = True
    else:
        stand_npc = False
    sc.blit(dog_house, (-playerX + 20, -playerY + 250))
    if door_close:
        sc.blit(door, (-playerX + 430, -playerY + -50))
    if door_open:
        sc.blit(door2, (-playerX + 430, -playerY + -50))
    sc.blit(start_npc, (-playerX + 450, -playerY + 80))
    if box_game == False:
        if key_blit:
            if win == 1:
                sc.blit(key, (-playerX + 370, -playerY + 180))
                key_rect = key.get_rect(center=(-playerX + 370, -playerY + 180))
            if win == 2:
                sc.blit(key, (-playerX + 460, -playerY + 180))
                key_rect = key.get_rect(center=(-playerX + 460, -playerY + 180))
            if win == 3:
                sc.blit(key, (-playerX + 530, -playerY + 180))
                key_rect = key.get_rect(center=(-playerX + 530, -playerY + 180))
    if box_game:
        sc.blit(box1, (-playerX + 450, -playerY + 180))
        if count_box == 1:
            sc.blit(rectangle, (-playerX + 370, -playerY + 180))
        if count_box == 2:
            sc.blit(rectangle, (-playerX + 450, -playerY + 180))
        if count_box == 3:
            sc.blit(rectangle, (-playerX + 530, -playerY + 180))
        sc.blit(box2, (-playerX + 370, -playerY + 180))
        sc.blit(box3, (-playerX + 530, -playerY + 180))
        if stand_npc:
            message_all.messaging_1()
            gamepad = False
            game = False
            heart_double = False
            message_game = False
            player_time = False
            if message_count >= 6:
                game = True
                heart_double = True

    if game:
        if count_box > 3:
            count_box = 3
        if count_box < 1:
            count_box = 1
    if dog_animation_walk:
        clock.tick(dog_speed)
        if animation_dog == reverse_animation_dog:
            if count_animation_dog > -1:
                count_animation_dog -= 1
                stand_dog = False
                if count_animation_dog == 0:
                    box_game = True
                    dog_animation_walk = False
        if animation_dog == true_animation_dog:
            if count_animation_dog < 19:
                count_animation_dog += 1

        dog = pygame.transform.scale(animation_dog[count_animation_dog], (60, 60))
        if count_animation_dog == 0:
            sc.blit(dog, (-playerX + 116, -playerY + 290))

        elif count_animation_dog == 1:
            sc.blit(dog, (-playerX + 132, -playerY + 290))

        elif count_animation_dog == 2:
            sc.blit(dog, (-playerX + 148, -playerY + 290))

        elif count_animation_dog == 3:
            sc.blit(dog, (-playerX + 164, -playerY + 290))

        elif count_animation_dog == 4:
            sc.blit(dog, (-playerX + 180, -playerY + 290))

        elif count_animation_dog == 5:
            sc.blit(dog, (-playerX + 196, -playerY + 290))

        elif count_animation_dog == 6:
            sc.blit(dog, (-playerX + 212, -playerY + 290))

        elif count_animation_dog == 7:
            sc.blit(dog, (-playerX + 228, -playerY + 290))

        elif count_animation_dog == 8:
            sc.blit(dog, (-playerX + 244, -playerY + 290))

        elif count_animation_dog == 9:
            sc.blit(dog, (-playerX + 260, -playerY + 290))

        elif count_animation_dog == 10:
            sc.blit(dog, (-playerX + 276, -playerY + 290))

        elif count_animation_dog == 11:
            sc.blit(dog, (-playerX + 292, -playerY + 290))

        elif count_animation_dog == 12:
            sc.blit(dog, (-playerX + 308, -playerY + 290))

        elif count_animation_dog == 13:
            sc.blit(dog, (-playerX + 324, -playerY + 290))

        elif count_animation_dog == 14:
            sc.blit(dog, (-playerX + 340, -playerY + 290))

        elif count_animation_dog == 15:
            sc.blit(dog, (-playerX + 356, -playerY + 290))

        elif count_animation_dog == 16:
            sc.blit(dog, (-playerX + 372, -playerY + 290))

        elif count_animation_dog == 17:
            sc.blit(dog, (-playerX + 388, -playerY + 290))

        elif count_animation_dog == 18:
            sc.blit(dog, (-playerX + 404, -playerY + 290))
            health_player -= 1
            animation_dog = reverse_animation_dog

        elif count_animation_dog == 19:
            sc.blit(dog, (-playerX + 404, -playerY + 290))

        if count_animation_dog == 18:
            marker2 = 1
    if marker2 == 5:
        gamepad = True
        player_time = True

    if marker2 == 1 and stand_dog:
        sc.blit(dog, (-playerX + 404, -playerY + 290))


    sc.blit(small_inventory, (0, 370))
    sc.blit(small_inventory, (0, 300))
    sc.blit(small_inventory, (0, 230))
    sc.blit(small_inventory, (0, 160))

    if key_blit_inventory:
        sc.blit(key, (0, 160))
        message_game = False
        box_game = False
        animation_npc = False
        door_close = True
        marker3 = 1


    if marker3 == 1 and stand_npc:
        if stop == 1:
           message_all_2.message_count_6()
           message_count = 6
           stop = 2
        message_all_2.messaging_2()
        gamepad = False
        game = False
        heart_double = False
        message_game = False
        player_time = False

        if message_count >= 8:
            heart_double = True
            player_time = True
            game = True
            table_time = True
            heart_double = True
            word_time = True
            message_count = 100

    if inventory_time:
        sc.blit(big_inventory, (300, 70))
        player_time = False
    if table_time:
        sc.blit(table, (0, 0))
        sc.blit(tree, (-playerX + 404, -playerY + 400))
    if word_time:
        if stop < 130:
           sc.blit(text, (350, 200))
           stop += 1
    #sc.blit(start_menu, (W//2, H//2))\


    if bt[pygame.K_a] == False and bt[pygame.K_d] == False and bt[pygame.K_w] == False and bt[pygame.K_s] == False:
        sc.blit(player, center)


    if player_time:
        if bt[pygame.K_a]:
            player_left[player_anim_count].set_colorkey((110, 117, 126))
            sc.blit(player_left[player_anim_count], center)
            if player_anim_count == 27:
                player_anim_count = 0
            else:
                player_anim_count += 1
            player = player_left_clone
            if walk_Left:
                playerX -= speed
                walk_Right = True
                walk_Down = True
                walk_Up = True
        elif bt[pygame.K_d]:
            player_right[player_anim_count].set_colorkey((110, 117, 126))
            sc.blit(player_right[player_anim_count], (center))
            if player_anim_count == 27:
                player_anim_count = 0
            else:
                player_anim_count += 1
            player = player_right_clone
            if walk_Right:
               playerX += speed
               walk_Left = True
               walk_Down = True
               walk_Up = True
        elif bt[pygame.K_w]:
            player_up[player_anim_count].set_colorkey((110, 117, 126))
            sc.blit(player_up[player_anim_count], (center))
            if player_anim_count == 27:
                player_anim_count = 0
            else:
                player_anim_count += 1
            player = player_up_clone
            if walk_Up:
               i += 1
               playerY -= speed
               walk_Right = True
               walk_Down = True
               walk_Left = True
        elif bt[pygame.K_s]:
            player_down[player_anim_count].set_colorkey((110, 117, 126))
            sc.blit(player_down[player_anim_count], (center))
            if player_anim_count == 27:
                player_anim_count = 0
            else:
                player_anim_count += 1
            player = player_down_clone
            if walk_Down:
               playerY += speed
               walk_Right = True
               walk_Left = True
               walk_Up = True
        player.set_colorkey((110, 117, 126))

    #sc.blit(fence, (-playerX + 320, -playerY + 535))
    #sc.blit(fence, (-playerX + 600, -playerY + 535))
    #sc.blit(fence, (-playerX + 600, -playerY + 330))
    #sc.blit(fence, (-playerX + 320, -playerY + 330))
    #sc.blit(fence, (-playerX + 320, -playerY + 125))
    #sc.blit(fence, (-playerX + 600, -playerY + 125))





    pygame.display.update()
    clock.tick(FPS)

