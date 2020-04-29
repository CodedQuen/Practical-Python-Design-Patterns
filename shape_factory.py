import pygame


class Shape(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        raise NotImplementedError()

    def move(self, direction):
        if direction == 'up':
            self.y -= 4
        elif direction == 'down':
            self.y += 4
        elif direction == 'left':
            self.x -= 4
        elif direction == 'right':
            self.x += 4

    @staticmethod
    def factory(shape_type, pos_x, pos_y):
        if shape_type == 'Circle':
            return Circle(pos_x, pos_y)
        if shape_type == 'Square':
            return Square(pos_x, pos_y)
        assert 0, "Bad shape requested:" + type


class Square(Shape):
    def __init__(self, x, y):
        if x < 0:
            x = 0
        elif x > 780:
            x = 780
        if y < 0:
            y = 0
        elif y > 580:
            y = 580
        super(Square, self).__init__(x,y)

    def draw(self):
        pygame.draw.rect(
            screen,
            (255, 255, 0),
            pygame.Rect(self.x, self.y, 20, 20)
        )

    def move(self, direction):
        if direction == 'up' and self.y > 0:
            super(Square, self).move('up')
        elif direction == 'down' and self.y < 580:
            super(Square, self).move('down')
        elif direction == 'left' and self.x > 0:
            super(Square, self).move('left')
        elif direction == 'right' and self.x < 780:
            super(Square, self).move('right')


class Circle(Shape):
    def __init__(self, x, y):
        if x < 10:
            x = 10
        elif x > 790:
            x = 790
        if y < 10:
            y = 10
        elif y > 590:
            y = 590
        super(Circle, self).__init__(x, y)

    def draw(self):
        pygame.draw.circle(
            screen,
            (0, 255, 255),
            (self.x, self.y),
            10
        )

    def move(self, direction):
        if direction == 'up' and self.y > 10:
            super(Circle, self).move('up')
        elif direction == 'down' and self.y < 590:
            super(Circle, self).move('down')
        elif direction == 'left' and self.x > 10:
            super(Circle, self).move('left')
        elif direction == 'right' and self.x < 790:
            super(Circle, self).move('right')

if __name__ == '__main__':
    window_dimensions = 800, 600
    screen = pygame.display.set_mode(window_dimensions)

    obj = Shape.factory('Square', 100, 100)

    player_quits = False

    while not player_quits:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                player_quits = True

            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_c]:
                obj = Shape.factory('Circle', obj.x, obj.y)
            if pressed[pygame.K_s]:
                obj = Shape.factory('Square', obj.x, obj.y)
            if pressed[pygame.K_UP]:
                obj.move('up')
            if pressed[pygame.K_DOWN]:
                obj.move('down')
            if pressed[pygame.K_LEFT]:
                obj.move('left')
            if pressed[pygame.K_RIGHT]:
                obj.move('right')

            screen.fill((0, 0, 0))
            obj.draw()
        pygame.display.flip()
