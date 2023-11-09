from noise import pnoise2

class Terrain:
    def __init__(self, width, height):
        self.terrain = self.generate_terrain(width, height)

    def generate_terrain(self, width, height, scale=0.1):
        terrain = []
        for y in range(height):
            row = []
            for x in range(width):
                noise_value = pnoise2(x * scale, y * scale)
                if noise_value < -0.05:
                    tile = 'water'
                elif -0.05 <= noise_value < 0.2:
                    tile = 'sand'
                elif 0.2 <= noise_value < 0.4:
                    tile = 'grass'
                elif 0.4 <= noise_value < 0.6:
                    tile = 'forest'
                else:
                    tile = 'mountains'
                row.append(tile)
            terrain.append(row)
        return terrain
