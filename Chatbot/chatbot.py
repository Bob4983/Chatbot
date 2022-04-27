import discord
import pandas as pd 
import numpy as np
from sklearn.tree import DecisionTreeClassifier as DTC
from sklearn.preprocessing import OneHotEncoder

#model = joblib.load('chatbotmodel.joblib')

client = discord.Client()
Token = "ODMzMzI2MjcyOTc2OTEyMzk0.YHwtkQ.hylpm7Uvxk8MjrwX884CNoeE-wE"
@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event 
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f"{username} : {user_message} ({channel})")
    
    if message.author == client.user :
        return
    if user_message.lower() == "hello" or user_message.lower() == "hlo" :
        await message.channel.send(f"blo {username}!")
        return
    elif user_message.lower() == "bye" :
        await message.channel.send(f"See you later {username}!")
        return

    if user_message.lower() == "die" :
        await message.channel.send(f"already broken!")
        await client.close()
        print("Bot Closed")

    if user_message.lower() == "ازيك" :
        await message.channel.send(f"الحمدلله انت عامل ايه")

    
    df = pd.read_csv('bot_dataset.csv')
    X = df.drop(columns=['Answer'])
    y = df.drop(columns=['Question'])
    y = y.drop(columns=["Unnamed: 0"])
    X = X.drop(columns =["Unnamed: 0"])
    Q_index = pd.DataFrame(data=np.array(range(len(X))),columns =["index"])
    model = DTC()
    Q_index.astype(float)
    model.fit(Q_index,y)
    
    for i in range(len(X)) :
       if user_message.lower() in X["Question"][i].lower():
            global pre 
            pre = model.predict(Q_index["index"][i].reshape(-1, 1))
            #pre =  y["Answer"][i]

    await message.channel.send(pre)

    
    

client.run(Token)