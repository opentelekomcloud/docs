# Message Signature Verification<a name="smn_ug_a9003"></a>

## Scenario<a name="section17809887144332"></a>

To ensure message security, SMN provides signature authentication for HTTP/HTTPS subscription confirmation messages, subscription cancellation messages, and notification messages. After receiving HTTP/HTTPS messages, you need to check them based on the signatures.

## Procedure<a name="section53719410101322"></a>

After receiving an HTTP/HTTPS message, check it with the following procedure:

1.  Verify the key-value pairs \(which vary depending on the message type\) contained in the message signature.
2.  Download the X509 certificate from the certificate URL \(**signing\_cert\_url**\) contained in the message.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >The request to download the certificate is always sent over HTTPS. When downloading a certificate, you need to verify the identity of the certificate server.  

3.  Extract the public key from the X509 certificate for verifying the message reliability and integrity.
4.  Determine which method will be used to verify the signature based on the message type \(the  **type**  field in the message\).
5.  Create signature strings. Obtain the signature parameters from the message and sort them in alphabetical order. Each parameter occupies a line, with its value following in the next line.

## **Signature Strings for Different Message Types**<a name="section39070097101940"></a>

1.  Notification messages
    -   A notification message signature must contain the following parameters \(If the value of  **subject**  is empty, do not include it in the signature\):

        ```
        message
        message_id
        subject
        timestamp
        topic_urn
        type
        ```

    -   For example, the signature information for a notification message is as follows:

        >![](public_sys-resources/icon-note.gif) **NOTE:**   
        >Each parameter occupies a line, with its value following in the next line.  

        ```
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
        ```

2.  Subscription confirmation and subscription cancellation messages
    -   A subscription confirmation or subscription cancellation message signature must contain the following parameters:

        ```
        message
        message_id
        subscribe_url
        timestamp
        topic_urn
        type
        ```

    -   For example, the signature information for a subscription confirmation message is as follows:

        >![](public_sys-resources/icon-note.gif) **NOTE:**   
        >Each parameter occupies a line, with its value following in the next line.  

        ```
        message
        You are invited to subscribe to topic: urn:smn:regionId:d91989905b8449b896f3a4f0ad57222d:demo. To confirm this subscription, Please visit the following SubscribeURL in this message.
        message_id
        def5c309cbff44d5a870787ed937edf8
        subscribe_url
        https://IP address/smn/subscription/confirm?Region ID&Token&Topic URN:demo
        timestamp
        2016-08-15T07:29:16Z
        topic_urn
        urn:smn:regionId:d91989905b8449b896f3a4f0ad57222d:demo
        type
        SubscriptionConfirmation
        ```



