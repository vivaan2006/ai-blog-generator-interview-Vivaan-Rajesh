# AI-Powered Blog Post Generator with Daily Automation

**Repository:** [ai-blog-generator-interview-Vivaan-Rajesh](https://github.com/vivaan2006/ai-blog-generator-interview-Vivaan-Rajesh)

---

## Table of Contents

1. [Project Overview](#project-overview)  
2. [Features](#features)  
3. [Tech Stack & Dependencies](#tech-stack--dependencies)  
4. [Prerequisites](#prerequisites)  
5. [Installation & Setup](#installation--setup)  
   - [1. Clone Repository](#1-clone-repository)  
   - [2. Create & Activate Virtual Environment](#2-create--activate-virtual-environment)  
   - [3. Install Dependencies](#3-install-dependencies)  
   - [4. Environment Variables](#4-environment-variables)  
   - [5. Run the Flask App](#5-run-the-flask-app)  
6. [Usage](#usage)  
   - [API Endpoint](#api-endpoint)  
   - [Scheduler / Daily Automation](#scheduler--daily-automation)  
7. [Example Generated Blog Post](#example-generated-blog-post)  
8. [Project Structure](#project-structure)  
9. [Troubleshooting & Tips](#troubleshooting--tips)  
10. [License](#license)  

---

## Project Overview

The **AI-Powered Blog Post Generator with Daily Automation** is a simple Python/Flask application that:

1. Accepts a keyword via an HTTP GET request (`/generate?keyword=<your_keyword>`).  
2. Performs SEO research (using Google Trends data via `pytrends`) to retrieve search interest metrics.  
3. Calls the OpenAI API to generate a structured blog post draft in Markdown format, complete with placeholder affiliate links (`{{AFF_LINK_n}}`).  
4. Automatically schedules a daily job (using APScheduler) to regenerate a blog post for a predefined keyword and save the result to a local file.

This project was built as part of a backend interview exercise for Hyperon. It demonstrates:  
- How to integrate SEO data (free, via Google Trends) in Python.  
- How to orchestrate calls to the OpenAI API.  
- How to expose a REST endpoint with Flask.  
- How to schedule recurring jobs via APScheduler (or cron).  

---

## Features

- **Flask REST API**:  
  - `GET /generate?keyword=<keyword>` returns a JSON response containing:
    - `content` (Markdown string of the blog post)  
    - `seo_data` (search interest score, etc.)  

- **SEO Data Integration**:  
  - Uses [pytrends](https://github.com/GeneralMills/pytrends) to fetch Google Trends search interest for the given keyword over the past 12 months.  
  - Transforms that interest score into a semiquantitative “search_volume” field.  
  - Uses default/mocked values for `keyword_difficulty` and `avg_cpc` (since fully free SEO data is limited).  

- **OpenAI Integration**:  
  - Leverages `openai.ChatCompletion` to generate a blog post outline and content in Markdown format.  
  - Replaces placeholder strings like `{{AFF_LINK_n}}` with dummy affiliate URLs.  

- **Daily Scheduler**:  
  - Integrates [APScheduler](https://apscheduler.readthedocs.io/) to run a background job once every 24 hours.  
  - The job automatically calls the `/generate` endpoint with a predefined keyword (e.g., `"wireless earbuds"`) and writes the Markdown output to `generated_posts/<timestamp>_<keyword>.md`.  

---

## Tech Stack & Dependencies

- **Language**: Python 3.8+  
- **Web Framework**: [Flask](https://palletsprojects.com/p/flask/)  
- **OpenAI Client**: [openai](https://pypi.org/project/openai/)  
- **SEO Data**: [pytrends](https://pypi.org/project/pytrends/) (Google Trends Python API)  
- **Task Scheduler**: [APScheduler](https://pypi.org/project/APScheduler/)  
- **Environment Variables**: [python-dotenv](https://pypi.org/project/python-dotenv/)  
- **HTTP Requests**: [requests](https://pypi.org/project/requests/) (if needed for future SEO API integrations)  

All packages are listed in `requirements.txt`.

---

## Prerequisites

1. **Python 3.8 or higher** installed on your system.  
2. **Git** (to clone the repository).  
3. (Optional) **Virtual environment tool** (e.g., `venv`, `virtualenv`) for dependency isolation.  
4. **OpenAI API Key** (required).  
   - Obtain from [OpenAI Dashboard → API Keys](https://platform.openai.com/account/api-keys).  
5. **No additional API keys** are required for SEO data since we are using Google Trends via `pytrends`.

---

## Installation & Setup

### 1. Clone Repository

```bash
git clone https://github.com/vivaan2006/ai-blog-generator-interview-Vivaan-Rajesh.git
cd ai-blog-generator-interview-Vivaan-Rajesh