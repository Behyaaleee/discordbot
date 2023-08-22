import random


def get_response(message: str) -> str:
    p_message = message.lower()



##ANSWER BACK FUNCTIONS 
    if p_message == 'hello':
        return 'Hey there!'
    
    if p_message == 'hi':
        return 'Hey!'
    
    if p_message == 'hewwo':
        return 'hewwo UwU'
    

##GAME FUNCTIONS
    if p_message == 'roll':
        return str(random.randint(1, 6))
    
    if p_message == 'toss' or p_message == 'flip':
        toss = random.choice(["Heads", "Tails"])
        return toss

    if p_message == 'help' :
        return '`This is a help message that you can modify.`'
    
    if p_message[:5] == '8ball':
        ball = random.choice(["● It is certain.",
                              "● It is decidedly so.",
                              "● Without a doubt.",
                              "● Yes definitely.",
                              "● You may rely on it.",
                              "● As I see it, yes.",
                              "● Most likely.",
                              "● Outlook good.",
                              "● Yes.",
                              "● Signs point to yes.",
                              "● Reply hazy, try again.",
                              "● Ask again later.",
                              "● Better not tell you now.",
                              "● Cannot predict now.",
                              "● Concentrate and ask again.",
                              "● Don't count on it.",
                              "● My reply is no.",
                              "● My sources say no.",
                              "● Outlook not so good.",
                              "● Very doubtful."])
        return ball  

    if p_message == 'cry':
        return ':sob:'
    
    if p_message == 'smile':
        return ':slight_smile:'
    
    if p_message.startswith('how are you'):
        mood = random.choice([":sob:",
                              ":slight_smile:",
                              ":weary:",
                              ":face_with_symbols_over_mouth:",
                              ":face_with_diagonal_mouth:",
                              ":smiling_imp:",
                              ":drool:",
                              ":sick:",
                              ":neutral_face:",
                              ":head_bandage:",
                              ":thermometer_face:"])
        return mood


##INTERACTIVE ??

    if p_message[:8] == 'cuss out':
        return '**** you'+ p_message[8:]+ '!'

    if p_message.startswith('repeat after me'):
        return p_message[len('repeat after me'):].strip()
    











