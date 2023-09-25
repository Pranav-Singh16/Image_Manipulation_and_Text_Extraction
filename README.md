# Image Text Extraction with Tesseract and Pillow

<div align="center">
  <img src="https://github.com/Pranav-Singh16/Image_Manipulation_and_Text_Extraction/assets/145978125/cb634d3e-5dba-48e2-8e3b-a76712602f9c" alt="Image for text extraction" width="500" height="275">
</div>

This Python script is designed to extract text from images using Tesseract OCR and the Pillow library. It allows you to process a batch of images, define the area for text extraction, and store the results in a CSV file.

## Prerequisites

Before using this script, make sure you have the following software and libraries installed:

- Python 3.x
- Tesseract OCR: You can download it from [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) and set the `tesseract_cmd` path accordingly in the script.
- Pillow (PIL): You can install it using pip: `pip install pillow`
- pytesseract: You can install it using pip: `pip install pytesseract`
- pandas: You can install it using pip: `pip install pandas`

## Getting Started

1. Clone the repository or download the script to your local machine.

2. Ensure you have all the prerequisites installed.

3. Create a folder that contains the images from which you want to extract text.

4. Open the script and set the `folder_path` variable to the path of the folder containing your images.

5. Run the script. It will process all image files in the specified folder.

6. For each image, you can choose to extract text from the entire image or a specific region. Follow the on-screen instructions to define the region.

7. After processing, the script will display the extracted text and save the results to a CSV file (`text_results.csv` by default).


<div align="center">
  <img src="https://github.com/Pranav-Singh16/Image_Manipulation_and_Text_Extraction/assets/145978125/49196275-c5b9-45b4-a89c-dbccc4d3cbd7" width="400" height="220">
    <img src="https://github.com/Pranav-Singh16/Image_Manipulation_and_Text_Extraction/assets/145978125/f475bf5b-9bb5-4338-a37e-6b5811094519" width="400" height="220">
</div>

<div align="center">
  <img src="https://github.com/Pranav-Singh16/Image_Manipulation_and_Text_Extraction/assets/145978125/6f952f7b-b9b4-4169-95dc-7c34caae0655" width="400" height="220">
    <img src="https://github.com/Pranav-Singh16/Image_Manipulation_and_Text_Extraction/assets/145978125/eef805ae-a617-488c-9c66-3c35acbaac37" width="400" height="220">
</div>


## Usage

- When you run the script, it will loop through all image files in the specified folder and prompt you to define the region for text extraction.

- You can select the entire image or draw a rectangle to specify a custom region.

- If you choose to define a custom region, you can move the boundaries and adjust the region until you are satisfied with the selection.

- The extracted text will be displayed on the screen and stored in a CSV file named `text_results.csv`.

- You can access the extracted text and image names in the CSV file for further analysis or processing.

**Note:** This README is a general guide. You should replace placeholders in the script, such as `folder_path`, with your specific information, and customize it according to your project's structure and requirements.
