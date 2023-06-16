# Wireshark tricks
## Improve your Wireshark skills

### Tutorials

The following tutorials are amazing to learn some cool basic tricks:

* [https://unit42.paloaltonetworks.com/unit42-customizing-wireshark-changing-column-display/](https://unit42.paloaltonetworks.com/unit42-customizing-wireshark-changing-column-display/)
* [https://unit42.paloaltonetworks.com/using-wireshark-display-filter-expressions/](https://unit42.paloaltonetworks.com/using-wireshark-display-filter-expressions/)
* [https://unit42.paloaltonetworks.com/using-wireshark-identifying-hosts-and-users/](https://unit42.paloaltonetworks.com/using-wireshark-identifying-hosts-and-users/)
* [https://unit42.paloaltonetworks.com/using-wireshark-exporting-objects-from-a-pcap/](https://unit42.paloaltonetworks.com/using-wireshark-exporting-objects-from-a-pcap/)

### Basic Functions

**Filter by protocol**
Search only for `DNS` protocol
![[Pasted image 20230412215055.png]]
Search only for `http`
![[Pasted image 20230412215456.png]]
Search only for `tcp`
![[Pasted image 20230412215545.png]]

**Filter by request**

![[Pasted image 20230412222516.png]]

**Filter by ip address**
Search for two ip address with `&&` and `ip.addr`. Could work with only one of them

![[Pasted image 20230412215625.png]]

Search by ip source with `ip.src`

![[Pasted image 20230412215737.png]]

By ip destination with `ip.dst`

![[Pasted image 20230412215817.png]]

By tcp port with `tcp.port`

![[Pasted image 20230412215908.png]]

Search for string content with `tcp contains PASS`

![[Pasted image 20230412221941.png]]

Same with `http.request.uri contains {word}`

![[Pasted image 20230412222638.png]]

#### Create filter for specific interface

Select the interface you want to track

![[Pasted image 20230412220235.png]]

Select a capture filter for the interface you selected

![[Pasted image 20230412220318.png]]

#### Create filter for all interfaces

Select the green flag in front of "...using this filter"

![[Pasted image 20230412220827.png]]

Click on `+` and create a new filter

![[Pasted image 20230412220858.png]]

The filter created is named `FTP` and its value is `port 21`

Select it in the same green flag from before

![[Pasted image 20230412220938.png]]

#### Follow Requests by protocol

Right click in a row, and go to `Follow [PROTOCOL]` 

![[Pasted image 20230412221136.png]]

![[Pasted image 20230412221222.png]]

#### Find open ports
Pode ser bom filtrar a conversa entre atacante e alvo antes disso.
Vá para `Statistics > Conversations` 

Vá para TCP e ordene por `packets`
![[Pasted image 20230417225326.png]]
Note que todas as portas com **mais de 2** packets estão abertas.
#### More information

https://wiki.wireshark.org/DisplayFilters
https://wiki.wireshark.org/CaptureFilters

### Analysed Information

**Expert Information**

Clicking on _**Analyze** --> **Expert Information**_ you will have an **overview** of what is happening in the packets **analyzed**:

![](<../../../.gitbook/assets/image (570).png>)

**Resolved Addresses**

Under _**Statistics --> Resolved Addresses**_ you can find several **information** that was "**resolved**" by wireshark like port/transport to protocol, MAC to the manufacturer, etc. It is interesting to know what is implicated in the communication.

![](<../../../.gitbook/assets/image (571).png>)

**Protocol Hierarchy**

Under _**Statistics --> Protocol Hierarchy**_ you can find the **protocols** **involved** in the communication and data about them.

![](<../../../.gitbook/assets/image (572).png>)

**Conversations**

Under _**Statistics --> Conversations**_ you can find a **summary of the conversations** in the communication and data about them.

![](<../../../.gitbook/assets/image (573).png>)

**Endpoints**

Under _**Statistics --> Endpoints**_ you can find a **summary of the endpoints** in the communication and data about each of them.

![](<../../../.gitbook/assets/image (575).png>)

**DNS info**

Under _**Statistics --> DNS**_ you can find statistics about the DNS request captured.

![](<../../../.gitbook/assets/image (577).png>)

**I/O Graph**

Under _**Statistics --> I/O Graph**_ you can find a **graph of the communication.**

![](<../../../.gitbook/assets/image (574).png>)

### Filters

Here you can find wireshark filter depending on the protocol: [https://www.wireshark.org/docs/dfref/](https://www.wireshark.org/docs/dfref/)\
Other interesting filters:

* `(http.request or ssl.handshake.type == 1) and !(udp.port eq 1900)`
  * HTTP and initial HTTPS traffic
* `(http.request or ssl.handshake.type == 1 or tcp.flags eq 0x0002) and !(udp.port eq 1900)`
  * HTTP and initial HTTPS traffic + TCP SYN
* `(http.request or ssl.handshake.type == 1 or tcp.flags eq 0x0002 or dns) and !(udp.port eq 1900)`
  * HTTP and initial HTTPS traffic + TCP SYN + DNS requests

### Search

If you want to **search** for **content** inside the **packets** of the sessions press _CTRL+f_. You can add new layers to the main information bar (No., Time, Source, etc.) by pressing the right button and then the edit column.

Practice: [https://www.malware-traffic-analysis.net/](https://www.malware-traffic-analysis.net)

## Identifying Domains

You can add a column that shows the Host HTTP header:

![](<../../../.gitbook/assets/image (403).png>)

And a column that add the Server name from an initiating HTTPS connection (**ssl.handshake.type == 1**):

![](<../../../.gitbook/assets/image (408) (1).png>)

## Identifying local hostnames

### From DHCP

In current Wireshark instead of `bootp` you need to search for `DHCP`

![](<../../../.gitbook/assets/image (404).png>)

### From NBNS

![](<../../../.gitbook/assets/image (405).png>)

## Decrypting TLS

### Decrypting https traffic with server private key

_edit>preference>protocol>ssl>_

![](<../../../.gitbook/assets/image (98).png>)

Press _Edit_ and add all the data of the server and the private key (_IP, Port, Protocol, Key file and password_)

### Decrypting https traffic with symmetric session keys

It turns out that Firefox and Chrome both support logging the symmetric session key used to encrypt TLS traffic to a file. You can then point Wireshark at said file and presto! decrypted TLS traffic. More in: [https://redflagsecurity.net/2019/03/10/decrypting-tls-wireshark/](https://redflagsecurity.net/2019/03/10/decrypting-tls-wireshark/)\
To detect this search inside the environment for to variable `SSLKEYLOGFILE`

A file of shared keys will look like this:

![](<../../../.gitbook/assets/image (99).png>)

To import this in wireshark go to \_edit > preference > protocol > ssl > and import it in (Pre)-Master-Secret log filename:

![](<../../../.gitbook/assets/image (100).png>)

## ADB communication

Extract an APK from an ADB communication where the APK was sent:

```python
from scapy.all import *

pcap = rdpcap("final2.pcapng")

def rm_data(data):
    splitted = data.split(b"DATA")
    if len(splitted) == 1:
        return data
    else:
        return splitted[0]+splitted[1][4:]

all_bytes = b""
for pkt in pcap:
    if Raw in pkt:
        a = pkt[Raw]
        if b"WRTE" == bytes(a)[:4]:
            all_bytes += rm_data(bytes(a)[24:])
        else:
            all_bytes += rm_data(bytes(a))
print(all_bytes)

f = open('all_bytes.data', 'w+b')
f.write(all_bytes)
f.close()
```


