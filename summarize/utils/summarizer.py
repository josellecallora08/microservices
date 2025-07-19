import os
import re
import httpx
from dotenv import load_dotenv
load_dotenv()
GROQ_API_KEY=os.getenv("GROQ_API_KEY")
MODEL = "llama3-70b-8192"

def clean_summary_output(text:str) -> str:
    patterns = [
        r"^(here (is|'s) (the )?summary[:\-]?\s*)",           # e.g. Here is the summary:
        r"^(sure[,:\-]?\s*)",                                 # e.g. Sure:
        r"^(as requested[,:\-]?\s*)",                         # e.g. As requested:
        r"^(let me summarize[,:\-]?\s*)",                     # e.g. Let me summarize:
        r"^(based on .*?,\s*)",   
    ]

    for pattern in patterns:
        text = re.sub(pattern, '', text, flags=re.IGNORECASE)

    return text.strip()



async def summarize_text(text:str) -> str:
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": MODEL,
        "messages": [
            {"role":"system", "content":(
            "You are an AI summarizer. You must respond with **only the summary** — no introductions, no phrases like 'Here is the summary', "
            "'Sure, here it is', or any other lead-in. Do not include closing lines or acknowledgments.\n\n"
            "**Rules:**\n"
            "- Output must start immediately with the summary content.\n"
            "- Return only the summary — nothing else.\n"
            "- Remove introductory phrase, filler words and redundant sentences.\n"
            "- Rewrite using clean, fluent English.\n"
            "- Maintain a neutral, professional tone.\n"
            "- Avoid using phrases or words that AI uses\n"
            "- If the input includes conversations, summarize key points or decisions.\n\n"
            "⚠️ If the input is short or simple, just return the summary. Nothing more."
            "Do not preface or follow the summary with any explanation, greetings, or commentary. Only return the summary content."
            "Be precise, neutral, and informative.")},
            {"role":"user","content":f"Summarize the following: \n\n{text}"}
        ],
        "temperature": 0.3
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, json=payload)

        if response.status_code != 200:
            raise Exception(f"Groq API error: {response.text}")
        
        summarized = response.json()["choices"][0]["message"]["content"]
        trimmed_result =  clean_summary_output(summarized)
        return trimmed_result

    