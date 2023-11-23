import requests
import json
def chat_with_gpt(input_) : 
    url = "http://127.0.0.1:5001/chat"
    response = requests.post(url, data=json.dumps({"message": input_}), headers = {"Content-Type": "application/json"})
    return response.text

if __name__ == "__main__":
    while True:
        input_ = input("Vous : \n")
        print("\n Chat GPT : \n" + chat_with_gpt(input_))