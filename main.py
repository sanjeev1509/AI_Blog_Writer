# main.py

import argparse
from agents.topic_agent import TopicAgent
from agents.research_agent import ResearchAgent
from agents.writing_agent import WritingAgent
from agents.seo_agent import SEOAgent
from agents.export_agent import ExportAgent


def main():
    parser = argparse.ArgumentParser(
        description="Agentic Python Blog Writer")
    parser.add_argument("topic", type=str, help="Blog topic")
    parser.add_argument("--tone", type=str, default="educational",
                        help="Tone of writing (e.g., formal, creative, educational)")
    args = parser.parse_args()

    # Step 1: Understand the topic
    topic_agent = TopicAgent(topic=args.topic, tone=args.tone)
    subtopics = topic_agent.plan_subtopics()

    # Step 2: Research
    research_agent = ResearchAgent()
    research_data = research_agent.gather(subtopics)

    # Step 3: Generate Content
    writing_agent = WritingAgent()
    blog_markdown = writing_agent.write_blog(
        topic=args.topic, subtopics=subtopics, research=research_data, tone=args.tone)

    # Step 4: SEO Optimization
    seo_agent = SEOAgent()
    metadata = seo_agent.optimize(topic=args.topic, blog_content=blog_markdown)

    # Step 5: Export
    export_agent = ExportAgent()
    export_agent.save(blog_markdown, metadata)

    print("\n Blog written, optimized, and exported successfully!")


if __name__ == "__main__":
    main()
