# agents/writing_agent.py
import time
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


class WritingAgent:
    def __init__(self):
        self.model = genai.GenerativeModel('gemini-1.5-pro')

    import time

    def ask_gemini(self, prompt: str) -> str:
        response = self.model.generate_content(prompt)
        time.sleep(30)  # Wait 30 seconds after each API call
        return response.text

    def write_blog(self, topic, subtopics, research, tone):
        print(f" Writing blog on: {topic} with tone: {tone}")

        # 1. Generate Outline
        outline_prompt = f"Create an H2-level outline for a blog titled '{topic}' for {tone} readers."
        outline = self.ask_gemini(outline_prompt)

        content = f"# {topic}\n\n## Outline\n{outline}\n\n"

        # 2. Introduction
        intro_prompt = f"Write an engaging introduction (100–150 words) for '{topic}' in a {tone} tone."
        intro = self.ask_gemini(intro_prompt)
        content += "## Introduction\n" + intro + "\n\n"

        # 3. Sections
        for subtopic in subtopics:
            research_notes = research.get(subtopic, {})
            news = " ".join(research_notes.get("news", []))
            keywords = ", ".join(research_notes.get("keywords", []))
            quote = research_notes.get("quote", "")

            section_prompt = f"""
Write a detailed section (~250 words) for a blog about '{subtopic}' under the topic '{topic}'.
Use a {tone} tone. Incorporate these news points: {news}.
Use these keywords: {keywords}. Include this quote if relevant: "{quote}".
Use Markdown formatting.
"""
            section_content = self.ask_gemini(section_prompt)
            content += f"## {subtopic}\n{section_content}\n\n"

        # 4. Conclusion
        conclusion_prompt = f"Write a strong conclusion (100-150 words) for the blog '{topic}' in a {tone} tone with a call-to-action."
        conclusion = self.ask_gemini(conclusion_prompt)
        content += "## Conclusion\n" + conclusion + "\n"

        return content
