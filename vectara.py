import requests
import json


# Step 1 Create Corpus
# url = "https://api.vectara.io/v1/create-corpus"

# payload = json.dumps(
#     {"corpus": {"name": "Interactive Video", "description": "Interactive Video"}}
# )
# headers = {
#     "Content-Type": "application/json",
#     "Accept": "application/json",
#     "x-api-key": "zut_IccVS9aWrgH6-s9K--BKSt9pVfYKgClXR8j3cg",
# }

# response = requests.request("POST", url, headers=headers, data=payload)

# print(response.text)


# Step 1 Reset Corpus
def ResetCorpus():
    url = "https://api.vectara.io/v1/reset-corpus"

    payload = json.dumps({"corpusId": 15})
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "x-api-key": "zut_IccVS9aWrgH6-s9K--BKSt9pVfYKgClXR8j3cg",
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


# Step 2 Add Transcription Txt to Corpus
def AddVideoTranscription():
    url = "https://api.vectara.io/v1/upload?c=566695243&o=15"

    payload = {}
    files = [
        ("file", ("video_transcription", open("message.txt", "rb"), "application/txt"))
    ]
    headers = {
        "customer-id": "566695243",
        "Accept": "application/json",
        "x-api-key": "zut_IccVS9aWrgH6-s9K--BKSt9pVfYKgClXR8j3cg",
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    print(response.text)


ResetCorpus()
AddVideoTranscription()
