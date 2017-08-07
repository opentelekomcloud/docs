## Message Signature Verification

### Scenarios

To ensure message security, SMN provides signature authentication for HTTP/HTTPS subscription confirmation messages, unsubscription confirmation messages, and notification messages. Specifically, SMN checks the HTTPS/HTTPS messages by their signatures.

### Procedure

After you receive an HTTP/HTTPS message, the system verifies the message in the following procedure:

<ul><li>Verify the key field values (vary depending on the message type) contained in the message signature.</li>

<li>Download the X509 certificate based on the certificate URL (<b>signing\_cert\_url</b>) contained in the message.
<dd><img src="figure/note.png"/>
The certificate downloading URL uses HTTPS and is verified when accessed.</dd></li>
<li>Extract the public key from the X509 certificate for verifying the message reliability and integrity.</li>
<li>Determine the method to verify the certificate signature based on the message type (<b>type</b> in the message).</li>
<li>Create signature strings. Obtain the signature parameters from the message and sort them in the alphabet sequence. Each parameter occupies a line, with its value following in the next line.</li>

### Signature Strings for Specified Message Types

1.  Notification messages

	A notification message signature must contain the following parameters (If the value of **subject** is empty, do not include it in the signature):

        message
    	message_id
    	subject
    	timestamp
    	topic_urn
    	type

	For example, the signature information of a notification message is as follows:

	    message
	    My test message
	    message_id
	    88c726942175432bac921eafd0036163
	    subject
	    demo
	    timestamp
	    2016-08-15T07:29:16Z
	    topic_urn
	    urn:smn:regionId:74dc9e44d0cc4573adfce91cdfdd3ba9:xxxx
	    type
	    Notification

1.  Subscription confirmation and unsubscription confirmation messages

	A subscription confirmation or unsubscription confirmation message signature must contain the following parameters:

		message
		message\_id
		subscribe\_url
		timestamp
		topic\_urn
		type

	For example, the signature information of a subscription confirmation message is as follows:

	    message
	    You are invited to subscribe to topic: urn:smn:regionId:d91989905b8449b896f3a4f0ad57222d:demo. To confirm this subscription, Please visit the following SubscribeURL in this message.
	    message\_id
	    def5c309cbff44d5a870787ed937edf8
	    subscribe\_url
	    https://*IP address*/smn/subscription/confirm?*Region ID*&*Token*&*Topic URN*:demo
	    timestamp
	    2016-08-15T07:29:16Z
	    topic\_urn
	    urn:smn:regionId:d91989905b8449b896f3a4f0ad57222d:demo
	    type
	    SubscriptionConfirmation
