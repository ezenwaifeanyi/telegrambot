import telebot
import time

# modules imported to display pictues using links
from PIL import Image
import requests
from _io import BytesIO


TOKEN = "5529599842:AAGYIZ-qdJdBU7jSJDfx6icJXdNnPVcb-2w"
bot = telebot.TeleBot(TOKEN)
# this is image link
IMAGE_LINK = "https://cdn.pixabay.com/photo/2016/01/08/11/49/text-1127657_1280.jpg"


def download_file(url, name="video.mp4"):
    r = requests.get(url, stream=True)
    with open(name, "wb") as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)


@bot.message_handler(commands=["start"])
def start(message):
    print(message.text)


@bot.message_handler(commands=["hello", "hi"])
def hello(message):
    bot.send_message(message.chat.id, "Hello Ben")


@bot.message_handler(commands=["image", "img"])
def image(message):
    img = open("hello.jpg", "rb")
    bot.send_photo(message.chat.id, img)


@bot.message_handler(commands=["imagenet", "imgnet"])
def imagenet(message):
    response = requests.get(IMAGE_LINK)
    imgnet = Image.open(BytesIO(response.content))
    # send the photo
    bot.send_photo(message.chat.id, imgnet)


@bot.message_handler(commands=["video", "vid"])
def video(message):
    vid = open("video.mp4", "rb")
    bot.send_video(message.chat_id, vid)


@bot.message_handler(commands=["videonet", "vidnet"])
def videonet(message):
    download_file("video url", "video name.mp4")

    vidnet = open("myvideo.mp4", "rb")
    bot.send_video(message.chat_id, vid)


@bot.message_handler(commands=["audio", "aud"])
def audio(message):
    aud = open("audio.wav", "rb")
    bot.send_audio(message.chat.id, aud)


while True:
    try:
        bot.polling()

    except:
        time.sleep(5)
