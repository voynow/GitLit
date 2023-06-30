# FableForge: An Open Source Project for Generating Picture Books

FableForge is an innovative open source project that allows users to generate a picture book from a single prompt. This project leverages the power of OpenAI's new function calling and Replicate's API for Stable Diffusion to generate images and corresponding prompts. All generated images and prompts are stored in Deep Lake, a cloud-based storage solution.

## Project Structure

The project is structured into several Python files, each serving a specific purpose:

- `api_utils.py`: Contains the `BuildBook` class that handles the generation of the book text and images.
- `deep_lake_utils.py`: Contains the `SaveToDeepLake` class that handles saving the generated images and prompts to Deep Lake.
- `main.py`: The main script that runs the application.
- `pdf_gen_utils.py`: Contains functions for generating the final PDF of the picture book.
- `prompts.py`: Contains the prompts used for generating the book text and images.

## Key Features

FableForge offers several key features:

- **Book Generation**: FableForge generates a picture book based on a single user-provided prompt. The book is generated in a PDF format, making it easy to download and share.
- **Image Generation**: The project uses Replicate's API for Stable Diffusion to generate images based on the book text. The images are then downloaded and stored for use in the final PDF.
- **Deep Lake Integration**: FableForge integrates with Deep Lake, allowing users to store all generated images and corresponding prompts in the cloud. This makes it easy to access and manage the generated data.
- **Customizable Styles**: Users can select from a variety of styles for their picture book, including Impressionism, Cubism, Surrealism, Japanese Ukiyo-e, Art Nouveau, Folk Art, and Expressionism.

## Installation and Usage

To use FableForge, users need to clone the repository and install the requirements specified in `requirements.txt`. Users also need to set up their OpenAI and Replicate API keys in `keys.env`. To save images and prompts, users need to set up their Activeloop Deep Lake token and dataset path in `keys.env`.

Once the setup is complete, users can start the application by running `streamlit run main.py`.

## Conclusion

FableForge is a powerful tool for generating picture books. It leverages the power of OpenAI and Replicate's API to generate engaging and visually appealing books based on a single prompt. With its Deep Lake integration, FableForge also makes it easy to store and manage the generated data. Whether you're an author looking for inspiration or a parent wanting to create a unique story for your child, FableForge is a great tool to explore.