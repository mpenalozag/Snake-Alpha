from collections import deque

class Player:
    def __init__(self) -> None:
        self.image = "🟩"
        self.size = 1
        self.alive = True
        self.snake_coords = deque(maxlen=self.size+1)
    
    def add_position_to_snake(self, position):
        self.snake_coords.appendleft(position)

    def update_snake_size(self):
        old_snake = self.snake_coords
        self.snake_coords = deque(old_snake, maxlen=self.size+1)

    def eat_food(self):
        self.size += 1
        self.update_snake_size()
        


if __name__ == "__main__":
    p = Player()
    p.last_coords = (1, 1)
    print(p.last_coords)
    p.last_coords = (2, 2)
    print(p.last_coords)
