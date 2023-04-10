# Log Analysis

Considerando que o log tenha o seguinte formato
```log
182.118.53.93 - - [08/Feb/2015:08:10:21 -0200] "GET / HTTP/1.1" 200 2477 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2251.0 Safari/537.36"
149.129.173.104 - - [08/Feb/2015:19:46:49 -0200] "GET /tmUnblock.cgi HTTP/1.1" 400 522 "-" "-"
82.213.78.2 - - [08/Feb/2015:22:04:52 -0200] "GET /cgi-bin/test-cgi HTTP/1.1" 404 532 "-" "the beast"
82.138.16.125 - - [08/Feb/2015:23:09:41 -0200] "GET /manager/html HTTP/1.1" 404 502 "-" "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0"
189.36.234.53 - - [09/Feb/2015:06:33:24 -0200] "GET / HTTP/1.1" 200 2533 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36"
189.36.234.53 - - [09/Feb/2015:06:33:24 -0200] "GET /css/layout.css HTTP/1.1" 200 2994 "http://www.grandbusiness.com.br/" "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36"
189.36.234.53 - - [09/Feb/2015:06:33:24 -0200] "GET /css/default.css HTTP/1.1" 200 5449 "http://www.grandbusiness.com.br/" "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36"
189.36.234.53 - - [09/Feb/2015:06:33:24 -0200] "GET /js/modernizr.js HTTP/1.1" 200 6542 "http://www.grandbusiness.com.br/" "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36"
189.36.234.53 - - [09/Feb/2015:06:33:24 -0200] "GET /css/media-queries.css HTTP/1.1" 200 1905 "http://www.grandbusiness.com.br/" "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36"
189.36.234.53 - - [09/Feb/2015:06:33:24 -0200] "GET /js/jquery-migrate-1.2.1.min.js HTTP/1.1" 200 3415 "http://www.grandbusiness.com.br/" "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36"
```

## Comandos úteis para buscar informações

### Identifique o formato do log
Veja como é o formato do log
```bash
head -n1 access.log
```

### Filtre os IPs 
Usando cut podemos delimitar por espaço, pegando a primeira posição
```bash
cat access.log | cut -d " " -f 1
```
E então filtrar por repetidos com `sort -u`
```bash
cat access.log | cut -d " " -f 1 | sort -u
```
Ou, podemos manter os repetidos e contar quantas requisições cada um teve com `uniq -c`
```bash
cat access.log | cut -d " " -f 1 | sort | uniq -c
```
E então ordenar de forma numérica com `-un`. utilize `r` para ser do maior para o menor.
```bash
cat access.log | cut -d " " -f 1 | sort | uniq -c | sort -unr
```

### Filtre as primeiras e últimas chamadas de um IP específico
Última linha com `tail -n1`
```bash
cat access.log | grep "{IP}" | tail -n1
```
Primeira linha com `head -n1`
```bash
cat access.log | grep "{IP}" | head -n1
```
É possível notar se este foi um ataque se todas as requisições estiverem muito perto uma da outra

### Pesquise por ferramentas
```bash
cat access.log | grep "{tool}" | tail -n1
```