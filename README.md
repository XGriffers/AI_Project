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
