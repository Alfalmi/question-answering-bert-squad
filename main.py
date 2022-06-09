import datasets
raw_datasets = datasets.load_dataset("squad")

print(raw_datasets)
print("Context: ", raw_datasets["train"][0]["context"])
print("Question: ", raw_datasets["train"][0]["question"])
print("Answer: ", raw_datasets["train"][0]["answers"])