# Recon flow

# Referências
## WHOIS

|**Command**|**Description**|
|---|---|
|`export TARGET="domain.tld"`|Assign target to an environment variable.|
|`whois $TARGET`|WHOIS lookup for the target.|

---

## DNS Enumeration

|**Command**|**Description**|
|---|---|
|`nslookup $TARGET`|Identify the `A` record for the target domain.|
|`nslookup -query=A $TARGET`|Identify the `A` record for the target domain.|
|`dig $TARGET @<nameserver/IP>`|Identify the `A` record for the target domain.|
|`dig a $TARGET @<nameserver/IP>`|Identify the `A` record for the target domain.|
|`nslookup -query=PTR <IP>`|Identify the `PTR` record for the target IP address.|
|`dig -x <IP> @<nameserver/IP>`|Identify the `PTR` record for the target IP address.|
|`nslookup -query=ANY $TARGET`|Identify `ANY` records for the target domain.|
|`dig any $TARGET @<nameserver/IP>`|Identify `ANY` records for the target domain.|
|`nslookup -query=TXT $TARGET`|Identify the `TXT` records for the target domain.|
|`dig txt $TARGET @<nameserver/IP>`|Identify the `TXT` records for the target domain.|
|`nslookup -query=MX $TARGET`|Identify the `MX` records for the target domain.|
|`dig mx $TARGET @<nameserver/IP>`|Identify the `MX` records for the target domain.|

---

## Passive Subdomain Enumeration

|**Resource/Command**|**Description**|
|---|---|
|`VirusTotal`|[https://www.virustotal.com/gui/home/url](https://www.virustotal.com/gui/home/url)|
|`Censys`|[https://censys.io/](https://censys.io/)|
|`Crt.sh`|[https://crt.sh/](https://crt.sh/)|
|`curl -s https://sonar.omnisint.io/subdomains/{domain} \| jq -r '.[]' \| sort -u`|All subdomains for a given domain.|
|`curl -s https://sonar.omnisint.io/tlds/{domain} \| jq -r '.[]' \| sort -u`|All TLDs found for a given domain.|
|`curl -s https://sonar.omnisint.io/all/{domain} \| jq -r '.[]' \| sort -u`|All results across all TLDs for a given domain.|
|`curl -s https://sonar.omnisint.io/reverse/{ip} \| jq -r '.[]' \| sort -u`|Reverse DNS lookup on IP address.|
|`curl -s https://sonar.omnisint.io/reverse/{ip}/{mask} \| jq -r '.[]' \| sort -u`|Reverse DNS lookup of a CIDR range.|
|`curl -s "https://crt.sh/?q=${TARGET}&output=json" \| jq -r '.[] \| "\(.name_value)\n\(.common_name)"' \| sort -u`|Certificate Transparency.|
|`cat sources.txt \| while read source; do theHarvester -d "${TARGET}" -b $source -f "${source}-${TARGET}";done`|Searching for subdomains and other information on the sources provided in the source.txt list.|

#### Sources.txt

```txt
baidu
bufferoverun
crtsh
hackertarget
otx
projecdiscovery
rapiddns
sublist3r
threatcrowd
trello
urlscan
vhost
virustotal
zoomeye
```

---

## Passive Infrastructure Identification

|**Resource/Command**|**Description**|
|---|---|
|`Netcraft`|[https://www.netcraft.com/](https://www.netcraft.com/)|
|`WayBackMachine`|[http://web.archive.org/](http://web.archive.org/)|
|`WayBackURLs`|[https://github.com/tomnomnom/waybackurls](https://github.com/tomnomnom/waybackurls)|
|`waybackurls -dates https://$TARGET > waybackurls.txt`|Crawling URLs from a domain with the date it was obtained.|

---

## Active Infrastructure Identification

|**Resource/Command**|**Description**|
|---|---|
|`curl -I "http://${TARGET}"`|Display HTTP headers of the target webserver.|
|`whatweb -a https://www.facebook.com -v`|Technology identification.|
|`Wappalyzer`|[https://www.wappalyzer.com/](https://www.wappalyzer.com/)|
|`wafw00f -v https://$TARGET`|WAF Fingerprinting.|
|`Aquatone`|[https://github.com/michenriksen/aquatone](https://github.com/michenriksen/aquatone)|
|`cat subdomain.list \| aquatone -out ./aquatone -screenshot-timeout 1000`|Makes screenshots of all subdomains in the subdomain.list.|

---

## Active Subdomain Enumeration

|**Resource/Command**|**Description**|
|---|---|
|`HackerTarget`|[https://hackertarget.com/zone-transfer/](https://hackertarget.com/zone-transfer/)|
|`SecLists`|[https://github.com/danielmiessler/SecLists](https://github.com/danielmiessler/SecLists)|
|`nslookup -type=any -query=AXFR $TARGET nameserver.target.domain`|Zone Transfer using Nslookup against the target domain and its nameserver.|
|`gobuster dns -q -r "${NS}" -d "${TARGET}" -w "${WORDLIST}" -p ./patterns.txt -o "gobuster_${TARGET}.txt"`|Bruteforcing subdomains.|

---

## Virtual Hosts

|**Resource/Command**|**Description**|
|---|---|
|`curl -s http://192.168.10.10 -H "Host: randomtarget.com"`|Changing the HOST HTTP header to request a specific domain.|
|`cat ./vhosts.list \| while read vhost;do echo "\n********\nFUZZING: ${vhost}\n********";curl -s -I http://<IP address> -H "HOST: ${vhost}.target.domain" \| grep "Content-Length: ";done`|Bruteforcing for possible virtual hosts on the target domain.|
|`ffuf -w ./vhosts -u http://<IP address> -H "HOST: FUZZ.target.domain" -fs 612`|Bruteforcing for possible virtual hosts on the target domain using `ffuf`.|

---

## Crawling

|**Resource/Command**|**Description**|
|---|---|
|`ZAP`|[https://www.zaproxy.org/](https://www.zaproxy.org/)|
|`ffuf -recursion -recursion-depth 1 -u http://192.168.10.10/FUZZ -w /opt/useful/SecLists/Discovery/Web-Content/raft-small-directories-lowercase.txt`|Discovering files and folders that cannot be spotted by browsing the website.|
|`ffuf -w ./folders.txt:FOLDERS,./wordlist.txt:WORDLIST,./extensions.txt:EXTENSIONS -u http://www.target.domain/FOLDERS/WORDLISTEXTENSIONS`|Mutated bruteforcing against|

## Subdomain

### History

- securitytrails.com
- subdomainfinder.c99.nl
- web.archive.org
- dnsdumpster.com
- github.com/Screetsec/Sudomy

### Certificados e passivos
- github.com/projectdiscovery/subfinder
- ssmate.com/certspotter
- github.com/UnaPibaGeek/ctfr (usa o crt.sh)
- chaos.projectdiscovery.io

### Brute Force

- github.com/aboul3la/Sublist3r
- github.com/TheRook/subbrute
- github.com/OWASP/Amass

### Manual Recon

```bash
for subdominio in $(cat sub.txt); echo "Testando: $subdominio.mercadolivre.com.br"; host "$subdominio.mercadolivre.com.br" | grep -v 'NXDOMAIN'; done;
```

## Application

### URL discovery

- github.com/lc/gau 
- github.com/hakluke/hakrawler 
- github.com/xmendez/wfuzz 
- github.com/ffuf/ffuf 
- github.com/maurosoria/dirsearch

### Content Discovery

- github.com/projectdiscovery/httpx
- github.com/michenriksen/aquatone
- github.com/m4ll0k/SecretFinder

### Parameter Discovery

- github.com/devanshbatham/ParamSpider
- github.com/tomnomnom/gf
- github.com/s0md3v/Parth
- github.com/tomnomnom/hacks/tree/master/kxss

# Encadeando ferramentas

Com o subfinder faz o discovery subdomínios, depois o httpx valida se o subdominio tem um servidor rodando, e com o gau descobre endereços em cada subdominio ativo.

```bash
subfinder -d mercadolivre.com.br -silent | httpx -silent | gau
```

Com o paramspider pegamos subdomínios conhecidos que tenha parâmetros sendo utilizados, e o `kxss` testa cada parâmetro

```bash
python3 paramspider.py -d testphp.vulnweb.com | kxss
```

# Metodologia pessoal

## Infra
### Autoridade
https://www.iana.org/whois?q=target.com.br

```bash
whois target.com.br
```

### Mais informações na autoridade
_Pesquise na autoridade_
https://registro.br/tecnologia/ferramentas/whois?search=sicrediregiaodaproducao.com.br

> Repita o processo com o DNS

### Pesquisa por IP

```bash
host target.com.br

whois <ip-address>
```

### BGP

### Analisando DNS

```bash
dig any habitissimo.com.br # @1.1.1.1
# Ou
nslookup -query=ANY habitissimo.com.br
```
## Web
### Google Dorking

```
site:trello.com "target"
site:pastebin.com "target"
site:notion.com "target"
site:github.com "target"

site:target.com ext:php 
site:target.com.br filetype:xls
```

### Shodan++
```bash

```

## Subdomínios

```bash
subfinder -d target.com.br -silent | httpx -silent | gau
```

Subfinder encontrará subdomínios de forma ativa. O httpx irá validar se estes subdomínios encontrados estão funcionando. Gau analizará todos os subdomínios ativos em busca de urls. 
Gau certamente irá encontrar vários arquivos nesta etapa
### URLs e JS Files para cada subdomínio

Mining URLs from dark corners of Web Archives

```bash
paramspider -d target.com.br
paramspider -l subdomains.txt
```

```bash
python3 waymore.py -i target.com.br -f -xcc -xav -xus -l 1000 -oU waymore.txt
```

Hakcrawler - Fast golang web crawler for gathering URLs and JavaScript file locations. This is basically a simple implementation of the awesome Gocolly library.

```bash
cat subdomains.txt | hakrawler
```

paramspider irá buscar por parâmetros fuzzable, e o kxss irá testar se estes parâmetros são refletidos na tela.

### Parâmetros refletidos com KXSS

```bash
cat urls.txt | kxss
```

### Exportar todas as URLs encontradas para o Site Map do Burp através de Proxy

```bash
xargs -n 1 curl -x http://127.0.0.1:8081 < gau.txt
```
Ou de uma forma mais bonita
```bash
#!/bin/bash

  

# Arquivo de URLs

URL_FILE="js-crawler.txt"

  

# Configuração do proxy

PROXY="127.0.0.1:8080"

  

# Verifica se o arquivo de URLs existe

if [ ! -f "$URL_FILE" ]; then

echo "Arquivo de URLs não encontrado: $URL_FILE"

exit 1

fi

  

# Loop sobre cada URL no arquivo

while IFS= read -r URL; do

# Verifica se a URL não está vazia ou é um comentário

if [ -n "$URL" ] && [[ ! "$URL" =~ ^# ]]; then

echo "Acessando URL: $URL"

# Utiliza o curl com a configuração de proxy

curl -x "$PROXY" "$URL"

echo "--------------------------------------"

fi

done < "$URL_FILE"****
```
### Secret Finder

```bash
i=1; for url in $(cat js-files.txt); do python3 /Users/eduardofaria/Developer/tools/SecretFinder/SecretFinder.py -i $url -o cli > ./secretfinder/${i}.html; i=$((i+1)); done
```

secret finder buscará por chaves em cada arquivo js encontrado pelo gau/waymore.
#### Encontre ainda mais links com xnLinkFinder

```bash
python3 xnLinkFinder.py -i target_js.txt -sf target.com
```
## Screenshoting

```bash
subfinder -d target.com.br -silent | httpx -silent | aquatone
```

Aquatone irá tirar screenshots, e além disso, mostrará tecnologias encontradas em cada subdomínio

## Github Dorking
### TruffleHog

TruffleHog is a great tool for automatically discovering exposed secrets. You can simply use the following Docker run to initiate a TruffleHog scan of your target's Github.

```bash
sudo docker run -it -v "$PWD:/pwd" trufflesecurity/trufflehog:latest github --org=target-name
```