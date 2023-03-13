
import decode_text
import encode_text
import sign_text
import authenticate_text
import discord
import process
from discord.ext import commands
import fDiscord



intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)


# dev stuff
class Private:
    @staticmethod
    def getActor():
        result = process.actorToString()
        return result;

    @staticmethod
    def resetActor():
        process.resetActor();
        return "reset successful"

    @staticmethod
    def initActor():
        process.initActor();
        return "init successful"

    @staticmethod
    def langEng():
        process.set_locale("eng");
        process.actor_locale("eng"); # change to reload later
        return "language set as " + "eng"

    @staticmethod
    def langRu():
        process.set_locale("ru");
        process.actor_locale("ru"); # change to reload later
        return "language set as " + "ru"

    @staticmethod
    def printGame():
        result = process.gameToString();
        return result

# dev prefix = % - remove later!!
commands = {"nuhrat": Private.getActor,
            "нухрат": Private.getActor,
            "%reset": Private.resetActor,
            "%init": Private.initActor,
            "eng": Private.langEng,
            "ru": Private.langRu,
            "%print": Private.printGame,
            };


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if isinstance(message.channel, discord.DMChannel):

        #try to detect custom command first (including dev)
        if (message.content.lower() in commands):
            return_message = commands[message.content.lower()]();
            await message.author.send(return_message);
            return;

        return_message = process.main(message.content);
        await message.author.send(return_message);

        # encode result to RSA later:
        #encodedMessage = encode_text.main(True, response);
        #filename = "c.txt"
        #encoded_file = discord.File("./ciphertext/c.txt", filename=filename)
        #await message.author.send(file=encoded_file);
    else:
        await bot.process_commands(message)

@bot.event
async def on_ready():
    print("{0.user} is now online!".format(bot))

@bot.command()
async def encode(ctx, arg):

    encodedMessage = encode_text.main(True, arg);

    filename = "c.txt"
    encoded_file = discord.File("./ciphertext/" + filename, filename=filename)

    return_message = "encoded " + fDiscord.spoiler(arg) + " as: "
    await ctx.send(return_message);
    await ctx.send(file=encoded_file);


@bot.command()
async def decode(ctx):
    try:
        attachment = ctx.message.attachments[0];
        content = str(await discord.Attachment.read(attachment, use_cached=False));
        content = content.replace("b'", "");
        content = content.replace("'", "");
        content = content.replace("\\r\\n", "\n");
        decodedMessage = decode_text.main(True, content, True, True);

        return_message = "decoded as:"
        await ctx.send(return_message);
        await ctx.send(decodedMessage);
    except Exception as err:
        exc_err = "command use: $decode + a txt attachment file to decode"
        print(exc_err);
        await ctx.send(exc_err);

@bot.command()
async def sign(ctx, arg):

    signedMessage = sign_text.main(True, arg, True);

    filename = "sig.txt"
    signed_file = discord.File("./signaturetext/" + filename, filename=filename)

    return_message = "signed " + fDiscord.spoiler(arg) + " as: "
    await ctx.send(return_message);
    await ctx.send(file=signed_file);

@bot.command()
async def authenticate(ctx):
    try:
        attachment = ctx.message.attachments[0];
        content = str(await discord.Attachment.read(attachment, use_cached=False));
        content = content.replace("b'", "");
        content = content.replace("'", "");
        content = content.replace("\\r\\n", "\n");
        authenticatedMessage = authenticate_text.main(True, content, True);

        return_message = "authenticated as:"
        await ctx.send(return_message);
        await ctx.send(authenticatedMessage);
    except Exception as err:
        exc_err = "command use: $authenticate + a txt attachment file to authenticate"
        print(exc_err);
        await ctx.send(exc_err);

token_enc = [];
path = "./token.txt"
with open(path) as f:
    token_enc = f.read()
token = decode_text.main(True, token_enc, True, False);
process.init();
bot.run(token);