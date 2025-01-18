import pandas as pd
import re

# Function to preprocess Amharic text (cleaning and tokenizing)
def preprocess_amharic_text(text):
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    text = text.lower()  # Convert text to lowercase (optional)
    return text

# Read data from the raw file (messages.json)
def load_raw_data():
    data = []
    with open('data/raw/messages.json', 'r', encoding='utf-8') as f:
        for line in f:
            data.append(json.loads(line))
    return data

# Function to preprocess messages
def preprocess_data():
    raw_data = load_raw_data()
    processed_data = []

    for message in raw_data:
        sender = message.get('sender_id')
        timestamp = message.get('timestamp')
        text = message.get('text')

        # Preprocess the text
        processed_text = preprocess_amharic_text(text)

        processed_data.append({
            'sender_id': sender,
            'timestamp': timestamp,
            'text': processed_text
        })

    # Save preprocessed data to CSV
    df = pd.DataFrame(processed_data)
    df.to_csv('data/processed/processed_messages.csv', index=False)
    print("Preprocessing completed and saved to CSV.")

# Run the preprocessing
if __name__ == "__main__":
    preprocess_data()
import pandas as pd
import re
import os

# Function to preprocess Amharic text
def preprocess_amharic_text(text):
    """
    Preprocesses Amharic text by performing the following:
    - Removing extra spaces
    - Removing non-alphanumeric characters (except spaces)
    - Lowercasing the text
    """
    if isinstance(text, str):
        # Remove extra spaces
        text = re.sub(r'\s+', ' ', text).strip()
        # Remove non-alphanumeric characters (keeping only letters and spaces)
        text = re.sub(r'[^\w\s፣፤፥፨፩፪፫፬፭፮፯፰፱፲፳፴፵፶፷፸፹፺፻]', '', text)
        # Convert to lowercase
        text = text.lower()
    return text

# Function to load and process raw data
def process_raw_data(input_file, output_file):
    """
    Loads the raw data from the input CSV file, preprocesses the text data,
    and saves it to the output CSV file.
    """
    # Load the raw data (CSV) into a DataFrame
    df = pd.read_csv(input_file, encoding='utf-8')

    # Ensure that the necessary columns exist
    if 'Message' not in df.columns:
        print("Error: 'Message' column not found in the raw data.")
        return
    
    # Preprocess the 'Message' column
    df['Processed_Message'] = df['Message'].apply(preprocess_amharic_text)

    # Save the processed data to a new CSV file
    df.to_csv(output_file, index=False, encoding='utf-8')
    print(f"Processed data saved to {output_file}")

# Main function to execute the processing
if __name__ == "__main__":
    input_file = 'data/raw/telegram_data.csv'  # Path to the raw CSV file
    output_file = 'data/processed/processed_data.csv'  # Path to save the processed CSV file

    # Check if the raw data file exists
    if not os.path.exists(input_file):
        print(f"Error: {input_file} does not exist.")
    else:
        # Process the raw data
        process_raw_data(input_file, output_file)





