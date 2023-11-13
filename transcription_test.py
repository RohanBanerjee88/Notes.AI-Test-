from youtube_transcript_api import YouTubeTranscriptApi
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import nltk
nltk.download('punkt')


def generate_summary(youtube_link, num_sentences=5):
    try:
        # Get the YouTube video ID from the link
        video_id = youtube_link.split("v=")[1]

        # Get the transcript for the video
        transcript = YouTubeTranscriptApi.get_transcript(video_id)

        # Combine all the text from the transcript into one string
        text = ' '.join([entry['text'] for entry in transcript])

        # Use Sumy for text summarization
        parser = PlaintextParser.from_string(text, Tokenizer("english"))
        summarizer = LsaSummarizer()

        # Get the summary
        summary_sentences = summarizer(parser.document, num_sentences)

        # Combine the summary sentences into one string
        summary = ' '.join(str(sentence) for sentence in summary_sentences)

        return summary

    except Exception as e:
        return f"An error occurred: {str(e)}"

# Example usage
youtube_link = "https://www.youtube.com/watch?v=y1F-M32Aytg&pp=ygUtcGlnZW9uIGhvbGUgcHJpbmNpcGxlIGVuZ2luZWVyaW5nIG1hdGhlbWF0aWNz"
summary = generate_summary(youtube_link)

print("Generated Summary:")
print(summary)
