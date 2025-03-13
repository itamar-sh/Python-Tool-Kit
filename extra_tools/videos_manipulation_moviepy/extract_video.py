from argparse import ArgumentParser
from moviepy.video.io.VideoFileClip import VideoFileClip

def extract_video(input_path, start_time, end_time, output_path):
    # Convert time strings to seconds
    start_time_seconds = sum(x * int(t) for x, t in zip([3600, 60, 1], start_time.split(':')))
    end_time_seconds = sum(x * int(t) for x, t in zip([3600, 60, 1], end_time.split(':')))

    # Load video clip
    video_clip = VideoFileClip(input_path)

    # Extract the desired section
    extracted_clip = video_clip.subclip(start_time_seconds, end_time_seconds)

    # Write the new video to a file
    extracted_clip.write_videofile(output_path, codec="libx264", audio_codec="aac", temp_audiofile="temp.m4a", remove_temp=True)

def main():
    parser = ArgumentParser()
    parser.add_argument('--input-video-path', required=True)
    parser.add_argument('--start-time', required=True)
    parser.add_argument('--end-time', required=True)
    parser.add_argument('--output-video-path', required=True)
    args = parser.parse_args()

    extract_video(args.input_video_path, args.start_time, args.end_time, args.output_video_path)

if __name__ == '__main__':
    main()
