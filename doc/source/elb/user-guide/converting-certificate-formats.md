# Converting Certificate Formats<a name="EN-US_TOPIC_0092382556"></a>

## Scenarios<a name="section5669342517545"></a>

ELB supports certificates only in PEM format. If you have a certificate in other format, you must convert it to a PEM-encoded certificate. There are some common methods for converting other certificate formats to PEM.

## From DER to PEM<a name="section606556821761"></a>

The DER format is usually used on a Java platform.

Run the following command to convert the certificate format:

```
openssl x509 -inform der -in certificate.cer -out certificate.pem
```

Run the following command to convert the private key format:

```
openssl rsa -inform DER -outform PEM -in privatekey.der -out privatekey.pem
```

## From P7B to PEM<a name="section4238940917631"></a>

The P7B format is usually used by Windows Server and Tomcat.

Run the following command to convert the certificate format:

```
openssl pkcs7 -print_certs -in incertificate.p7b -out outcertificate.cer
```

## From PFX to PEM<a name="section13954081778"></a>

The PFX format is usually used by Windows Server.

Run the following command to convert the certificate format:

```
openssl pkcs12 -in certname.pfx -nokeys -out cert.pem
```

Run the following command to convert the private key format:

```
openssl pkcs12 -in certname.pfx -nocerts -out key.pem -nodes
```

