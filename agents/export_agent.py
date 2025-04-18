# agents/export_agent.py

import json
import os


class ExportAgent:
    def save(self, blog_markdown, metadata):
        os.makedirs("output", exist_ok=True)

        with open("output/blog.md", "w", encoding="utf-8") as f:
            f.write(blog_markdown)

        with open("output/metadata.json", "w", encoding="utf-8") as f:
            json.dump(metadata, f, indent=2)

        print(f" Exported blog and metadata to 'output/' folder.")
