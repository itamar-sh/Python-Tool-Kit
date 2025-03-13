import whisper
from argparse import ArgumentParser

def transcribe_audio(audio_file_path, model_size="large", language=None):
    model = whisper.load_model(model_size)
    result = model.transcribe(audio_file_path, language=language)
    return result['text']

def save_transcript(transcript, output_file_path):
    with open(output_file_path, 'w') as f:
        f.write(transcript)

def main():
    parser = ArgumentParser()
    parser.add_argument('--audio-file-path', required=True, help="Path to audio file")
    parser.add_argument('--output-file-path', required=True, help="Path to save transcript")
    parser.add_argument('--model-size', default="large", help="Whisper model size (tiny, base, small, medium, large)")
    parser.add_argument('--language', default="he", help="Language code (e.g., 'he' for Hebrew, 'en' for English)")
    args = parser.parse_args()

    transcript = transcribe_audio(args.audio_file_path, args.model_size, args.language)
    save_transcript(transcript, args.output_file_path)
    print(f"Transcription saved to {args.output_file_path}")

if __name__ == '__main__':
    main()
