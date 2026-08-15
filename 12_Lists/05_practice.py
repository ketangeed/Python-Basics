tools = ["linear regression","decision tree", "neural network" ]

tools.append("kmeans")
print(tools)
print(tools[2])



hyperparameter = (0.01, 64, "adam")
print(hyperparameter[1])


predictions = ["apple", "banana", "apple", "cherry", "banana"]

unique_prediction = set(predictions)
print(unique_prediction)
unique_prediction.add("date")
print(unique_prediction)



user_profile = { "username" : "Ketan", "role" : "AI learner", " completed_course" : 14}

user_profile["completed_course"] = 15
print(user_profile)
user_profile ["status"] = "active"
print(user_profile)


raw_words = ["python", "AI", "python", "ml", "ai", "Neural", "ml"]

clean_words = []

for i in raw_words:
    clean_words.append(i.lower())
print(len(clean_words))

unique_vocab = set(clean_words)
print(len(unique_vocab))

dataset_summary = {f"total processes word" : len(clean_words), "total word count" : len(unique_vocab)}

print(dataset_summary)
 
   
