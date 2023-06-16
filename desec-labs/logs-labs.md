# Análise de Logs - Labs

## Análise de Logs I
Analise o arquivo de log e responda:  
  
Quantos endereços IPs estão envolvidos no log?  
  
Exemplo:vinteecinco  
  
Arquivo para a análise: ACCESS.LOG

[http://www.businesscorp.com.br/access.log](http://www.businesscorp.com.br/access.log)

```bash
cat logs1.txt | cut -d " " -f 1 | sort -u | wc -l
      79
```

```
setentaenove
```

## Análise de Logs II
Analise o arquivo de log e responda:  
  
Qual o endereço IP do atacante?  
  
Exemplo: 200.200.200.200  
  
Arquivo para a análise: ACCESS.LOG

[http://www.businesscorp.com.br/access.log](http://www.businesscorp.com.br/access.log)

```bash
❯ cat logs1.log | cut -d " " -f 1 | uniq -c | sort | tail -n4
1440 177.138.28.7
2532 177.138.28.7
26777 177.138.28.7
5046 177.138.28.7
```

```
177.138.28.7
```

## Análise de Logs III
Analise o arquivo de log e responda: 
  
Quando o ataque começou e quando terminou?  
  
Exemplo: 22/04/2018:15:41:10,23/04/2018:02:15:45  
  
Dica: Atenção ao formato da data.  
  
Arquivo para a análise: ACCESS.LOG

[http://www.businesscorp.com.br/access.log](http://www.businesscorp.com.br/access.log)

```bash
❯ cat logs1.log | grep "177.138.28.7" | cut -d " " -f 4 | head -n3
[13/Feb/2015:00:21:12
[13/Feb/2015:00:21:12
[13/Feb/2015:00:21:12
❯ cat logs1.log | grep "177.138.28.7" | cut -d " " -f 4 | tail -n3
[13/Feb/2015:08:58:35
[13/Feb/2015:08:58:35
[13/Feb/2015:08:58:35
```

```
13/02/2015:00:21:12,13/02/2015:08:58:35
```

## Investigando o Ataque - Lab1
Examine o arquivo de log e identifique o endereço IP do atacante.  
  
exemplo: 188.222.222.12  
  
Arquivo para a análise: LAB.LOG

[http://www.businesscorp.com.br/lab.log](http://www.businesscorp.com.br/lab.log)

```bash
❯ cat lab.log | cut -d " " -f 1 | grep -v "::1" | sort | uniq -c | sort
   1 104.211.216.163
   1 158.140.180.170
   1 186.202.173.147
   1 191.255.183.136
   1 196.52.2.31
   1 45.231.194.246
   1 47.89.192.12
   1 94.183.117.16
   2 66.102.6.117
   3 177.154.139.197
   3 185.6.9.205
   9 189.102.100.189
  24 189.4.82.26
  26 189.29.147.17
  26 201.78.230.51
  51 177.154.145.99
  71 138.204.84.95
1896 205.251.150.186
```

```
205.251.150.186
```

## Investigando o Ataque - Lab2
Examine o arquivo de log e responda em qual diretório o atacante encontrou a informação sensível?  
  
Exemplo: uploads  
  
Arquivo para a análise: LAB.LOG

[http://www.businesscorp.com.br/lab.log](http://www.businesscorp.com.br/lab.log)

```bash
❯ cat lab.log | grep "205.251.150.186" | grep "GET" | grep "200" | grep -v "404" | grep -v "GET / "
205.251.150.186 - - [12/Sep/2019:11:07:10 -0300] "GET /robots.txt HTTP/1.1" 200 381 "-" "Mozilla/5.00 (Nikto/2.1.6) (Evasions:None) (Test:robots)"
205.251.150.186 - - [12/Sep/2019:11:07:10 -0300] "GET /_restrito/ HTTP/1.1" 200 948 "-" "Mozilla/5.00 (Nikto/2.1.6) (Evasions:None) (Test:)"
205.251.150.186 - - [12/Sep/2019:11:07:11 -0300] "GET /_docs/ HTTP/1.1" 200 1139 "-" "Mozilla/5.00 (Nikto/2.1.6) (Evasions:None) (Test:)"
205.251.150.186 - - [12/Sep/2019:11:07:11 -0300] "GET /admin/ HTTP/1.1" 200 940 "-" "Mozilla/5.00 (Nikto/2.1.6) (Evasions:None) (Test:)"
205.251.150.186 - - [12/Sep/2019:11:07:14 -0300] "GET /favicon.png HTTP/1.1" 200 1491 "-" "Mozilla/5.00 (Nikto/2.1.6) (Evasions:None) (Test:favicon)"
205.251.150.186 - - [12/Sep/2019:11:08:29 -0300] "GET /configuracoes/ HTTP/1.1" 200 706 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"
205.251.150.186 - - [12/Sep/2019:11:08:29 -0300] "GET /icons/blank.gif HTTP/1.1" 200 438 "http://businesscorp.com.br/configuracoes/" "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"
205.251.150.186 - - [12/Sep/2019:11:08:29 -0300] "GET /icons/back.gif HTTP/1.1" 200 505 "http://businesscorp.com.br/configuracoes/" "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"
205.251.150.186 - - [12/Sep/2019:11:08:29 -0300] "GET /icons/unknown.gif HTTP/1.1" 200 534 "http://businesscorp.com.br/configuracoes/" "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"
205.251.150.186 - - [12/Sep/2019:11:08:48 -0300] "GET /configuracoes/db.sql HTTP/1.1" 200 573 "-" "Wget/1.20.3 (linux-gnu)"
205.251.150.186 - - [12/Sep/2019:11:08:58 -0300] "GET /index.html HTTP/1.1" 200 7348 "-" "Mozilla/5.00 (Nikto/2.1.6) (Evasions:None) (Test:multiple_index)"
205.251.150.186 - - [12/Sep/2019:11:09:04 -0300] "GET /intranet/ HTTP/1.1" 200 377 "-" "curl/7.65.1"
205.251.150.186 - - [12/Sep/2019:11:09:16 -0300] "GET /intranet/ HTTP/1.1" 200 406 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"
205.251.150.186 - - [12/Sep/2019:11:09:56 -0300] "GET /./ HTTP/1.1" 200 7348 "-" "Mozilla/5.00 (Nikto/2.1.6) (Evasions:None) (Test:000037)"
205.251.150.186 - - [12/Sep/2019:11:10:06 -0300] "GET /intranet/ HTTP/1.1" 200 406 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"
```

```
configuracoes
```

## Investigando o Ataque - Lab3
Examine o arquivo de log e responda qual o nome do arquivo sensível que o atacante baixou.  
  
Exemplo: senhas.xls

[http://www.businesscorp.com.br/lab.log](http://www.businesscorp.com.br/lab.log)

```bash
205.251.150.186 - - [12/Sep/2019:11:08:48 -0300] "GET /configuracoes/db.sql HTTP/1.1" 200 573 "-" "Wget/1.20.3 (linux-gnu)"
```

```
db.sql
```

## Investigando o Ataque - Lab4
Examine o arquivo de log e responda qual o nome e versão da ferramenta utilizada para baixar o arquivo sensível?  
  
Ex: curl/7.65.1

```bash
205.251.150.186 - - [12/Sep/2019:11:08:48 -0300] "GET /configuracoes/db.sql HTTP/1.1" 200 573 "-" "Wget/1.20.3 (linux-gnu)"
```

```
Wget/1.20.3
```

## Investigando o Ataque - Lab5
Examine o arquivo de log e informe qual a data e hora que o atacante realizou o download do arquivo sensível?  
  
Ex: 22/04/2019:08:01:25  
  
Dica: Atenção ao formato da data.

```bash
205.251.150.186 - - [12/Sep/2019:11:08:48 -0300] "GET /configuracoes/db.sql HTTP/1.1" 200 573 "-" "Wget/1.20.3 (linux-gnu)"
```

```
12/09/2019:11:08:48
```

## Investigando o Ataque - Lab6
Examine o arquivo de log e informe qual foi o próximo diretório que o atacante comprometeu após efetuar download do arquivo sensível?  
  
Exemplo: arquivos

[http://www.businesscorp.com.br/lab.log](http://www.businesscorp.com.br/lab.log)

```bash
205.251.150.186 - - [12/Sep/2019:11:08:48 -0300] "GET /configuracoes/db.sql HTTP/1.1" 200 573 "-" "Wget/1.20.3 (linux-gnu)"
205.251.150.186 - - [12/Sep/2019:11:08:58 -0300] "GET /index.html HTTP/1.1" 200 7348 "-" "Mozilla/5.00 (Nikto/2.1.6) (Evasions:None) (Test:multiple_index)"
205.251.150.186 - - [12/Sep/2019:11:09:04 -0300] "GET /intranet/ HTTP/1.1" 200 377 "-" "curl/7.65.1"
205.251.150.186 - - [12/Sep/2019:11:09:16 -0300] "GET /intranet/ HTTP/1.1" 200 406 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"
205.251.150.186 - - [12/Sep/2019:11:09:56 -0300] "GET /./ HTTP/1.1" 200 7348 "-" "Mozilla/5.00 (Nikto/2.1.6) (Evasions:None) (Test:000037)"
205.251.150.186 - - [12/Sep/2019:11:10:06 -0300] "GET /intranet/ HTTP/1.1" 200 406 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"
```

```
intranet
```

## Investigando o Ataque - Lab7
Examine o arquivo de log e responda em qual horário o atacante acessou este próximo diretório comprometido?  
  
Ex: 22/04/2019:08:01:25  
  
Dica: Atenção ao formato da data.

[http://www.businesscorp.com.br/lab.log](http://www.businesscorp.com.br/lab.log)

```bash
205.251.150.186 - - [12/Sep/2019:11:09:04 -0300] "GET /intranet/ HTTP/1.1" 200 377 "-" "curl/7.65.1"
```

```
12/09/2019:11:09:04
```

## Investigando o Ataque - Lab8
Examine o arquivo de log e responda qual programa o atacante utilizou para acessar este diretório comprometido pela primeira vez?  
  
Ex: python2.7

[http://www.businesscorp.com.br/lab.log](http://www.businesscorp.com.br/lab.log)

```
curl/7.65.1
```

## Investigando o Ataque - Lab9
Examine o arquivo de log e responda qual a versão do navegador usado pelo atacante ao acessar o diretório comprometido? 
  
Ex: Chrome/74.0

[http://www.businesscorp.com.br/lab.log](http://www.businesscorp.com.br/lab.log)

```bash
205.251.150.186 - - [12/Sep/2019:11:09:04 -0300] "GET /intranet/ HTTP/1.1" 200 377 "-" "curl/7.65.1"
205.251.150.186 - - [12/Sep/2019:11:09:16 -0300] "GET /intranet/ HTTP/1.1" 200 406 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"
205.251.150.186 - - [12/Sep/2019:11:09:56 -0300] "GET /./ HTTP/1.1" 200 7348 "-" "Mozilla/5.00 (Nikto/2.1.6) (Evasions:None) (Test:000037)"
205.251.150.186 - - [12/Sep/2019:11:10:06 -0300] "GET /intranet/ HTTP/1.1" 200 406 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"
```

```
Firefox/60.0
```
