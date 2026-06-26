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

## Dokumentacia MarkDown

- Syntax [MarkDown](https://markdowncheatsheet.com/reference)
- Everything you need to learn Markdown [MarkDown](https://www.markdownguide.org/)
- Basic syntax [BasicSyntax]([text](https://www.markdownguide.org/basic-syntax/))

## Difference between HTML and CSS  

<https://www.geeksforgeeks.org/css/difference-between-html-and-css/>  

[HTML Tutorial](https://www.geeksforgeeks.org/html/html-tutorial/)  
[Štúdium a pokračovanie](https://www.geeksforgeeks.org/html/html-elements/)

[Best HTML Coding Practices You Must Know](https://www.geeksforgeeks.org/html/best-html-coding-practices-you-must-know/)  
[HTML vo Visual Studio Code](https://code.visualstudio.com/Docs/languages/html)  
Dopĺňanie tagov a náhľad pravým tlačítkom myši v zozname súborov  
Odporúčam prečítať si článok ako pracovať s editor pri písaní html kódu  

[CSS Tutorial](https://www.geeksforgeeks.org/css/css-tutorial/)  
