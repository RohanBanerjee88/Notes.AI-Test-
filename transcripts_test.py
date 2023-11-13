import openai
from youtube_transcript_api import YouTubeTranscriptApi

def get_full_transcript(youtube_link):
    try:
        # Get the YouTube video ID from the link
        video_id = youtube_link.split("v=")[1]

        # Get the transcript for the video
        transcript = YouTubeTranscriptApi.get_transcript(video_id)

        # Combine all the text from the transcript into one string
        full_transcript = ' '.join([entry['text'] for entry in transcript])

        return full_transcript

    except Exception as e:
        return f"An error occurred: {str(e)}"

def generate_summary(transcript, max_tokens=150):
    try:
        # Set up your OpenAI API key
        openai.api_key = 'key_keys'

        # Generate a summary using OpenAI GPT-3
        response = openai.Completion.create(
            engine="text-davinci-003",  # Specify the GPT-3 engine
            prompt=f"Summarize the following text:\n'{transcript}'",
            max_tokens=max_tokens
        )

        summary = response['choices'][0]['text'].strip()
        return summary

    except Exception as e:
        return f"An error occurred: {str(e)}"

# Example usage
youtube_link = "https://www.youtube.com/watch?v=y1F-M32Aytg&pp=ygUtcGlnZW9uIGhvbGUgcHJpbmNpcGxlIGVuZ2luZWVyaW5nIG1hdGhlbWF0aWNz"
transcript = get_full_transcript(youtube_link)

print("Full Transcript:")
print(transcript)

summary = generate_summary(transcript)
print("\nSummary:")
print(summary)
