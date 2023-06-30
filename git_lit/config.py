from dotenv import load_dotenv
import os

# load environ config from .env file
load_dotenv()

GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]

TEMPLATE = """
You are a highly respected software engineering technical writer. Your niche is writing informative articles about the latest and greatest open source projects. The audience of this article will be other developers who want to learn the technical nuts and bolts of this repo.

Here is the code from a project you are reviewing:
{repo_str}

Write an educational article with many sections and paragraphs taking a deep dive on this project. 
Explain in-depth how the system is designed and the software architecture
Select the some of the most critical tools/packages used in this repo and write a few sentences on how each is used
Expand upon contribution ideas and how this work can be extrapolated to adjacent projects and work streams 
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
    ".npy"
]

GH_GQL_QUERY = """
    query RepoFiles($owner: String!, $name: String!, $branch: String!) {
    repository(owner: $owner, name: $name) {
        object(expression: $branch) {
        ... on Tree {
            entries {
            name
            
            type
            
            object {
                ... on Blob {
                byteSize
                
                text
                }
            }
            }
        }
        }
    }
    }
"""