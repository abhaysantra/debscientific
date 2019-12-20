from django.template.defaulttags import register
from django.db.models import Q
import json
from debadmin.models import user_addon_cart_item, sub_product, user_cart_item, addon_order, product
from debadmin.models import countries, states, cities

@register.filter
def multiply(value, arg):
	return value * arg
    
@register.filter
def upper(arg):
	return arg.upper()

@register.filter
def loop_range(min, value):
	return range(min, value)

@register.filter
def sub(big, small):
	return (big - small)

@register.filter
def add(big, small):
	return (big + small)

@register.filter
def get_country_name(country_id):
	if country_id == None or country_id == 0:
		return None
	county_obj = countries.objects.filter(country_id = country_id)[0]
	return county_obj.name

@register.filter
def get_state_name(state_id):
	if state_id == None or state_id == 0:
		return None
	county_obj = states.objects.filter(state_id = state_id)[0]
	return county_obj.name

@register.filter
def get_city_name(city_id):
	if city_id == None or city_id == 0:
		return None
	county_obj = cities.objects.filter(city_id = city_id)[0]
	return county_obj.name

@register.filter
def get_product_qty(dictionary, key):
	# print('get_product_qty : ',dictionary, key)
	return dictionary.get(str(key))

@register.filter
def get_int_value(value):
	return int(value)

@register.filter
def get_addon_list_for_non_loggedin_user(product_id_addon_id_list):
	addon_id_list = tuple(product_id_addon_id_list.split('_')[1:])
	addon_list = sub_product.objects.filter(id__in = addon_id_list)
	return addon_list

@register.filter
def get_total_addon_for_non_loggedin_user(product_id_addon_id_list):
	addon_id_list = product_id_addon_id_list.split('_')[1:]
	return len(addon_id_list)

@register.filter
def get_addon_price_for_non_loggedin_user(product_id_addon_id_list):
	addon_id_list = product_id_addon_id_list.split('_')[1]
	addon_list = sub_product.objects.filter(id = addon_id_list)
	total_price = 0
	for each_addon in addon_list:
		total_price += each_addon.sub_product_price

	return total_price

@register.filter
def get_total_addon_cart_pro(cart_id):
	addon_list = user_addon_cart_item.objects.filter(cart_id=cart_id)
	total_addon_pro = len(list(addon_list))
	return int(total_addon_pro)

@register.filter
def get_total_addon_cart_item(cart_id):
	addon_obj = user_cart_item.objects.filter(id=cart_id)[0]
	jsonDec = json.decoder.JSONDecoder()
	addon_product_list = jsonDec.decode(addon_obj.addon_id_list)
	total_addon_pro = len(addon_product_list)
	return int(total_addon_pro)

@register.filter
def get_addon_price_of_cart_item(cart_id):
	addon_obj = user_cart_item.objects.filter(id=cart_id)[0]
	jsonDec = json.decoder.JSONDecoder()
	addon_product_list = jsonDec.decode(addon_obj.addon_id_list)
	if int(addon_product_list.strip()) == 0:
		return 0
	else:
		addon_list = sub_product.objects.filter(id = addon_product_list)
		total_price = 0
		for each_addon in addon_list:
			total_price += each_addon.sub_product_price

		return total_price

@register.filter
def get_addon_name_of_cart_item(cart_id):
	addon_obj = user_cart_item.objects.filter(id=cart_id)[0]
	jsonDec = json.decoder.JSONDecoder()
	addon_product_list = jsonDec.decode(addon_obj.addon_id_list)
	if int(addon_product_list.strip()) == 0:
		return "No Addon Product"
	else:
		addon_obj = sub_product.objects.filter(id = addon_product_list)
		return addon_obj[0].sub_product_name

@register.filter
def get_addon_list(cart_id):
	# addon_list = user_addon_cart_item.objects.raw('SELECT * FROM debadmin_user_addon_cart_item ac JOIN debadmin_sub_product s ON ac.addon_item_id = s.id WHERE ac.cart_id = %s'%cart_id)
	addon_obj = user_cart_item.objects.filter(id=cart_id)[0]
	jsonDec = json.decoder.JSONDecoder()
	addon_product_list = jsonDec.decode(addon_obj.addon_id_list)
	addon_product_list = sub_product.objects.filter(id__in=addon_product_list)
	return addon_product_list

@register.filter
def get_addon_order_list(order_id,product_id):
	addon_order_list = addon_order.objects.raw('SELECT * FROM debadmin_addon_order ar JOIN debadmin_sub_product s ON ar.addon_product_id = s.id WHERE ar.order_id = %s AND ar.product_id = %s'%(order_id,product_id))
	return addon_order_list


@register.filter
def single_cart_and_addon_cart_price(cart_id, user_id):
	addon_list = user_addon_cart_item.objects.filter(cart_id=cart_id, user_id=user_id)
	cart_list = user_cart_item.objects.filter(id=cart_id,user_id=user_id)
	total_addon_price = 0
	total_cart_price = cart_list[0].cart_item_qty * cart_list[0].cart_sell_price

	for addon_row in addon_list:
		total_addon_price += addon_row.addon_item_sell_price

	total_price = total_addon_price + total_cart_price
	return total_price

@register.filter
def calculate_cart_and_addon_product_price_non_loggedin_user(sess_product_qty, product_id_addon_id_list):
	product_id = product_id_addon_id_list.split('_')[0]
	product_sell_price = product.objects.filter(id=int(product_id))[0].sell_price
	addon_id_list = tuple(product_id_addon_id_list.split('_')[1:])
	addon_list = sub_product.objects.filter(id__in = addon_id_list)

	prduct_total_price = sess_product_qty * product_sell_price
	total_addon_price = 0
	for addon_obj in addon_list:
		total_addon_price += addon_obj.sub_product_price

	total_price = prduct_total_price + total_addon_price
	return total_price