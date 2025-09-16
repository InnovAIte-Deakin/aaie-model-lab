{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # LM Studio Documentation\
\
## 1. LM Studio\
\
\pard\pardeftab720\qj\partightenfactor0

\fs26 \cf2 \expnd0\expndtw0\kerning0
LMStudio is designed to download and run open-source models (like Gemma, Qwen, Llama, Phi, etc.) on your own computer locally. The best thing about LM Studio is that it creates a local web server that mimics the API structure of a commercial service, specifically the OpenAI API. This means you can use the same code and tools you would use for GPT-4 to interact with a model running on your own machine, by just changing the API endpoint URL.
\fs28 \

\fs24 \cf0 \kerning1\expnd0\expndtw0 \
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0
\cf0 \
## 2. Setup Process\
\
### 2.1 Download and Install LM Studio\
- Navigate to the official LM Studio website: [https://lmstudio.ai/](https://lmstudio.ai/)  \
- Download the version for your operating system (Windows, macOS, or Linux). Below is an example for macOS.\
![LM Studio Download Page](images/lmstudio-download.png)\
- Download and install the application\
\
### 2.2 Find and Download an AI Model\
- Open LM Studio.  \
- Use the search bar to find a model you want.  For example, check the image below to search for the Gemma model \
![Model Search Example](images/lmstudio-search-gemma.png)\
- Click on the required model and then click the download button at the bottom right.\
\
### 2.3 Start the Local API Server\
- Select the model you want to use from the list of downloaded models.  \
- Click on the model like Gemma 3 1 B.  \
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0
\cf0 ![Model Selection](images/lmstudio-model-selection.png)\
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0
\cf0 - Review the server settings on the left (default Host: localhost, Port: 1234 are usually fine).  \
- Click Start Server.  \
![LM Studio Server Logs](images/lmstudio-server-start.png)\
Once started, you will see server logs, and the button will change to **Stop Server**.  \
Your local, OpenAI-compatible API is now running and ready to receive requests.\
\
## 3. LM Studio API Endpoints\
\
LM Studio exposes a local API that mimics commercial AI services. Below are the main endpoints:\
\
### 1. GET http://localhost:1234/v1/models\
- Retrieves a list of the models currently loaded and available.  \
- Useful for checking which model is active before sending a request.  \
- Returns a JSON object containing the model's identifier.\
\
### 2. POST http://localhost:1234/v1/chat/completions\
- Primary endpoint for generating text in a conversational format.  \
- Requires a JSON payload with a messages array.  \
- Each object in messages has:\
  - role (system, user, assistant)\
  - content (text)\
- The model responds with the next message based on the conversation context.\
\
### 3. POST http://localhost:1234/v1/completions\
- Generates text from a single prompt.  \
- Requires a JSON payload with a prompt key containing your text.  \
- Best for one-off tasks like summarization or headline generation.\
\
### 4. POST http://localhost:1234/v1/embeddings\
- Converts one or more text strings into numerical vector representations (embeddings).  \
- Requires a JSON payload with an input key containing a string or an array of strings.  \
- Returns a high-dimensional vector for each input string.\
\
## 4. Key Features\
\
- **Local Model Hosting**: Run models like Gemma, Qwen, LLaMA, Phi directly on your machine.  \
- **API Compatibility**: Mimics the OpenAI API, allowing easy integration with existing GPT-based tools.  \
- **Offline Operation**: Works without internet, great for sensitive data or limited connectivity.  \
- **Flexibility & Customization**: Experiment with models and parameters locally.  \
- **Ease of Integration**: Plug into existing applications without major code changes.\
\
## 5. Limitations\
\
- **Resource Intensive**: Running LLMs locally can consume 8\'9630+ GB RAM and benefit from a high-VRAM GPU.  \
- **Performance**: Slower inference compared to commercial cloud APIs unless using powerful hardware.  \
- **Single-User Focus**: Not optimized for high-concurrency production workloads.  \
- **No Commercial Support**: Relies on community forums for troubleshooting and updates.\
}