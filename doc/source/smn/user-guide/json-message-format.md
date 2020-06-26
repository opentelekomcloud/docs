# JSON Message Format<a name="smn_ug_a1000"></a>

## Description<a name="section534667717028"></a>

The JSON format allows you to specify different message content for different subscription protocols, including  **Default**,  **SMS**,  **HTTP**,  **HTTPS**,  **DMS**, and  **Email**. The message content you specify will be sent to subscription endpoints using applicable protocols.

```
{
  "default": "Dear Sir or Madam, this is a default message.",
  "email": "Dear Sir or Madam, this is an email message.",
  "http": "{'message':'Dear Sir or Madam, this is an HTTP message.'}",
  "https": "{'message':'Dear Sir or Madam, this is an HTTPS message.'}",
  "sms": "This is an SMS message."
  
  
  "dms":"Dear Sir or Madam, this is a DMS message."
    }
```

It is recommended that you specify general message content for all subscription types in the default protocol and enter customized content for specific protocols.

In the following example, you enter a shorter message for the SMS protocol because of the length limit on SMS messages. SMS subscribers in the topic receive the message "This is an SMS message.", while other types of subscribers \(email, DMS, HTTP, and HTTPS\) receive "Dear Sir or Madam, this is a default message."

```
{
  "sms": "This is an SMS message.",
  "default": "Dear Sir or Madam, this is a default message."
 }
```

## Constraints<a name="section9710251165825"></a>

-   The content must comply with JSON format requirements.
-   You must configure the default protocol in the JSON message. 
-   The total size of a JSON message cannot exceed 256 KB.

## Calculation on the JSON Message Size<a name="section11977745123756"></a>

The total size of a JSON message, including braces, quotation marks, spaces, line breaks, and message content, cannot exceed 256 KB. The size of the JSON message generated for each protocol may vary.

For example, the message content is "This is a default message.", which contains 26 bytes.

The system automatically adds the default protocol when generating a JSON message.

```
{
  "default": "This is a default message.",
  "protocol1": "This is a default message.",
  "protocol2": "This is a default message.",
  ...
}
```

The total number of protocols is N, including the default protocol and those you selected.

The size of the message is calculated as follows:

-   Three spaces in each of the N protocols: 3 x N = 3N bytes
-   Four quotation marks in each of the N protocols: 4 x N = 4N bytes
-   One colon in each of the N protocols: 1 x N = N bytes
-   Message content "This is a default message." for each of the N protocols: 26 x N = 26N bytes
-   Commas in N – 1 protocols: 1 x \(N – 1\) = N – 1 bytes
-   Line breaks in N + 1 protocols: 1 x \(N + 1\) = N + 1 bytes
-   Two braces: 2 bytes
-   Protocol name  **default**: 7 bytes

Bytes of protocols you selected:

-   Protocol name  **http**: 4 bytes
-   Protocol name  **https**: 5 bytes
-   Protocol name  **email**: 5 bytes
-   Protocol name  **sms**: 3 bytes
-   Protocol name  **dms**: 3 bytes

The total size equals to 36N + 9 + Bytes of selected protocols

For example, you selected the HTTP, HTTPS, and email protocols, the message is as follows:

```
{
  "default": "This is a default message.",
  "email": "This is a default message.",
  "http": "This is a default message.",
  "https": "This is a default message."
}
```

The system adds a default protocol, and therefore the value of N is 4. The size of your JSON messages is:

-   Fixed length: 36 x 4 + 9 + 153 bytes
-   Protocol name  **http**: 4 bytes
-   Protocol name  **https**: 5 bytes
-   Protocol name  **email**: 5 bytes

The total size is 167 \(153 + 4 + 5 + 5\) bytes.

