## JSON Message Format

### Description

In a JSON message, you can specify different message content for different subscription protocols, including **Default**, **SMS, HTTP**, **HTTPS**, and **Email**. The message content you specified will be sent to subscription endpoints of applicable protocols.

    {
	     "default": "Dear Sir or Madam, this is a default message.",
	     "email": "Dear Sir or Madam, this is an email message.",
	     "sms": "This is an SMS message.",
	     "http": "{'message':'Dear Sir or Madam, this is an HTTP message.'}",
	     "https": "{'message':'Dear Sir or Madam, this is an HTTPS message.'}"
     }

We recommend that you specify message content general to all subscription types in the default protocol and enter customized content for a specific protocol.

In the following example, you enter shorter message content for the SMS protocol because of the length limit on SMS messages. Therefore, SMS subscribers in the topic receive "This is an SMS message.", and subscribers of other types (email, HTTP, and HTTPS) receive "Dear Sir or Madam, this is a default message."

    {
	     "sms": "This is an SMS message.",
	     "default": "Dear Sir or Madam, this is a default message."
    }

###Constraints

- The content must comply with JSON format requirements.

- You must configure the default protocol in the JSON message.

- The total JSON message cannot exceed 256 KB.

### Calculation on the JSON Message Size

The total size of the JSON message, including the braces, quotation marks, spaces, line breaks, and message content, cannot exceed 256 KB. The size of the JSON message generated for each protocol may vary. The following tells you how to calculate the size of a JSON message.

The message content is "**This is a default message.**"

The protocols you selected include **SMS**, **HTTP**, **HTTPS**, and **Email** (The system automatically adds the default protocol).

In this case, the following JSON message is generated:

    {
	     "default": "This is a default message.",
	     "sms": "This is a default message.",
	     "http": "This is a default message.",
	     "https": "This is a default message.",
	     "email": "This is a default message."
    }

The total size of the message is calculated as follows:

- Three spaces in each of the five protocols: 3 x 5 = 15 bytes

- Four quotation marks in each of the five protocols: 4 x 5 = 20 bytes

- One colon in each of the five protocols: 1 x 5 = 5 bytes

- Message content "This is a default message." for each of the five protocols: 26 x 5 = 130 bytes

- Protocol name **default**: 7 bytes

- Protocol name **sms**: 3 bytes

- Protocol name **http**: 4 bytes

- Protocol name **https**: 5 bytes

- Protocol name **email**: 5 bytes

- Two braces: 2 bytes

- Four commas: 4 bytes

- Six line breaks: 6 bytes

Therefore, the total size of the JSON message is 206 bytes.
