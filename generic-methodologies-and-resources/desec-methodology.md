# Desec Methodology
## Análise de Logs
[Análise de Logs](forensics/basic-forensic-methodology/log-analysis)
[Labs](desec-labs/logs-labs)
## Análise de Protocolos
[Wireshark tricks](forensics/basic-forensic-methodology/pcap-inspection/wireshark-tricks.md)
## Vencendo o Firewall
Caso o firewall esteja bloqueando bind e reverse shell, abra mais portas e aguarde pela conexão em algumas delas
Na sua própria máquina
```bash
#!/bin/bash
echo "Opening ports..."
nc -lvpn 80&
sleep 2
nc -lvpn 443&
sleep 2
nc -lvpn 53&
sleep 2
echo "Ports opened"
netstat -nlpt
```
Na máquina alvo
```bash
echo "Testing ports..."
nc -vn [my-ip] 80&
sleep 2
nc -vn [my-ip] 443&
sleep 2
nc -vn [my-ip] 53&
__
./test_fw.sh | grep "open"
```
## Information Gathering
### Business
> theHarvester é uma ótima ferramenta nesta etapa
- [ ] Mapear colaboradores
	- [ ] Efetuar buscas na página do LinkedIn da empresa em busca de colaboradores
	- [ ] Mapear pessoas envolvidas com a tecnologia (Devs, TI, Segurança)
	- [ ] Pesquisar o perfil desses profissionais, tecnologias que dominam, github, projetos, etc
	- [ ] Pesquisar comportamentos nas redes sociais
- [ ] Mapear vagas de emprego
- [ ] Mapear endereços de e-mail
	- [ ] https://hunter.io
- [ ] Mapear padrão de usuários
- [ ] Mapear vazamento de dados
	- [ ] https://haveibeenpwned.com
	- [ ] Mapear credenciais na DeepWeb
		- [ ] https://dehashed.com (pago)
		- [ ] http://pwndb2am4tzkvold.onion/
- [ ] Mapear dados no Pastebin
	- [ ] https://pastebin.com/
- [ ] Mapear dados no Trello
- [ ] Mapear domínios similares
- [ ] Mapear cache de sites
- [ ] Realizar Google Hacking
	- [ ] [Google Dorking](generic-methodologies-and-resources/external-recon-methodology/google-dorking.md)
	- [ ] https://www.exploit-db.com/google-hacking-database
- [ ] Realizar Bing Hacking
- [ ] Non Delivery Notification
- [ ] Mapear metadados em arquivos
	- [ ] exiftool
- [ ] Mapear informações relevantes
- [ ] Waybackmachine em pontos de interesse
### INFRA
- [ ] Pesquisa Whois 
	- [ ] [whois](generic-methodologies-and-resources/external-recon-methodology/whois.md)
- [ ] Pesquisa RDAP
	- [ ] https://client.rdap.org
- [ ] Pesquisa por IP
	- [ ] [Ip Search](generic-methodologies-and-resources/external-recon-methodology/ip-search.md)
- [ ] Pesquisa BGP
	- [ ] https://bgp.he.net
	- [ ] https://bgpview.io
- [ ] Pesquisa Shodan
	- [ ] [Shodan](generic-methodologies-and-resources/pentesting-network/shodan.md)
- [ ] Pesquisa Censys
- [ ] Pesquisa em certificados
- [ ] Pesquisa DNS
	- [ ]  [DNS search](dns.md)
	- [ ] tool `dnsenum --enum businesscorp.com.br`
- [ ] Pesquisa passiva (virustotal)
- [ ] Pesquisa passiva (dnsdumpster)
- [ ] Pesquisa passiva (securitytrails)
- [ ] Pesquisa SPF
	- [ ] [SPF Send policy Framework](generic-methodologies-and-resources/pentesting-network/spf.md)
- [ ] Pesquisa por subdomínios
- [ ] Pesquisa subdomain takeover
	- [ ] [Domain/Subdomain takeover](pentesting-web/domain-subdomain-takeover.md)

### WEB
- [ ] Pesquisa Robots.txt
- [ ] Pesquisa sitemap.xml
- [ ] Identificar directory listing
- [ ] Realizar mirror website
	- [ ] `wget -m businesscorp.com.br`
	- [ ] `wget -m -e robots=off businesscorp.com.br`
- [ ] Identificar erros e códigos
- [ ] Identificar webserver
- [ ] Identificar métodos aceitos
- [ ] Pesquisa por diretórios
- [ ] Pesquisa por arquivos
- [ ] Pesquisa passiva (wappalyzer)
- [ ] Identificar WAF

### Scanning
- [ ] Mapear a rota
	- [ ] [Mapping network route](generic-methodologies-and-resources/pentesting-network/mapping-network-route.md)
- [ ] Mapear hosts ativos
	- [ ] [Internal scan with ARP protocol](generic-methodologies-and-resources/pentesting-network/internal-scan-with-arp-protocol.md)
	- [ ] [Find active hosts with nmap](generic-methodologies-and-resources/pentesting-network/find-active-hosts.md)
- [ ] [Portscan](generic-methodologies-and-resources/pentesting-network/portscan.md)
	- [ ] Mapear portas TCP abertas
	- [ ] Mapear portas UDP abertas
	- [ ] Network sweeping
	- [ ] Mapear serviços ativos
	- [ ] Identificar o Sistema Operacional
- [ ] Identificar mecanismos de defesa
	- [ ] [IDS and IPS Evasion](generic-methodologies-and-resources/pentesting-network/ids-evasion)

### Enumeration / Análise do ambiente
- [ ] Identificar detalhes dos serviços
- [ ] Identificar pontos de entrada
- [ ] Identificar má configuração
- [ ] Identificar dados sensíveis
- [ ] Identificar credenciais default
- [ ] Identificar brute force

### Avaliação de Vulnerabilidades
- [ ] Pesquisa por vulnerabilidades públicas
- [ ] Pesquisa por exploits públicos
- [ ] Pesquisa por vulnerabilidade não conhecida