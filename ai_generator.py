from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_blog_post(keyword, seo_data):
    prompt = f"""
    Write a detailed, SEO-optimized blog post about "{keyword}". Use structured sections like:
    1. Introduction
    2. Key Features
    3. Comparisons
    4. Conclusion

    Use placeholder affiliate links like {{AFF_LINK_1}}, {{AFF_LINK_2}}.
    Here’s some SEO data to guide you:
    - Search Volume: {seo_data['search_volume']}
    - Keyword Difficulty: {seo_data['keyword_difficulty']}
    - CPC: ${seo_data['avg_cpc']}

    Format it in Markdown.
    """

    try:
        print("Making OpenAI call...")
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
        )
        print("OpenAI response:", response)
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"[OpenAI ERROR] {e}")
        return None
