# AI-Assisted Data Science

This Web site links to resources for the book "AI-Assisted Data Science" by Immanuel Trummer, ordered by chapter. For each resource, you find a link and a short description.

## Chapter 1: Analyzing Data with Large Language Models

| Resource | Description |
| --- | --- |
| [Prompt](https://docs.google.com/document/d/1f3M2PV5mgy1kyg3J5C4QiiBqcsxxz4SBXYzHSJQ0NEw/edit?usp=sharing)|  Example prompt for product review classification |
| [Template](https://docs.google.com/document/d/1eDnrMe1G5UapYswZrIdRDxlEQTTKupVVyWUaQR7pOZM/edit?usp=sharing)| Prompt template for product review classification |

## Chapter 2: A Chat with ChatGPT

| Resource | Description |
| --- | --- |
| [ChatGPT](https://chat.openai.com/) | Link to the ChatGPT Web interface by OpenAI |
| [Review](https://docs.google.com/document/d/1LKVnR62O5iIzJNS0urvGDuc5GQ9zLkT-XRvrwhVNMpg/edit?usp=sharing)| Example review of BananaBook laptop|
| [BananaDB](https://colab.research.google.com/drive/10AT3uNRxQRDJU5giWWcktfS2BuoLGASE?usp=sharing) | Notebook supporting queries on the BananaDB database|

## Chapter 3: The OpenAI API

| Resource | Description |
| --- | --- |
| [Listing 1](https://github.com/itrummer/DataScienceWithGPT/blob/main/src/api/listing1.py) | Listing available GPT models|
| [Listing 2](https://github.com/itrummer/DataScienceWithGPT/blob/main/src/api/listing2.py) | Example output listing available models |
| [Listing 3](https://github.com/itrummer/DataScienceWithGPT/blob/main/src/api/listing3.py) | Making GPT tell us a story (text completion)|
| [Listing 4](https://github.com/itrummer/DataScienceWithGPT/blob/main/src/api/listing4.py) | Extract of output for text completion|
| [Listing 5](https://github.com/itrummer/DataScienceWithGPT/blob/main/src/api/listing5.py) | Customizing story generation via parameters|
| [Listing 6](https://github.com/itrummer/DataScienceWithGPT/blob/main/src/api/listing6.py) | Text completion with OpenAI's chat models|
| [Listing 7](https://github.com/itrummer/DataScienceWithGPT/blob/main/src/api/listing7.py) | Example output of chat completion|

## Chapter 4: Analyzing Text Data

| Resource | Description |
| --- | --- |
| [Reviews.csv](https://github.com/itrummer/DataScienceWithGPT/blob/main/data/reviews.csv) | Small set of movie reviews for sentiment classification |
| [Listing 1](https://github.com/itrummer/DataScienceWithGPT/blob/main/src/text/listing1.py) | Classifying text by underlying sentiment |
| [Biographies.csv](https://github.com/itrummer/DataScienceWithGPT/blob/main/data/biographies.csv) | Small collection of biographies for text extraction |
| [Listing 2](https://github.com/itrummer/DataScienceWithGPT/blob/main/src/text/listing2.py) | Extracting structured data from text documents |
| [Textmix.csv](https://github.com/itrummer/DataScienceWithGPT/blob/main/data/textmix.csv) | Mix of poems and emails, to be used for document clustering |
| [Listing 3](https://github.com/itrummer/DataScienceWithGPT/blob/main/src/text/listing3.py) | Clustering text documents via their embedding vectors |
| [Listing 4](https://github.com/itrummer/DataScienceWithGPT/blob/main/src/text/listing4.py) | Example result when using GPT for text embedding |

## Chapter 5: Analyzing Structured Data

| Resource | Description |
| --- | --- |
| [Games](https://github.com/itrummer/DataScienceWithGPT/blob/main/data/videogames.csv) | Tabular data set describing video game sales|
| [Games SQLite](https://drive.google.com/file/d/1qdX3vbgVFkt14Wq5db09LuQolm8csSUQ/view?usp=sharing)| SQLite database file containing games data |
| [Games NLQI](https://github.com/itrummer/DataScienceWithGPT/blob/main/src/tables/gamesnlqi.py) | A natural language query interface on the games database |
| [Listing 1](https://github.com/itrummer/DataScienceWithGPT/blob/main/src/tables/listing1.py) | Translating text questions about video games to SQL queries|
| [Listing 2](https://github.com/itrummer/DataScienceWithGPT/blob/main/src/tables/listing2) | Example prompt for translating question to SQL query|
| [Listing 3](https://github.com/itrummer/DataScienceWithGPT/blob/main/src/tables/listing3.py) | Translating questions to SQL queries on arbitrary tabular data|
| [Listing 4](https://github.com/itrummer/DataScienceWithGPT/blob/main/src/tables/listing4) | Example interaction with natural language query interface|
| [Listing 5](https://github.com/itrummer/DataScienceWithGPT/blob/main/src/tables/listing5) | Example prompt for translating questions into Cypher queries|
| [Listing 6](https://github.com/itrummer/DataScienceWithGPT/blob/main/src/tables/listing6.py) | Translating questions about movies into Cypher queries|

## Chapter 6: Analyzing Images and Videos

| Resource | Description |
| --- | --- |
| [Listing 1](https://github.com/itrummer/DataScienceWithGPT/blob/main/src/images/listing1.py) | Answering questions about images |
| [Fruit 1](https://github.com/itrummer/DataScienceWithGPT/blob/main/data/fruit1.jpg) | A JPEG image of an apple |
| [Listing 2](https://github.com/itrummer/DataScienceWithGPT/blob/main/src/images/listing2.py) | Tagging people in images |
| [Tagging](https://github.com/itrummer/DataScienceWithGPT/blob/main/data/peoplepictures.zip) | Pictures of people for image tagging |
| [Listing 3](https://github.com/itrummer/DataScienceWithGPT/blob/main/src/images/listing3.py) | Generating suitable titles for videos |
| [Cars](https://github.com/itrummer/DataScienceWithGPT/blob/main/data/cars.mp4) | A video of cars on a road |

## Chapter 7: Analyzing Audio Data

| Resource | Description |
| --- | --- |
| [Listing 1](https://github.com/itrummer/DataScienceWithGPT/blob/main/src/audio/listing1.py) | Transcribing audio recordings to text |
| [Audio](https://github.com/itrummer/DataScienceWithGPT/blob/main/data/QuoteFromTheAlchemist.mp3) | A sample audio recording for transcription |
| [Listing 2](https://github.com/itrummer/DataScienceWithGPT/blob/main/src/audio/listing2.py) | A voice query interface for tabular data |
| [Listing 3](https://github.com/itrummer/DataScienceWithGPT/blob/main/src/audio/listing3.py) | A speech-to-speech translator |

## Chapter 11: The Transformer

| Resource | Description |
| --- | --- |
| [Visualizations](https://github.com/jessevig/bertviz) | Notebook for visualizing attention in the BERT model|

## Chapter 12: Transfer Learning

| Resource | Description |
| --- | --- |
| [Roberta XLM](https://huggingface.co/xlm-roberta-base) | Example description of Roberta Transformer model |
