import streamlit as st
from PIL import Image
import io
from reportlab.pdfgen.canvas import Canvas
import tempfile
import base64

# Function to convert image to dice representation
def convert_to_dice_representation(image_path, num_dice_wide, num_dice_tall):
    source_image = Image.open(image_path)
    die_one = Image.open("DiceImages/DiceImages/1.png")
    die_two = Image.open("DiceImages/DiceImages/2.png")
    die_three = Image.open("DiceImages/DiceImages/3.png")
    die_four = Image.open("DiceImages/DiceImages/4.png")
    die_five = Image.open("DiceImages/DiceImages/5.png")
    die_six = Image.open("DiceImages/DiceImages/6.png")

    dice_image_width, dice_image_height = die_one.size
    resized_image = source_image.resize((num_dice_wide, num_dice_tall))
    resized_image = resized_image.convert('L')
    pix_val = list(resized_image.getdata())

    for i in range(len(pix_val)):
        if pix_val[i] < 42:
            pix_val[i] = 1
        elif 42 <= pix_val[i] < 84:
            pix_val[i] = 2
        elif 84 <= pix_val[i] < 126:
            pix_val[i] = 3
        elif 126 <= pix_val[i] < 168:
            pix_val[i] = 4
        elif 168 <= pix_val[i] < 210:
            pix_val[i] = 5
        else:
            pix_val[i] = 6

    output_image_size = (dice_image_width * num_dice_wide, dice_image_height * num_dice_tall)
    output_image = Image.new('L', output_image_size, color=0)

    for i in range(len(pix_val)):
        x_location = int((int(dice_image_width) * i)) % (dice_image_width * num_dice_wide)
        y_location = int(i / num_dice_wide) * dice_image_height
        if pix_val[i] == 1:
            output_image.paste(die_one, (x_location, y_location))
        elif pix_val[i] == 2:
            output_image.paste(die_two, (x_location, y_location))
        elif pix_val[i] == 3:
            output_image.paste(die_three, (x_location, y_location))
        elif pix_val[i] == 4:
            output_image.paste(die_four, (x_location, y_location))
        elif pix_val[i] == 5:
            output_image.paste(die_five, (x_location, y_location))
        elif pix_val[i] == 6:
            output_image.paste(die_six, (x_location, y_location))

    return output_image

# Function to convert PIL Image to bytes
def ImageToBytes(image):
    img_byte_array = io.BytesIO()
    image.save(img_byte_array, format='PNG')
    return img_byte_array.getvalue()

# Streamlit app
def main():
    st.title("Dice Image Generator")

    # Upload image through Streamlit
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        num_dice_wide = st.number_input("Number of dice wide:", min_value=1, max_value=100, value=50)
        num_dice_tall = st.number_input("Number of dice tall:", min_value=1, max_value=100, value=50)

        st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)

        if st.button("Generate Dice Image"):
            output_image = convert_to_dice_representation(uploaded_file, int(num_dice_wide), int(num_dice_tall))
            st.image(output_image, caption="Generated Dice Image.", use_column_width=True)
            st.success("Image generated successfully!")

            # Download button for the generated image
            image_bytes = ImageToBytes(output_image)
            download_link_image = f'<a href="data:image/png;base64,{base64.b64encode(image_bytes).decode()}" download="generated_image.png">Download Generated Image</a>'
            st.markdown(download_link_image, unsafe_allow_html=True)

if __name__ == "__main__":
    main()