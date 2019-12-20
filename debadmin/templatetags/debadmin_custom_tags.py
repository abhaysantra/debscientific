
from django.template.defaulttags import register
import urllib, base64
from io import BytesIO, StringIO
from debadmin.models import product, adminUser
import num2words, json
from django.db.models import Q
from debadmin.models import user_addon_cart_item, sub_product, user_cart_item, addon_order, order_details

@register.filter
def multiply(value, arg):
    return value * arg

@register.filter
def get64(url):
    """
    Method returning base64 image data instead of URL
    """
    if url.startswith("http"):
        image = StringIO(urllib.urlopen(url).read())
        return 'data:image/jpg;base64,' + base64.b64encode(image.read())

    return url

@register.filter
def get_product_name(product_id):
	pro_details_info = product.objects.filter(id = product_id)[0]
	return pro_details_info.product_name

@register.filter
def get_user_name(user_id):
	user_info = adminUser.objects.filter(id = user_id)[0]
	return user_info.full_name

@register.filter
def calculate_sub_total(order_details_info):
	sub_total = 0
	for each_order in order_details_info:
		order_qty = each_order.order_product_qty
		order_price = each_order.order_product_price
		sub_total += (order_qty*order_price)

	return sub_total

@register.filter
def convert_num2words(number):
	words = num2words.num2words(number).title()
	return words

@register.filter
def get_addon_order_list(order_id,product_id):
	addon_order_list = addon_order.objects.raw('SELECT * FROM debadmin_addon_order ar JOIN debadmin_sub_product s ON ar.addon_product_id = s.id WHERE ar.order_id = %s AND ar.product_id = %s'%(order_id,product_id))
	return addon_order_list

@register.filter
def get_details_of_addon_product_list(addon_product_list):
	print('addon_product_list :',addon_product_list)
	jsonDec = json.decoder.JSONDecoder()
	addon_product_list = jsonDec.decode(addon_product_list)
	print('addon_product_list after decode : ',addon_product_list)
	addon_product_details_list = sub_product.objects.filter(id__in = addon_product_list)
	print('addon_product_details_list : ',addon_product_details_list)
	# addon_order_list = addon_order.objects.raw('SELECT * FROM debadmin_addon_order ar JOIN debadmin_sub_product s ON ar.addon_product_id = s.id WHERE ar.order_id = %s AND ar.product_id = %s'%(order_id,product_id))
	return addon_product_details_list

# not in use
@register.filter
def calculate_total_order_price_of_each_product(order_id,product_id):
	total_order_price = 0
	# find total order for each order id
	pro_details_info = order_details.objects.filter(order_id = order_id, order_product_id = product_id)
	for each_order in pro_details_info:
		qty = each_order.order_product_qty
		price = each_order.order_product_price
		total_order_price +=(qty*price)

	total_addon_price = 0
	# find total addon product for each order id
	addon_order_info = addon_order.objects.filter(order_id = order_id, product_id = product_id)
	for each_addon in addon_order_info:
		total_addon_price += each_addon.addon_product_price

	total_price = total_order_price + total_addon_price
	# addon_order_list = addon_order.objects.raw('SELECT * FROM debadmin_addon_order ar JOIN debadmin_sub_product s ON ar.addon_product_id = s.id WHERE ar.order_id = %s AND ar.product_id = %s'%(order_id,product_id))
	return total_price

@register.filter
def calculate_total_order_price_of_each_product_with_addon(order_details_obj):
	total_order_price = 0
	qty = order_details_obj.order_product_qty
	price = order_details_obj.order_product_price
	total_order_price +=(qty*price)

	total_addon_price = 0
	# find total addon product for each order id
	jsonDec = json.decoder.JSONDecoder()
	addon_product_list = jsonDec.decode(order_details_obj.addon_product_id_list)
	addon_product_details_list = sub_product.objects.filter(id__in = addon_product_list)

	# addon_order_info = addon_order.objects.filter(order_id = order_id, product_id = product_id)
	for each_addon in addon_product_details_list:
		total_addon_price += each_addon.sub_product_price

	total_price = total_order_price + total_addon_price
	return total_price