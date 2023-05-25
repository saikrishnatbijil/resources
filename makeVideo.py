from moviepy.editor import TextClip,ImageClip, CompositeVideoClip, CompositeAudioClip, VideoFileClip, AudioFileClip, concatenate_videoclips, vfx

def resize_video(clip, output_path, new_width, new_height, image_path, text):
    # Load the video clip
    clip = clip

    # Resize the video clip while maintaining aspect ratio
    resized_clip = clip.resize(height=new_height)
    
    # Calculate the crop dimensions
    x_center = (resized_clip.size[0] - new_width) // 2
    y_center = (resized_clip.size[1] - new_height) // 2
    crop_x1 = x_center
    crop_y1 = y_center
    crop_x2 = x_center + new_width
    crop_y2 = y_center + new_height
    
    # Apply the crop
    cropped_clip = resized_clip.crop(x1=crop_x1, y1=crop_y1, x2=crop_x2, y2=crop_y2)

    # Load the image clip
    image_clip = ImageClip(image_path)
    image_clip = image_clip.set_duration(cropped_clip.duration)  # Set image duration same as video

    # Create the text clip for credits
    credits_text = TextClip(text, fontsize=30, color='black', font='Arial-Bold',
                            stroke_color='black', stroke_width=1, ) 
    credits_text = credits_text.margin(left=20, bottom=30, opacity=0)
    credits_text = credits_text.set_position(("left", "bottom")).set_duration(cropped_clip.duration)

    # Composite the video, image, and text clips
    final_clip = CompositeVideoClip([cropped_clip, image_clip.set_position(("center"))])
    final_clip = CompositeVideoClip([final_clip, credits_text])

    # Write the final clip to a new file
    final_clip.write_videofile(output_path)

    # Close the clips
    clip.close()
    resized_clip.close()
    cropped_clip.close()
    image_clip.close()
    credits_text.close()
    final_clip.close()

background_clip = VideoFileClip("background.mov").subclip(0, 3).without_audio()
background_clip2 = VideoFileClip("background.mov").subclip(3, 6).without_audio()
background_clip3 = VideoFileClip("second.mov").subclip(6, 9).without_audio()
background_clip4 = VideoFileClip("background.mov").subclip(9, 12).without_audio()
background_clip5 = VideoFileClip("second.mov").subclip(0, 3).without_audio()
background_clip6 = VideoFileClip("background.mov").subclip(20, 21).without_audio()
# background_clip7 = VideoFileClip("background.mov").subclip(15, 20).without_audio()
# background_clip8 = VideoFileClip("second.mp4").subclip(4, 15).without_audio()


audio = AudioFileClip("audio.mp3").fx(vfx.speedx, 1)
combined =  concatenate_videoclips([background_clip, background_clip2, background_clip3, background_clip4, background_clip5, background_clip6])
# combined =  concatenate_videoclips([background_clip])

combined = combined.set_audio(CompositeAudioClip([audio]))
# combined.audio = CompositeAudioClip([audio])
print(combined.size)

# Example usage
output_path = 'output_video.mp4'
new_width = 1080
new_height = 1920
image_path = 'heading.png'
text = 'Credits: Mrwhosetheboss'

resize_video(combined, output_path, new_width, new_height, image_path, text)
