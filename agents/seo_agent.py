# agents/seo_agent.py

import aiohttp
import asyncio
import re
import textstat  # 📚 NEW


class SEOAgent:
    def __init__(self):
        pass

    async def fetch_related_keywords(self, topic):
        url = f"https://api.datamuse.com/words?ml={topic}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                data = await resp.json()
                return [item["word"] for item in data[:7]]

    def slugify(self, text):
        text = text.lower()
        text = re.sub(r'[^a-z0-9]+', '-', text)
        return text.strip('-')

    def estimate_reading_time(self, text):
        words = text.split()
        words_per_minute = 200
        return max(1, len(words) // words_per_minute)

    def calculate_readability(self, text):
        # Flesch Reading Ease: higher = easier to read
        score = textstat.flesch_reading_ease(text)
        return round(score, 2)

    def optimize(self, topic, blog_content):
        print(f"📈 Optimizing SEO for topic: {topic}")

        async def optimize_async():
            keywords = await self.fetch_related_keywords(topic)

            return {
                "title": topic,
                "meta_description": f"Discover how {topic} impacts the world today and explore insights you shouldn't miss.",
                "keywords": keywords,
                "slug": self.slugify(topic),
                "reading_time_minutes": self.estimate_reading_time(blog_content),
                #  NEW
                "readability_score": self.calculate_readability(blog_content)
            }

        return asyncio.run(optimize_async())
