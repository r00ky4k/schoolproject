import telebot, wikipedia, re
from telebot import types

bot = telebot.TeleBot('token')

wikipedia.set_lang("ru")




anton = 'Антон Стрельцов - создатель бота.\nУченик 11"А" класса.\nУвлекается спортом.\nЛюбимый предмет - физика, а так же нравятся информатика и физкультура.\nЛюбимый вид спорта - футбол.\nЛюбит много кушать, особенно пельмени.'
LA = 'Козлова Людмила Александровна - мой классный руководитель, а также преподаватель урока физики.\nОчень добрый, отзывчивый, честный и справедливый человек.'
AA = 'Cкойбеда Анастасия Анатольевна - руководитель моего проекта.\nЗаместитель директора, а также учитель информатики.\nОчень добрый, квалифицированный педагог. Всегда поможет, если что-то не получается, поддержит в трудную минуту, а любой сложный материал обьясняет доступным языком. На ее интересные уроки, мы ходим с удовольствием)+_.'
licey = 'Лицей - крупнейший образовательный комплекс Электрогорска, включающий два здания школы и два детских сада.\nНаши корпуса оснащены всем необходимым для качественной организации образовательного процесса, а образовательную деятельность ведут настоящие профессионалы своего дела!\nИменно здесь работают лучшие учителя города.'
inform = "Напиши текст и я найду статью в Википедии\n\nСписок команд: \n/start - старт бота \n/info - информация \n/author - Коротко о создателе проэкта\n/school - о школе\n/teachers - про пару учителей\n/links - полезные ссылки"
lincs = 'полезные ссылки:'


def getwiki(s):
    try:
        ny = wikipedia.page(s)
        wikitext=ny.content[:1000]
        wikimas=wikitext.split('.')
        wikimas = wikimas[:-1]
        wikitext2 = ''
        for x in wikimas:
            if not('==' in x):
                if(len((x.strip()))>3):
                    wikitext2=wikitext2+x+'.'
            else:
                break
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\{[^\{\}]*\}', '', wikitext2)
        return wikitext2
    except Exception as e:
        return f'Напишите более коректную информацию не получилось найти((('




@bot.message_handler(commands=["1"])
def phone(m, res=False):
    bot.send_message(m.chat.id, '/info /help /start /1 /teachers /autor /links' )

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Как пользоваться ботом: /info' )

@bot.message_handler(commands=["info"])
def help(m, res=False):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Школьная группа", url="https://vk.com/el_licey"))
    markup.add(types.InlineKeyboardButton("Страница Антона", url="https://vk.com/r00ky4k"))
    bot.send_message(m.chat.id, inform, reply_markup=markup)

@bot.message_handler(commands=["links"])
def help(m, res=False):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("github", url="https://github.com/r00ky4k/schoolproject"))
    markup.add(types.InlineKeyboardButton("Диск", url="https://disk.yandex.ru/d/moOtItfYFWOLZQ"))
    bot.send_message(m.chat.id, lincs, reply_markup=markup)

@bot.message_handler(commands=["help"])
def help(m, res=False):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Школьная группа", url="https://vk.com/el_licey"))
    markup.add(types.InlineKeyboardButton("Страница Антона", url="https://vk.com/r00ky4k"))
    bot.send_message(m.chat.id, inform, reply_markup=markup)

@bot.message_handler(commands=["author"])
def aurhor(m, res=False):
    markupsecond = types.InlineKeyboardMarkup()
    markupsecond.add(types.InlineKeyboardButton("Страница Антона", url="https://vk.com/r00ky4k"))
    bot.send_message(m.chat.id, anton, reply_markup=markupsecond )

@bot.message_handler(commands=["school"])
def info(m, res=False):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Школьная группа", url="https://vk.com/el_licey"))
    bot.send_message(m.chat.id, licey, reply_markup=markup )

@bot.message_handler(commands=["teachers"])
def info(m, res=False):
    markuph = types.InlineKeyboardMarkup()
    markuph.add(types.InlineKeyboardButton("Страница Анастасии Анатольевны", url="https://vk.com/licey_a"))
    markuph.add(types.InlineKeyboardButton("Страница Людмилы Александровны", url="https://school.mosreg.ru/user/user.aspx?user=1000000015856"))
    bot.send_message(m.chat.id, "Коротко об моих учителях:\n\n"+LA+"\n\n"+AA, reply_markup=markuph )

@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text =='Антон Стрельцов':
        markupsecond = types.InlineKeyboardMarkup()
        markupsecond.add(types.InlineKeyboardButton("Страница Антона", url="https://vk.com/r00ky4k"))
        bot.send_message(message.chat.id, anton, reply_markup=markupsecond)
    else:
        if message.text == 'Лицей':
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Школьная группа", url="https://vk.com/el_licey"))
            bot.send_message(message.chat.id, "По вашему запросу: " +message.text + " было найдено следующие: \n\n" + getwiki(message.text)+ "\n\nA также это школа в которой я учусь)", reply_markup=markup)
        else:
            if message.text =='Анастасия Анатольевна':
                markuph = types.InlineKeyboardMarkup()
                markuph.add(types.InlineKeyboardButton("Страница Анастасии Анатольевны", url="https://vk.com/licey_a"))
                bot.send_message(message.chat.id, AA , reply_markup=markuph)
            else:
                if message.text == 'Людмила Александровна':
                    markupsecond = types.InlineKeyboardMarkup()
                    markupsecond.add(types.InlineKeyboardButton("Страница Людмилы Александровны", url="https://school.mosreg.ru/user/user.aspx?user=1000000015856"))
                    bot.send_message(message.chat.id,LA,reply_markup=markupsecond)
                else:
                    if message.text == 'Стрельцов Антон':
                        markupsecond = types.InlineKeyboardMarkup()
                        markupsecond.add(types.InlineKeyboardButton("Страница Антона", url="https://vk.com/r00ky4k"))
                        bot.send_message(message.chat.id, anton, reply_markup=markupsecond)
                    else:
                        bot.send_message(message.chat.id, 'По вашему запросу "' +message.text + '" было найдено следующие: \n\n' + getwiki(message.text))


bot.polling(none_stop=True, interval=0)
