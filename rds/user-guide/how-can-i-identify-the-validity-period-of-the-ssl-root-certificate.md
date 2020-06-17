# How Can I Identify the Validity Period of the SSL Root Certificate?<a name="rds_faq_0051"></a>

When you connect to an RDS MySQL DB instance using an SSL connection, run the following command to check whether the certificate has expired:

```
show status like '%ssl_server%';
```

Update the root certificate to the latest version before it expires:

1.  Download the new certificate or certificate bundle.
2.  Reboot the DB instance for the new certificate to take effect.
3.  Connect to the DB instance using the new certificate or certificate bundle.

    >![](/images/icon-note.gif) **NOTE:**   
    >Replace the certificate to be expired with an officially issued certificate to improve system security.  


