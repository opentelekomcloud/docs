# How Can I Prevent Untrusted Source IP Addresses from Accessing RDS?<a name="rds_faq_0056"></a>

-   After you enable the remote access function, your EIP DNS and database port may be obtained by malicious personnel. To protect your information including your EIP, DNS, database port, database account, and password, you are advised to set the range of source IP addresses in the RDS security group to ensure that only trusted source IP addresses can access your DB instances.
-   To prevent your database password from being maliciously cracked, set a strong password according to the password strength policies and periodically change it.
-   RDS for MySQL supports defense against brute force cracking. If malicious individuals have obtained your EIP DNS, database port, or database login information and try to crack your database with brute force, your service connections may be delayed. In this case, you can restrict the source connections and change the database username and password to prevent further damage.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >-   RDS for PostgreSQL does not support defense against brute force cracking.  
    >-   For RDS for Microsoft SQL Server, defense against brute force cracking is enabled by default and cannot be disabled.  


