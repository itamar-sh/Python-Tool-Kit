# This script is using for cut out a piece of video
from argparse import ArgumentParser

from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.editor import concatenate_videoclips

def cut_video(input_path, start_time, end_time, output_path):
    # Convert time strings to seconds
    start_time_seconds = sum(x * int(t) for x, t in zip([3600, 60, 1], start_time.split(':')))
    end_time_seconds = sum(x * int(t) for x, t in zip([3600, 60, 1], end_time.split(':')))

    # Load video clip
    video_clip = VideoFileClip(input_path)

    # Clip before the specified range
    clip_before = video_clip.subclip(0, start_time_seconds)

    # Clip after the specified range
    clip_after = video_clip.subclip(end_time_seconds, video_clip.duration)

    # Concatenate the clips
    final_clip = concatenate_videoclips([clip_before, clip_after])

    # Write the new video to a file
    final_clip.write_videofile(output_path, codec="libx264", audio_codec="aac", temp_audiofile="temp.m4a", remove_temp=True)

def main():
    parser = ArgumentParser()
    parser.add_argument('--input-video-path', required=True)
    parser.add_argument('--start-time', required=True)
    parser.add_argument('--end-time', required=True)
    parser.add_argument('--output-video-path', required=True)
    args = parser.parse_args()

    # Example usage
    # input_video_path = "screen.mp4"
    # start_time = "00:46:34"
    # end_time = "01:01:42"
    # output_video_path = "cut_screen.mp4"

    cut_video(args.input_video_path, args.start_time, args.end_time, args.output_video_path)

if __name__ == '__main__':
    main()
