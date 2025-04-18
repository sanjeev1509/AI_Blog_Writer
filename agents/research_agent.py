# agents/research_agent.py

import aiohttp
import asyncio
import os
import ssl
from dotenv import load_dotenv

load_dotenv()

NEWSDATA_API_KEY = os.getenv("NEWSDATA_API_KEY")


class ResearchAgent:
    def __init__(self):
        self.session = None

    async def fetch_news(self, topic):
        ssl_context = ssl.create_default_context()
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE

        url = f"https://newsdata.io/api/1/news?apikey={NEWSDATA_API_KEY}&q={topic}&language=en"
        try:
            async with self.session.get(url, ssl=ssl_context) as resp:
                data = await resp.json()
                articles = data.get("results", [])
                return [article["title"] for article in articles[:3]]
        except Exception as e:
            print(f"⚠️ News API failed: {e}")
            return [f"Recent developments in {topic}", f"Top stories about {topic}", f"Experts discuss {topic}"]

    async def fetch_keywords(self, topic):
        url = f"https://api.datamuse.com/words?ml={topic}"
        try:
            async with self.session.get(url) as resp:
                data = await resp.json()
                return [item["word"] for item in data[:5]]
        except Exception as e:
            print(f"⚠️ Keywords API failed: {e}")
            return [topic, "AI", "Python", "Tech", "Innovation"]

    async def fetch_quote(self, topic):
        ssl_context = ssl.create_default_context()
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE

        url = f"https://api.quotable.io/search/quotes?query={topic}"
        try:
            async with self.session.get(url, ssl=ssl_context) as resp:
                data = await resp.json()
                results = data.get("results", [])
                if results:
                    return results[0]["content"]
                return None
        except Exception as e:
            print(f"⚠️ Quote API failed: {e}")
            return f"Inspiration about {topic} drives innovation."

    async def gather_subtopic_data(self, subtopic):
        news = await self.fetch_news(subtopic)
        keywords = await self.fetch_keywords(subtopic)
        quote = await self.fetch_quote(subtopic)
        return {
            "news": news,
            "keywords": keywords,
            "quote": quote
        }

    def gather(self, subtopics):
        print(f"🔍 Researching for subtopics: {subtopics}")

        async def gather_all():
            async with aiohttp.ClientSession() as session:
                self.session = session
                tasks = [self.gather_subtopic_data(sub) for sub in subtopics]
                results = await asyncio.gather(*tasks)
                return dict(zip(subtopics, results))

        return asyncio.run(gather_all())
