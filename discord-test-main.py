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
import debug


intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents);
mapGameActive = True; #for testing
img_file_name = "image.jpg"
img_path = "./data/" + img_file_name;
html_map_name = "magicmap.html";
html_map_path = "./data/" + html_map_name;

localhost = "http://kamilashi.pythonanywhere.com/magicmap/mapplot.html"

adminId = "349070619566014464";
#targetUserFallbackID = None;#"895246650187087924";
targetUserSaveFileName = "targetSnowflakeID.txt";
targetUserSavePath = "./data/" + targetUserSaveFileName;

# dev stuff
class Private:
    @staticmethod
    def getActor():
        result = process.actorToString()
        return result;
    @staticmethod
    def respondMax():
        result = "Да, но не совсем.\n\Имя персонажа :wink: "
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
    def debugBookCipher():
        result = debug.analyzeRiddleText();
        return result

    @staticmethod
    def deleteImage():
        os.remove(img_path);
        return "image deleted"

    @staticmethod
    def deleteHTML():
        os.remove(html_map_path);
        return "html deleted"

    @staticmethod
    async def drawAllPoints(args, sender):
        map.drawAllPoints(img_path);
        image_file = discord.File(img_path, filename=img_file_name);
        result = "debug full map image";
        #if(targetUser == None):
        with open(targetUserSavePath) as f:
            targetUserFallbackID = f.read();
            targetUser = await bot.fetch_user(str(targetUserFallbackID));
        await targetUser.send(file=image_file);
        return result

    @staticmethod
    async def sendHTMLmap(args, sender):
        if not(os.path.exists(html_map_path)):
            await map.plotEmpty();

        html_file = discord.File(html_map_path, filename = html_map_name);
        await sender.send(file=html_file);
        return_message = "Открой меня!"
        #return_message = "Карте нужны координаты :wink: "
        result = return_message;
        sent_message = "keyword " + args;
        await Private.logReport(sent_message, result, sender)
        return result

    @staticmethod
    async def plotPointDebug(args, sender):
        argsArray = args.split(" ");
        lat_deg = float(argsArray[0]);
        long_deg = float(argsArray[1]);
        radius_cm = float(argsArray[2]);
        await map.plotPointDebug(lat_deg, long_deg, radius_cm);
        [return_message, hit] = map.main(lat_deg, long_deg, radius_cm);
        #await sender.send(localhost);
        result = "Debug full map\n\n";
        result += fDiscord.bold("Return Message:") + "\n" + str(return_message) + "\n";
        result += fDiscord.bold("Hit:") + "\n" + str(hit);
        return result

    @staticmethod
    async def getPageNumber(args, sender):
        argsArray = args.split(" ");
        x = float(argsArray[0]);
        x_perc = (x-6)/119.0;
        y = x_perc*105;
        y = y + 5;
        result = str(y) + " +- 1 "
        return result

    @staticmethod
    async def mapMiniGame(args, sender):
        if mapGameActive:
            argsArray = args.split(" ");
            lat_deg = float(argsArray[0]);
            long_deg = float(argsArray[1]);
            radius_cm = float(argsArray[2]);
            #await sender.send(localhost);
            await map.plotPoint(lat_deg, long_deg, radius_cm);
            [return_message, hit] = map.main(lat_deg, long_deg, radius_cm);
            if hit: #To-Do: add check for already located points
                await sender.send("В небе зажглась звезда!");
                map.drawDot(lat_deg, long_deg, img_path);
                image_file = discord.File(img_path, filename = img_file_name);
                await sender.send(file=image_file);
            result = return_message;
        else:
            result = "Карта деактивирована Ж(";
        sent_message = "magicmap " + args;

        await Private.logReport(sent_message, result, sender)
        return result

    @staticmethod
    async def sendToAdmin(args, sender):
        targetUser = sender;
        targetUserFallbackID = targetUser.id;
        with open(targetUserSavePath, 'w+') as f:
            print("registered new target user: " + str(targetUserFallbackID));
            f.write(str(targetUserFallbackID));
        f.close();
        log_report_message = fDiscord.bold(
            "Relayed from " + str(sender) + ", id: " + str(sender.id)) + ":\n" + args;
        admin = await bot.fetch_user(str(adminId));
        await admin.send(log_report_message);
        result = "Я получил твое послание, мне надо его обдумать... :thinking:";
        return result

    @staticmethod
    async def sendToTargetUser(args, sender):
        with open(targetUserSavePath) as f:
            targetUserFallbackID = f.read();
            targetUser = await bot.fetch_user(str(targetUserFallbackID));
        f.close();
        await targetUser.send(args);
        result = "reply sent successfully!";
        return result

    @staticmethod
    async def logReport(sent_message, return_message, sender):
        # if the sender user wasn't admin, relay log message to admin:
        admin = await bot.fetch_user(adminId);
        if (sender != admin):
            log_report_message = fDiscord.bold("Log from " + str(sender) + ", id: "+ str(sender.id)) + ":\n" + sent_message;
            log_report_message += fDiscord.bold("\nResponce ") + ":\n" + return_message;
            await admin.send(log_report_message);


# dev prefix = %
# keep the command names LOWERCASE!
commands = {"nuhrat": Private.getActor,
            "нухрат": Private.getActor,
            "макс": Private.respondMax,
            "max": Private.respondMax,
            "%reset": Private.resetActor,
            "%init": Private.initActor,
            "%debugbookcipher": Private.debugBookCipher,
            #"%eng": Private.langEng,
            "%ru": Private.langRu,
            #"%printgame": Private.printGame,
            "%printactordebug": Private.printActorDebug,
            "%resetimage": Private.deleteImage,
            "%resethtml": Private.deleteHTML
            };
commandsWithArgs = {
            #"%drawallpoints": Private.drawAllPoints,  #DO NOT USE! REWRITES THE SAVED IMAGE
            "relay":Private.sendToAdmin,
            "%reply":Private.sendToTargetUser,
            "%plotpointdebug":Private.plotPointDebug,
            "magicmagicmap":Private.sendHTMLmap,
            "magicmap":Private.mapMiniGame,
            "%getpageno":Private.getPageNumber
            };

@bot.event
async def on_message(message):

    if message.author == bot.user:
        return
    # if messaged bot's dm
    if isinstance(message.channel, discord.DMChannel):
        message_args = message.content.split();
        keyword = message_args[0].lower();

        # try to detect custom command first (including dev)
        if (keyword in commands):
            return_message = commands[keyword]();
            await message.author.send(return_message);
            await Private.logReport(message.content, return_message, message.author);
            return;
        # then check all commands that require special arguments
        if (keyword in commandsWithArgs):
            args = ' '.join(message_args[1:]); # join all arguments except for the first keyword
            return_message = await commandsWithArgs[keyword](args, message.author);
            await message.author.send(return_message);
            return;

        # otherwise try to process the passwords
        [return_message, key_piece] = process.main(message.content);
        await message.author.send(return_message);

        # encode result to RSA later:
        if(key_piece != None):
            encode_text.main(True, key_piece);
            filename = "c.txt"
            encoded_file = discord.File("./ciphertext/" + filename, filename=filename)
            await message.author.send(file=encoded_file);
            os.remove("./ciphertext/" + filename);

        await Private.logReport(message.content, return_message, message.author);

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
f.close();
token = decode_text.main(True, token_enc, True, False);
process.init();
bot.run(token);