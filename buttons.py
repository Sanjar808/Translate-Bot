from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

language = {
	'uz':"🇺🇿 Uzbekistan",
	'tg':"🇹🇯 Tajik",
	'ky':"🇰🇿 Kazakh",
	'ru':"🇷🇺 Russian",
	'ar':"🇸🇦 Saudi Arabia",
	'af':"🇦🇫 Afghanistan",
	'az':"🇦🇿 Azerbaijan",
	'de': "🇩🇪 Deutsch",
	'tl': "🇵🇭 Filipino",
	'fi': "🇫🇮 Suomi",
	'hy':"🇦🇲 Armenia",
	'uk':"🇺🇦 Ukraine",
	'fr':"🇫🇷 France",
	'hi': "🇮🇳 India",
	'zh-CN':"🇨🇳 China",
	'nl': "🇳🇱 Nederlands",
	'sl': "🇸🇮 Slovensko",
	'sq': "🇦🇱 Shqip",
	'da': "🇩🇰 Dansk",
	'es':"🇪🇸 Spain",
	'tr':"🇹🇷 Turkey",
	'it':"🇮🇹 Italy",
	'kn':"🇨🇦 Canada",
	'de':"🇩🇪 Germany",
	'be':"🇧🇾 Belarus",
	'ko':"🇰🇵 North Korea",
	'ja':"🇯🇵 Japan",
	'en':"🇺🇸 United States"
	


}

async def lan_buttons():
	markup = InlineKeyboardMarkup(row_width=3)
	for key, value in language.items():
		markup.insert(InlineKeyboardButton(text=value,callback_data=f"key_{key}"))
	return markup 