# calls OpenAI with a structured prompt to generate a blog post draft (HTML or Markdown),
# replacing {{AFF_LINK_n}} placeholders with dummy URLs.

import openai
import os
from dotenv import load_dotenv
from openai import responses

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_blog_post(keyword, seo_data):
    def generate_blog_post(keyword, seo_data):
        prompt = f"""
        Write a blog post about "{keyword}" with specific sections like introduction, benefits, comparison, and conclusion.
        Include placeholder affiliate links as {{AFF_LINK_1}}, {{AFF_LINK_2}}.
        SEO Info: Volume={seo_data['search_volume']}, Difficulty={seo_data['keyword_difficulty']}, CPC=${seo_data['avg_cpc']}.
        Format it in Markdown.
        """

        response = openai.ChatCompletion.create(
            model = "gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )

        return response.choices[0].message.content.strip()