# Naming a Bucket and Object<a name="EN-US_TOPIC_0125560349"></a>

If a request contains a bucket name or an object key, OBS will only begin to process the request after checking that the bucket name or object key conforms to the specified naming rules.

## Bucket Names<a name="section31291646"></a>

A bucket name must conform to the following rules:

-   Contains only lowercase letters, digits, hyphens \(-\), and periods \(.\)
-   Must start with a digit or a letter.
-   Contains 3 to 63 characters.
-   Cannot be an IP address.
-   Cannot end with a hyphen \(-\) or a period \(.\).
-   Cannot contain two consecutive periods \(.\)
-   A period \(.\) cannot precede or follow a hyphen \(-\), for example,  **my-.bucket**  and  **my.-bucket**.

>![](public_sys-resources/icon-notice.gif) **NOTICE:**   
>To avoid SSL certificate verification problems, it is recommended that no period \(.\) is contained in the bucket name when you are accessing the bucket through HTTPS. If the bucket name contains periods \(.\), it is recommended that you access the bucket through the path. For example: https://obs.example.com/bucketname  

## Object Names<a name="section13189358"></a>

An object is named after an object key, which is a sequence of characters whose UTF-8 encoding is at most 1024 bytes long. Each object in a bucket must have a unique object key.

