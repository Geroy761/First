from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
import requests
from bs4 import BeautifulSoup as BS

t = requests.get('https://obhavo.uz/tashkent')
html_t = BS(t.content, 'html.parser')

for el in html_t.select('.container'):
	min = el.select('.weather-row-forecast .forecast-night')[0].text
	max = el.select('.weather-row-forecast .forecast-day')[0].text
	t_min = min[4:]
	t_max = max[5:]
	print(t_min, t_max)


def city():
	return [
		[InlineKeyboardButton("Toshkent", callback_data=f"01")]
	]


def back():
	return [
		[InlineKeyboardButton("Orqaga", callback_data=f"back1")]
	]

def inline_hendlerlar(update, context):
	query = update.callback_query
	data = query.data.split("_")

	if data[0] == "01":
		query.message.edit_text(f"Bugun Toshkent shaxrida havo o'zgarib turadi min {t_min}\nmax " f"{t_max} \nbo'lishi kutilmoqda", reply_markup=InlineKeyboardMarkup(back()))
	elif data[0] == 'back1':
		query.message.edit_text(
				f"Bu yerdan Shahar yoki viloyatni tanla👇",
				reply_markup=InlineKeyboardMarkup(city())
			)



def start(update, context):
	user = update.message.from_user
	update.message.reply_text(f"""Salom {user.first_name} 👋\nBu yerdan Shahar yoki viloyatni tanla👇""")


def main():
	Token = "5479668001:AAH23eO5ksxKBp5FV63hmp2rJlrQrv-6Ccs"
	updater = Updater(Token)
	updater.dispatcher.add_handler(CommandHandler("start", start))
	updater.start_polling()
	updater.idle()

if __name__ == '__main__':
	main()