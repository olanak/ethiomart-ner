from telethon import TelegramClient
import csv
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv('.env')
api_id = os.getenv('TG_API_ID')
api_hash = os.getenv('TG_API_HASH')
phone = os.getenv('PHONE_NUMBER')

# Function to scrape data from a single channel
async def scrape_channel(client, channel_username, writer, media_dir):
    # Get the channel entity (metadata)
    entity = await client.get_entity(channel_username)
    channel_title = entity.title  # Extract the channel's title
    
    # Scrape messages from the channel
    async for message in client.iter_messages(entity, limit=1000):
        media_path = None
        if message.media and hasattr(message.media, 'photo'):
            # Create a unique filename for the photo
            filename = f"{channel_username}_{message.id}.jpg"
            media_path = os.path.join(media_dir, filename)
            # Download the media (photo) to the specified directory
            await client.download_media(message.media, media_path)
        
        # Write the scraped data (including channel info, message content, and media)
        writer.writerow([channel_title, channel_username, message.id, message.message, message.date, media_path])

# Initialize the client once
client = TelegramClient('scraping_session', api_id, api_hash)

async def main():
    # Start the Telegram client
    await client.start()

    # Create a directory for storing media (photos)
    media_dir = 'data/raw/photos'
    os.makedirs(media_dir, exist_ok=True)

    # Open the CSV file to write the scraped data
    with open('data/raw/telegram_data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Channel Title', 'Channel Username', 'ID', 'Message', 'Date', 'Media Path'])  # Column headers
        
        # List of channels to scrape data from
        channels = [
            '@qnashcom',  
            '@Fashiontera',                     
            '@kuruwear',
            '@gebeyaadama',
            '@MerttEka'
        ]
        
        # Iterate over the channels and scrape data
        for channel in channels:
            await scrape_channel(client, channel, writer, media_dir)
            print(f"Scraped data from {channel}")

# Run the main function with the Telegram client
with client:
    client.loop.run_until_complete(main())
