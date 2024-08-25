class Map:
    def __init__(self, game_map, height, width) -> None:
        self.coordinates = game_map
        self.height = height
        self.width = width

    def __str__(self) -> str:
        """ Returns the map in a legible way. """
        return "\n".join(["".join(row) for row in self.coordinates])

class MapBuilder:
    def __init__(self) -> None:
        pass

    def build_map_foundation(self, height, width):
        """ Given a height and a width, returns a 2D list of the map,
            with the playable area being height * width. Also, builds 
            an extra layer where the walls will be.
        """
        game_map = [["  " for _ in range(width+1)] for _ in range(height+1)]
        return game_map
    
    def build_walls(self, map_foundation):
        map_foundation[0] = [" #" for _ in range(len(map_foundation[0]))]
        map_foundation[-1] = ["# " for _ in range(len(map_foundation[0]))]
        for row in map_foundation:
            row[0] = "#"
            row[-1] = "#"

    def build_map(self, height=0, width=0):
        """ Given a height and a width, returns a Map object with a playable area
            sorrounded by walls, along with its height and width.
        """
        map_foundation = self.build_map_foundation(height, width)
        self.build_walls(map_foundation)
        return Map(map_foundation, height, width)
    

if __name__ == '__main__':
    map_builder = MapBuilder()
    game_map = map_builder.build_map(height=20, width=30)
    print(game_map)