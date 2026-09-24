from dotenv import load_dotenv
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    google_api_key=os.environ["GOOGLE_API_KEY"],
    output_dimensionality=768
)
vector = embeddings.embed_query("test incident runbook")
print(len(vector))   # 768 aana chahiye