import os

import decode_text
import encode_text
import sign_text
import authenticate_text
import discord
import process
import map
from discord.ext import commands
import fDiscord



intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents);
mapGameActive = True; #for testing
img_file_name = "image.jpg"
img_path = "./data/" + img_file_name;

adminId = "349070619566014464";

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

    @staticmethod
    def printActorDebug():
        result = process.actorToStringDebug();
        return result

    @staticmethod
    def deleteImage():
        os.remove(img_path);
        return "image deleted"

    @staticmethod
    async def drawAllPoints(args, sender):
        global targetUser;

        map.drawAllPoints(img_path);
        image_file = discord.File(img_path, filename=img_file_name);
        result = "debug full map";
        await targetUser.send(file=image_file);
        return result

    @staticmethod
    async def sendToAdmin(args, sender):
        global targetUser;
        global admin;

        targetUser = sender;
        admin = await bot.fetch_user(adminId);
        await admin.send(args);
        result = "message relayed successfully!";
        return result

    @staticmethod
    async def sendToTargetUser(args, sender):
        global targetUser;
        global admin;

        await targetUser.send(args);
        result = "reply sent successfully!";
        return result

# dev prefix = % - remove later!!
commands = {"nuhrat": Private.getActor,
            "нухрат": Private.getActor,
            "%reset": Private.resetActor,
            "%init": Private.initActor,
            "%eng": Private.langEng,
            "%ru": Private.langRu,
            #"%printgame": Private.printGame,
            "%printactordebug": Private.printActorDebug,
            "%resetimage": Private.deleteImage
            };
commandsWithArgs = {
            #"%drawallpoints": Private.drawAllPoints,  #DO NOT USE! REWRITES THE SAVED IMAGE
            "relay":Private.sendToAdmin,
            "%reply":Private.sendToTargetUser
            };

@bot.event
async def on_message(message):

    if message.author == bot.user:
        return
    # if messaged bot's dm
    if isinstance(message.channel, discord.DMChannel):
        message_args = message.content.split();
        keyword = message_args[0].lower();
        #admin = await bot.get_user_info(user_id="Kamila#8332");
        # try to detect custom command first (including dev)
        if (keyword in commands):
            return_message = commands[keyword]();
            await message.author.send(return_message);
            return;
        # then check all commands that require special arguments
        if (keyword in commandsWithArgs):
            args = ' '.join(message_args[1:]); # join all arguments except for the first keyword
            return_message = await commandsWithArgs[keyword](args, message.author);
            await message.author.send(return_message);
            return;
        # map minigame - processed independently, user is not bound to the map loop
        if (keyword == "magicmap" and mapGameActive):
            lat_deg = float(message_args[1]);
            long_deg = float(message_args[2]);
            radius_cm = float(message_args[3]);
            [return_message, hit] = map.main(lat_deg, long_deg, radius_cm);
            if hit: #To-Do: add check for already located points
                await message.author.send("В небе зажглась звезда!");
                map.drawDot(lat_deg, long_deg, img_path);
                #map.drawAllPoints(img_path)
                image_file = discord.File(img_path, filename = img_file_name);
                await message.author.send(file=image_file);
            await message.author.send(return_message);
            return;
        # otherwise try to process the passwords
        [return_message, final_key_piece] = process.main(message.content);
        await message.author.send(return_message);

        # encode result to RSA later:
        if(final_key_piece != None):
            encode_text.main(True, final_key_piece);
            filename = "c.txt"
            encoded_file = discord.File("./ciphertext/" + filename, filename=filename)
            await message.author.send(file=encoded_file);
            os.remove("./ciphertext/" + filename);
    else:
        #if not in the bot's dms operate like a regular en-dec tool
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