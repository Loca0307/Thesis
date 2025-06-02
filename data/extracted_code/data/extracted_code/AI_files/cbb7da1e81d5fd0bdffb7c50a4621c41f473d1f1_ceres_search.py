    # Helper function to check a word in a given direction
    def check_word(x, y, dx, dy):
        for i in range(4):
            new_x = x + i * dx
            new_y = y + i * dy
            if new_x < 0 or new_x >= rows or new_y < 0 or new_y >= cols or grid[new_x][new_y] != word[i]:
                return False
        return True