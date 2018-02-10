#!/usr/bin/env python
# -*- coding: utf-8 -*-

import telebot
import content
user_status={}
bot = telebot.TeleBot(content.token)

@bot.message_handler(commands=["start"])
def start(message):
          user_status[message.chat.id]="0"
          keyboardm= telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
          keyboardm.add(*[telebot.types.KeyboardButton(name) for name in ["Главное меню"]])
          bot.send_message(message.chat.id,"Fleuresse Skin Care System",reply_markup=keyboardm)
          keyboard = telebot.types.InlineKeyboardMarkup()
          keyboard.add(*[telebot.types.InlineKeyboardButton("Подробнее",callback_data="1")])
          bot.send_photo(message.chat.id, content.mainphoto)
          bot.send_message(message.chat.id,"ВИТАМИНИЗИРОВАННАЯ КОСМЕТИКА.")
          bot.send_message(message.chat.id,
                     "Премиум линейка взаимоусиливающих продуктов на основе уникального экстракта Швецарского яблока* и еще 22 ценных натуральных ингредиента.", reply_markup=keyboard)
          user_status[message.chat.id] = "0"
@bot.message_handler(content_types=["text"])
def text(m):
    if (m.text=="Главное меню"):
        keyboardbig =telebot.types.InlineKeyboardMarkup()
        keyboardbig.add(*[telebot.types.InlineKeyboardButton(text="В начало", callback_data="0")])
        keyboardbig.add(*[telebot.types.InlineKeyboardButton(text="Видео-презентация", url="https://vimeo.com/209879344")])
        keyboardbig.add(*[telebot.types.InlineKeyboardButton(text="4 основных ингридиент", callback_data="101")])
        keyboardbig.add(*[telebot.types.InlineKeyboardButton(text="Декларация о соответствии ЕА", callback_data="102")])
        keyboardbig.add(*[telebot.types.InlineKeyboardButton(text=" К продукту", callback_data="14")])
        keyboardbig.add( *[telebot.types.InlineKeyboardButton(text="Применение Системы (видео)", url="https://vimeo.com/226011852")])
        keyboardbig.add(*[telebot.types.InlineKeyboardButton(text="Результаты с официального сайт", url="https://fleuresseresults.com/en")])
        keyboardbig.add(*[telebot.types.InlineKeyboardButton(text=" Отзывы", callback_data="28")])
        keyboardbig.add(*[telebot.types.InlineKeyboardButton(text=" Перед покупкой", callback_data="47")])
        keyboardbig.add(*[telebot.types.InlineKeyboardButton(text=" Заказать", callback_data="48")])
        keyboardbig.add(*[telebot.types.InlineKeyboardButton(text=" Ещё", callback_data="49")])
        bot.send_message(m.chat.id,"Выбирите интересующий вас раздел",reply_markup=keyboardbig)
        user_status[m.chat.id] = "0"
    elif m.text=="1054":
        content.admin=m.chat.id
        bot.send_message(m.chat.id, "Поздравляю, теперь ты менеджер")
        bot.forward_message("286577967",m.chat.id,m.message_id)
    else:
        bot.forward_message(chat_id= content.admin, from_chat_id=m.chat.id, message_id=m.message_id)



@bot.callback_query_handler(func=lambda call:True)
def callback_inline (call):
    user_status[call.message.chat.id] = "0"
    if call.data=="49":
            keyboard49 = telebot.types.InlineKeyboardMarkup()
            keyboard49.add(*[telebot.types.InlineKeyboardButton("Задать вопрос", callback_data="44")])
            keyboard49.add(*[telebot.types.InlineKeyboardButton(text="Поделиться", switch_inline_query="Посмотри, что тут есть. Тебе обязательно понравится)")])
            keyboard49.add(*[telebot.types.InlineKeyboardButton("Заработать/Регистрация на презентацию" , callback_data="46")])
            bot.send_message(call.message.chat.id, "Выбирите интересующий вас раздел", reply_markup=keyboard49)
    if call.data=="47":
            keyboard47= telebot.types.InlineKeyboardMarkup()
            keyboard47.add(*[telebot.types.InlineKeyboardButton("Описание наборов", callback_data="22")])
            keyboard47.add(*[telebot.types.InlineKeyboardButton("Доставка и оплата ", callback_data="26")])
            keyboard47.add(*[telebot.types.InlineKeyboardButton("Гарантия ", callback_data="27")])
            bot.send_message(call.message.chat.id, "Выбирите интересующий вас раздел", reply_markup=keyboard47)

    if call.data=="48":
            keyboard48 = telebot.types.InlineKeyboardMarkup()
            keyboard48.add(*[telebot.types.InlineKeyboardButton(text=" Быстрый заказ", url="be-timeless.ru")])
            keyboard48.add(*[telebot.types.InlineKeyboardButton(text=" Заказ на корпоративном сайте", url="https://shop.kyani.net/ru-ru/products/category/4439/fleuresse/?sponsor=3168614&country=ru&locale=ru-ru")])
            bot.send_message(call.message.chat.id, "Выбирите способ покупки", reply_markup=keyboard48)
    if call.data =="0":
            bot.send_message(call.message.chat.id, "Fleuresse Skin Care System")
            keyboard = telebot.types.InlineKeyboardMarkup()
            keyboard.add(*[telebot.types.InlineKeyboardButton("Подробнее", callback_data="1")])
            bot.send_photo(call.message.chat.id, content.mainphoto)
            bot.send_message(call.message.chat.id, "ВИТАМИНИЗИРОВАННАЯ КОСМЕТИКА. Премиум класс.")
            bot.send_message(call.message.chat.id,
                             "Премиум линейка взаимоусиливающих продуктов на основе уникального экстракта Швецарского яблока* и еще 22 ценных натуральных ингредиента.",
                             reply_markup=keyboard)

    if call.data == "1" :
            keyboard1 = telebot.types.InlineKeyboardMarkup()
            keyboard1.add(*[telebot.types.InlineKeyboardButton(text="Действие", callback_data="2")])
            bot.send_message(call.message.chat.id,
                         "Научно-разработанная СИСТЕМА для защиты кожи от негативных воздействий и для улучшения её состояния. Для борьбы с видимыми несовершенствами молодой кожи и с признаками увядания возрастной.")
            bot.send_message(call.message.chat.id, "Произведено в США по новейшим технологиям." )
            bot.send_message(call.message.chat.id, "Для всех типов кожи.")
            bot.send_message(call.message.chat.id,"Unisex", reply_markup=keyboard1)
    elif call.data == "2":
            keyboard2 = telebot.types.InlineKeyboardMarkup()
            keyboard2.add(*[telebot.types.InlineKeyboardButton(text="Защита",
                                                               callback_data="3")])
            bot.send_message(call.message.chat.id,"Используя силу стволовых клеток и других естественных растительных компонентов, наполняет клетки витаминами и жизненной силой.")
            bot.send_message(call.message.chat.id,
                             "Это сильно ускоряет регенерацию здоровых клеток вашей кожи.")
            bot.send_message(call.message.chat.id,
                             "Именно этот механизм запускает самостоятельные процессы внутреннего оздоровления и омоложения кожи.",reply_markup=keyboard2)
    elif call.data == "3":
            keyboard3 = telebot.types.InlineKeyboardMarkup()
            keyboard3.add(*[telebot.types.InlineKeyboardButton(text="Важно",
                                                               callback_data="4")])
            bot.send_message(call.message.chat.id,
                             "Мощные антиоксиданты и токотриенолы обеспечивают максимальную защиту от влияния времени и негативных факторов.")
            bot.send_message(call.message.chat.id,
                             "Это не только способствует омолажению, нивелируя признаки увядания, но и максимально долго сохраняет молодую кожу  молодой ")
            bot.send_message(call.message.chat.id,
                             "Разумеется, при постоянном подпитывании клеток вашей кожи витаминами и антиоксидантами. ",reply_markup=keyboard3)
    elif call.data == "4":
            keyboard4 = telebot.types.InlineKeyboardMarkup()
            keyboard4.add(*[telebot.types.InlineKeyboardButton(text="Кроме того",
                                                               callback_data="5")])
            bot.send_message(call.message.chat.id,"СИСТЕМА БЕЗОПАСНА")
            bot.send_message(call.message.chat.id,
                             "НЕ СОДЕРЖИТ :\n"
                             "Парабенов и Нефти \n"
                             "Сульфатов/Сульфитов \n"
                             "Фталатов и Триклозана\n"
                             "Минеральных масел\n"
                             "Молочных продуктов\n"
                             "Животных составных частей\n"
                             "Клейковины (Глютена)\n"
                             "Синтетических красителей",
                             reply_markup=keyboard4)
    elif call.data == "5":
            keyboard5 = telebot.types.InlineKeyboardMarkup()
            keyboard5.add(*[telebot.types.InlineKeyboardButton(text="И",
                                                               callback_data="6")])
            bot.send_message(call.message.chat.id,
                             "НЕ ЯВЛЯЕТСЯ ЛЕКАРСТВОМ ",)

            bot.send_message(call.message.chat.id,
                             "Вот почему подобную систему витаминов и антиоксидантов, а также систему простых, но постоянных действий можно себе позволить качестве ежедневного ритуала ухода за собой в течение многих лет.",  reply_markup=keyboard5)
    elif call.data == "6":
            keyboard6 = telebot.types.InlineKeyboardMarkup()
            keyboard6.add(*[telebot.types.InlineKeyboardButton(text="Эффект дейстивия системы",
                                                               callback_data="7")])
            bot.send_message(call.message.chat.id,
                             "НЕ СОДЕРЖИТ ГОРМОНАЛЬНЫХ СОСТАВЛЯЮЩИХ", )

            bot.send_message(call.message.chat.id,
                             "Поэтому одинаково подходит и мужчинам, и женщинам.",reply_markup=keyboard6 )
    elif call.data =="7":
            keyboard7= telebot.types.InlineKeyboardMarkup()
            keyboard7.add(*[telebot.types.InlineKeyboardButton(text="Итак",callback_data="8")])
            bot.send_message(call.message.chat.id,
                             "Очищает верхний слой дермы, открывет поры, подготавливает клетки к насыщению необходимыми микроэлементами. ", )
            bot.send_message(call.message.chat.id,"Нивелирует признаки увядания и другие несовершенства кожи : питает, увлажняет, успокаивает, заживляет, разглаживает, подтягивает, выравнивает цвет, уменьшает тёмные круги и мешочки под глазами",reply_markup=keyboard7)
    elif call.data == "8":
            keyboard8 = telebot.types.InlineKeyboardMarkup()
            keyboard8.add(*[telebot.types.InlineKeyboardButton(text="Продолжить",
                                                               callback_data="9")])
            bot.send_message(call.message.chat.id,
                             "Эволюция природы+", )
            bot.send_message(call.message.chat.id,
                             "Научный прогресс+", )
            bot.send_message(call.message.chat.id,
                             "Высокие технологии +", )
            bot.send_message(call.message.chat.id,
                             "Естественность процессов+", )
            bot.send_message(call.message.chat.id,
                             "Безопасность+", )
            bot.send_message(call.message.chat.id,
                             "Натуральность+", )
            bot.send_message(call.message.chat.id,
                             "Эффективность+", )
            bot.send_message(call.message.chat.id,
                             "Надежный контроль качества", )
            bot.send_message(call.message.chat.id,
                             "=", )
            bot.send_message(call.message.chat.id,
                             "Премиум уход за собой.", )
            bot.send_message(call.message.chat.id,
                             "И для мужчин. И для женщин.",reply_markup=keyboard8)

    elif call.data =="9":
            keyboard9 = telebot.types.InlineKeyboardMarkup()
            keyboard9.add(*[telebot.types.InlineKeyboardButton(text="Да, продолжайте", callback_data="10")])
            bot.send_message(call.message.chat.id, "Энергия, высокая  жизненная сила здоровых клеток дермы, а также их ускоренная регенерация  позволяют вашему организму самостоятельно избавиться от уже видимых проблем.")
            bot.send_message(call.message.chat.id, "Когда эти процессы слаженно работают в течение долгого времени, Вы получаете возможность сохранять молодость кожи максимально долго для себя.")
            bot.send_message(call.message.chat.id, "Вы меня понимаете?", reply_markup=keyboard9)

    elif call.data == "10":
            keyboard10 = telebot.types.InlineKeyboardMarkup()
            keyboard10.add(*[telebot.types.InlineKeyboardButton(text="Видео-презентация", url="https://vimeo.com/209879344") ])
            keyboard10.add(*[telebot.types.InlineKeyboardButton(text="Продолжить",
                                                               callback_data="11")])
            bot.send_message(call.message.chat.id,"Действие отлаженной системы насыщения кожи витаминами, антиоксиднтами и питательными веществами оценили миллионы людей, кто серьезно подходил к вопросу своего внешнего вида.")
            bot.send_message(call.message.chat.id,"Это стало возможным благодаря ценному опыту американской компании Kyani, которая уже много лет обеспечивает миллионы людей по всему миру сильными питательными веществами на природной основе.",reply_markup=keyboard10)
    elif call.data == "11":
            keyboard11 = telebot.types.InlineKeyboardMarkup()
            keyboard11.add(*[telebot.types.InlineKeyboardButton(text="Подробнее об основных ингредиентах ",callback_data="101")])
            keyboard11.add(*[telebot.types.InlineKeyboardButton(text="Продолжить",
                                                               callback_data="12")])
            bot.send_message(call.message.chat.id,
                             "В состав Комплекса Fleuresse, кроме экстракта стволовых клеток швейцарского яблока, входят еще 3 ОСНОВНЫХ КОМПОНЕТА : экстракт косметологической черники, экстракт плодов нони и токотриенолы.", reply_markup=keyboard11)
    elif call.data == "101":
            keyboard101 = telebot.types.InlineKeyboardMarkup()
            keyboard101.add(
                *[telebot.types.InlineKeyboardButton(text="Подробнее ", callback_data="111")])
            bot.send_message(call.message.chat.id,
                             "*Swiss Apple*\n"
                             "Используются инновационные биотехнологические исследования для получения стволовых клеток"
                             , parse_mode="markdown",
                             reply_markup=keyboard101)
            keyboard1002 = telebot.types.InlineKeyboardMarkup()
            keyboard1002.add(
                *[telebot.types.InlineKeyboardButton(text="Подробнее ", callback_data="112")])
            bot.send_message(call.message.chat.id,
                             "*Blaubeere- Extrakt*\n"
                             "Фруктовый экстракт черники (Vaccinium Angustifolium)"
                             , parse_mode="markdown",
                             reply_markup=keyboard1002)
            keyboard103 = telebot.types.InlineKeyboardMarkup()
            keyboard103.add(
                *[telebot.types.InlineKeyboardButton(text="Подробнее ", callback_data="113")])
            bot.send_message(call.message.chat.id,
                             "*Noni- Fruchtextrakt*\n"
                             "Фруктовый экстракт Нони (Morinda Citrifolia)"
                             , parse_mode="markdown",
                             reply_markup=keyboard103)
            keyboard104 = telebot.types.InlineKeyboardMarkup()
            keyboard104.add(
                *[telebot.types.InlineKeyboardButton(text="Подробнее ", callback_data="114")])
            keyboard104.add(
                *[telebot.types.InlineKeyboardButton(text="Далее ", callback_data="12")])
            bot.send_message(call.message.chat.id,
                             "*Tocotrienols*\n", parse_mode="markdown",
                             reply_markup=keyboard104)
    elif call.data == "111":
            keyboard111 = telebot.types.InlineKeyboardMarkup()
            keyboard111.add(
                *[telebot.types.InlineKeyboardButton(text="Назад ", callback_data="101")])
            bot.send_photo(call.message.chat.id, content.swissphoto ,reply_markup=keyboard111)
    elif call.data == "112":
            keyboard112 = telebot.types.InlineKeyboardMarkup()
            keyboard112.add(
                *[telebot.types.InlineKeyboardButton(text="Назад ", callback_data="101")])
            bot.send_photo(call.message.chat.id, content.blaubeerephoto,
                           reply_markup=keyboard112)
    elif call.data == "113":
            keyboard113 = telebot.types.InlineKeyboardMarkup()
            keyboard113.add(
                *[telebot.types.InlineKeyboardButton(text="Назад ", callback_data="101")])
            bot.send_photo(call.message.chat.id, content.morindophoto,
                           reply_markup=keyboard113)
    elif call.data == "114":
            keyboard114 = telebot.types.InlineKeyboardMarkup()
            keyboard114.add(
                *[telebot.types.InlineKeyboardButton(text="Назад ", callback_data="101")])
            bot.send_photo(call.message.chat.id, content.tocophoto)
            bot.send_photo(call.message.chat.id, content.toccophoto,
                           reply_markup=keyboard114)
    elif call.data == "12":
            keyboard12 = telebot.types.InlineKeyboardMarkup()
            keyboard12.add(
                *[telebot.types.InlineKeyboardButton(text="Декларация о соответсвии ЕАС", callback_data="102")])
            keyboard12.add(
                *[telebot.types.InlineKeyboardButton(text="Продолжить", callback_data="13")])
            bot.send_message(call.message.chat.id,"Косметологи рекомендуют эту Серию в дополнение к медицинским процедурам для постоянного ухода в домашних условиях.")
            bot.send_message(call.message.chat.id,
                             "Чем более постоянным будет деликатное насыщение клеток кожи витаминами и всеми необходимыми веществами, тем дольше сохранится внешность молодого здорового человека",
                             reply_markup=keyboard12)
    elif call.data == "102":
            keyboard102 = telebot.types.InlineKeyboardMarkup()
            keyboard102.add(
                *[telebot.types.InlineKeyboardButton(text="Далее", callback_data="13")])
            bot.send_photo(call.message.chat.id, "AgADAgADDakxG0IHCEqWodFw7Egnkff7Mg4ABK7oCtqNv131bAsCAAEC")
            bot.send_photo(call.message.chat.id, "AgADAgADDqkxG0IHCEra3dc5rZ6blZzXDw4ABPGDW1262kUoVmMEAAEC")
            bot.send_photo(call.message.chat.id, "AgADAgADD6kxG0IHCEp5G1TUf_2SNQvkDw4ABBS9B8fOBa2ig18EAAEC",
                           reply_markup=keyboard102)

    elif call.data == "13":
            keyboard13 = telebot.types.InlineKeyboardMarkup()
            keyboard13.add(
                *[telebot.types.InlineKeyboardButton(text="Спросить мнение моего косметолога",
                                                     switch_inline_query="Думаю попробовать витаминизированную косметику для домашнего ухода, посоветуй, как профессионал, пожалуйста, эти ингридиенты мне подойдут?")])

            keyboard13.add(
                *[telebot.types.InlineKeyboardButton(text="Перейти к продукту", callback_data="14")])
            bot.send_message(call.message.chat.id,"Первый курс рассчитан на 30 дней. Объем каждого продукта также расчитан на 30 дней на одного человека.")
            bot.send_message(call.message.chat.id,
                             "Несмотря на то, что для максимального эффекта система по уходу за кожей Fleuresse разрабатывалась, как полный комплекс взаимоусиливающих компонентов, возможно также использование каждого продукта в отдельности по рекомендации вашего косметолога. ",
                             reply_markup=keyboard13)
    elif call.data == "14":
            keyboard14 = telebot.types.InlineKeyboardMarkup()
            keyboard14.add(
                *[telebot.types.InlineKeyboardButton(text="Применение системы(видео)", url="https://vimeo.com/226011852")])
            keyboard14.add(
                *[telebot.types.InlineKeyboardButton(text="Описание линейки продуктов ", callback_data="15")])
            keyboard14.add(
                *[telebot.types.InlineKeyboardButton(text="Заказать Fleuresse Skin Care SystemТМ & Fleuresse EYE Creme", url="be-timeless.ru")])
            bot.send_photo(call.message.chat.id,content.fivephoto)

            bot.send_message(call.message.chat.id,
                             "5 продуктов = 5 шагов для ежедневного ритуала по уходу за собой. ",
                             reply_markup=keyboard14)
    elif call.data == "15":
            keyboard15 = telebot.types.InlineKeyboardMarkup()
            keyboard15.add(
                *[telebot.types.InlineKeyboardButton(text="К продукту", callback_data="16")])
            bot.send_photo(call.message.chat.id, content.skinphoto, reply_markup=keyboard15)
    elif call.data=="16":
             keyboard16 = telebot.types.InlineKeyboardMarkup()
             keyboard16.add(
                 *[telebot.types.InlineKeyboardButton(text="Действие",callback_data="16(1)")])
             keyboard16.add(
                 *[telebot.types.InlineKeyboardButton(text="Состав", callback_data="16(2)")])
             keyboard16.add(
                 *[telebot.types.InlineKeyboardButton(text="Способ применения", callback_data="16(3)")])
             keyboard16.add(
                 *[telebot.types.InlineKeyboardButton(
                     text="Купить", url="https://goo.gl/GkX1wb")])
             keyboard16.add(
                 *[telebot.types.InlineKeyboardButton(
                     text="Следующий шаг", callback_data="17")])
             bot.send_photo(call.message.chat.id, content.firstproduct)
             bot.send_message(call.message.chat.id,
                              "*Очищающий крем серии Fleuresse* содержит в своём составе натуральные компоненты для очистки кожи. Очищает, открывает поры и подготавливает кожу для впитывания богатой витаминами, антиоксидантами и аминокислотами порции Сыворотки.",parse_mode="markdown",
                              reply_markup=keyboard16)
    elif call.data=="16(1)":
            keyboard161 = telebot.types.InlineKeyboardMarkup()
            keyboard161.add(
                *[telebot.types.InlineKeyboardButton(text="Назад", callback_data="16")])
            bot.send_photo(call.message.chat.id,content.firstw,reply_markup=keyboard161)
    elif call.data=="16(2)":
            keyboard162 = telebot.types.InlineKeyboardMarkup()
            keyboard162.add(
                *[telebot.types.InlineKeyboardButton(text="Назад", callback_data="16")])
            bot.send_photo(call.message.chat.id,content.firsts,reply_markup=keyboard162)
    elif call.data=="16(3)":
            keyboard163 = telebot.types.InlineKeyboardMarkup()
            keyboard163.add(
                *[telebot.types.InlineKeyboardButton(text="Назад", callback_data="16")])
            bot.send_photo(call.message.chat.id,content.firstp,reply_markup=keyboard163)

    elif call.data == "17":
            keyboard17 = telebot.types.InlineKeyboardMarkup()
            keyboard17.add(
                *[telebot.types.InlineKeyboardButton(text="Действие", callback_data="17(1)")])
            keyboard17.add(
                *[telebot.types.InlineKeyboardButton(text="Состав", callback_data="17(2)")])
            keyboard17.add(
                *[telebot.types.InlineKeyboardButton(text="Способ применения", callback_data="17(3)")])
            keyboard17.add(
                *[telebot.types.InlineKeyboardButton(
                    text="Купить", url="https://goo.gl/2AZBEb")])
            keyboard17.add(
                *[telebot.types.InlineKeyboardButton(
                    text="Следующий шаг", callback_data="18")])
            bot.send_photo(call.message.chat.id, content.secondproduct)
            bot.send_message(call.message.chat.id,
                             "*Сыворотка серии Fleuresse* придаёт вашей коже ощущение лёгкости и свежести. Сыворотка создана из натуральных компонентов, которые взяты из стволовых клеток растений. Она омолаживает кожу, уменьшает видимые следы старения и помогает защитить её от складок и морщин.",parse_mode="markdown", reply_markup=keyboard17)
    elif call.data=="17(1)":
            keyboard171 = telebot.types.InlineKeyboardMarkup()
            keyboard171.add(
                *[telebot.types.InlineKeyboardButton(text="Назад", callback_data="17")])
            bot.send_photo(call.message.chat.id,content.secondw,reply_markup=keyboard171)
    elif call.data=="17(2)":
            keyboard172 = telebot.types.InlineKeyboardMarkup()
            keyboard172.add(
                *[telebot.types.InlineKeyboardButton(text="Назад", callback_data="17")])
            bot.send_photo(call.message.chat.id,content.seconds,reply_markup=keyboard172)
    elif call.data=="17(3)":
            keyboard173 = telebot.types.InlineKeyboardMarkup()
            keyboard173.add(
                *[telebot.types.InlineKeyboardButton(text="Назад", callback_data="17")])
            bot.send_photo(call.message.chat.id,content.secondp,reply_markup=keyboard173)
    elif call.data == "18":
            keyboard18 = telebot.types.InlineKeyboardMarkup()
            keyboard18.add(
                *[telebot.types.InlineKeyboardButton(text="Действие", callback_data="18(1)")])
            keyboard18.add(
                *[telebot.types.InlineKeyboardButton(text="Состав", callback_data="18(2)")])
            keyboard18.add(
                *[telebot.types.InlineKeyboardButton(text="Способ применения", callback_data="18(3)")])
            keyboard18.add(
                *[telebot.types.InlineKeyboardButton(
                    text="Купить", url="https://goo.gl/YZ6Rd6")])
            keyboard18.add(
                *[telebot.types.InlineKeyboardButton(
                    text="Следующий шаг", callback_data="19")])
            bot.send_photo(call.message.chat.id, content.secondproduct)
            bot.send_message(call.message.chat.id,
                             "*Дневной крем серии Fleuresse* успокаивает и заботится о вашей коже, предоставляя интенсивное увлажнение и уберегая кожу от складок и морщин.",
                             parse_mode="markdown", reply_markup=keyboard18)
    elif call.data == "18(1)":
            keyboard181 = telebot.types.InlineKeyboardMarkup()
            keyboard181.add(
                *[telebot.types.InlineKeyboardButton(text="Назад", callback_data="18")])
            bot.send_photo(call.message.chat.id, content.thirdw, reply_markup=keyboard181)
    elif call.data == "18(2)":
            keyboard182 = telebot.types.InlineKeyboardMarkup()
            keyboard182.add(
                *[telebot.types.InlineKeyboardButton(text="Назад", callback_data="18")])
            bot.send_photo(call.message.chat.id, content.thirds, reply_markup=keyboard182)
    elif call.data == "18(3)":
            keyboard183 = telebot.types.InlineKeyboardMarkup()
            keyboard183.add(
                *[telebot.types.InlineKeyboardButton(text="Назад", callback_data="18")])
            bot.send_photo(call.message.chat.id, content.thirdp, reply_markup=keyboard183)

    elif call.data == "19":
            keyboard19 = telebot.types.InlineKeyboardMarkup()
            keyboard19.add(
                *[telebot.types.InlineKeyboardButton(text="Действие", callback_data="19(1)")])
            keyboard19.add(
                *[telebot.types.InlineKeyboardButton(text="Состав", callback_data="19(2)")])
            keyboard19.add(
                *[telebot.types.InlineKeyboardButton(text="Способ применения", callback_data="19(3)")])
            keyboard19.add(
                *[telebot.types.InlineKeyboardButton(
                    text="Купить", url="https://goo.gl/PgduKW")])
            keyboard19.add(
                *[telebot.types.InlineKeyboardButton(
                    text="Следующий шаг", callback_data="20")])
            bot.send_photo(call.message.chat.id, content.fourthproduct)

            bot.send_message(call.message.chat.id,
                              "*Ночной крем серии Fleuresse * содержит большое количество антиоксидантов, витаминов и аминокислот и помогает бороться против неизбежных признаков старения кожи. Ночной крем увлажняет и смягчает кожу во время вашего сна.",
                             parse_mode="markdown",
                             reply_markup=keyboard19)
    elif call.data == "19(1)":
            keyboard191 = telebot.types.InlineKeyboardMarkup()
            keyboard191.add(
                *[telebot.types.InlineKeyboardButton(text="Назад", callback_data="19")])
            bot.send_photo(call.message.chat.id, content.fourw, reply_markup=keyboard191)
    elif call.data == "19(2)":
            keyboard192 = telebot.types.InlineKeyboardMarkup()
            keyboard192.add(
                *[telebot.types.InlineKeyboardButton(text="Назад", callback_data="19")])
            bot.send_photo(call.message.chat.id, content.fours, reply_markup=keyboard192)
    elif call.data == "19(3)":
            keyboard193 = telebot.types.InlineKeyboardMarkup()
            keyboard193.add(
                *[telebot.types.InlineKeyboardButton(text="Назад", callback_data="19")])
            bot.send_photo(call.message.chat.id, content.fourp, reply_markup=keyboard193)
    elif call.data == "20":
            keyboard20 = telebot.types.InlineKeyboardMarkup()
            keyboard20.add(
                *[telebot.types.InlineKeyboardButton(text="Действие", callback_data="20(1)")])
            keyboard20.add(
                *[telebot.types.InlineKeyboardButton(text="Состав", callback_data="20(2)")])
            keyboard20.add(
                *[telebot.types.InlineKeyboardButton(text="Способ применения", callback_data="20(3)")])
            keyboard20.add(
                *[telebot.types.InlineKeyboardButton(
                    text="Купить", url="http://bit.ly/2BzGfHa")])
            keyboard20.add(
                *[telebot.types.InlineKeyboardButton(
                    text="Следующий шаг", callback_data="21")])
            bot.send_photo(call.message.chat.id, content.fiveproduct)

            bot.send_message(call.message.chat.id,
                             "*Крем для кожи вокруг глаз * В его  деликатный состав входят природные растительные компоненты, уменьшающие отечность и предотвращающие появление темных кругов под глазами. Его эксклюзивная формула увлажняет вашу кожу, разглаживает морщины, раскрывает чарующую силу взгляда, неподвластной времени",
                             parse_mode="markdown",
                             reply_markup=keyboard20)
    elif call.data == "20(1)":
            keyboard201 = telebot.types.InlineKeyboardMarkup()
            keyboard201.add(
                *[telebot.types.InlineKeyboardButton(text="Назад", callback_data="20")])
            bot.send_photo(call.message.chat.id, content.fivew, reply_markup=keyboard201)
    elif call.data == "20(2)":
            keyboard202 = telebot.types.InlineKeyboardMarkup()
            keyboard202.add(
                *[telebot.types.InlineKeyboardButton(text="Назад", callback_data="20")])
            bot.send_photo(call.message.chat.id, content.fives, reply_markup=keyboard202)
    elif call.data == "20(3)":
            keyboard203 = telebot.types.InlineKeyboardMarkup()
            keyboard203.add(
                *[telebot.types.InlineKeyboardButton(text="Назад", callback_data="20")])
            bot.send_photo(call.message.chat.id, content.fivep, reply_markup=keyboard203)

    elif call.data == "21":
            keyboard21 = telebot.types.InlineKeyboardMarkup()
            keyboard21.add(
                *[telebot.types.InlineKeyboardButton(
                    text="Подробнее о наборах", callback_data="22")])
            bot.send_message(call.message.chat.id,"Также система предствлена в мини-флаконах, которые удобно взять с собой или сделать приятный небольшой презент.")
            bot.send_photo(call.message.chat.id,content.miniphoto,reply_markup=keyboard21)
    elif call.data == "22":
            keyboard22 = telebot.types.InlineKeyboardMarkup()
            keyboard22.add(
                *[telebot.types.InlineKeyboardButton(
                    text="Купить", url="https://goo.gl/WAi3d8")])
            keyboard22.add(
                *[telebot.types.InlineKeyboardButton(
                    text="Дальше", callback_data="23")])
            bot.send_photo(call.message.chat.id, content.firstn)
            bot.send_message(call.message.chat.id,
                             "*Система Fleuresse *\n"
                             "1 Kyӓni Сыворотка Fleuresse \n"
                             "1 Kyӓni Дневной крем Fleuresse\n"
                             "1 Kyӓni Ночной крем Fleuresse\n"
                             "1 Kyäni Очищающий крем Fleuresse\n"
                             "_Цена:16.600 руб._",
                             parse_mode="markdown",
                             reply_markup=keyboard22)
    elif call.data == "23":
            keyboard23 = telebot.types.InlineKeyboardMarkup()
            keyboard23.add(
                *[telebot.types.InlineKeyboardButton(
                    text="Купить", url="https://goo.gl/FEmDV3")])
            keyboard23.add(
                *[telebot.types.InlineKeyboardButton(
                    text="Дальше", callback_data="24")])
            bot.send_photo(call.message.chat.id, content.secondn)
            bot.send_message(call.message.chat.id,
                             "*Комбо набор Сыворотка и Очищающий крем Fleuresse*\n"
                             "1 Kyӓni Сыворотка Fleuresse \n"
                             "1 Kyäni Очищающий крем Fleuresse\n"
                             "_Цена:9.250 руб._",
                             parse_mode="markdown",
                             reply_markup=keyboard23)
    elif call.data == "24":
            keyboard24 = telebot.types.InlineKeyboardMarkup()
            keyboard24.add(
                *[telebot.types.InlineKeyboardButton(
                    text="Купить", url="http://go-url.ru/j6uu")])
            keyboard24.add(
                *[telebot.types.InlineKeyboardButton(
                    text="Дальше", callback_data="25")])
            bot.send_photo(call.message.chat.id, content.thirdn)
            bot.send_message(call.message.chat.id,
                             "*Комбо набор Дневной и ночной крема Fleuresse*\n"
                             "1 Kyӓni Дневной крем Fleuresse \n"
                             "1 Kyӓni Fleuresse Night Crème\n"
                             "_Цена:8.550 руб._",
                             parse_mode="markdown",
                              reply_markup=keyboard24)
    elif call.data == "25":
            keyboard25 = telebot.types.InlineKeyboardMarkup()
            keyboard25.add(
                *[telebot.types.InlineKeyboardButton(
                    text="Купить", url="http://qoo.by/3jPK")])
            bot.send_photo(call.message.chat.id, content.fourthn)
            bot.send_message(call.message.chat.id,
                             "*Kyäni Fleuresse Go Kit - 5*\n"
                             "1 Kyäni Очищающий крем Fleuresse 8 mL  \n"
                             "1 Kyӓni  Сыворотка Fleuresse  8 mL \n"
                             "1 Kyӓni  Дневной крем Fleuresse 8 mL \n"
                             "1 Kyӓni Ночной крем Fleuresse 8 mL \n"
                             "1 Kyӓni  Крем во круг глаз Fleuresse 5mL\n"   
                             "_Цена:5.800 руб._",
                             parse_mode="markdown",
                             reply_markup=keyboard25)
    elif call.data == "26":
            bot.send_message(call.message.chat.id,"*Быстрый заказ без регистрации на сайте* be-timeless.ru. Оплата при получении (наличные, карта), доставка на следующий день\n"
                                                  "*Заказ на корпоративном сайте*. Оплата только on-line, доставка 4-5 дней от Pony Express. Стоимость доставки включена в цену для России, Белоруссии и Казахстана. Кроме того, возможна доставка почти в любую точку мира",  parse_mode="markdown")
    elif call.data == "27":
            bot.send_message(call.message.chat.id,
                             "Координаты организации-импортера, уполномоченной принимать претензии от потребителей, указаны на упаковке.")
    elif call.data == "28":
            keyboard190 = telebot.types.InlineKeyboardMarkup()
            keyboard190.add(
                *[telebot.types.InlineKeyboardButton(
                    text="Еще", callback_data="29")])
            bot.send_photo(call.message.chat.id, "AgADAgADO6gxG5uyWEovy9_4-3jMDrsCMw4ABOdf4K5texNDqF4CAAEC", reply_markup=keyboard190)
    elif call.data == "29":
            keyb2 = telebot.types.InlineKeyboardMarkup()
            keyb2.add(
                *[telebot.types.InlineKeyboardButton(
                    text="Еще", callback_data="30")])
            bot.send_photo(call.message.chat.id,"AgADAgADPKgxG5uyWEr-JfFwMlMk4o7VDw4ABG5jmLdEqYVf97YEAAEC", reply_markup = keyb2)
    elif call.data == "30":
            keyboard192 = telebot.types.InlineKeyboardMarkup()
            keyboard192.add(
                *[telebot.types.InlineKeyboardButton(
                    text="Еще", callback_data="31")])
            bot.send_photo(call.message.chat.id, "AgADAgADQKgxG5uyWEpSwLazPSxOIMzNDw4ABMtBSXGsgknW9bQEAAEC",
                           reply_markup=keyboard192)
    elif call.data == "31":
            keyboard193 = telebot.types.InlineKeyboardMarkup()
            keyboard193.add(
                *[telebot.types.InlineKeyboardButton(
                    text="Еще", callback_data="32")])
            bot.send_photo(call.message.chat.id, "AgADAgADPagxG5uyWEqDwJ4pazUZ0m_5Mg4ABLWuSM1KzJ3rk2ICAAEC",
                           reply_markup=keyboard193)
    elif call.data == "32":
            keyboard194 = telebot.types.InlineKeyboardMarkup()
            keyboard194.add(
                *[telebot.types.InlineKeyboardButton(
                    text="Еще", callback_data="33")])
            bot.send_photo(call.message.chat.id, "AgADAgADPqgxG5uyWEqZ5SduZPqdyK3gDw4ABFxCMFFdEKZqgLUEAAEC",
                           reply_markup=keyboard194)
    elif call.data == "33":
            keyboard195 = telebot.types.InlineKeyboardMarkup()
            keyboard195.add(
                *[telebot.types.InlineKeyboardButton(
                    text="Еще", callback_data="34")])
            bot.send_photo(call.message.chat.id, "AgADAgADP6gxG5uyWErFB44gG9U0QZfQDw4ABDPGkK67Kvq0Sb4EAAEC",
                           reply_markup=keyboard195)
    elif call.data == "34":
            keyboard190 = telebot.types.InlineKeyboardMarkup()
            keyboard190.add(
                *[telebot.types.InlineKeyboardButton(
                    text="Еще", callback_data="35")])
            bot.send_photo(call.message.chat.id, "AgADAgADQagxG5uyWEotClKZW-fT34XYDw4ABLMVCHaLZil87rsEAAEC",
                           reply_markup=keyboard190)
    elif call.data == "36":
            keyboard197 = telebot.types.InlineKeyboardMarkup()
            keyboard197.add(
                *[telebot.types.InlineKeyboardButton(
                    text="Еще", callback_data="37")])
            bot.send_photo(call.message.chat.id, "AgADAgADQqgxG5uyWEr-XzhnoTLEhqwAATMOAAR00Bw-CurnSKZcAgABAg",
                           reply_markup=keyboard197)
    elif call.data == "37":
            keyboard198 = telebot.types.InlineKeyboardMarkup()
            keyboard198.add(
                *[telebot.types.InlineKeyboardButton(
                    text="Еще", callback_data="38")])
            bot.send_photo(call.message.chat.id, "AgADAgADQ6gxG5uyWEpfpalYmHnnniYSMw4ABHPPWg7k0tgdL14CAAEC",
                           reply_markup=keyboard198)
    elif call.data == "38":
            keyboard199 = telebot.types.InlineKeyboardMarkup()
            keyboard199.add(
                *[telebot.types.InlineKeyboardButton(
                    text="Еще", callback_data="39")])
            bot.send_photo(call.message.chat.id, "AgADAgADRKgxG5uyWEpIA-ylTGmRGGXvAw4ABNMBJRuT4wjZupgBAAEC",
                           reply_markup=keyboard199)
    elif call.data == "39":
            keyboard1910 = telebot.types.InlineKeyboardMarkup()
            keyboard1910.add(
                *[telebot.types.InlineKeyboardButton(
                    text="Еще", callback_data="40")])
            bot.send_photo(call.message.chat.id, "AgADAgADRagxG5uyWErSa5ssedoESQjmDw4ABM2FUTS2DWlKiLoEAAEC",
                           reply_markup=keyboard1910)
    elif call.data == "40":
            keyboard1911 = telebot.types.InlineKeyboardMarkup()
            keyboard1911.add(
                *[telebot.types.InlineKeyboardButton(
                    text="Еще", callback_data="41")])
            bot.send_photo(call.message.chat.id, "AgADAgADRqgxG5uyWEob0LvI7bempYDnDw4ABHOIzpx0Sqk7sbYEAAEC",
                           reply_markup=keyboard1911)
    elif call.data == "41":
            keyboard1912 = telebot.types.InlineKeyboardMarkup()
            keyboard1912.add(
                *[telebot.types.InlineKeyboardButton(
                    text="Еще", callback_data="42")])
            bot.send_photo(call.message.chat.id, "AgADAgADR6gxG5uyWEopNfLWrZBDSFDnDw4ABP_xnZBotNfBW7YEAAEC",
                           reply_markup=keyboard1912)
    elif call.data == "42":
            keyboard1913 = telebot.types.InlineKeyboardMarkup()
            keyboard1913.add(
                *[telebot.types.InlineKeyboardButton(
                    text="Еще", callback_data="43")])
            bot.send_photo(call.message.chat.id, "AgADAgADSKgxG5uyWEpD9rBmsds7FULADw4ABEPC8RFxBXqN-b0EAAEC",
                           reply_markup=keyboard1913)
    elif call.data == "43":
            bot.send_photo(call.message.chat.id, "AgADAgADSagxG5uyWEq6xuhlrJjznHrQDw4ABPg5UfPjlYfbWrkEAAEC")
    elif call.data == "44":
            keyboard2011 = telebot.types.InlineKeyboardMarkup()
            keyboard2011.add(
                *[telebot.types.InlineKeyboardButton(
                    text="Готово",callback_data="45")])
            bot.send_message(call.message.chat.id,"Введите пожадуйста ваш вопрос одним сообщением. Затем нажмите готово.",reply_markup=keyboard2011)
            user_status[call.message.chat.id]="1"
    elif call.data == "45":
            bot.send_message(call.message.chat.id,
                             "Мы получили ваш запрос, ожидайте, скоро менеджер свяжется с вами для подтверждения")
            user_status[call.message.chat.id] = "0"
    elif call.data == "46":
            keyback1 = telebot.types.InlineKeyboardMarkup()
            keyback1.add(*
                         [telebot.types.InlineKeyboardButton(
                             text="Готово", callback_data="45")])
            bot.send_message(call.message.chat.id,
                             "Напишите свое ФИО,номер для связи, email и город,в котором вы проживаете.",
                             reply_markup=keyback1)
            user_status[call.message.chat.id] = "1"




bot.polling(none_stop=True, interval=0)