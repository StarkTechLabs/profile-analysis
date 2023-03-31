# profile-analysis

Collection of python code to pull data from twitter and compare two twitter profiles to one another. Will be expanded to profiles outside of twitter and possibly used to search for similar profiles of a given profile.

## Setup

- `python3 -m venv .venv` create virutal env with python3
- `source .venv/bin/activate` activate virtual env
- `pip install -r requirements.txt` install required dependencies

### Environment Variables

- TWITTER_APP_TOKEN - bearer token from twitter developer console
- PINECONE_API_KEY - pinecode api key to access embeddings index

### Running

`python run.py -d`
