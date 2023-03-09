
import decode_text
import encode_text
import sign_text
import authenticate_text
import discord
import process
from discord.ext import commands
import fDiscord;

import os
#os.system('python -m http.server')
#encodedMessage = encode_text.main(False);
#decodedMessage = decode_text.main(False, True);
#print(decodedMessage);

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
#client = discord.Client(intents=intents);
bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print("{0.user} is now online!".format(bot))

@bot.command()
async def encode(ctx, arg):

    encodedMessage = encode_text.main(True, arg);

    filename = "c.txt"
    encoded_file = discord.File("./ciphertext/c.txt", filename=filename)

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
async def echo(ctx, arg):
    print("on command echo")
    await ctx.send(arg)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if isinstance(message.channel, discord.DMChannel):
        response = process.main(message.content);


        return_message = response;
        await message.author.send(return_message);

        # encode result to RSA later:
        #encodedMessage = encode_text.main(True, response);
        #filename = "c.txt"
        #encoded_file = discord.File("./ciphertext/c.txt", filename=filename)
        #await message.author.send(file=encoded_file);
    else:
        await bot.process_commands(message)


token_enc = [];
path = "./token.txt"
with open(path) as f:
    token_enc = f.read()
token = decode_text.main(True, token_enc, True, False);
process.init();
bot.run(token);