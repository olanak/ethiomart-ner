import pandas as pd
import re
import os

# Load the raw data (from telegram_data.csv)
def load_raw_data():
    """Load the raw CSV data."""
    data = pd.read_csv('data/raw/telegram_data.csv', encoding='utf-8')
    return data

# Function to remove emojis from the text
def remove_emojis(text):
    """
    Remove emojis from the text using a regular expression.
    """
    emoji_pattern = re.compile(
        "[" 
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport & map symbols
        "\U0001F700-\U0001F77F"  # alchemical symbols
        "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
        "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
        "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
        "\U0001FA00-\U0001FA6F"  # Chess Symbols
        "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
        "\U00002702-\U000027B0"  # Dingbats
        "\U000024C2-\U0001F251" 
        "]+", 
        flags=re.UNICODE
    )
    return emoji_pattern.sub(r'', text)

# Function to preprocess and clean the data
def preprocess_data():
    """Clean the data by removing NaN values, emojis, and normalize text."""
    # Load raw data
    df = load_raw_data()

    # Check for NaN values in the 'Message' column and drop them
    print("Checking for NaN values in the 'Message' column:")
    nan_count = df['Message'].isnull().sum()
    print(f"Number of NaN values in 'Message' column: {nan_count}")

    # Drop rows with NaN values in the 'Message' column
    df = df.dropna(subset=['Message'])

    # Show the dataset shape after dropping NaN values
    print(f"Dataset shape after dropping NaN values in 'Message' column: {df.shape}")

    # Clean the 'Message' column by removing emojis and normalizing the text
    df['Message'] = df['Message'].apply(remove_emojis)  # Remove emojis

    # Normalize the text (convert to lowercase)
    df['Message'] = df['Message'].str.lower()

    # Optionally, you can add further cleaning (e.g., removing unwanted punctuation, extra spaces)
    df['Message'] = df['Message'].str.replace(r'\s+', ' ', regex=True).str.strip()

    # Save the cleaned data to a new CSV file
    cleaned_data_path = 'data/processed/clean_data.csv'
    df.to_csv(cleaned_data_path, index=False, encoding='utf-8')
    print(f"Cleaned data saved to {cleaned_data_path}")

    # Return the cleaned DataFrame
    return df

# Main function to run the preprocessing
if __name__ == "__main__":
    cleaned_df = preprocess_data()
    print("Sample of cleaned data:")
    print(cleaned_df.head())
