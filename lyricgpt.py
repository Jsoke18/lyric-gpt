import openai

openai.api_key = "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"

def generate_lyrics(prompt, model="text-davinci-002", tokens=400, temperature=0.5):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=tokens,
        n=1,
        stop=None,
        temperature=temperature,
    )

    return response.choices[0].text.strip()

# Replace 'Artist1', 'Artist2', etc. with the names of your favorite artists
prompt = """
Generate music lyrics inspired by the styles of Lil Uzi Vert and Playboi Carti. The song should capture their signature flows, ad-libs, and use of wordplay. Incorporate themes often found in their music, such as luxury lifestyle, relationships, and ambition. The lyrics should be catchy and have the potential to become a hit song. 

Structure the song with a captivating hook, energetic verses, and a memorable bridge. Include ad-libs and unique pronunciations that are characteristic of Lil Uzi Vert and Playboi Carti's music.

Verse 1:
"""


generated_lyrics = generate_lyrics(prompt, model="text-davinci-002", tokens=400, temperature=0.5)

print(generated_lyrics)
