def total_message(messages):
    return len(messages)

# messages per user 
def messages_per_user(messages):
    count ={}

    for msg in messages:
        user = msg['speaker']

        if user not in count:
            count[user]=0
        
        count[user]+=1

    return count

#Average message length
def average_mesage_length(messages):
    msg_per_user = messages_per_user(messages)
    msg_len = {}
    for speaker,msg in messages:
        sent= list(msg.split(" "))
        sent_len = len(sent)

        if speaker not in msg_len:
            msg_len[speaker]=sent_len

        msg_len[speaker]+=sent_len

    average_msg_len = {}
    for user,length in msg_len.items():
        average = length/messages_per_user[user]
        average_msg_len[user]= average

    return average_msg_len



    
