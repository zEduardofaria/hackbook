# AD CS Account Persistence

 

## Active User Credential Theft via Certificates – PERSIST1

If the user is allowed to request a certificate that allows domain authentication, an attacker could **request** and **steal** it to **maintain** **persistence**.

The **`User`** template allows that and comes by **default**. However, it might be disabled. So, [**Certify**](https://github.com/GhostPack/Certify) allows you to find valid certificates to persist:

```
Certify.exe find /clientauth
```

Note that a **certificate can be used for authentication** as that user as long as the certificate is **valid**, **even** if the user **changes** their **password**.

From the **GUI** it's possible to request a certificate with `certmgr.msc` or via the command-line with `certreq.exe`.

Using [**Certify**](https://github.com/GhostPack/Certify) you can run:

```
Certify.exe request /ca:CA-SERVER\CA-NAME /template:TEMPLATE-NAME
```

The result will be a **certificate** + **private key** `.pem` formatted block of text

```bash
openssl pkcs12 -in cert.pem -keyex -CSP "Microsoft Enhanced Cryptographic Provider v1.0" -export -out cert.pfx
```

To **use that certificate**, one can then **upload** the `.pfx` to a target and **use it with** [**Rubeus**](https://github.com/GhostPack/Rubeus) to **request a TGT** for the enrolled user, for as long as the certificate is valid (default lifetime is 1 year):

```bash
Rubeus.exe asktgt /user:harmj0y /certificate:C:\Temp\cert.pfx /password:CertPass!
```

{% hint style="warning" %}
Combined with the technique outlined in the [**THEFT5**](certificate-theft.md#ntlm-credential-theft-via-pkinit-theft5) section, an attacker can also persistently **obtain the account’s NTLM hash**, which the attacker could use to authenticate via **pass-the-hash** or **crack** to obtain the **plaintext** **password**. \
This is an alternative method of **long-term credential theft** that does **not touch LSASS** and is possible from a **non-elevated context.**
{% endhint %}

## Machine Persistence via Certificates - PERSIST2

If a certificate template allowed for **Domain Computers** as enrolment principals, an attacker could **enrol a compromised system’s machine account**. The default **`Machine`** template matches all those characteristics.

If an **attacker elevates privileges** on compromised system, the attacker can use the **SYSTEM** account to enrol in certificate templates that grant enrolment privileges to machine accounts (more information in [**THEFT3**](certificate-theft.md#machine-certificate-theft-via-dpapi-theft3)).

You can use [**Certify**](https://github.com/GhostPack/Certify)  to  gather a certificate for the machine account elevating automatically to SYSTEM with:

```bash
Certify.exe request /ca:dc.theshire.local/theshire-DC-CA /template:Machine /machine
```

Note that with access to a machine account certificate, the attacker can then **authenticate to Kerberos** as the machine account. Using **S4U2Self**, an attacker can then obtain a **Kerberos service ticket to any service on the host** (e.g., CIFS, HTTP, RPCSS, etc.) as any user.

Ultimately, this gives an attack a machine persistence method.

## Account Persistence via Certificate Renewal - PERSIST3

Certificate templates have a **Validity Period** which determines how long an issued certificate can be used, as well as a **Renewal period** (usually 6 weeks). This is a window of **time before** the certificate **expires** where an **account can renew it** from the issuing certificate authority.

If an attacker compromises a certificate capable of domain authentication through theft or malicious enrolment, the attacker can **authenticate to AD for the duration of the certificate’s validity period**. The attacker, however, can r**enew the certificate before expiration**. This can function as an **extended persistence** approach that **prevents additional ticket** enrolments from being requested, which **can leave artifacts** on the CA server itself.

 
