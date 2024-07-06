quiz = {
    "question 1":{
        "question":"What is the capital of India?",
        "option1":"Delhi",
        "option2":"Mumbai",
        "option3":"Kolkata",
        "option4":"Chennai",
        "answer":"Delhi"
    },
    "question 2":{
        "question":"What is the capital of USA?",
        "option1":"New York",
        "option2":"Washington D.C",
        "option3":"Los Angeles",
        "option4":"Chicago",
        "answer":"Washington D.C"
    },
    "question 3":{
        "question":"What is the capital of Australia?",
        "option1":"Sydney",
        "option2":"Melbourne",
        "option3":"Canberra",
        "option4":"Brisbane",
        "answer":"Canberra"
    },
    "question 4":{
        "question":"What is the capital of France?",
        "option1":"Paris",
        "option2":"Lyon",
        "option3":"Marseille",
        "option4":"Nice",
        "answer":"Paris"
    },
    "question 5":{
        "question":"What is the capital of Germany?",
        "option1":"Berlin",
        "option2":"Hamburg",
        "option3":"Munich",
        "option4":"Frankfurt",
        "answer":"Berlin"
    },
    "question 6":{
        "question":"What is the capital of Japan?",
        "option1":"Tokyo",
        "option2":"Osaka",
        "option3":"Nagoya",
        "option4":"Kyoto",
        "answer":"Tokyo"
    },
}

score = 0 
for key, value in quiz.items():
    print(key, value['question'])
    for i in value['option1'], value['option2'], value['option3'], value['option4']:
        print(i)
    ans= input ("Answer ?: ")
    if ans.lower() == value['answer'].lower():
        print("Correct")
        score +=1
    else:
        print("Incorrect")
        print("the correct answer is ", value["answer"])
    
    print("Your score is ", score, "\n")

print("\n Your score is ", score)
print("You got ", score, "out of 6 questions correctly")
print("Your percentage is ", (score/6)*100, "%")
