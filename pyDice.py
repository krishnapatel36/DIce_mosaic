from PIL import Image

#Values for the number of dice wide and tall the output image should be
numDiceWide = 50
numDiceTall = 50

#Opens the example image and all dice images
source_image = Image.open("example.png")
die_one = Image.open("DiceImages/1.png")
die_two = Image.open("DiceImages/2.png")
die_three = Image.open("DiceImages/3.png")
die_four = Image.open("DiceImages/4.png")
die_five = Image.open("DiceImages/5.png")
die_six = Image.open("DiceImages/6.png")
#Reads the size of the dice image
dice_image_width, dice_image_height = die_one.size
#Resizes the source_image to one pixel per die
resized_image = source_image.resize((numDiceWide, numDiceTall))
#Converts the resized_image to black and white
resized_image = resized_image.convert('L')
#Creates a list of the pixel greyscale values (0-255)
pix_val=list(resized_image.getdata())
#print(pix_val)

#Maps the greyscale value (0-255) of each pixel to 1-6
for i in range(len(pix_val)):
    if (pix_val[i] < 42):
        pix_val[i] = 6
    if (pix_val[i] >= 42 and pix_val[i] < 84):
        pix_val[i] = 5
    if (pix_val[i] >= 84 and pix_val[i] < 126):
        pix_val[i] = 4
    if (pix_val[i] >= 126 and pix_val[i] < 168):
        pix_val[i] = 3
    if (pix_val[i] >= 168 and pix_val[i] < 210):
        pix_val[i] = 2
    if (pix_val[i] >= 210):
        pix_val[i] = 1
    pass

#This calculates the size of the output image
output_image_size = (dice_image_width*numDiceWide,dice_image_height*numDiceTall)
#Creates a black image the size of the output image
output_image = Image.new('L', output_image_size, color=0)

#Iterates over the list and pastes the correct
#value die onto the corresponding pixel location
for i in range(len(pix_val)):
    #Calculates the x_location of the top left corner of die location
    x_location = int((int(dice_image_width)*i))%(dice_image_width*numDiceWide)
    #Calculates the y_location of the top left corner of the die image
    y_location = int(i/numDiceWide)*dice_image_height
    if (pix_val[i] == 1):
        output_image.paste(die_one, (x_location,y_location))
    if (pix_val[i] == 2):
        output_image.paste(die_two, (x_location,y_location))
    if (pix_val[i] == 3):
        output_image.paste(die_three, (x_location,y_location))
    if (pix_val[i] == 4):
        output_image.paste(die_four, (x_location,y_location))
    if (pix_val[i] == 5):
        output_image.paste(die_five, (x_location,y_location))
    if (pix_val[i] == 6):
        output_image.paste(die_six, (x_location,y_location))
    pass
#Save the output_image
output_image.save('arduino.png')