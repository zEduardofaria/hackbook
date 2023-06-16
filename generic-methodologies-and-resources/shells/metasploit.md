# Metasploit
## Database
```bash
└─# msfdb                                                    

Manage the metasploit framework database

You can use an specific port number for the
PostgreSQL connection setting the PGPORT variable
in the current shell.

Example: PGPORT=5433 msfdb init

  msfdb init     # start and initialize the database
  msfdb reinit   # delete and reinitialize the database
  msfdb delete   # delete database and stop using it
  msfdb start    # start the database
  msfdb stop     # stop the database
  msfdb status   # check service status
  msfdb run      # start the database and run msfconsole
```

```bash
└─# systemctl start postgres
└─# msfdb init

msf6 > services # search in db for services found by msf
msf6 > services -p 445 # search in db for services in port 445 found by msf
msf6 > hosts # search in db for hosts found by msf
msg6 > hosts -i "Samba 3.0.20-Debian" 172.16.1.5 # Add information to host 
msf6 > creds # search in db for creds found by msf
msf6 > vulns # search in db for vulns that msf could detect froms its database

msf6 > db_nmap -v --open -sV -Pn <IP> # save all result from nmap in msf db
db_import /opt/<fileresult>.xml # save result from nmap outside msf to msf db
```

## Init
```bash
└─# msfconsole
```

## Aux commands
```bash
msf6 > show -h # show all modules that it can shows
msf6 > show payloads # show all payload
msf6 > show auxiliary # show all auxiliary modules
msf6 > use auxiliary/scanner/portscan/tcp # select aux module to be used

msf6 auxiliary(scanner/portscan/tcp) > info # See info about module selected
msf6 auxiliary(scanner/portscan/tcp) > show options # options used by the module. Usually are information about the target and local host and ports
msf6 auxiliary(scanner/portscan/tcp) > set <VARIABLE> <VALUE> # set option value

msf6 exploit(any/exploit) > show payloads # to show all available payloads
msf6 exploit(any/exploit) > set payload <ID | payload locale> # to show all available payloads

msf6 exploit(any/exploit) > exploit # to run exploit on target

msf6 > search -h # show commands for search aux command
msf6 > search type:auxiliary portscan # example of search for aux
msf6 > search type:exploit fullname:"Samba 3.0.20" # To be more specific in the search
msf6 > search type:exploit smb # example of search for exploit

msf6 > sessions # list all open sessions in target got from modules
msf6 > sessions -i 1 # example to use session by id

msf6 > back # to exit module



```

## Brute force attacks
```bash
auxiliary/scanner/ssh/ssh_login # example of module used for brute force ssh
```

## Recon with msf example
```bash
msf6 > db_nmap -p 139,445 --open -sS -Pn 172.16.1.0/24
msf6 > search type:auxiliary smb_version
msf6 auxiliary(scanner/smb/smb_version) > services -p 445 --rhosts
msf6 auxiliary(scanner/smb/smb_version) > run
```

## Detect vulnerabilities using auxiliary modules
```bash
msf6 > search type:auxiliary smb
msf6 > auxiliary/scanner/smb/smb_ms17_010
```

## Payloads
![[Pasted image 20230611211458.png]]

- `Staged Payloads`: Staged payloads are delivered to the target system in multiple stages. The initial stage, known as the stager, is small in size and is responsible for establishing a communication channel with the Metasploit framework on the attacker's machine. Once the communication is established, the subsequent stages, also known as stages, are delivered to the target system. These stages contain the actual payload and are larger in size. Staging allows for flexibility and helps evade detection as it reduces the size of the initial delivery. However, it requires a stable and reliable network connection between the attacker and the target system for successful delivery.
- `Inline Payloads`: Inline payloads, also known as non-staged payloads, are delivered to the target system all at once, without multiple stages. The entire payload is sent in a single transmission. Inline payloads are often smaller in size compared to staged payloads since they don't require the additional stages for delivery. They are more suitable for situations where network stability is a concern or when the target environment doesn't allow large payloads. However, inline payloads may be easier to detect since the entire payload is delivered in one shot.