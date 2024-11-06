import requests
import pyttsx3
import time

def TTS(text):
    talking_thing_somethin_idk = pyttsx3.init()
    talking_thing_somethin_idk.say(text)
    talking_thing_somethin_idk.runAndWait()



def main():
    urls = {
        "dad_joke": "https://icanhazdadjoke.com/",
        "normal_joke": "https://v2.jokeapi.dev/joke/Any",
        "Programming_joke": "https://v2.jokeapi.dev/joke/Programming"
    }

    while True:
        print("1)Dad Jokes\n2)Basic Jokes\n3)Programming Jokes\n4)Exit")

        user_input = int(input("> "))

        if user_input == 1:
            dad_response = requests.get(urls["dad_joke"], headers={"Accept": "application/json"})

            if dad_response.status_code == 200:
                dad_jokes = dad_response.json().get("joke")
                print(f"Joke (Dad Joke): {dad_jokes}\n")
                TTS(dad_jokes)

            else:
                print(f"Oh Noes. Something has gone wrong!\nError: {dad_response}")
                TTS(f"Oh Noes. Something has gone wrong!\nError: {dad_response}")
            continue

        elif user_input == 2:
            while True:
                joke_response = requests.get(urls["normal_joke"], params={"format": "json"})

                if joke_response.status_code == 200:
                    jokes = joke_response.json()

                    if jokes["type"] == "twopart":
                        print("Joke: ", jokes["setup"])
                        TTS(jokes["setup"])
                        time.sleep(1)
                        print(f"Punchline:  {jokes["delivery"]}\n")
                        TTS(jokes["delivery"])
                    else:
                        continue
                    main()

                else:
                    print(f"Oh Noes. Something has gone wrong!\nError: {joke_response}")
                    TTS(f"Oh Noes. Something has gone wrong!\nError: {joke_response}")

        elif user_input == 3:
            while True:
                pro_req = requests.get(urls["Programming_joke"], headers={"Accept": "application/json"})

                if pro_req.status_code == 200:
                    json = pro_req.json()
                    if json["type"] == "twopart":

                        print(f"Joke(Programming Joke): {json["setup"]}\n")
                        TTS(json["setup"]) 
                        time.sleep(1)
                        print(f"Punchline: {json["delivery"]}")
                        TTS(json["delivery"])
                    else:
                        continue
                    main()


                else:
                    print(f"Oh Noes. Something has gone wrong!\nError: {pro_req}")
                    TTS(f"Oh Noes. Something has gone wrong!\nError: {pro_req}")
                    continue
                
        elif user_input == 4:
            print("Goodbye!")
            TTS("GoodBye!")
            exit()

        else:
            print("Enter A Valid Choice!")
            continue


if __name__ == "__main__":
    main()
