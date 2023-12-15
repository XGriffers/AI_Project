# AI Content Generator Web App

This project aims to build a web app that uses AI to scrape online content, rewrite/summarize it, and publish new blog posts in predefined niches.

## Project Structure

1. **Web Scraping with Scrapy Spider**: The Scrapy spider is programmed with a set of seed URLs related to the niches. It dynamically discovers new URLs, follows links, extracts relevant content, and outputs the scraped data for ingestion into the AI pipeline.

2. **AI Pipeline Architecture**: The AI pipeline ingests the scraped data, preprocesses it, fine-tunes the AI model (e.g., GPT-3) on the specific task, generates new blog posts, and supplies the rewritten posts via a JSON API.

3. **Web App Development**: The Ruby on Rails web app consumes the JSON API, displays the AI-generated content, and provides user interaction features.

## Getting Started

To get started with this project, you'll need to have Python and Ruby on Rails installed on your machine. You'll also need to install the Scrapy library for Python.

## Running the Project

Detailed instructions for running the project will be provided once the development is complete.
