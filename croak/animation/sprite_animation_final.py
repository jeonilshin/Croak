import pygame, sys

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

class Player(pygame.sprite.Sprite):
	def __init__(self, pos_x, pos_y):
		super().__init__()
		self.attack_animation = False
		self.sprites = []
		self.sprites.append(pygame.image.load('attack_1.png'))
		self.sprites.append(pygame.image.load('attack_2.png'))
		self.sprites.append(pygame.image.load('attack_3.png'))
		self.sprites.append(pygame.image.load('attack_4.png'))
		self.sprites.append(pygame.image.load('attack_5.png'))
		self.sprites.append(pygame.image.load('attack_6.png'))
		self.sprites.append(pygame.image.load('attack_7.png'))
		self.sprites.append(pygame.image.load('attack_8.png'))
		self.sprites.append(pygame.image.load('attack_9.png'))
		self.sprites.append(pygame.image.load('attack_10.png'))
		self.current_sprite = 0
		self.image = self.sprites[self.current_sprite]

		self.rect = self.image.get_rect()
		self.rect.topleft = [pos_x,pos_y]

	def attack(self):
		self.attack_animation = True

	def update(self,speed):
		if self.attack_animation == True:
			self.current_sprite += speed
			if int(self.current_sprite) >= len(self.sprites):
				self.current_sprite = 0
				self.attack_animation = False

		self.image = self.sprites[int(self.current_sprite)]

logo = pygame.image.load('logo.png')
pygame.display.set_icon(logo)

# General setup
pygame.init()
clock = pygame.time.Clock()

# Game Screen
screen_width = 280
screen_height = 250
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Croak!")

# Creating the sprites and groups
moving_sprites = pygame.sprite.Group()
player = Player(-60, -40)
moving_sprites.add(player)

# Audio setup
pygame.mixer.init()
audio_path = "croak.mp3"
audio = pygame.mixer.music.load(audio_path)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.attack()
                pygame.mixer.music.play()
                
			# Adjust volume with arrow keys
            elif event.key == pygame.K_UP:
                volume = pygame.mixer.music.get_volume()
                if volume < 1.0:
                    volume += 0.1
                pygame.mixer.music.set_volume(volume)
            elif event.key == pygame.K_DOWN:
                volume = pygame.mixer.music.get_volume()
                if volume > 0.0:
                    volume -= 0.1
                pygame.mixer.music.set_volume(volume)

    # Drawing
    bg = Background('background.png', [0, 0])
    screen.fill([255, 255, 255])
    screen.blit(bg.image, bg.rect)
    moving_sprites.draw(screen)
    moving_sprites.update(0.25)
    pygame.display.flip()
    clock.tick(60)