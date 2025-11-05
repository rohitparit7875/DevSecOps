sentence = input("Enter a sentence: ").lower()
vowels = "aeiou"
count = sum(1 for char in sentence if char in vowels)
print("Number of vowels:", count)
