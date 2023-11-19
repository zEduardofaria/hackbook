# Web Recon flow

# Referências

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

## Subdomínios

```bash
subfinder -d target.com.br -silent | httpx -silent | gau
```

Subfinder encontrará subdomínios de forma ativa. O httpx irá validar se estes subdomínios encontrados estão funcionando. Gau analizará todos os subdomínios ativos em busca de urls. 
Gau certamente irá encontrar vários arquivos nesta etapa

## Parâmetros para cada subdomínio

```bash
paramspider -d target.com.br | kxss
```

paramspider irá buscar por parâmetros fuzzable, e o kxss irá testar se estes parâmetros são refletidos na tela.

## Secret Finder

```bash
i=1; for url in $(cat js-files.txt); do python3 /Users/eduardofaria/Developer/tools/SecretFinder/SecretFinder.py -i $url -o cli > ./secretfinder/${i}.html; i=$((i+1)); done
```

secret finder buscará por chaves em cada arquivo js encontrado pelo gau.

```bash

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