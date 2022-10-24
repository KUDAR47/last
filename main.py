

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


bot = Bot(token='5669086755:AAGLDFhWkpo-KCg4I0wcs6_o_gzWIiajXKM')
dp = Dispatcher(bot)

button1 = InlineKeyboardButton(text="Year(3)")
button2 = InlineKeyboardButton(text="Year(2)")
button3 = InlineKeyboardButton(text="Year(1)")
button4 = InlineKeyboardButton(text="Year(4)")
button5 = InlineKeyboardButton(text="first term")
button6 = InlineKeyboardButton(text="second term")
button7 = InlineKeyboardButton(text="Location", request_location=True)
button9 = InlineKeyboardButton(text="Python")
button10= InlineKeyboardButton(text="theory of mechine")
button11= InlineKeyboardButton(text="seeds of research")
button12= InlineKeyboardButton(text="Thermodynamics")
button13= InlineKeyboardButton(text="Analog electronic circuit")
button14= InlineKeyboardButton(text="analog program of electrical engineering")
button15= InlineKeyboardButton(text="contact us")



keyboard_inline = InlineKeyboardMarkup().add(button1, button2)

keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add("Year(1)").add("Year(2)").add("Year(3)").add("Year(4)").add(button7,button15)
button8 = InlineKeyboardButton(text="Back")
keyboard2= ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).add(button5,button6).add(button8)
keyboard3=ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button9,button10).add(button8)
@dp.message_handler(commands=['start','help'])
async def welcome(message: types.Message):
    await message.reply("Welcome to HETLER world organazation",reply_markup=keyboard1)
insult=['fuck you','Fuck you','Bitch','bitch','Slut','Gay','gay','fuck','slut','Whore','whore']
greetings=['Hello','hello','Hi','hi','yo','Yo']
welcomeing=['How are you','whats up','how are you']
insultAr=['مخنوث','مركبه','فاكيو','فاك يو','انيك عارك','يامركبه','انا انيكك','يامخنوث','ياعاصي','قحبه']
welcomeingAr=['هلا','سلام','السلام عليكم','مرحبا','أهلا','ياحيا']
cute=['meow','Meow','wow','Wow']
careless=['Fine','fine','good','Good','Very good','very good']
@dp.message_handler()
async def keyboard(message: types.Message):
    if message.text=="Year(3)":
        await message.reply("Select a term:", reply_markup=keyboard2)


    elif message.text=="Year(2)":
        await message.answer_photo("https://ae01.alicdn.com/kf/H30cfc3adb41641e497c1ce2f446b091aV.jpg")

    elif message.text=="Year(1)":
        await message.answer_photo("https://onecms-res.cloudinary.com/image/upload/s--5mKjyqQ9--/f_auto%2Cq_auto/c_fill%2Cg_auto%2Ch_622%2Cw_830/v1/tdy-migration/200131_cat_ig.jpg?itok=GvEa_9kb")
    elif message.text=="first term":
        await message.reply("choose the subject",reply_markup=keyboard3)

    elif message.text=="second term":
        document1=open("C:/Users/KUDAR/PycharmProjects/pythonProject/Assets/lecture#12.pdf","rb")
        await bot.send_document(message.chat.id,document=document1)
    elif message.text=="Python":
        await message.reply("please wait its sending")

        d1=open("C:/Users\KUDAR/PycharmProjects/pythonProject/Assets/lecture#1.pdf","rb")
        await bot.send_document(message.chat.id,document=d1)
        d2 = open("C:/Users\KUDAR/PycharmProjects/pythonProject/Assets/lecture#2.pdf","rb")
        await bot.send_document(message.chat.id, document=d2)
        d3=open("C:/Users\KUDAR/PycharmProjects/pythonProject/Assets/lecture#3.pdf","rb")
        await bot.send_document(message.chat.id,document=d3)
        d4=open("C:/Users\KUDAR/PycharmProjects/pythonProject/Assets/lecture#4.pdf","rb")
        await bot.send_document(message.chat.id, document=d4)
        d5=open("C:/Users\KUDAR/PycharmProjects/pythonProject/Assets/lecture#5.pdf","rb")
        await bot.send_document(message.chat.id, document=d5)
        d6=open("C:/Users\KUDAR/PycharmProjects/pythonProject/Assets/lecture#6.pdf","rb")
        await bot.send_document(message.chat.id, document=d6)
        d7=open("C:/Users\KUDAR/PycharmProjects/pythonProject/Assets/lecture#7.pdf","rb")
        await bot.send_document(message.chat.id, document=d7)
        d8=open("C:/Users\KUDAR/PycharmProjects/pythonProject/Assets/lecture#8.pdf","rb")
        await bot.send_document(message.chat.id, document=d8)
        d9=open("C:/Users\KUDAR/PycharmProjects/pythonProject/Assets/lecture#8.pdf","rb")
        await bot.send_document(message.chat.id, document=d9)
        d10=open("C:/Users/KUDAR/PycharmProjects/pythonProject/Assets/lecture#10.pdf","rb")
        await bot.send_document(message.chat.id,document=d10)
        d11=open("C:/Users/KUDAR/PycharmProjects/pythonProject/Assets/lecture#11.pdf","rb")
        await bot.send_document(message.chat.id, document=d11)
        d12=open("C:/Users/KUDAR/PycharmProjects/pythonProject/Assets/lecture#12.pdf","rb")
        await bot.send_document(message.chat.id, document=d12)
        d13=open("C:/Users/KUDAR/PycharmProjects/pythonProject/Assets/lecture#13.pdf","rb")
        await bot.send_document(message.chat.id, document=d13)
        d14=open("C:/Users/KUDAR/PycharmProjects/pythonProject/Assets/lecture#14.pdf","rb")
        await bot.send_document(message.chat.id,document=d14)
    elif message.text=="theory of mechine":
        await message.reply("please wait its sending")
        d1=open("C:/Users\KUDAR/PycharmProjects/pythonProject/Assets/machines and mechanisms.pdf","rb")
        await bot.send_document(message.chat.id,document=d1)


    elif message.text=="Year(4)":
        await message.answer_photo("https://i.ytimg.com/vi/ndsaoMFz9J4/maxresdefault.jpg")
    elif message.text=="Location":
        await message.reply("your Location: ")
    elif message.text=="contact us":
        await message.reply("Mohammes Salmin: \n\n Num= +967779218110\n\nEmail= @moddqudar")
        await message.reply("Rakan Almroof: \n\n Num= +967730666839 \n\n Num= +967776570870")
        await message.reply("Abed Radwan: \n\n Num= +967730302345")
    elif message.text in insult:
        await message.reply("stop being a bitch🤬🤬")
    elif message.text in greetings:
        await message.reply("Hello👋👋")
    elif message.text in welcomeing:
        await message.reply("Im fine what about you?")
    elif message.text in insultAr:
        await message.reply("أسكت أسكت يا زبيييييي🤬🤬🤬")
    elif message.text in welcomeingAr:
        await message.reply("مرحبا\nفي منظمه هتلر العالمية")
    elif message.text in cute:
        await message.reply("cute🥰🥰")
    elif message.text in careless:
        await message.reply("Dont care")
    elif message.text=="Back":
        await message.answer('.',reply_markup=keyboard1)
    else:
        await message.reply("WTF are you saying?\n اهدااااااااا")


executor.start_polling(dp)
