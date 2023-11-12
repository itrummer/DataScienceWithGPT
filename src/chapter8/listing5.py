'''
Created on Nov 11, 2023

@author: immanueltrummer
'''
import argparse
import cv2
import base64
import openai
import time


def extract_frames(video_path):
    """ Extracts frames from a video.
    
    Args:
        video_path: path to video file.
    
    Returns:
        list of video frames.
    """
    video = cv2.VideoCapture(video_path)
    frames = []
    while video.isOpened():
        success, frame = video.read()
        if not success:
            break
        
        _, buffer = cv2.imencode('.jpg', frame)
        encoded = base64.b64encode(buffer)
        frame = encoded.decode('utf-8')
        frames += [frame]
    
    video.release()
    return frames


def create_prompt(frames):
    """ Create prompt to generate title for video.
    
    Args:
        frames: frames of video.
    
    Returns:
        prompt containing multimodal data (as list).
    """
    prompt = ['Generate a concise title for the video.']
    for frame in frames[:10]:
        element = {'image':frame, 'resize':768}
        prompt += [element]
    return prompt


def call_llm(prompt):
    """ Query large language model and return answer.
    
    Args:
        prompt: input prompt for language model.
    
    Returns:
        Answer by language model.
    """
    for nr_retries in range(1, 4):
        try:
            response = openai.ChatCompletion.create(
                model='gpt-4-vision-preview',
                messages=[
                    {'role':'user', 'content':prompt}
                    ]
                )
            return response['choices'][0]['message']['content']
        except:
            time.sleep(nr_retries * 2)
    raise Exception('Cannot query OpenAI model!')


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('openaikey', type=str, help='OpenAI access key')
    parser.add_argument('videopath', type=str, help='Path of video file')
    args = parser.parse_args()
    
    openai.api_key = args.openaikey
    
    frames = extract_frames(args.videopath)
    prompt = create_prompt(frames)
    title = call_llm(prompt)
    print(title)