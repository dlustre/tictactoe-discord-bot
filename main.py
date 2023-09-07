import discord
import os
import tictactoe
import random

client = discord.Client(intents=discord.Intents.default())


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  username = str(message.author).split('#')[0]
  user_message = str(message.content)
  channel = str(message.channel.name)
  print(f'{username}: {user_message} ({channel})')

  if message.author == client.user:
    return

  if message.channel.name == 'general':
    if user_message.lower() == 'hello':
      await message.channel.send(f'What\'s up {username}')
      return
    elif user_message.lower() == 'bye':
      await message.channel.send(f'Lol bye {username}')
      return
    elif user_message.lower() == '!tictactoe':
      if tictactoe.isEmpty():
        output = 'You vs. me buddy'
        coin = random.randint(0, 1)
        if coin == 0:
          output += '\n You start this time'
          output += '\n\n' + tictactoe.getBoard()
        elif coin == 1:
          output += '\n I\'ll start this time'
          tictactoe.placeRandomMove()
          output += '\n\n' + tictactoe.getBoard()
        await message.channel.send(output)
      else:
        await message.channel.send("A game is in progress dude...")
      return
    elif user_message.lower().startswith('!move') and len(
        user_message.split(' ')) == 3 and user_message.split(' ')[1] in [
          "0", "1", "2"
        ] and user_message.split(' ')[2] in ["0", "1", "2"]:
      output = ""
      if tictactoe.canPlace(int(user_message.split(' ')[1]),
                            int(user_message.split(' ')[2])):
        tictactoe.placeMove('X', int(user_message.split(' ')[1]),
                            int(user_message.split(' ')[2]))
        output += '\n\n' + tictactoe.getBoard()
        if tictactoe.checkWin() == tictactoe.player1:
          output += "\n\nYou won I guess."
          tictactoe.clearBoard(board)
        else:
          output += "\n\nNice move..."
          output += "\n\nMy turn now"
          tictactoe.placeRandomMove()
          output += '\n\n' + tictactoe.getBoard()
          if tictactoe.checkWin() == tictactoe.player2:
            output += "\n\nOh wow you actually lost lol"
            tictactoe.clearBoard(board)
      else:
        output += "Can\'t place it there dude"
        output += '\n\n' + tictactoe.getBoard()

      await message.channel.send(output)
      return


try:
  client.run(os.getenv('TOKEN'))
except discord.errors.HTTPException as e:
  print("\n\n\nBLOCKED BY RATE LIMITS\n\n\n")
