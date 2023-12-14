# videogen/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

def generate_video(input_path, output_path):
    # Load the video clip
    video_clip = VideoFileClip(input_path)

    # Create a text clip
    text_clip = TextClip("Hello, World!", fontsize=70, color='white')

    # Overlay the text clip on the video clip
    text_overlay = CompositeVideoClip([video_clip, text_clip.set_pos('center')])

    # Write the result to an output file
    text_overlay.write_videofile(output_path, codec='libx264', audio_codec='aac')

class VideoGenerationView(APIView):
    def get(self, request):
        input_video_path = "/home/subham/Downloads/video.mp4"  # Replace with your actual input video file path
        output_video_path = "/home/subham/Downloads/video.mp4"
        generate_video(input_video_path, output_video_path)

        return Response({"message": "Video generated successfully"}, status=status.HTTP_200_OK)
