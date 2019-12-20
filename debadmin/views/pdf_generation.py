from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.conf import settings  
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from datetime import datetime
import json, os,sys
from django.template import Context
from django.template import loader
from django.template.loader import get_template
from xhtml2pdf import pisa 
import uuid, barcode, random
from barcode.writer import ImageWriter
from . import accounts, order_list, deb_utility
from debadmin.models import contactUs, product, order_invoice, order, order_details, billing_address, user_address  

def generate_pdf_from_html(request, order_id):
	# generate barcode and store in database
	order_invoice_info = generate_barcode(order_id)
	#order invoice generation
	random_char = str(uuid.uuid4().hex[0:6])
	invoice_number = 'DEB-INVOICE-'+ random_char + '-' + str(order_id)
	invoice_name = invoice_number + '.pdf'
	final_invoice = 'generated_invoice/' + invoice_name
	order_invoice_info.invoice = final_invoice
	order_invoice_info.invoice_number = invoice_number
	order_invoice_info.save(update_fields=['invoice_number','invoice',])

	# for context of billing and delivery address
	contact_info = contactUs.objects.all()
	order_info = order.objects.filter(id=order_id)
	order_details_info = order_details.objects.filter(order_id=order_id)
	# pro_image_info = product_image.objects.raw('SELECT * FROM debadmin_product_image GROUP BY product_id')
	pro_details_info = product.objects.all()
	bil_address_info = billing_address.objects.raw('SELECT * FROM debadmin_billing_address ba JOIN debadmin_order_address oa ON ba.id = oa.bill_address_id WHERE oa.order_id = %s'%order_id)
	deli_address_info = user_address.objects.raw('SELECT * FROM debadmin_user_address ua JOIN debadmin_order_address oa ON ua.id = oa.deli_address_id WHERE oa.order_id = %s'%order_id)
	logo = 'logo/deb_logo.png'
	context = {
			'contact_info':contact_info,
			'order_info':order_info,
			'order_details_info':order_details_info,
			'bil_address_info':bil_address_info,
			'deli_address_info':deli_address_info,
			'pro_details_info':pro_details_info,
			'order_list_active':'active',
			'admin':'Deb Scientific',
			'order_invoice_info': order_invoice_info,
			'logo':logo
			}
	############################
	
	template = get_template('invoice_template/admin_pro_invoice.html')
	html  = template.render(context)

	links = lambda uri, rel: os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ''))
	# pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")),dest=result, link_callback=links)
	file = open('media/generated_invoice/%s'%invoice_name, "w+b")
	pisaStatus = pisa.CreatePDF(html.encode('utf-8'), dest=file, encoding='utf-8', link_callback=links)

	file.seek(0)
	pdf = file.read()
	file.close()     
	# return render(request, 'invoice_template/admin_pro_invoice.html',context)    
	# return HttpResponse(pdf, 'application/pdf')
	return redirect(order_list.order_details_view,order_id)

def generate_barcode(order_id):
	# get user_id
	order_obj = order.objects.filter(id=order_id)[0]
	# this barcode must be 12 
	random_code = str(random.randint(00000000,99999999)) + str(order_id)
	# if length of barcode less than 12 make it 12
	if len(random_code)<12:
		remaining_len = 12 - len(random_code)
		for i in range(remaining_len):
			random_code = str(random_code) + str(i)
			
	ean = barcode.get('ean13', random_code, writer=ImageWriter())
	barcode_name = 'ean13-' + random_code
	barcode_image = ean.save('media/barcode/'+barcode_name)
	# barcode_image = ean.save('debscientific/media/barcode/'+barcode_name) # linux server

	barcode_image_with_out_media = barcode_image.replace('media/','')
	# barcode_image_with_out_media = barcode_image.replace('debscientific/media/','') # linux server

	# Store barcode into Database
	# resized_barcode_image= deb_utility.image_resize(barcode_image,(100,20))

	check_exist_invoice = order_invoice.objects.filter(order_id=order_id)

	if check_exist_invoice:
		exist_invoive_update = check_exist_invoice[0]
		exist_invoive_update.barcode = barcode_image_with_out_media
		exist_invoive_update.created_date = datetime.now().date()
		exist_invoive_update.save(update_fields=['barcode','created_date'])
		return exist_invoive_update
	else:
		order_invoice_info = order_invoice(
					user_id = order_obj.order_customer_id, 
					order_id = order_id,      
					barcode = barcode_image_with_out_media,
					created_date=datetime.now().date(),
		)
		order_invoice_info.save()
		return order_invoice_info

	# messages.success(request,'Order Invoice created Successfully!')
	


