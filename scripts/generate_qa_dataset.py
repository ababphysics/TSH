import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
try:
    client = OpenAI()
except Exception as e:
    print(f"Error initializing OpenAI client: {e}")
    print("Please make sure OPENAI_API_KEY is set in your .env file.")
    exit(1)

def generate_qa_pairs(chunk, num_pairs=3):
    prompt = f"""
    Read the following text about the Thickness Structure Hypothesis (TSH).
    Generate {num_pairs} question and answer pairs based solely on this text.
    The questions should test the understanding of the core concepts of TSH.
    Output JSON format exactly like this:
    {{
        "pairs": [
            {{"user": "Question here", "assistant": "Answer here"}}
        ]
    }}
    Text: {chunk}
    """
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        response_format={ "type": "json_object" }
    )
    
    return json.loads(response.choices[0].message.content)

def create_dataset():
    data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'tsh_paper.txt')
    output_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'tsh_finetune.jsonl')
    
    if not os.path.exists(data_path):
        print(f"Error: {data_path} not found. Please run extract_text.py first.")
        return

    print(f"Reading text from {data_path}...")
    with open(data_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # Simple chunking by paragraph (split by double newlines)
    paragraphs = text.split('\n\n')
    # Only take substantial paragraphs
    valid_chunks = [p for p in paragraphs if len(p.strip()) > 200]
    
    print(f"Found {len(valid_chunks)} chunks for dataset generation.")
    
    dataset = []
    
    # Process chunks to generate QA pairs
    # Note: Processing all chunks can consume API tokens. 
    # For a full run, remove the slicing `[:5]`.
    for i, chunk in enumerate(valid_chunks):
        print(f"Processing chunk {i+1}/{len(valid_chunks)}...")
        try:
            result = generate_qa_pairs(chunk, num_pairs=3)
            
            for pair in result.get("pairs", []):
                qa_line = {
                    "messages": [
                        {"role": "system", "content": "You are an expert AI assistant specializing in the Thickness Structure Hypothesis (TSH) by Hirokazu Abe."},
                        {"role": "user", "content": pair["user"]},
                        {"role": "assistant", "content": pair["assistant"]}
                    ]
                }
                dataset.append(qa_line)
        except Exception as e:
            print(f"Error processing chunk: {e}")
            
    # Save the dataset in JSONL format
    print(f"Saving dataset to {output_path}...")
    with open(output_path, 'w', encoding='utf-8') as f:
        for item in dataset:
            f.write(json.dumps(item, ensure_ascii=False) + '\n')
            
    print(f"Dataset generated successfully! Saved {len(dataset)} examples.")

if __name__ == "__main__":
    create_dataset()
