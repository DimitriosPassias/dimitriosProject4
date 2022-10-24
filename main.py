#Developer: Dimitrios Passias
#Issues: None
#Instructions: Import a file with the name "nationsPop.txt" in order for it be read and graphed and in the format of countryName,countryPopulation,CountryPercentage

import arcade
axisX = 100
axisY = 100
scale = (800 - 100)/len(range(100, 1500, 100))
currentCountry = 1


#Opens file and reads lines
file = open("nationsPop.txt", "r")
myFile = file.readlines()


#Opens Window
myWindow = arcade.open_window(1820, 800, "Project 4, By: Dimitrios Passias")

#sets background color and starts render
arcade.set_background_color(arcade.color.BEIGE)
arcade.start_render()

#Draws the title
title = arcade.Text("Population of the largest pop Nations on Earth", 600, 780, arcade.color.BLACK)
title.draw()
#X & Y Axis lines
arcade.draw_line(100, 775, 100, 100, arcade.color.BLACK, 5)
arcade.draw_line(100, 100, 1400, 100, arcade.color.BLACK, 5)

currentY = axisY
#Y axis drawing
for i in range(100, 1500, 100):
    currentLabel = arcade.Text(f"{i}M", 25, currentY, arcade.color.BLACK)
    currentLabel.draw()
    currentY += scale

#X axis drawing
for lines in myFile:
    #Splits values by the ","
    lineValue = lines.strip().split(",")
    xvalue = (90 * currentCountry) + 10
    currentCountryName = lineValue[0]
    bar_height = ((int(lineValue[1])-100_000_000)/1_950_000)

    #Draws the countries at the start of the bar
    country = arcade.Text(currentCountryName, xvalue, 25, arcade.color.BLACK)
    country.draw()

    #Draws the bars and changes according to percent change with negative red and positive green.
    if(float(lineValue[2]) < 0 ):
        arcade.draw_xywh_rectangle_filled(xvalue, 100, 70, bar_height, arcade.color.RED)
    else:
        arcade.draw_xywh_rectangle_filled(xvalue, 100, 70, bar_height, arcade.color.GREEN)

    currentCountry += 1

#Finishes render and runs the program
arcade.finish_render()
arcade.run()
