import nest_asyncio
nest_asyncio.apply()

from llama_parse import LlamaParse
from llama_parse.base import Document
from py_dotenv import read_dotenv
import os

read_dotenv(os.path.join(os.path.dirname(__file__), '../.env'))

async def parse_file(file: bytes, file_name: str) -> list[Document]:
    documents = None

    parser = LlamaParse(
        result_type="text",
        fast_mode=True,
        num_workers=4,
        verbose=True,
    )
    
    documents = await parser.aload_data(file, extra_info={"file_name": file_name})
        
    return documents