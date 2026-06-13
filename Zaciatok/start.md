# Start

```bash
python -m venv venv
 # Windows
venv\Scripts\activate      
```

```bash
 # Linux/WSL
source venv/bin/activate 
```

```bash
pip install flask
```

```python
from markitdown import MarkItDown
from openai import OpenAI

md = MarkItDown(
    enable_plugins=True,
    llm_client=OpenAI(),
    llm_model="gpt-4o",
)
result = md.convert("document_with_images.pdf")
print(result.text_content)
```