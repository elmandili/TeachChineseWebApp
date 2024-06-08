import ffmpeg

def convert_mp3_to_pcm(input_file, output_file):
    try:
        ffmpeg.input(input_file).output(output_file, format='s16le', acodec='pcm_s16le', ac=1, ar=16000).run(overwrite_output=True)
        print(f'Successfully converted {input_file} to {output_file}')
    except ffmpeg.Error as e:
        print(f'Error occurred: {e.stderr.decode()}')

if __name__ == "__main__":
    # Define input and output file paths here
    input_mp3_file = r'./input'  # Change this to your input MP3 file path
    output_pcm_file = r'./output_pcm'  # Change this to your desired output PCM file path

    convert_mp3_to_pcm(input_mp3_file, output_pcm_file)
