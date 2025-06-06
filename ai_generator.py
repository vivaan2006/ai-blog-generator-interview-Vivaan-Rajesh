import os
from dotenv import load_dotenv
from openai import OpenAI

# Load .env and initialize OpenAI client
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def replace_affiliate_links(content):
    # Replace the single‐brace placeholders {AFF_LINK_n} with real URLs
    for i in range(1, 6):
        content = content.replace(f"{{AFF_LINK_{i}}}", f"https://example.com/product{i}")
    return content

def generate_blog_post(keyword, seo_data):
    prompt = f"""
Write a detailed, SEO-optimized blog post about "{keyword}". Use exactly this structure:

1. Introduction  
2. Key Features  
3. Comparisons  
4. Conclusion  

In the **Comparisons** section, include at least two products. For each product, use Markdown links of the form:

[Check Price Here]({{AFF_LINK_1}})  
…and…  
[Check Price Here]({{AFF_LINK_2}})

Use `{{AFF_LINK_3}}`, `{{AFF_LINK_4}}`, etc. **only if** you want to mention additional products.

Here is some SEO data to guide you:
- Search Volume: {seo_data['search_volume']}
- Keyword Difficulty: {seo_data['keyword_difficulty']}
- CPC: ${seo_data['avg_cpc']}

Format everything in clean Markdown—include headings (`##`), bullet points, bold/italic styling where appropriate, and make sure each affiliate link placeholder appears exactly as `{{AFF_LINK_n}}` in the final text.
"""

    try:
        print("Making OpenAI call...")
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )

        # The model’s response is raw Markdown (no triple‐backticks)
        raw_content = response.choices[0].message.content.strip()
        final_content = replace_affiliate_links(raw_content)
        return final_content

    except Exception as e:
        print(f"[OpenAI ERROR] {e}")
        return None