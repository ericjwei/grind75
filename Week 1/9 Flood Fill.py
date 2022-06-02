def floodFill(image: list[list[int]], sr: int, sc: int, newColor: int) -> list[list[int]]:
    replace, image[sr][sc] = image[sr][sc], newColor
    image = floodfillHelper(image, sr + 1, sc, newColor, replace)
    image = floodfillHelper(image, sr - 1, sc, newColor, replace)
    image = floodfillHelper(image, sr, sc + 1, newColor, replace)
    image = floodfillHelper(image, sr, sc - 1, newColor, replace)
    return image

def floodfillHelper(image: list[list[int]], sr: int, sc: int, newColor: int, replace: int) -> list[list[int]]:
    if sr >= len(image) or sr < 0 or sc >= len(image[sr]) or sc < 0:
        return image
    if image[sr][sc] == replace:
        image[sr][sc] = newColor
        image = floodfillHelper(image, sr + 1, sc, newColor, replace)
        image = floodfillHelper(image, sr - 1, sc, newColor, replace)
        image = floodfillHelper(image, sr, sc + 1, newColor, replace)
        image = floodfillHelper(image, sr, sc - 1, newColor, replace)
    return image
    
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 2
sc = 2
newColor = 2
image = floodFill(image, sr, sc, newColor)
print(*image)