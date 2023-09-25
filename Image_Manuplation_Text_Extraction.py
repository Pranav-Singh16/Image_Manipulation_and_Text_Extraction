# Import all necessary library
import os
import PIL
from PIL import Image, ImageDraw, ImageFilter
from io import BytesIO
from IPython.display import display
from PIL import ImageEnhance
import pytesseract
import requests
import pandas as pd

# give location of tesseract ocr
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Folder containing the images you want to process
folder_path = r"C:\Users\Downloads\Pillow"

df = pd.DataFrame(columns=["Image Name", "Extracted Text"])
image_files = [file for file in os.listdir(folder_path) if file.endswith(('.jpg', '.jpeg', '.png', '.bmp'))]
print(image_files)
for image_file in image_files:
    print(image_file)

    # Construct the full path to the image
    img_path = os.path.join(folder_path, image_file)
    
    # Open the image using Pillow
    img = Image.open(img_path).convert("RGB")
    img.load()
    img1 = img.copy()
    img1.load()

    # Get the image dimensions
    width, height = img.size

    # defining boundries
    x1, y1 = 0, 0
    x2, y2 = width, height

    img.show()

    # To get exact border
    border = int(input("if you want to extract text from the full image then type 0, or if you want to extract a part then type 1:\n"))

    if border == 1:

        # Create a drawing object to draw on the image
        draw = ImageDraw.Draw(img)

        # Calculate the coordinates for the rectangle
        x1, y1 = width // 4, height // 4
        x2, y2 = 3 * width // 4, 3 * height // 4
        x11, y11, x21, y21 = x1, y1, x2, y2

        # Draw a black rectangle on the image
        draw.rectangle([x1, y1, x2, y2], outline=(0, 0, 0))
        
        # Display the modified image
        img.show()

        def boundry():
            global border, x1, y1, x2, y2, x11, y11, x21, y21, img

            while border == 1:            
                
                border = int(input("if text covered in the rectangle then input 0, otherwise input 1:\n"))
                if border == 1:
                    l1 = input("give input according to the given instruction \n if horizontal lines want to move left then input -1, and if move to right input +1, and if don't want to move then press 0 \n similarly for vertical lines, if want to move upward input -1, and if downward input +1, and if the same then 0 \n input in the given format (upper_horizontal lower_horizontal left_vertical right_vertical) (<-- and ^ = -1) \n (0 0 0 0) separated by space").strip().split(" ")
                    
                    l = list(map(lambda x: int(x), l1))

                    # Changing rectangle boundaries

                    def minus(x,y):
                        y = x
                        x = y - x // 4
                        return x, y

                    def plus(x,y):
                        y = x
                        x = y + x // 4
                        return x, y

                    for i in range(4):
                        if i == 0 and y1 < y2:
                            if l[i] == -1:
                                y1, y11 = minus(y1, y11)
                            elif l[i] == 1:
                                y1, y11 = plus(y1, y11)

                        if i == 1 and y2 > y1:
                            if l[i] == -1:
                                y2, y21 = minus(y2, y21)
                            elif l[i] == 1:
                                y2, y21 = plus(y2, y21)

                        if i == 2 and x1 < x2:
                            if l[i] == -1:
                                x1, x11 = minus(x1, x11)
                            elif l[i] == 1:
                                x1, x11 = plus(x1, x11)

                        if i == 3 and x2 > x1:
                            if l[i] == -1:
                                x2, x21 = minus(x2, x21)
                            elif l[i] == 1:
                                x2, x21 = plus(x2, x21)
                    # Check and adjust x1 and y1

                    x1 = max(x1,0)
                    y1 = max(y1,0)

                    # Check and adjust x2 and y2
                    x2 = min(x2,width)
                    y2 = min(y2,height)

                    img = img1.copy()
                    draw_updated = ImageDraw.Draw(img)
                    draw_updated.rectangle([x1, y1, x2, y2], outline=(0, 0, 0))
                    img.show()
                    
        boundry()

    final_text = ''
    #(left, upper, right, lower11)
    image = img.crop((x1, y1, x2, y2))
    enhanced_image = image.filter(ImageFilter.FIND_EDGES)
    enhanced_image.show()

    image = enhanced_image.convert('L')
    image.show()

    processed_text = pytesseract.image_to_string(image)

    # Replacing all new line with space
    processed_text = processed_text.replace('\n', ' ')
    final_text += processed_text
    print(final_text)
    
    # Append the data to the DataFrame
    df = df.append({"Image Name": image_file, "Extracted Text": final_text}, ignore_index=True)
    # break

# Save the DataFrame to a CSV file
csv_filename = r"F:\Codes\pranav\project\text_results.csv"
df.to_csv(csv_filename, encoding="utf-8")
