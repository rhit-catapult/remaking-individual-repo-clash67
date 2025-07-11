import pygame
import sys
import random

from pygame import MOUSEBUTTONDOWN


# You will implement this module ENTIRELY ON YOUR OWN!

# TODO: Create a Ball class.
# TODO: Possible member variables: screen, color, x, y, radius, speed_x, speed_y
# TODO: Methods: __init__, draw, move
class Ball:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.speed_x = random.randint( 2, 7)
        self.speed_y = random.randint(2, 7)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint (0, 255))
        self.hasbounced = False
        self.radius = random.randint(5, 20)
    def move(self):
        self.x = self.x + self.speed_x
        self.y = self.y + self.speed_y
    def bounce(self):
        if self.x - self.radius >= 1000 or self.x + self.radius <= 0:
            self.speed_x = -self.speed_x
            self.hasbounced = True
        self.speed_x = self.speed_x
        if self.y - self.radius >= 1000 or self.y + self.radius <= 0:
            self.speed_y = -self.speed_y
            self.hasbounced = True
        self.speed_y = self.speed_y
        self.newspeed_x = self.speed_x + random.randint(-2, 2)
        self.newspeed_y = self.speed_y + random.randint(-2, 2)
    def velocity(self):
        if self.hasbounced == True:
            self.speed_x = self.newspeed_x
            self.speed_y = self.newspeed_y
            self.hasbounced = False
        else:
            self.speed_x = self.speed_x
            self.speed_y = self.speed_y
    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 1000))
    pygame.display.set_caption('Bouncing Ball')
    screen.fill(pygame.Color('gray'))
    clock = pygame.time.Clock()
    ball1 = Ball(screen, random.randint(30,300),random.randint(25,250))
    balls = []
    # TODO: Create an instance of the Ball class called ball1
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                balls.append(Ball(screen, random.randint(30, 900), random.randint(30, 900)))
            if event.type == pygame.QUIT:
                sys.exit()

        clock.tick(60)
        screen.fill(pygame.Color('gray'))
        ball1.move()
        ball1.draw()
        ball1.bounce()
        ball1.velocity()
        for ball in balls:
            ball.move()
            ball.draw()
            ball.bounce()
            ball.velocity()
        # TODO: Move the ball
        # TODO: Draw the ball

        pygame.display.update()


main()


# Optional challenges (if you finish and want do play a bit more):
#   After you get 1 ball working make a few balls (ball2, ball3, etc) that start in different places.
#   Make each ball a different color
#   Make the screen 1000 x 800 to allow your balls more space (what needs to change?)
#   Make the speed of each ball randomly chosen (1 to 5)
#   After you get that working try making a list of balls to have 100 balls (use a loop)!
#   Use random colors for each ball
