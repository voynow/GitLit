from dotenv import load_dotenv
import os

# load environ config from .env file
load_dotenv()

GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]

OUTLINE_TEMPLATE = """
You are a highly respected software engineering technical writer. Your niche is writing informative articles about the latest and greatest open source projects. The audience of this article will be other developers who want to learn the technical nuts and bolts of this repo.

Here is the code from a project you are reviewing:
{repo_str}

Write an outline for an educational article taking a deep dive on this project. The article will talk about system architecture, design decisions, the technical details of the code, and etc.
"""

ARTICLE_TEMPLATE = """
You are a highly respected software engineering technical writer. Your niche is writing informative articles about the latest and greatest open source projects. The audience of this article will be other developers who want to learn the technical nuts and bolts of this repo.

Here is the code from a project you are reviewing:
{repo_str}

Here is an outline for an educational article with many sections and paragraphs taking a deep dive on this project:
{outline}

Write the article based on the outline using all of your software technical writing expertise to make the article as informative and educational as possible. Expand upon the code/outline with details, code examples, and explanations. Focus on what makes the repo unique rather than things like .gitignore or setup.py. Feel free to add more sections and paragraphs as you see fit. Restructure the article to improve the user experience. Format in markdown.
"""
EXCLUDE_EXTENSIONS = [
    ".ipynb",
    ".yaml",
    ".yml",
    ".json",
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".svg",
    ".csv",
    ".txt",
    ".jsonl",
    ".struct",
    ".map",
    ".obj",
    ".cleaned",
    ".dict",
    ".GIF",
    ".tiktoken",
    ".lock",
    ".pack",
    ".sub",
    ".zh_CN",
    ".dae",
    ".zh_CN_tgt",
    ".dat",
    ".tsv",
    ".tokens",
    ".off",
    ".sense",
    ".log",
    ".bvh",
    ".onnx",
    ".gltf",
    ".cif",
    ".geojson",
    ".pkl",
    ".bin",
    ".pdb",
    ".sdf",
    ".xmi",
    ".out",
    ".train",
    ".stl",
    ".kicad_pcb",
    ".mp3",
    ".pdf",
    ".npy",
    ".pyc",
    ".ttf",
    ".woff",
    ".woff2",
    ".eot",
    ".otf",
    ".wav",
    ".mp4",
    ".swp",
    ".mat",
]
