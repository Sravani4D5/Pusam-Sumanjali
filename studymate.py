import pdfplumber
import openai

openai.api_key = "sk-your_actual_api_key_here"  # Replace with your actual API key

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

def ask_question(context, question):
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {question}"}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=150,
        temperature=0,
    )
    return response.choices[0].message['content'].strip()

def main():
    pdf_path = input("Enter the path to your PDF file: ")
    print("Extracting text from PDF...")
    context = extract_text_from_pdf(pdf_path)
    print("Text extracted. You can now ask questions.")

    while True:
        question = input("\nAsk a question (or type 'exit' to quit): ")
        if question.lower() == 'exit':
            print("Goodbye!")
            break
        answer = ask_question(context, question)
        print(f"Answer: {answer}")

if __name__ == "__main__":
    main()
