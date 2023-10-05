# from PIL import Image, ImageDraw, ImageFont
# import os

# def generate_certificate(name, course_title, completion_date):
#     # Load the certificate template image
#     template_path = 'D:/LMS/project/SoftUI_LMS/media/media/certificate.jpg'  # Replace with the path to your certificate template image
#     certificate_img = Image.open(template_path)

#     # Define fonts and font sizes
#     name_font = ImageFont.truetype('D:/LMS/project/SoftUI_LMS/media/media/font/ten.ttf', 140)  # Replace with the path to the font file for the name
#     title_font = ImageFont.truetype('D:/LMS/project/SoftUI_LMS/media/media/font/ten.ttf', 30)  # Replace with the path to the font file for the title
#     date_font = ImageFont.truetype('D:/LMS/project/SoftUI_LMS/media/media/font/ten.ttf', 20)  # Replace with the path to the font file for the date

#     # Create a drawing context
#     draw = ImageDraw.Draw(certificate_img)

#     # Define the coordinates to position the text on the certificate
#     name_x, name_y = 300, 400
#     title_x, title_y = 300, 500
#     date_x, date_y = 300, 600

#     # Add text to the certificate image
#     draw.text((name_x, name_y), name, fill='black', font=name_font)
#     draw.text((title_x, title_y), course_title, fill='black', font=title_font)
#     draw.text((date_x, date_y), completion_date, fill='black', font=date_font)

#     # Save the generated certificate
#     output_path = 'D:/LMS/project/SoftUI_LMS/lms/static/'  # Replace with the path to the folder where you want to save the certificate
#     certificate_filename = f'{name.replace("abc", "_")}_certificate.png'
#     certificate_img.save(os.path.join(output_path, certificate_filename))

#     return os.path.join(output_path, certificate_filename)

# # Example usage:
# name = "John Doe"
# course_title = "Introduction to Python"
# completion_date = "August 6, 2023"
# certificate_path = generate_certificate(name, course_title, completion_date)
# print(f"Certificate generated: {certificate_path}")


# from PIL import Image, ImageDraw, ImageFont
# import os

# def generate_certificate(name, course_title, completion_date, image_path):
#     # Load the certificate template image
#     template_path = 'D:/LMS/project/SoftUI_LMS/media/media/certificate.jpg'  # Replace with the path to your certificate template image
#     certificate_img = Image.open(template_path)

#     # Define fonts and font sizes
#     name_font = ImageFont.truetype('D:/LMS/project/SoftUI_LMS/media/media/font/ten.ttf', 40)  # Replace with the path to the font file for the name
#     cerficate = ImageFont.truetype('D:/LMS/project/SoftUI_LMS/media/media/font/ten.ttf', 100)  # Replace with the path to the font file for the name
#     title_font = ImageFont.truetype('D:/LMS/project/SoftUI_LMS/media/media/font/ten.ttf', 30)  # Replace with the path to the font file for the title
#     date_font = ImageFont.truetype('D:/LMS/project/SoftUI_LMS/media/media/font/ten.ttf', 20)  # Replace with the path to the font file for the date

#     # Load the image to be placed on the certificate
#     image = Image.open('D:/LMS/project/SoftUI_LMS/media/media/dp_image11-796.jpg')

#     # Create a drawing context
#     draw = ImageDraw.Draw(certificate_img)

#     # Define the coordinates to position the text and image on the certificate
#     name_x, name_y = 300, 400
#     title_x, title_y = 300, 500
#     date_x, date_y = 300, 600
#     certificate_x, y = 820,500
#     image_x, image_y = 800, 10  # Adjust the coordinates as needed

#     # Add text to the certificate image
#     draw.text((name_x, name_y), name, fill='black', font=name_font)
#     draw.text((certificate_x, y), 'CERIFICATE', fill='black', font=cerficate)
#     draw.text((title_x, title_y), course_title, fill='black', font=title_font)
#     draw.text((date_x, date_y), completion_date, fill='black', font=date_font)

#     # Add the image to the certificate
#     # certificate_img.paste(image, (image_x, image_y))

#     # Save the generated certificate
#     output_path = 'D:/LMS/project/SoftUI_LMS/lms/static/'  # Replace with the path to the folder where you want to save the certificate
#     certificate_filename = f'{name.replace("abc", "_")}_certificate.png'
#     certificate_img.save(os.path.join(output_path, certificate_filename))

#     return os.path.join(output_path, certificate_filename)

# # Example usage:
# name = "John Doe"
# course_title = "Introduction to Python"
# completion_date = "August 6, 2023"
# image_path = 'path/to/image.png'  # Replace with the path to the image you want to add
# certificate_path = generate_certificate(name, course_title, completion_date, image_path)
# print(f"Certificate generated: {certificate_path}")
from PIL import Image, ImageDraw, ImageFont
import os

def generate_certificate(name, course_title, completion_date, image_path):
    # Load the certificate template image
    template_path = 'D:/LMS/project/SoftUI_LMS/media/media/certificate.jpg' # Replace with the path to your certificate template image
    certificate_img = Image.open(template_path)

    # Define fonts and font sizes
    name_font = ImageFont.truetype('D:/LMS/project/SoftUI_LMS/media/media/font/ten.ttf', 50)  # Replace with the path to the font file for the name
    title_font = ImageFont.truetype('D:/LMS/project/SoftUI_LMS/media/media/font/ten.ttf', 50)  # Replace with the path to the font file for the title
    date_font = ImageFont.truetype('D:/LMS/project/SoftUI_LMS/media/media/font/ten.ttf', 40)  # Replace with the path to the font file for the date

    # Load the image to be placed on the certificate
    image = Image.open('D:/LMS/project/SoftUI_LMS/media/media/dp_image11-796.jpg')

    # Calculate the centered position for the image and text
    image_x = (certificate_img.width - image.width) // 2
    image_y = 100  # Adjust the vertical position as needed

    name_width, _ = name_font.getsize(name)
    name_x = (certificate_img.width - name_width) // 2.01
    name_y = image_y + image.height + 20  # Adjust the vertical position as needed

    title_width, _ = title_font.getsize(course_title)
    title_x = (certificate_img.width - title_width) // 6
    title_y = name_y + name_font.getsize(name)[1] + 70

    date_width, _ = date_font.getsize(completion_date)
    date_x = (certificate_img.width - date_width) // 15
    date_y = title_y + title_font.getsize(course_title)[1] + 250

    stamp_width, _ = date_font.getsize(completion_date)
    date1_x = (certificate_img.width - date_width) // 1
    date1_y = title_y + title_font.getsize(course_title)[1] + 250

    # Create a drawing context
    draw = ImageDraw.Draw(certificate_img)

    # Add text to the certificate image
    draw.text((name_x, name_y), 'Certificate', fill='black', font=name_font)
    draw.text((title_x, title_y), f"{name} has successfully completed the course of {course_title} on {completion_date}", fill='black', font=title_font)
    draw.text((date_x, date_y), '__________ \n Signature', fill='black', font=date_font)
    draw.text((date1_x, date1_y), '_______ \n Stamp', fill='black', font=date_font)

    # Add the image to the certificate
    certificate_img.paste(image, (image_x, image_y))

    # Save the generated certificate
    output_path = 'D:/LMS/project/SoftUI_LMS/lms/static/'  # Replace with the path to the folder where you want to save the certificate
    certificate_filename = f'{name.replace(" ", "_")}_certificate.png'
    certificate_img.save(os.path.join(output_path, certificate_filename))

    return certificate_filename
#     from reportlab.lib.pagesizes import letter
#     from reportlab.lib.utils import ImageReader
#     from reportlab.pdfgen import canvas

# # Load your image
#     image_path = img

# # Create a PDF
#     pdf_path = 'output.pdf'
#     c = canvas.Canvas(pdf_path, pagesize=letter)

# # Determine the size of the image in the PDF
#     image_width, image_height = letter

# # Draw the image on the PDF
#     c.drawImage(ImageReader(image_path), 100, 100, width=image_width, height=image_height)

# # Save the PDF
#     c.save()

    # print(f'PDF created: {pdf_path}')


# Example usage:
# name = "John Doe"
# course_title = "Introduction to Python"
# completion_date = "August 6, 2023"
# image_path = 'path/to/image.png'  # Replace with the path to the image you want to add
# certificate_path = generate_certificate(name, course_title, completion_date, image_path)
# print(f"Certificate generated: {certificate_path}")
