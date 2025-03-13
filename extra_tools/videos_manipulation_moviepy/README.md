# Manipulation Video

This package provides Python scripts to manipulate videos using `moviepy`. It includes functionalities to:
- Extract a portion of a video
- Remove a section of a video and merge the remaining parts
- Overlay one video onto another (e.g., a speaker video over a background video)

## Installation
Ensure you have Python installed and install the required dependency:
```bash
pip install moviepy
```

## Scripts Usage

### 1. Extract a Portion of a Video
This script extracts a section of a video between a given start and end time.

#### Usage:
```bash
python extract_video.py --input-video-path input.mp4 --start-time 00:10:00 --end-time 00:15:00 --output-video-path output.mp4
```

#### Example:
```bash
python extract_video.py --input-video-path sample.mp4 --start-time 00:05:00 --end-time 00:10:00 --output-video-path extracted.mp4
```

### 2. Remove a Section of a Video
This script removes a section of a video between a given start and end time and merges the remaining parts.

#### Usage:
```bash
python cut_video.py --input-video-path input.mp4 --start-time 00:10:00 --end-time 00:15:00 --output-video-path output.mp4
```

#### Example:
```bash
python cut_video.py --input-video-path sample.mp4 --start-time 00:02:30 --end-time 00:04:30 --output-video-path modified.mp4
```

### 3. Merge Two Videos (Overlay Speaker on Background)
This script overlays a speaker video onto a background video.

#### Usage:
```bash
python merge_videos.py --background-video-path background.mp4 --speaker-video-path speaker.mp4 --output-video-path output.mp4
```

#### Example:
```bash
python merge_videos.py --background-video-path presentation.mp4 --speaker-video-path speaker.mp4 --output-video-path final_video.mp4
```

## Notes
- **Input videos** must be in a format supported by `moviepy` (e.g., `.mp4`).
- Ensure the videos have compatible resolutions and frame rates for the best results.
- If necessary, use `ffmpeg` to preprocess videos:
  ```bash
  ffmpeg -i input.mp4 -vf "scale=1280:720" -r 30 output.mp4
  ```

## License
This project is open-source and free to use.