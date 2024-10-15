import argparse
import os.path
import sys
import cv2
# parser=argparse.ArgumentParser()
# parser.add_argument("--a",type=int,help="A number")# positonal argument
# parser.add_argument("way",type=str,help="A str")# optional argument
# parser.add_argument("--verbose",action="store_true",help="Print Message")
# args=parser.parse_args()
# print(args.a)
# print(args.way)
# print(args.verbose)

import argparse
import cv2
import numpy as np

def parse_args():
    parser = argparse.ArgumentParser(description="Cut and save a part of an image.")
    parser.add_argument("image_path", type=str, help="Path to the input image.")
    parser.add_argument("x", type=int, help="X coordinate of the top-left corner of the cut area.")
    parser.add_argument("y", type=int, help="Y coordinate of the top-left corner of the cut area.")
    parser.add_argument("width", type=int, help="Width of the cut area.")
    parser.add_argument("height", type=int, help="Height of the cut area.")
    parser.add_argument("--output_path", type=str, help="Path to save the output image.")
    return parser.parse_args()

def cut_image(image_path, x, y, width, height):
    # Read the image
    orgin=os.path.join(image_path, "image.jpg")
    output=os.path.join(image_path, "cut.jpg")
    image = cv2.imread(orgin)
    if image is None:
        raise ValueError("Image not found or path is incorrect")
    # Cut the image
    cut_image = image[y:y+height, x:x+width]
    # Save the cut image
    cv2.imwrite(output, cut_image)
    print(f"Image saved to {output}")

def main():
    args = parse_args()
    # Save the cut image
    cut_image(args.image_path, args.x, args.y, args.width, args.height)

if __name__ == "__main__":
    main()