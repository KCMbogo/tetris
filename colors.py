"""This is a file that contains all the colors that
will be used in the game for the various blocks

Returns:
    list: returns a list of colors in a class level
"""

class Colors:
    dark_grey = (26, 31, 40) # no block
    green = (47, 230, 23) # L-block
    red = (232, 18, 18) # J-block
    orange = (226, 116, 17)
    yellow = (237, 234, 4)
    purple = (166, 0, 247)
    cyan = (21, 204, 209)
    blue = (13, 64, 216)
    white = (255, 255, 255)
    dark_blue = (44, 44, 127)
    light_blue = (59, 85, 162)
    
    @classmethod
    def get_cell_colors(cls):
        return [cls.dark_grey, cls.green, cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.blue]
