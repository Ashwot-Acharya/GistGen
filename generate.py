import openai
import os
openai.api_key = os.getenv("OPENAI_API_KEY")


def TextSummary(text_pdf):
    openai.api_key = api

    input_text = text_pdf
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=input_text,
        max_tokens=1024,
        n=1,
        temperature=0.5,
    )

    output_summary = completions.choices[0].text

    return output_summary