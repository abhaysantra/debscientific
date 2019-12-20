import json, os,sys
from django.template import Context
from django.core.files.uploadedfile import InMemoryUploadedFile
import PIL
from PIL import Image
from io import BytesIO, StringIO
from pdf2image import convert_from_path
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

def image_resize(uploaded_image,img_size):
	print('uploaded_image :',uploaded_image)
	imageTemproary = Image.open(uploaded_image)
	img_format = imageTemproary.format
	outputIoStream = BytesIO()
	imageTemproaryResized = imageTemproary.resize(img_size)

	imageTemproaryResized.save(outputIoStream, format=img_format, quality=100)
	outputIoStream.seek(0)
	uploadedImage = InMemoryUploadedFile(outputIoStream,'ImageField', "%s" %(uploaded_image), 'image/%s'%img_format.lower(), sys.getsizeof(outputIoStream), None)

	return uploadedImage

def convert_pdf_2_image(uploaded_image_path, uploaded_image,img_size):
	project_dir = os.getcwd()
	print('project_dir : ',project_dir)
	os.chdir(uploaded_image_path)
	print('after changing current directory :',os.getcwd())
	print('uploaded_image : ',uploaded_image)

	file_name = str(uploaded_image).replace('.pdf','')
	print('file_name : ',file_name)
	output_file = file_name+'.jpg'
	pages = convert_from_path(uploaded_image, 200)
	for page in pages:
		page.save(output_file, 'JPEG')
		break
	os.chdir(project_dir)
	img = Image.open(output_file)
	img = img.resize(img_size, PIL.Image.ANTIALIAS)
	img.save(output_file)
	return output_file