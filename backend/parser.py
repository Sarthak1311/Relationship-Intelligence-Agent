
from metrics import messages_per_user,average_mesage_length,total_message
def parse_chat(file_path):
    messages =[]

    with open(file_path,'r',encoding='utf-8') as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()

        #skip empty lines
        if not line:
            continue

        #split only on first colon
        if ':' in line:
            speaker ,message = line.split(':')

            messages.append(
                {
                    "speaker":speaker,
                    "message":message
                }
            )
    
    return messages


def get_users(meassages):
    users = set()

    for message in messages:
        users.add(message['speaker'])

    return list(users)


messages =parse_chat("/Users/sarthaktyagi/Desktop/30days-3oprojects/RelationshipIA/high_interest_1.txt")
print(messages[:2])

print( "message per user ")
msu=messages_per_user(messages)
for user,msg in msu.items():
    print(f"{user}:{msg}")

print( "total message ")
tot=total_message(messages)
print(tot)

print( "average message length ")
avu=average_mesage_length(messages)
for user,msg in avu.items():
    print(f"{user}:{msg}")

