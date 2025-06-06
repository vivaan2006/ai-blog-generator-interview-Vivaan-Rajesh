# Backend Interview: AI-Powered Blog Post Generator with Daily Automation (Vivaan Rajesh)


This repository contains a Python/Flask application that, given a keyword, performs light SEO research, calls OpenAI to generate a complete blog post in Markdown, replaces placeholder affiliate links with dummy URLs, and automatically generates a new post once per day via APScheduler.

---

## Table of Contents

1. [Features](#features)  
2. [Prerequisites](#prerequisites)  
3. [Installation](#installation)  
4. [Environment Variables](#environment-variables)  
5. [Running the Flask App](#running-the-flask-app)  
6. [Using the `/generate` Endpoint](#using-the-generate-endpoint)  
7. [Daily Scheduler (APScheduler)](#daily-scheduler-apscheduler)  
8. [Example Generated Post](#example-generated-post)  
9. [Project Structure](#project-structure)  
10. [Dependencies](#dependencies)  
11. [Ignored Files](#ignored-files)  
12. [Notes & Troubleshooting](#notes--troubleshooting)

---

## Features

- **Flask REST API**: Single endpoint `GET /generate?keyword=<keyword>` returns a JSON payload containing:
  - `content`: a full blog post in raw Markdown (no triple backticks).
  - `keyword`: the requested keyword.
  - `seo_data`: a dictionary with `search_volume`, `keyword_difficulty`, and `avg_cpc`.
- **SEO Data Fetcher**:  
  - Either mocks fixed values _or_ uses a free approach (e.g., Google Trends via `pytrends`) to estimate search interest.  
- **AI Generator**: Builds a prompt that includes SEO data, requests a four-section post (Introduction, Key Features, Comparisons, Conclusion), injects placeholders `{{AFF_LINK_1}}`/`{{AFF_LINK_2}}`, and calls OpenAI to generate Markdown. Then replaces each `{{AFF_LINK_n}}` with a dummy URL `https://example.com/product<n>`.
- **Daily Automation**: Uses APScheduler to run `daily_generator()` once every 24 hours (interval trigger) with a fixed keyword (`"wireless earbuds"`). Each run creates a new Markdown file under `generated_posts/`.
- **Example Output**: A polished sample blog post (`example_smart_watches.md`) demonstrates exactly how the generated content is structured.

---

## Prerequisites

- Python 3.9+  
- A valid OpenAI API key  
- (Optional) If using Google Trends for SEO data, install `pytrends`. Otherwise, mocks are built in.  

---

## Installation

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/vivaan2006/ai-blog-generator-interview-Vivaan-Rajesh.git
   cd ai-blog-generator-interview-Vivaan-Rajesh
