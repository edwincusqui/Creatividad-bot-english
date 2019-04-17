from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

def initbot(conv):
    bot = ChatBot(
    'Joe',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3')
    """

    conv=open('bot/conversaciones/c1.txt','r').readlines()
    conv1=open('bot/conversaciones/c2.txt','r').readlines()
    conv2=open('bot/conversaciones/c3.txt','r').readlines()
    conv3=open('bot/conversaciones/c4.txt','r').readlines()

    trainer = ListTrainer(bot)
    trainer.train(conv)
    trainer.train(conv1)
    trainer.train(conv2)
    trainer.train(conv3)"""
    """trainer = ChatterBotCorpusTrainer(bot)"""
    """
    trainer.train(
    "chatterbot.corpus.english"
    )"""
    response = bot.get_response(str(conv))
    return response
    """print("bot: ",response)                            
    while True:
        try:
            response = bot.get_response(input("User: "))

            print("bot: ",response)

        

        except(KeyboardInterrupt, EOFError, SystemExit):
            break


"""
