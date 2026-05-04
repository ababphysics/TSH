import os
from bs4 import BeautifulSoup

def extract_text_from_html(html_path, output_path):
    print(f"Reading HTML from {html_path}...")
    with open(html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Remove script and style elements
    for script in soup(["script", "style"]):
        script.extract()

    # Get text
    text = soup.get_text(separator='\n\n')

    # Break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # Break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # Drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)

    # Save to file
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(text)
    
    print(f"Extracted text saved to {output_path}")

if __name__ == "__main__":
    html_file = os.path.join(os.path.dirname(__file__), '..', 'data', 'tsh_paper.html')
    output_file = os.path.join(os.path.dirname(__file__), '..', 'data', 'tsh_paper.txt')
    extract_text_from_html(html_file, output_file)
