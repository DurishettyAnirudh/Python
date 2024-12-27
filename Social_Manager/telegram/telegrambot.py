import asyncio
import telegram
import mysql.connector
import sys
import os


TOKEN = "7099822791:AAH7F1oZPEZkT3obxjVE3bZ5CtHc2l2tc5U"
chat_id = '-4269996897'

# Channel ID Sample: -1001829542722
bot = telegram.Bot(token=TOKEN)
async def send_video(video, chat_id):
    async with bot:
        await bot.send_video(video=video, chat_id=chat_id)
async def send_message(text, chat_id):
    async with bot:
        await bot.send_message(text=text, chat_id=chat_id)
# async def send_document(document, chat_id):
#     async with bot:
#         await bot.send_document(document=document, chat_id=chat_id)
# async def send_photo(photo, chat_id):
#     async with bot:
#         await bot.send_photo(photo=photo, chat_id=chat_id)
async def main():

    row_index = sys.argv[1]
    print(row_index)
#configure database
    DB_CONFIG = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'root',
    'database': 'client_upload'
    }
    
    #connect to database
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute(
                'SELECT serial_number, title, category, video_path, privacy_status, description, keywords, date_time FROM videos where serial_number = %s', (row_index,))
    rows = cursor.fetchall()
    row = rows[0]
    serial_number, title, category, video_path, privacy_status, description, keywords, date_time = row



    # Sending a video
    print(video_path)
    await send_video(video=open(video_path, 'rb'), chat_id=chat_id)
    # Sending a message
    await send_message(text=title + "\n" + description , chat_id=chat_id)
    # Sending a document
    # await send_document(document=open('/path/to/document.pdf', 'rb'), chat_id=chat_id)
    # # Sending a photo
    # await send_photo(photo=open('/path/to/photo.jpg', 'rb'), chat_id=chat_id)
if __name__ == '__main__':
    asyncio.run(main())