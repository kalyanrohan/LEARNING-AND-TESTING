
message=input(">")
words= message.split(" ")
emojis={":)":"\U0001F601",":/":"\U0001F610","rotfl":"\U0001F923","lol":"\U0001F602"}
output= ""
for word in words:
    output += emojis.get(word,word)+ " "
print(output)


