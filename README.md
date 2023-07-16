# psuob.py: unoriginal powershell obfuscator

this is the first powershell obfuscator i've written, but i'm proud of what came out of it.

usage: psuob.py "[cmd]"

the script will print two main outputs: the variable assignation and the actual command execution.
for the time being, it'll use a simple Invoke-Expression statement. i've tried using base64 decoding and running
it through a couple IEX pipes. it works, although not flawlessly. be careful!
