from settings import *
from sys import exit

from game import Game
from score import Score
from preview import Preview

from random import choice

class Main:
    def __init__(self):
        pygame.init()
        self.display_surface=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
        self.clock=pygame.time.Clock()
        pygame.display.set_caption("Tetris Game")

        self.next_shapes=[choice(list(MULTIPLE.keys())) for shape in range(3)]

        self.game=Game(self.get_next_shape, self.update_score)
        self.score=Score()
        self.preview=Preview()

    def update_score(self, lines, score, level):
        self.score.lines=lines
        self.score.score=score
        self.score.level=level



    def get_next_shape(self):
        next_shape=self.next_shapes.pop(0)
        self.next_shapes.append(choice(list(MULTIPLE.keys())))
        return next_shape

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    exit()

            self.display_surface.fill(GRAY)
            self.game.run()
            self.score.run()
            self.preview.run(self.next_shapes)
            pygame.display.update()
            self.clock.tick()

if __name__ == "__main__":
    main=Main()
    main.run()