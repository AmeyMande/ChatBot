qna = {
    "hi":"hey",
    "hey":"hi",
    "how are you":"I am fine",
    "how it's going":"Trying to do better",
    "how are you doing":"Doing Fine till now",
    "what's up":"Hi tell me about your query",
    "what is your name":"I am Jarvis",
    "how old are you":"I am a bot,I don't have age",
    "i neer some advice":"Yes tell me in detail what you want to know",
    "i need your help":"Yes tell me your problem",
    "help":"Yes tell me your problem",
    "tell me something":"Hi my name is Jarvis made by Amey",
    "what can you do":"I can help you",
    "do you have a joke":"No",
    "do you like people":"Yes,I like to chat with them",
    "are you a part of Matrix":"No",
    "are you a human":"No,I am just a bot",
    "are you a robot":"Yes",
    "what day is toady":"Monday",
    "do you save what I say":"No",
    "who made you":"Amey",
    "which language can you speak":"English",
}

while  True:
    qs = input()
    
    if(qs == "exit"):
        break
        
    else:
        print(qna[qs])