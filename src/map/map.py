from field import Field, gen_random


class Map:
    def __init__(self, width, height):
        self.__x = 0
        self.__y = 0
        self.state = []
        for i in range(width):
            fields = []
            for j in range(height):
                fields.append(gen_random())
            self.state.append(fields)

    @property
    def map(self):
        return self.state[self.__x][self.__y].print_state()

    @property
    def enemies(self):
        return self.state[self.__x][self.__y].enemies

    def move_forward(self):
        self.__y += 1

    def move_left(self):
        self.__x -= 1

    def move_right(self):
        self.__x += 1

    def move_backward(self):
        self.__y -= 1
