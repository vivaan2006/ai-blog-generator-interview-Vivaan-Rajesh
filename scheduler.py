from apscheduler.schedulers.background import BackgroundScheduler
from ai_generator import generate_blog_post
from seo_fetcher import fetch_seo_data
import datetime, os

def daily_generator():
    keyword = "wireless earbuds"
    seo_data = fetch_seo_data(keyword)
    content = generate_blog_post(keyword, seo_data)
    filename = f"generated_posts/{keyword.replace(' ', '_')}_{datetime.date.today()}.md"
    os.makedirs("generated_posts", exist_ok=True)
    with open(filename, "w") as f:
        f.write(content)


def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(daily_generator, 'interval', days=1)
    scheduler.start()