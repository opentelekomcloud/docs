# What Are the Limitations on SMS Messages?<a name="smn_faq_0009"></a>

If the content of an SMS message consists of only ASCII characters, it will be encoded using GSM. In this case, each SMS message can contain up to 254 characters.

If the content includes non-ASCII characters, it will be encoded using UCS-2, and each SMS message can contain up to 127 characters.

If an SMS message is oversized, SMN will split it into multiple parts but only send the first two parts to subscribers.

