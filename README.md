# AI Blog Content Generator

This project aims to build a web application that uses AI to scrape online content, rewrite/summarize it, and publish new blog posts in predefined niches. The niches we focus on include making money online, digital marketing, personal finance, fitness, and self-improvement.

## Project Structure

The project is divided into several parts:

1. **Web Scraping with BeautifulSoup**: We define a scraping algorithm to pull data from websites in an array and push it to a JSON file. The scraped data is then output for ingestion into the AI pipeline.

2. **AI Pipeline Architecture**: The AI pipeline will consist of several stages:

    - **Data Ingestion**: We use the BeautifulSoup module to collect content from the chosen niches.
    - **Data Preprocessing**: The scraped data is cleaned and formatted for the AI model.
    - **Feature Engineering and Selection**: If necessary, we perform feature engineering and selection.
    - **Model Training**: We fine-tune the AI model (To Be Determined) on the specific task.
    - **Model Evaluation**: We ensure the AI model generates high-quality content.
    - **Content Generation**: We generate new blog posts based on the processed data.
    - **API Integration**: We develop a JSON API for the AI pipeline to supply rewritten posts.

3. **Web App Development**: The web app is developed using Ruby on Rails. The steps involved are:

    - **Setup**: We set up the Ruby on Rails web app.
    - **Feature Implementation**: We implement the web app features.
    - **Integration**: We integrate the web app with the AI pipeline via the JSON API.
    - **Design**: We style and design the user interface.
    - **Testing**: We test and refine the web app.
    - **Deployment**: We deploy the web app.

**Progress**

We have successfully implemented the web scraping part using BeautifulSoup and created a JSON file with the scraped data. The AI pipeline is set up with a model architecture that includes an LSTM layer and a Dense layer with a softmax activation function. The model is trained on the scraped data and is able to generate new text, although the quality of the generated text needs improvement. We are currently working on improving the quality of the generated text by fine-tuning the model and exploring different data sources for web scraping.

Data Loading and Processing: The code begins by loading and processing a JSON data file. The data is extracted and tokenized, converting the text data into a format suitable for machine learning.
Model Preparation: The code then prepares a tokenizer with a specified vocabulary size and fits it on the text data. It also creates sequences of tokens to be used as input to the model.
Data Splitting: The sequences are split into training and testing sets using the prepare_data function from the model module.
Model Training: The code checks if a pre-trained model exists. If it does, the model is loaded; otherwise, a new model is created and trained using the training data. The model is then saved for future use.
Text Generation: The trained model is used to generate new text based on seed texts. The generated text is appended to a list.
Output Saving: The list of generated texts is saved to a JSON file.