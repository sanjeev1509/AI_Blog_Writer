# agents/topic_agent.py

class TopicAgent:
    def __init__(self, topic, tone="educational"):
        self.topic = topic
        self.tone = tone

    def plan_subtopics(self):
        # Later: use Gemini API
        print(f" Planning subtopics for: {self.topic} (Tone: {self.tone})")
        return ["Introduction", "Use Cases", "Tools and Libraries", "Future Trends"]
