from summary import generate_summary
from detailed import *
from transcripts_test import get_full_transcript

if __name__ == "__main__":
    youtube_link = "https://www.youtube.com/watch?v=y1F-M32Aytg&pp=ygUtcGlnZW9uIGhvbGUgcHJpbmNpcGxlIGVuZ2luZWVyaW5nIG1hdGhlbWF0aWNz"
    transcript = get_full_transcript(youtube_link)

    # print("Full Transcript:")
    # print(transcript)

    summary = generate_summary(transcript)
    print("\nGenerated Summary:")
    print(summary)
    
    
    notes = detailed_notes(transcript)
    print("\nGenerated Detailed Notes:")
    print(notes)
