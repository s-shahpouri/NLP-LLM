
from MySimpleChat import MySimpleChat

my_chat = MySimpleChat(chat_model="llama2")

query = input("User : ")

while query != 'q' and query is not None:
    response = my_chat.chat(query)
    print(f"Assistant : {response}")
    query = input("User : ")
