import random as random
import matplotlib.pyplot as plt
import matplotlib.colors 
def placeColors():
    blue = []
    red = []
    grey = []
    for x in range(0,5):
        for y in range(0,5):
            grey.append((x+0.5,y+0.5))

    color = random.randint(0,1)

    for i in range(0,7):
        pos = random.randint(0, len(grey)-1)
        red.append(grey.pop(pos))
        pos = random.randint(0, len(grey)-1)
        blue.append(grey.pop(pos))

    pos = random.randint(0, len(grey)-1)
    if color == 0:
        red.append(grey.pop(pos))
        print('red')
    else:
        blue.append(grey.pop(pos))
        print('blue')

    pos = random.randint(0, len(grey)-1)

    black = grey.pop(pos)

    # plot
    x_grey,y_grey = zip(*grey)
    x_black,y_black = black
    x_blue,y_blue = zip(*blue)
    x_red,y_red = zip(*red)

    plt.scatter(x_grey,y_grey, s = 2400, c ='grey')
    plt.scatter(x_black,y_black, s = 2400, c ='black')
    # plt.scatter(x_blue,y_blue, s = 2400, c ='MediumSeaGreen')
    plt.scatter(x_blue,y_blue, s = 2400, c ='blue')
    #olivedrab MediumSeaGreen
    # plt.scatter(x_red,y_red, s = 2400, c ='Salmon')
    plt.scatter(x_red,y_red, s = 2400, c ='red')
    plt.grid()
    # plt.grid(color='grey', linestyle = '-', linewidth = 0.7)
    plt.xlim(0,5)
    plt.ylim(0,5)
    plt.show()

if __name__ == "__main__":
    placeColors()
