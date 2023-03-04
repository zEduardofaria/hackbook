# AD CS Certificate Theft

 

## What can I do with a certificate

Before checking how to steal the certificates here you have some info about how to find what the certificate is useful for:

```powershell
# Powershell
$CertPath = "C:\path\to\cert.pfx"
$CertPass = "P@ssw0rd"
$Cert = New-Object
System.Security.Cryptography.X509Certificates.X509Certificate2 @($CertPath, $CertPass)
$Cert.EnhancedKeyUsageList

# cmd
certutil.exe -dump -v cert.pfx
```

## Exporting Certificates Using the Crypto APIs – THEFT1

The easiest way to extract a user or machine certificate and private key is through an **interactive desktop session**. If the **private key** is **exportable**, one can simply right click the certificate in `certmgr.msc`, and go to `All Tasks → Export`… to export a password protected .pfx file. \
One can accomplish this **programmatically** as well. Examples include PowerShell’s `ExportPfxCertificate` cmdlet or [TheWover’s CertStealer C# project](https://github.com/TheWover/CertStealer).

Underneath, these methods use the **Microsoft CryptoAPI** (CAPI) or more modern Cryptography API: Next Generation (CNG) to interact with the certificate store. These APIs perform various cryptographic services that needed for certificate storage and authentication (amongst other uses).

If the private key is non-exportable, CAPI and CNG will not allow extraction of non-exportable certificates. **Mimikatz’s** `crypto::capi` and `crypto::cng` commands can patch the CAPI and CNG to **allow exportation** of private keys. `crypto::capi` **patches** **CAPI** in the current process whereas `crypto::cng` requires **patching** **lsass.exe’s** memory.

## User Certificate Theft via DPAPI – THEFT2

More info about DPAPI in:

{% content-ref url="../../windows-local-privilege-escalation/dpapi-extracting-passwords.md" %}
[dpapi-extracting-passwords.md](../../windows-local-privilege-escalation/dpapi-extracting-passwords.md)
{% endcontent-ref %}

Windows **stores certificate private keys using DPAPI**. Microsoft breaks out the storage locations for user and machine private keys. When manually decrypting the encrypted DPAPI blobs, a developer needs to understand which cryptography API the OS used as the private key file structure differs between the two APIs. When using SharpDPAPI, it automatically accounts for these file format differences.&#x20;

Windows most **commonly stores user certificates** in the registry in the key `HKEY_CURRENT_USER\SOFTWARE\Microsoft\SystemCertificates`, though some personal certificates for users are **also** stored in `%APPDATA%\Microsoft\SystemCertificates\My\Certificates`. The associated user **private key locations** are primarily at `%APPDATA%\Microsoft\Crypto\RSA\User SID\` for **CAPI** keys and `%APPDATA%\Microsoft\Crypto\Keys\` for **CNG** keys.

To obtain a certificate and its associated private key, one needs to:

1. Identify w**hich certificate one wants to steal** from the user’s certificate store and extract the key store name.
2. Find the **DPAPI masterkey** needed to decrypt the associated private key.
3. Obtain the plaintext DPAPI masterkey and use it to **decrypt the private key**.

To **get the plaintext DPAPI masterkey**:

```bash
# With mimikatz
## Running in a process in the users context
dpapi::masterkey /in:"C:\PATH\TO\KEY" /rpc

# with mimikatz
## knowing the users password
dpapi::masterkey /in:"C:\PATH\TO\KEY" /sid:accountSid /password:PASS
```

To simplify masterkey file and private key file decryption, [**SharpDPAPI’s**](https://github.com/GhostPack/SharpDPAPI) `certificates` command can be used with the `/pvk`, `/mkfile`, `/password`, or `{GUID}:KEY` arguments to decrypt the private keys and associated certificates, outputting a `.pem` text file.

```bash
SharpDPAPI.exe certificates /mkfile:C:\temp\mkeys.txt

# Transfor .pem to .pfx
openssl pkcs12 -in cert.pem -keyex -CSP "Microsoft Enhanced Cryptographic Provider v1.0" -export -out cert.pfx
```

## Machine Certificate Theft via DPAPI – THEFT3

Windows stores machine certificates in the registry key `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\SystemCertificates` and stores private keys in several different places depending on the account.\
Although SharpDPAPI will search all these locations, the most interesting results tend to come from `%ALLUSERSPROFILE%\Application Data\Microsoft\Crypto\RSA\MachineKeys` (CAPI) and `%ALLUSERSPROFILE%\Application Data\Microsoft\Crypto\Keys` (CNG). These **private keys** are associated with the **machine certificate** store and Windows encrypts them with the **machine’s DPAPI master keys**.\
One cannot decrypt these keys using the domain’s DPAPI backup key, but rather **must** use the **DPAPI\_SYSTEM LSA secret** on the system which is **accessible only by the SYSTEM user**.&#x20;

You can do this manually with **Mimikatz’** **`lsadump::secrets`** command and then use the extracted key to **decrypt machine masterkeys**. \
You can also patch CAPI/CNG as before and use **Mimikatz’** `crypto::certificates /export /systemstore:LOCAL_MACHINE` command. \
**SharpDPAPI’s** certificates command with the **`/machine`** flag (while elevated) will automatically **elevate** to **SYSTEM**, **dump** the **DPAPI\_SYSTEM** LSA secret, use this to **decrypt** and found machine DPAPI masterkeys, and use the key plaintexts as a lookup table to decrypt any machine certificate private keys.

## Finding Certificate Files – THEFT4

Sometimes **certificates are just in the filesystem**, like in file shares or in the Downloads folder.\
The most common type of Windows-focused certificate files we have seen are **`.pfx`** and **`.p12`** files, with **`.pkcs12`** and ** `.pem` ** sometimes showing up but less often.\
Other interesting certificate-related file extensions are: **`.key`** (_private key_), **`.crt/.cer`** (_just cert_), **`.csr`** (_Certificate Signing Request, it doesn't contain certs of priv keys_), **`.jks/.keystore/.keys`** (_Java Keystore. May contain certs + private keys used by Java applications_).

To find this files, just search for those extensions using powershell or the cmd.

If you find a **PKCS#12** certificate file and it is **password protected**, you can extract a hash using [pfx2john.py](https://fossies.org/dox/john-1.9.0-jumbo-1/pfx2john\_8py\_source.html) **crack** it using JohnTheRipper.

## NTLM Credential Theft via PKINIT – THEFT5

> In order to **support NTLM authentication** \[MS-NLMP] for applications connecting to network services that **do not support Kerberos** authentication, when PKCA is used, the KDC returns the **user’s NTLM** one-way function (OWF) in the privilege attribute certificate (PAC) **`PAC_CREDENTIAL_INFO`** buffer

So, if account authenticates and gets a **TGT through PKINIT**, there is a built-in “failsafe” that allows the current host to **obtain our NTLM hash from the TGT** to support legacy authentication. This involves **decrypting** a **`PAC_CREDENTIAL_DATA`** **structure** that is a Network Data Representation (NDR) serialized representation of the NTLM plaintext.

[**Kekeo**](https://github.com/gentilkiwi/kekeo) can be used to ask for a TGT with this information an retrieve the users NTML

```bash
tgt::pac /caname:thename-DC-CA /subject:harmj0y /castore:current_user /domain:domain.local
```

Kekeo’s implementation will also work with smartcard-protected certs that are currently plugged in if you can [**recover the pin**](https://github.com/CCob/PinSwipe)**.** It will also be supported in [**Rubeus**](https://github.com/GhostPack/Rubeus).

## References

* All the info was taken from [https://www.specterops.io/assets/resources/Certified\_Pre-Owned.pdf](https://www.specterops.io/assets/resources/Certified\_Pre-Owned.pdf)

 
