# gpt-adcreator
this will automatically create a video ad with visuals, scripts, audio, and hooks

i took the code from the open-source '[gpt-researcher]([url](https://github.com/assafelovic/gpt-researcher)https://github.com/assafelovic/gpt-researcher)' and edited the prompts and report outputs

current state:
- ask a question (e.g. 'how did people fix their chronic back pain?')
- it generates 4 google queries
- it scrapes reddit and online forums to research each of the 4 google queries
- it outputs a 'Customer Language Report' that tells customer stories of a product/niche in your question
- another option is a 'Script Report' where i tell it to use the research to write sales copy using a proven framework

future state:
- take the output from the 'Script Report' and feed it into a text2audio AI like ElevenLabs or Bark AI
- fine-tune LLM on hundreds of script examples so script reads natural
- use deforum stable diffusion to generate visuals based on prompts from GPT4
- ingest b-roll footage from brands and let GPT4 decide how to storyboard them
- let GPT4 decide on stock footage based on the script and product
- use moviepy or Canva API to stitch videos together
- ingest performance data to create positive feedback loop of what's working
- and much more!

things you need to run it:
- an API key from OpenAI with GPT4 access

steps to run it:
Step 0 - Install Python 3.11 or later. See here for a step-by-step guide.


Step 1 - Download the project

$ git clone https://github.com/mchen29/gpt-adcreator.git

$ cd gpt-adcreator

Step 2 - Install dependencies

$ pip install -r requirements.txt

Step 3 - Create .env file with your OpenAI Key or simply export it

$ export OPENAI_API_KEY={Your API Key here}

Step 4 - Run the agent with FastAPI

$ uvicorn main:app --reload


massive props to the gpt-researcher guys.
