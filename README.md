## About the Chatbot - Meet Llamastar
Let's introduce you to the star of the show, Llamastar! This AI comedian bot was crafted using TheBloke's Llama-2-7B-chat-GPTQ model. But that's not all; I've spiced it up with Gradio and Langchain applications to provide you with an interactive and entertaining experience. Feel free to explore Llamastar's comedic talents and have a blast at the AI Comedy Club! 🎤😄
## Prerequisites

Before you begin, ensure you have the following prerequisites:

- A system with an NVIDIA GPU.
- NVIDIA Docker runtime (nvidia-docker2) installed. You can find installation instructions here: [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-runtime).(optional)

## Local Setup (Without Docker)

### Step 1: Clone the Repository

If you haven't already, clone the AI Comedy Club repository to your local machine:

```bash
git clone https://github.com/onur-rgb/ai-joke-bot.git
```

### Step 2: Install Dependencies

1. Open a terminal and navigate to the project directory:

```bash
cd ai-joke-bot
```

2. Install the necessary Python dependencies using pip:

```bash
pip install -r requirements.txt
```

### Step 3: Run the AI Comedian Bot

You can now run your AI comedian bot locally using the following command:

```bash
python joke_bot.py
```

The AI comedian bot is now running locally, and you can interact with it as needed.

## Docker Setup (With GPU Support)

### Step 1: Clone the Repository

If you haven't already, clone the AI Comedy Club repository to your local machine:

```bash
git clone https://github.com/onur-rgb/ai-joke-bot.git
```

### Step 2: Build the Docker Image

1. Open a terminal and navigate to the project directory:

```bash
cd ai-joke-bot
```

2. Build the Docker image using the following command:

```bash
docker build -t my-joke-bot .
```

This command builds a Docker image named `my-joke-bot` with GPU support based on the contents of the Dockerfile.

### Step 3: Run the Docker Container

To run your AI comedian bot inside a Docker container with GPU support, use the following command:

```bash
docker run --gpus all -it my-joke-bot
```

AI comedian bot is now running within the Docker container. You can interact with it as needed.

