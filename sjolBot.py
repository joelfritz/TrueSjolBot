#Sjol Bot created by Zyronn

#Importing everything that I will need for the bot.
import random
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
#import chalk
import csv
import time
from discord import opus

#Setting the prefix for the bot.
bot = commands.Bot(command_prefix='!')
client = discord.Client()



#A list of the quotes.
quoteList = [
    "You're an insane person.",
    "What an insane person.",
    "ONLY AN INSANE PERSON WOULD ORGANIZE THEIR WORK LIKE THAT.",
    "Are you a snoozer? like those guys who snooze their alarm? if you do, you automatically start your day with a failure.",
    "Do you make your bed before you leave for school?",
    "Pens are for people who never make mistakes.",
    "Go outside and try again.",
    ":it: IT. I dont know what IT is, can you be more specific about what IT is? :it:",
    "Name that band?",
    "I'm so disappointed.",
    "Congratulations on still using that word  (solve) incorrectly.",
    "don't WORK HORIZONTALLY.",
    "If you can't ask questions correctly, I won't help you.",
    "What do YOU think I want.",
    "Show me what you DO know.",
    "wHat is yOuR pLaN?",
    "It's not that you failed, it's that you gave up. Now try and fail.",
    "Did you remember to extend your fraction bar all the way across? I bet not.",
    "You THINK you understand it. But you don't",
    "You can do it. ... and never mind.",
    "What are all of you doing? Get to work.",
    "I'm laughing because it's funny.",
    "You guys are boring.",
    "Keep going. You're wrong, but keep going.",
    "You need a better plan.",
    "Let him fail.",
    "You know what is better then the first person struggling? The 10th person struggling.",
    "Your exasperated sounds reflect what I am thinking.",
    "What language should I speak so you understand?",
    "Did you finish the warm up?",
    "Was that the question?",
    "You can never have too much Dev.",
    "The time is crab o'clock!",
    "There is nobody like Dev.",
    "Concave is an adjective not a verb.",
    "Saying oh well is for people who do not learn from their mistakes.",
    "In the words of the great Dev Bhatt 'Fair enough'.",
    "I know you feel ridiculous. You look ridiculous.",
    "I can do whatever I want, and they can't fire me. I could punch ANY of you, and they still wouldn't fire me. They'd inspect it for 6 years. 'It's a conspiracy,' they'll say.",
    "That's wrong! That's like going outside and seeing the sky is green.",
    "Therapy dogs are for people who are too weak to go outside alone, so they make up an illness and take their dogs into restaurants and get HAIR in my food.",
    "I didn't take trail mix this time. I took 4 1/2 pounds of bacon.",
    "It was like beef jerky but bacon.",
    "People who think raisins are bad raise your hand. People who are correct keep your hands raised.",
    "I know you THINK that's loud. Its not.",
    "Uh oh. What did I say?",
    "Raisins are literally grapes that are left to rot on vines.",
    "If you like ketchup, then you're a child.",
    "I only had this discussion with you because I thought you guys were done.",
    "I don't grade the homework. I hike instead.",
    "I'm a teacher, trying to buy a house. I don't have money for Kleenex.",
	"'Sjol Wars: A New Slope' - Dev Bhatt",
	"The book doesn't use it right so you can't use it.",
	"Don't make that face. That's a stupid face.",
	"Your not insane but you are completely wrong.",
    "No Dev that not correct...",
    "Does anyone want to try answering this? ...Except for the guy wearing the green shirt?",
	"Hey, your shoes are untied. Do you want me to tie them for you? I would do it.",
	"Put your shoes back on, you dirty hippie.",
	"Yawning is only contagious if you like the person. That is why I never yawn when you guys do.",
	"I would yawn for you Dev",
	"Dev you made my year",
	"No matter who I'm teaching, if you can teach them like children, you are able to get the best results",
	"Being compared to college professors makes me feel like I'm doing a good job or they are pretending that I'm doing a good job"

]

#A list of the facts.
factList = [
    "You can only use MVT when a function is differentiable and continuous (only on the given interval)",
    "dy/dx = f'(x).",
    "The first thing to do with a limit is substitution. If the function becomes 0/0 it is indeterminate form.",
    "When f'>0 , f is increasing. When f'<0, f is decreasing.",
    "Derivative of lnx is 1/x times dx.",
    "When f''>0, f is concave up. When f''<0, f is concave down.",
    "Tangent lines and normal lines intersect at a point of tangency and are perpendicular.",
    "Two lines of the same slopes are parallel, two lines with one slope being the opposite reciprocal is perpendicular.",
    "Continuity is everything.",
    "Lim as x approaches 0 of sinx/x is 1.",
    "Dy/dx is really the change in y over the change in x.",
    "Acceleration is the derivative of velocity which is the derivative of position.",
    "Area under velocity graph is position, area under acceleration graph is velocity.",
    "When the sign of f' changes from positive to negative, f has a local maximum at that point.",
    "When the sign of f' changes from negative to positive, f has a local minimum at that point."
]

#A list of pick up lines
pickuplinelist = [
    "My limit only approaches you.",
    "You're the justification to my answer.",
    "You're my asymptote I'll always approach you, and, if you want, we can cross",
    "You're the limit as X approaches sinx/x for me.",
    "Hey, what's your sine? It must be (pi/2) because you're the 1.",
	"If I'm sin(x)^2, and your cos(x)^2, we would equal one if we added ourselves together, you're the one for me."
]

#A list where the suggestions will go.
quoteSuggestions = [


                    ]

#A list where the suggestions will go.
factSuggestions = []


#This will print to the console that the bot is working.
@bot.event
async def on_ready():
    print ("Sjol bot is up and running.")
    print ("I am " + bot.user.name)
    bot.remove_command('help')

@bot.command(pass_context=True)
async def commands(ctx):
    embed = discord.Embed(title="Sjol Bot", description="The Ultimate Teacher Bot. List of commands are:", color=0xeee657)
    embed.add_field(name="!commands", value="Gives additional information about the commands. Seems like you already found this command.", inline=False)
    embed.add_field(name="!quote", value="This command will send out a random quote from the man the myth the legendary Sjol himself.", inline=False)
    embed.add_field(name="!homework", value="This command will tell the user what the homework is. Will be updated daily (daily not included).", inline=False)
    embed.add_field(name="!addquote 'quote'", value="This command will take user input as a quote to be added later.", inline=False)
    embed.add_field(name="!throwdice @user", value="This command will takes a user as input and throw a dice at them so they stop writing.", inline=False)
    embed.add_field(name="!louder @user", value="This commands takes a user as input and tells that users that they need to be loud.", inline=False)
    embed.add_field(name="!fact", value="This command takes a random fact from factList and sends it to the chat.", inline=False)
    embed.add_field(name="!rubix", value="This command will send a random size rubix cube as Sjols favorite.",inline=False)
    embed.add_field(name="!calcpickupline", value="This command will send a calculus based pick up line in chat.", inline=False)
    embed.add_field(name="!yesorno", value="This command will either say yes or no. Very useful for settleing debates.", inline=False)
    await bot.say(embed=embed)

#This command will send out a random quote from the man the myth the legendary Sjol himself.
@bot.command(pass_context=True)
async def quote(ctx):
    await bot.say(quoteList[random.randrange(len(quoteList))])

#This command will tell the user what the homework is. Will be updated daily.
@bot.command(pass_context=True)
async def homework(ctx):
    await bot.say("Advice for next year")

#This command will take user input as a quote to be added later.
@bot.command(pass_context=True)
async def addquote(ctx, newQuote):
    quoteSuggestions.append(newQuote)
    await bot.say("Quote has been suggested and will be reviewed at some point.")

#This command will send out the list of quotes that are already in the list.
@bot.command(pass_context=True)
async def listofquotes(ctx):
    await bot.say("Sjol bot is Sjol approved")

#This will send the list of quotes that have been suggested.
@bot.command(pass_context=True)
async def suggestedquotes(ctx):
    await bot.say(quoteSuggestions)

#This command will takes a user as input and throw a dice at them so they stop writing.
@bot.command(pass_context=True)
async def throwdice(ctx, user: discord.Member):
    await bot.say(":game_die: {}! Stop writing when someone else is talking.".format(user.name))

#This commands takes a user as input and tells that users that they need to be loud.
@bot.command(pass_context=True)
async def louder(ctx, user: discord.Member):
    await bot.say(":ear: {} you need to speak loud. Not louder. :ear:".format(user.name))

#This command takes a random fact from factList and sends it to the chat.
@bot.command(pass_context=True)
async def fact(ctx):
    await bot.say(factList[random.randrange(len(factList))])

#This command takes in user input as a fact to be added later
@bot.command(pass_context=True)
async def addfact(ctx, newFact):
    factSuggestions.append(newFact)
    await bot.say("Fact has been suggested and will be reviewed at some point.")

#This command sends the list of facts that are already added.
@bot.command(pass_context=True)
async def listoffacts(ctx):
    await bot.say(factList)

#This sill send the list of quotes that have been suggested.
@bot.command(pass_context=True)
async def suggestedfacts(ctx):
    await bot.say(factSuggestions)

#This command will send a random size rubix cube as SJols favorite,
@bot.command(pass_context=True)
async def rubix(ctx):
    x = str(random.randrange(100))
    y = str(random.randrange(100))
    z = str(random.randrange(100))
    await bot.say("My favorite rubix cube is the "+x+ " by "+y+" by "+z+".")

#This command will provide calculus pick up lines.
@bot.command(pass_context=True)
async def calcpickupline(ctx):
    await bot.say(pickuplinelist[random.randrange(len(pickuplinelist))])

@bot.command(pass_context=True)
async def yesorno(ctx, question):
    x = random.randrange(2)
    if x == 1:
        await bot.say("Yes")
    else:
        await bot.say("No")

@bot.command(pass_context=True)
async def play(ctx, game):
	await bot.change_presence(game=discord.Game(name=game))

@bot.command(pass_context=True)
async def update(ctx):
    await bot.change_presence(game=discord.Game(name="Being updated",url="https://twitch.tv/officialzyronn",type=1))

@bot.event
async def on_message_delete(message):
    print("'"+ message.content +"' was deleted")

@bot.command(pass_context=True)
async def test(ctx, user: discord.Member):
    await bot.say(user.server.default_channel.name)

#@bot.event
#async def on_member_join(member):
#    await bot.send_message(discord.Object(id='456752882243600416'),"Welcome to the "+ member.server.name + " " + member.mention + ". Feel free to request your AP classes with you teacher specified as your role in <#456783703675502594>")


#@bot.event
#async def on_message(msg):
#    if ' it ' in msg.content:
#        print(msg.content)
#        await bot.send_message(discord.Object(id=msg.channel.id), msg.author.nick +' Just said it!')
#        bot.process_commands(msg)

@bot.event
async def on_message_edit(before, after):
    print(before.content + " --> "+ after.content)



    
















































































bot.run("MzczMjkwMjA2NzU5MDkyMjM0.DgRYhw.cTtzYMOce0Xn_IZVYqy2JRAZhmg")