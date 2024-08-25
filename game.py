import random
from map_builder import MapBuilder
from player import Player

class Game:
    def __init__(self) -> None:
        self.map = MapBuilder().build_map(height=20, width=30)
        self.player = Player()
        self.player.add_position_to_snake((self.map.height//2, self.map.width//2))
        self.food = "🟥"
        self.set_player_initial_position_and_food()

    def place_food_on_map(self):
        """ Place a piece of food in an available position in the map. """
        while True:
            x = random.randint(0, self.map.height-1)
            y = random.randint(0, self.map.width-1)
            if (x, y) not in self.player.snake_coords and "#" not in self.map.coordinates[x][y]:
                self.map.coordinates[x][y] = self.food
                break

    def set_player_initial_position_and_food(self):
        """ 
        We set the initial position for the player. It will
        be placed in the center of the map.
        """
        self.map.coordinates[self.player.snake_coords[0][0]][self.player.snake_coords[0][1]] = self.player.image
        self.place_food_on_map()

    def get_player_new_position(self, direction):
        """ 
        Given a direction, we return the new position for the player.
        """
        if direction == "up":
            return (self.player.snake_coords[0][0]-1, self.player.snake_coords[0][1])
        elif direction == "down":
            return (self.player.snake_coords[0][0]+1, self.player.snake_coords[0][1])
        elif direction == "left":
            return (self.player.snake_coords[0][0], self.player.snake_coords[0][1]-1)
        elif direction == "right":
            return (self.player.snake_coords[0][0], self.player.snake_coords[0][1]+1)
        
    def check_player_status(self, new_coords):
        """ 
        We check if the player is alive or has eaten food.
        """
        if "#" in self.map.coordinates[new_coords[0]][new_coords[1]]:
            self.player.alive = False
        elif self.map.coordinates[new_coords[0]][new_coords[1]] == self.food:
            self.player.eat_food()
            self.place_food_on_map()
        elif new_coords in self.player.snake_coords:
            self.player.alive = False

    def paint_snake(self):
        """ 
        We paint the snake on the map.
        """
        for coord in self.player.snake_coords:
            self.map.coordinates[coord[0]][coord[1]] = self.player.image
        self.map.coordinates[self.player.snake_coords[-1][0]][self.player.snake_coords[-1][1]] = "  "
    
    def move_player(self, direction):
        """ 
        Given a direction, we move the player in that direction.
        """
        new_position = self.get_player_new_position(direction)
        self.check_player_status(new_position)
        if self.player.alive:
            self.player.add_position_to_snake(new_position)
            self.paint_snake()


if __name__ == '__main__':
    game = Game()
    print(game.map)
    