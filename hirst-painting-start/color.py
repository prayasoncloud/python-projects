import colorgram

colors = colorgram.extract("image.jpg", 30)
rgb_color = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b= color.rgb.b
    new_color = (r, g, b)
    rgb_color.append(new_color)


print(rgb_color)

colo