# Why Is the Email Address Format Changed in the SOA Record?<a name="dns_faq_009"></a>

The email address you entered when creating a zone is used to receive error or problem reports about the zone. You can specify an email address you frequently use as the zone administrator's mailbox. However, according to RFC 2142, we strongly recommend you to preferentially use **HOSTMASTER@***Domain name* as the email address.

After the zone is created, the email you specified is displayed in the SOA record set of the zone. You must note that the "@" sign in the SOA record set has other meanings. Therefore, the system replaces @ in the email address with a dot \(.\). If there is already a dot before @, the system replaces the dot with a backslash \(\\\). However, emails are still sent to the email address you specified. For more details, see RFC 1035.

Take **test.hostmaster@example.com** as an example.

If you have specified **test.hostmaster@example.com** when creating the zone, the email address displayed in the SOA record set is **test\\.hostmaster.example.com**.

