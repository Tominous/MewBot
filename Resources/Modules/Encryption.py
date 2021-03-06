import discord, asyncio, aiohttp, base64, Resources.Lib.GDLib as GDLib, Resources.Lib.ImgLib as ImgLib, itertools, math, hashlib, binascii, subprocess
from discord.ext import commands
from textwrap import wrap

class Encryption:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, aliases=["rtee", "rteencode", "robtopterribleencryptione", "robtopterribleencryptionencode", "robencode"], description="Encode a message using Robtop's Terrible Encryption™!", brief="`mb!robe Hello, world!`")
    async def robe(self, ctx, *args):
        y = GDLib.rtee(' '.join(args))
        if(y != 0):
            emb = (discord.Embed(color=0xf7b8cf))
            emb.add_field(name="RTE Encoded Message", value=y.decode())
            await ctx.send(embed=emb)
        else:
            await ctx.send("Input not long enough! *(>=6 characters!)*")

    @commands.command(pass_context=True, aliases=["rted", "rtedecode", "robtopterribleencryptiond", "robtopterribleencryptiondecode", "robdecode"], description="Decode a message encoded with Robtop's Terrible Encryption™!", brief="`mb!robd elNfWlseFkRZRl5SEg==`")
    async def robd(self, ctx, *args):
        if(args != ()):
            try:
                y = GDLib.rted(''.join(args))
                if(y == ""):
                    await ctx.send("That is not a valid RTE Encoded string!")
                    return
                emb = (discord.Embed(color=0xf7b8cf))
                emb.add_field(name="RTE Encoded Message", value=y)
                await ctx.send(embed=emb)
            except binascii.Error:
                await ctx.send("That is not a valid RTE Encoded string!")
        else:
            await ctx.send("You need to type something to decode!")

    @commands.command(pass_context=True, description="Encode or Decode a message using atbash!", brief="`mb!atbash Hello, world!`")
    async def atbash(self, ctx, *args):
        if(args != ()):
            x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                 'v', 'w', 'x', 'y', 'z']
            z = ' '.join(args)
            s = list(z.lower())
            for i in range(len(s)):
                for j in range(len(x)):
                    if (x[j] == s[i]):
                        break
                if (s[i] in x):
                    s[i] = x[25 - j]
                if (z[i] == z[i].upper()):
                    s[i] = s[i].upper()
            emb = (discord.Embed(color=0xf7b8cf))
            emb.add_field(name="Atbash Cipher", value=''.join(s))
            await ctx.send(embed=emb)
        else:
            await ctx.send("You need to type something to atbash!")

    @commands.command(pass_context=True, aliases=["sha512encode"], description="Hash a message with SHA-512!", brief="`mb!sha512e Hello, world!`")
    async def sha512e(self, ctx, *args):
        if(args != ()):
            emb = (discord.Embed(color=0xf7b8cf))
            emb.add_field(name="SHA512 Hash", value=hashlib.sha512(' '.join(args).encode('utf-8')).hexdigest())
            await ctx.send(embed=emb)
        else:
            await ctx.send("You need to type something to encode!")

    @commands.command(pass_context=True, aliases=["sha256encode"], description="Hash a message with SHA-256!", brief="`mb!sha256e Hello, world!`")
    async def sha256e(self, ctx, *args):
        if(args != ()):
            emb = (discord.Embed(color=0xf7b8cf))
            emb.add_field(name="SHA256 Hash", value=hashlib.sha256(' '.join(args).encode('utf-8')).hexdigest())
            await ctx.send(embed=emb)
        else:
            await ctx.send("You need to type something to encode!")

    @commands.command(pass_context=True, aliases=["md5decode"], description="Decode md5 hashes! (Only works with up to 7 lowercase or 0-9 characters, and may not work with all)", brief="`mb!md5d d5aedf560b928e289dc4a76d8765bc4e`")
    async def md5d(self, ctx, md5hash):
        if(len(md5hash) == 32):
            for i in list(md5hash):
                if(i not in "1234567890abcdef"):
                    await ctx.send("That is not a valid md5 hash!")
                    return
            dehash = subprocess.check_output(['cd', "C:/MewBot/Resources/Interactive", "&", "rcrack", ".", "-h", md5hash], shell=True).decode()
            if("<not found>" in dehash):
                await ctx.send("Sorry, that hash is not in my rainbow table. Wait for me to update it!")
                return
            dehash = dehash.split()[-2]
            emb = (discord.Embed(color=0xf7b8cf))
            emb.add_field(name="MD5 Unhash", value=dehash)
            await ctx.send(embed=emb)
        else:
            await ctx.send("That is not a valid md5 hash!")

    @commands.command(pass_context=True, aliases=["md5encode"], description="Hash a message with MD5!", brief="`mb!md5e Hello, world!`")
    async def md5e(self, ctx, *args):
        if(args != ()):
            emb = (discord.Embed(color=0xf7b8cf))
            emb.add_field(name="MD5 Hash", value=hashlib.md5(' '.join(args).encode('utf-8')).hexdigest())
            await ctx.send(embed=emb)
        else:
            await ctx.send("You need to type something to encode!")

    @commands.command(pass_context=True, aliases=["hexadecimald", "hexdecode", "hexadecimaldecode"], description="Decode a message from Hexadecimal!", brief="`mb!hexd 48656C6C6F2C20776F726C6421`")
    async def hexd(self, ctx, *args):
        if(args != ()):
            try:
                s = ''.join(args)
                emb = (discord.Embed(color=0xf7b8cf))
                emb.add_field(name="Hex Decoded String", value=base64.b16decode(s.replace(' ', '').upper().encode('utf-8')).decode())
                await ctx.send(embed=emb)
            except binascii.Error:
                await ctx.send("That is not a valid Hex encoded string!")
        else:
            await ctx.send("You need to type something to decode!")

    @commands.command(pass_context=True, aliases=["hexadecimale", "hexencode", "hexadecimalencode"], description="Encode a message using Hexadecimal!", brief="`mb!hexe Hello, world!`")
    async def hexe(self, ctx, *args):
        if(args != ()):
            emb = (discord.Embed(color=0xf7b8cf))
            emb.add_field(name="Hex Encoded String", value=base64.b16encode(' '.join(args).encode('utf-8')).decode())
            await ctx.send(embed=emb)
        else:
            await ctx.send("You need to type something to encode!")

    @commands.command(pass_context=True, aliases=["morsecoded"], description="Decode a message from Morse Code!", brief="`mb!morsed .... . .-.. .-.. ---`")
    async def morsed(self, ctx, *args):
        if(args != ()):
            mcd = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                       'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                       'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                       'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
                       '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ',': '--..--', '.': '.-.-.-',
                       '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', ':': '---...', "'": '.----.',
                       '"': ".-..-.", '@': '.--.-.', '=': '-...-'}
            fin = ""
            bad = False
            for i in args:
                    if (i == "/"):
                        fin += " "
                    elif(i in mcd.values()):
                        fin += [key for key, value in mcd.items() if value == i][0]
                    else:
                        bad = True
            if(bad):
                await ctx.send("That is not a valid Morse Encoded String")
            else:
                emb = (discord.Embed(color=0xf7b8cf))
                emb.add_field(name="Morse Decoded String", value=fin)
                await ctx.message.channel.send(embed=emb)
        else:
            await ctx.send("You need to type something to decode!")

    @commands.command(pass_context=True, aliases=["morsecodee"], description="Encode a message into Morse Code!", brief="`mb!morsee Hello`")
    async def morsee(self, ctx, *args):
        if(args != ()):
            mcd = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                       'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                       'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                       'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
                       '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ',': '--..--', '.': '.-.-.-',
                       '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', ':': '---...', "'": '.----.',
                       '"': ".-..-.", '@': '.--.-.', '=': '-...-'}
            fin = ""
            for i in ' '.join(args):
                if(i.upper() not in mcd.keys()):
                    fin += i
                elif i != " ":
                    if (i == "!"):
                        i = "."
                    fin += mcd[i.upper()] + " "
                else:
                    fin += " / "
            emb = (discord.Embed(color=0xf7b8cf))
            emb.add_field(name="Morse Encoded String", value=fin)
            await ctx.send(embed=emb)
        else:
            await ctx.send("You need to type something to encode!")

    @commands.command(pass_context=True, aliases=["upper"], description="PUT A MESSAGE INTO ALL UPPERCASE", brief="`mb!uppercase hello, world!`")
    async def uppercase(self, ctx, *args):
        if(args != ()):
            emb = (discord.Embed(color=0xf7b8cf))
            emb.add_field(name="Uppercase String", value=' '.join(args).upper())
            await ctx.send(embed=emb)
        else:
            await ctx.send("You need to type something to turn into uppercase!")

    @commands.command(pass_context=True, aliases=["lower"], description="put a message into all lowercase", brief="`mb!lowercase HELLO, WORLD!`")
    async def lowercase(self, ctx, *args):
        if(args != ()):
            emb = (discord.Embed(color=0xf7b8cf))
            emb.add_field(name="Lowercase String", value=' '.join(args).lower())
            await ctx.send(embed=emb)
        else:
            await ctx.send("You need to type something to turn into lowercase!")

    @commands.command(pass_context=True, aliases=["len"], description="Get the length of a string!", brief="`mb!length Hello, world!`")
    async def length(self, ctx, *args):
        emb = (discord.Embed(color=0xf7b8cf))
        emb.add_field(name="Length of String", value=str(len(list(' '.join(args)))))
        await ctx.send(embed=emb)

    @commands.command(pass_context=True, aliases=["prime"], description="Check if a number is prime!", brief="`mb!isprime 3301`")
    async def isprime(self, ctx, *args):
        if(''.join(args).isdigit()):
            s = int(''.join(args))
            emb = (discord.Embed(color=0xf7b8cf))
            try:
                a = s > 1 and all(s % i for i in itertools.islice(itertools.count(2), int(math.sqrt(s) - 1)))
                emb.add_field(name="Is " + str(s) + " prime?", value=str(s) + " is prime." if a else str(s) + " is not prime. Its factors are: " + ', '.join([str(j) for j in range(1, math.ceil(s/2)) if s/j == math.floor(s/j) ]))
            except(ValueError):
                emb.add_field(name="Is " + str(s) + " prime?", value=str(s) + " may be prime.")
            await ctx.send(embed=emb)
        else:
            await ctx.send("That's not a whole number!")

    @commands.command(pass_context=True, aliases=["gjpdecode", "geometryjumppassworddecode", "geometryjumppasswordd"], description="Encode a message using GJP encryption!", brief="`mb!gjpe Hello, world!`")
    async def gjpd(self, ctx, *args):
        try:
            if(args != ()):
                emb = (discord.Embed(color=0xf7b8cf))
                emb.add_field(name="GJP Decoded Message", value=GDLib.gjpd(' '.join(args)))
                await ctx.send(embed=emb)
            else:
                await ctx.send("You need to type something to decode!")
        except binascii.Error:
            await ctx.send("That is not a valid GJP Encoded Message!")

    @commands.command(pass_context=True, aliases=["gjpencode", "geometryjumppasswordencode", "geometryjumppassworde"], description="Decode a message encoded with GJP encryption!", brief="`mb!gjpd e1JZXlkfF0JdRF9TFA==`")
    async def gjpe(self, ctx, *args):
        y = GDLib.gjpe(' '.join(args))
        if(y != 0):
            emb = (discord.Embed(color=0xf7b8cf))
            emb.add_field(name="GJP Encoded Message", value=y.decode())
            await ctx.send(embed=emb)
        else:
            await ctx.send("Input not long enough! *(>=6 characters!)*")

    @commands.command(pass_context=True, aliases=["a85decode", "ascii85d", "ascii85decode"], description="Decode a message from ASCII85", brief="`mb!a85d <~87cURD_*#TDfTZ)+T~>`")
    async def a85d(self, ctx, *args):
        if(args != ()):
            emb = (discord.Embed(color=0xf7b8cf))
            dm = base64.a85decode(''.join(args).encode(), adobe=True).decode() if ' '.join(args).endswith('~>') else base64.a85decode(' '.join(args).encode()).decode()
            if(dm == ""):
                await ctx.send("That's not a valid Ascii85 encoded message!")
                return
            emb.add_field(name="Ascii85 Decoded Message", value=dm)
            await ctx.send(embed=emb)
        else:
            await ctx.send("You need to type something to decode!")

    @commands.command(pass_context=True, aliases=["a85encode", "ascii85e", "ascii85encode"], description="Encode a message using ASCII85", brief="`mb!a85e Hello, world!`")
    async def a85e(self, ctx, *args):
        if(args != ()):
            emb = (discord.Embed(color=0xf7b8cf))
            emb.add_field(name="Ascii85 Encoded Message", value=base64.a85encode(' '.join(args).encode(), adobe=True).decode())
            await ctx.send(embed=emb)
        else:
            await ctx.send("You need to type something to encode!")

    @commands.command(pass_context=True, aliases=["bind", "binaryd", "bindecode", "binarydecode"], description="Decode a message from Binary", brief="`mb!binaryd 0100100001101001`")
    async def unbinary(self, ctx, *args):
        if(args != ()):
            try:
                z = wrap(' '.join(args), 8)
                f = ""
                for i in range(len(z)):
                    f = f + chr(int(z[i], 2))
                emb = (discord.Embed(color=0xf7b8cf))
                emb.add_field(name="Binary to Text", value=f)
                await ctx.send(embed=emb)
            except ValueError:
                await ctx.send("You need to send a binary string, not a normal one!")
        else:
            await ctx.send("You need to type something to decode!")

    @commands.command(pass_context=True, aliases=["bine", "binarye", "binencode", "binaryencode"], description="Encode a message using Binary", brief="`mb!binarye Hello`")
    async def binary(self, ctx, *args):
        if(args != ()):
            emb = (discord.Embed(color=0xf7b8cf))
            emb.add_field(name="Text to Binary", value=''.join([bin(ord(ch))[2:].zfill(8) for ch in ' '.join(args)]))
            await ctx.send(embed=emb)
        else:
            await ctx.send("You need to type something to encode!")

    @commands.command(pass_context=True, aliases=["b64decode", "base64d", "base64decode"], description="Decode a message from Base64", brief="`mb!b64d SGVsbG8sIHdvcmxkIQ==`")
    async def b64d(self, ctx, *args):
        if(args != ()):
            try:
                emb = (discord.Embed(color=0xf7b8cf))
                emb.add_field(name="Decoded Base64 String", value=base64.b64decode(' '.join(args)).decode())
                await ctx.send(embed = emb)
            except binascii.Error:
                await ctx.send("It seems that was not a valid Base64 string!")
        else:
            await ctx.send("You need to type something to decode!")

    @commands.command(pass_context=True, aliases=["b64encode", "base64e", "base64encode"], description="Encode a message using Base64", brief="`mb!b64e Hello, world!`")
    async def b64e(self, ctx, *args):
        if(args != ()):
            emb = (discord.Embed(color=0xf7b8cf))
            emb.add_field(name="Encoded Base64 String", value=base64.b64encode(' '.join(args).encode()).decode())
            await ctx.send(embed = emb)
        else:
            await ctx.send("You need to type something to encode!")

    @commands.command(pass_context=True, aliases=["reverse"], description="Flip a string around!", brief="`mb!flip Hello, world!`")
    async def flip(self, ctx, *args):
        if(args != ()):
            emb = (discord.Embed(color=0xf7b8cf))
            emb.add_field(name="Flipped Text", value=' '.join(args)[::-1])
            await ctx.send(embed = emb)
        else:
            await ctx.send("You need to type something to flip!")

def setup(bot):
    bot.add_cog(Encryption(bot))
