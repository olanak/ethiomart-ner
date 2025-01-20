EthioMart: E-commerce NER Project
Overview
The EthioMart project aims to build a centralized platform for e-commerce activities on Telegram in Ethiopia. The project's goal is to automate the extraction of key business entities such as product names, prices, and locations from Telegram messages using Named Entity Recognition (NER) techniques.

Current Progress:

Data Collection:
Data was collected from multiple Ethiopian-based Telegram e-commerce channels using the Telethon library, which scraped messages containing product details, prices, and location information.

Data Preprocessing:
The collected data was cleaned by removing NaN values, emojis, and extra spaces from the messages.
The cleaned data was saved into a CSV file (clean_data.csv).

Data Labeling:
The text data was manually labeled for Named Entity Recognition (NER), with labels for product names, prices, and locations.
The labeled data was saved in a CoNLL format text file (labeled_telegram_product_price_location.txt).
Tokenization:

The labeled data was tokenized using both a pretrained tokenizer (xlm-roberta-base) and a custom Amharic tokenizer using SentencePiece to improve tokenization of Amharic text.
The final tokenized and labeled data was saved in a CSV file (final_tokens_labels.csv), ready for training an NER model.

Repository Structure
ethioMart/
├── data/                   
│   ├── raw/                
│   │   ├── telegram_data.csv  # Raw scraped data
│   │   └── photos/           # Media files (photos) from Telegram channels
│   ├── processed/
│   │   └── clean_data.csv     # Cleaned data
│   └── labeled/
│       └── labeled_telegram_product_price_location.txt  # Labeled data (CoNLL format)
├── src/                    
│   ├── ingestion.py          # Data ingestion script (scraping Telegram channels)
│   ├── data_processing.py    # Data preprocessing script (cleaning and preparing data)
│   └── tokenization.ipynb    # Tokenization and alignment of tokens with labels
├── .env                     # Environment variables (for API credentials)
├── .gitignore               # Files to ignore (including sensitive data)
├── README.md                # Project documentation


Getting Started
Follow these steps to set up and run the project.

1. Clone the Repository
Clone the repository to your local machine:



git clone https://github.com/your_username/ethioMart.git
cd ethioMart

2. Install Dependencies
Ensure you have Python 3.6+ installed. Install the required dependencies by running:

pip install -r requirements.txt

You may need to create a virtual environment to manage dependencies:
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
.\venv\Scripts\activate   # On Windows

Then install the dependencies:
pip install -r requirements.txt

3. Environment Variables
Create a .env file in the root directory and add your Telegram API credentials (API ID, API Hash, and phone number):

TG_API_ID=your_api_id
TG_API_HASH=your_api_hash
PHONE_NUMBER=your_phone_number

4. Data Collection (Ingestion)
Run the ingestion.py script to scrape messages from Telegram e-commerce channels:
python src/ingestion.py
This will scrape data from the specified Telegram channels and save the raw data to data/raw/telegram_data.csv.

5. Data Preprocessing and Labeling
Run the data_processing.py script to preprocess the data by removing NaN values, emojis, and normalizing the text:
python src/data_processing.py

Then, manually label the data (product names, prices, locations) in the labeled_telegram_product_price_location.txt file following the CoNLL format.

6. Tokenization
After labeling, you can run the tokenization.ipynb notebook for tokenizing and aligning the labeled data with the appropriate labels:

Load the labeled data (labeled_telegram_product_price_location.txt).
Tokenize the text using both the pretrained tokenizer (xlm-roberta-base) and the custom Amharic tokenizer (using SentencePiece).
Align the tokens with their respective labels and save the results to final_tokens_labels.csv.

Run the notebook in a Jupyter environment:

jupyter notebook src/tokenization.ipynb

Next Steps
Fine-tuning an NER Model:

Once the data is tokenized and labeled, the next step is to fine-tune an NER model (e.g., xlm-roberta-base) to identify the desired entities (product names, prices, locations) in new Telegram messages.
Model Evaluation:

After training the NER model, evaluate its performance on unseen Telegram messages to assess the accuracy of entity extraction.

License
This project is licensed under the MIT License - see the LICENSE file for details.