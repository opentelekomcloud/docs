# Downloading a Certificate File<a name="css_03_0050"></a>

## Function<a name="section162880126447"></a>

This API is used to download the HTTPS certificate file of the server.

## URI<a name="section1928871264412"></a>

```
GET /v1.0/dev/cluster/sslCert
```

## Request<a name="section6319121215446"></a>

None

## Response<a name="section769920722712"></a>

**Table  1**  Parameter description

<a name="table372832271213"></a>
<table><thead align="left"><tr id="row172822201216"><th class="cellrowborder" valign="top" width="15.414141414141417%" id="mcps1.2.4.1.1"><p id="p102799549123"><a name="p102799549123"></a><a name="p102799549123"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="11.797979797979798%" id="mcps1.2.4.1.2"><p id="p1927965418126"><a name="p1927965418126"></a><a name="p1927965418126"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="72.7878787878788%" id="mcps1.2.4.1.3"><p id="p8279254121216"><a name="p8279254121216"></a><a name="p8279254121216"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1728172231215"><td class="cellrowborder" valign="top" width="15.414141414141417%" headers="mcps1.2.4.1.1 "><p id="p656312616454"><a name="p656312616454"></a><a name="p656312616454"></a>certBase64</p>
</td>
<td class="cellrowborder" valign="top" width="11.797979797979798%" headers="mcps1.2.4.1.2 "><p id="p1527915415128"><a name="p1527915415128"></a><a name="p1527915415128"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="72.7878787878788%" headers="mcps1.2.4.1.3 "><p id="p027905411219"><a name="p027905411219"></a><a name="p027905411219"></a>This string is obtained after the certificate file is transcoded using Base64. You need to run the following command to parse the string into a certificate file. The generated certificate file is saved in the folder where the command to be executed is located. In the following command, <strong id="b14404525113511"><a name="b14404525113511"></a><a name="b14404525113511"></a>"$certBase64"</strong> indicates the string returned in the response message. The name of the generated certificate file is <strong id="b1488792415380"><a name="b1488792415380"></a><a name="b1488792415380"></a><span class="filepath" id="filepath1680665763813"><a name="filepath1680665763813"></a><a name="filepath1680665763813"></a><b>CloudSearchService.cert</b></span></strong>. You can specify another name for the certificate file, but must use <span class="filepath" id="filepath198061102394"><a name="filepath198061102394"></a><a name="filepath198061102394"></a><b>.cert</b></span> as the suffix of the name.</p>
<p id="p27325578483"><a name="p27325578483"></a><a name="p27325578483"></a><strong id="b13625121515355"><a name="b13625121515355"></a><a name="b13625121515355"></a>echo -n "$certBase64" | base64 -d &gt;</strong> <strong id="b174300615312"><a name="b174300615312"></a><a name="b174300615312"></a>CloudSearchService.cert</strong></p>
</td>
</tr>
</tbody>
</table>

## Examples<a name="section2082663016185"></a>

Example request

```
GET /v1.0/dev/cluster/sslCert
```

Example response

```
{   "certBase64":"MIIDnTCCAoWgAwIBAgIEXXdMtTANBgkqhkiG9w0BAQsFADB/MRAwDgYDVQQGEwdHZXJtYW55MQ0wCwYDVQQIEwROb25lMQ0wCwYDVQQHEwROb25lMRkwFwYDVQQKExBPcGVuVGVsZWtvbUNsb3VkMRUwEwYDVQQLEwxEYXRhQW5hbHlzaXMxGzAZBgNVBAMTEkNsb3VkU2VhcmNoU2VydmljZTAeFw0xODExMTcxODE4NDJaFw0xOTAyMTUxODE4NDJaMH8xEDAOBgNVBAYTB0dlcm1hbnkxDTALBgNVBAgTBE5vbmUxDTALBgNVBAcTBE5vbmUxGTAXBgNVBAoTEE9wZW5UZWxla29tQ2xvdWQxFTATBgNVBAsTDERhdGFBbmFseXNpczEbMBkGA1UEAxMSQ2xvdWRTZWFyY2hTZXJ2aWNlMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEApHai9+LMoFSlWqI+YodGiFLw597Vuoo7gG3qTCs+szQTn3PTZtbnzy7TNWjn8K41mkBgUY16wtkhH1nu6AmhRLpZA+2fwAz34v/tDOYahPq045bk9S/znJXQeWWeux93I15z7OP/XC68IF2AKl2NXjmm9bAD/DsqaLuJpoE77d71862sD6uRCBQYyZoQaHw+eKuL8/+5PjWvG9mS+Rxp0DcLd1waFkyK4BjB5Ae3og4bAivKo7vQHH79fgnuK0SQnNpxlU8xLIGaKsQ0/yeJrTrlfy3vBQmj949SbCzFjvmXgkbv4I0jcT5Ax1P68tlasUUnCqFTjGTbzeT82CeE6QIDAQABoyEwHzAdBgNVHQ4EFgQUPPZLu9ElUzQgKURRwn8HpzIliEcwDQYJKoZIhvcNAQELBQADggEBAI/e/sGbZ1jB3ao7Car2p7rm1Pg8ro1kSy9o+Jug6XjJpkwITKGkhPYugtGuKgL6oiYkdJhqmfrm/1R7phf1qzBgRoWtR7eCBg4uorNaYvTelAjbIoYGL03D1c5K6e1XwRsdqNWT3TwiHZ5CuiVOsjAtvt3OrvF2YtPUOJpbbvdXlnLKaLHoaklcyyMJ+KmUbkd2XFhzlhwj4eOaloL8XQcAk/urYFFNTymJPnNiEXjLAgGCfE/j8rX26WKvPUGmcuuqBiK7Ob+VfnfpnssDQoBtQsN9eUNxkYkg6eua8U6zR3nSPxXpdn+TZo3HHnUp3x0f1Xev49MHKe/aPMJOTYE="
}
```

After obtaining the preceding character string, run the following command to obtain the  **CloudSearchService.cert**  certificate file:

```
echo -n "MIIDnTCCAoWgAwIBAgIEXXdMtTANBgkqhkiG9w0BAQsFADB/MRAwDgYDVQQGEwdHZXJtYW55MQ0wCwYDVQQIEwROb25lMQ0wCwYDVQQHEwROb25lMRkwFwYDVQQKExBPcGVuVGVsZWtvbUNsb3VkMRUwEwYDVQQLEwxEYXRhQW5hbHlzaXMxGzAZBgNVBAMTEkNsb3VkU2VhcmNoU2VydmljZTAeFw0xODExMTcxODE4NDJaFw0xOTAyMTUxODE4NDJaMH8xEDAOBgNVBAYTB0dlcm1hbnkxDTALBgNVBAgTBE5vbmUxDTALBgNVBAcTBE5vbmUxGTAXBgNVBAoTEE9wZW5UZWxla29tQ2xvdWQxFTATBgNVBAsTDERhdGFBbmFseXNpczEbMBkGA1UEAxMSQ2xvdWRTZWFyY2hTZXJ2aWNlMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEApHai9+LMoFSlWqI+YodGiFLw597Vuoo7gG3qTCs+szQTn3PTZtbnzy7TNWjn8K41mkBgUY16wtkhH1nu6AmhRLpZA+2fwAz34v/tDOYahPq045bk9S/znJXQeWWeux93I15z7OP/XC68IF2AKl2NXjmm9bAD/DsqaLuJpoE77d71862sD6uRCBQYyZoQaHw+eKuL8/+5PjWvG9mS+Rxp0DcLd1waFkyK4BjB5Ae3og4bAivKo7vQHH79fgnuK0SQnNpxlU8xLIGaKsQ0/yeJrTrlfy3vBQmj949SbCzFjvmXgkbv4I0jcT5Ax1P68tlasUUnCqFTjGTbzeT82CeE6QIDAQABoyEwHzAdBgNVHQ4EFgQUPPZLu9ElUzQgKURRwn8HpzIliEcwDQYJKoZIhvcNAQELBQADggEBAI/e/sGbZ1jB3ao7Car2p7rm1Pg8ro1kSy9o+Jug6XjJpkwITKGkhPYugtGuKgL6oiYkdJhqmfrm/1R7phf1qzBgRoWtR7eCBg4uorNaYvTelAjbIoYGL03D1c5K6e1XwRsdqNWT3TwiHZ5CuiVOsjAtvt3OrvF2YtPUOJpbbvdXlnLKaLHoaklcyyMJ+KmUbkd2XFhzlhwj4eOaloL8XQcAk/urYFFNTymJPnNiEXjLAgGCfE/j8rX26WKvPUGmcuuqBiK7Ob+VfnfpnssDQoBtQsN9eUNxkYkg6eua8U6zR3nSPxXpdn+TZo3HHnUp3x0f1Xev49MHKe/aPMJOTYE=" | base64 -d > CloudSearchService.cert
```

## Status Code<a name="section15133145417185"></a>

**Table  2**  Status code

<a name="table12321369178"></a>
<table><thead align="left"><tr id="css_03_0018_row1972183521418"><th class="cellrowborder" valign="top" width="15.939999999999998%" id="mcps1.2.4.1.1"><p id="css_03_0018_p14560134151414"><a name="css_03_0018_p14560134151414"></a><a name="css_03_0018_p14560134151414"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="31.04%" id="mcps1.2.4.1.2"><p id="css_03_0018_p5563194141411"><a name="css_03_0018_p5563194141411"></a><a name="css_03_0018_p5563194141411"></a>Code</p>
</th>
<th class="cellrowborder" valign="top" width="53.02%" id="mcps1.2.4.1.3"><p id="css_03_0018_p256616411143"><a name="css_03_0018_p256616411143"></a><a name="css_03_0018_p256616411143"></a>Status Code Description</p>
</th>
</tr>
</thead>
<tbody><tr id="css_03_0018_row129720356144"><td class="cellrowborder" valign="top" width="15.939999999999998%" headers="mcps1.2.4.1.1 "><p id="css_03_0018_p1957004131410"><a name="css_03_0018_p1957004131410"></a><a name="css_03_0018_p1957004131410"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="31.04%" headers="mcps1.2.4.1.2 "><p id="css_03_0018_p165731141171419"><a name="css_03_0018_p165731141171419"></a><a name="css_03_0018_p165731141171419"></a>BadRequest</p>
</td>
<td class="cellrowborder" valign="top" width="53.02%" headers="mcps1.2.4.1.3 "><p id="css_03_0018_p65778413148"><a name="css_03_0018_p65778413148"></a><a name="css_03_0018_p65778413148"></a>Invalid request.</p>
<p id="css_03_0018_p1557974171415"><a name="css_03_0018_p1557974171415"></a><a name="css_03_0018_p1557974171415"></a>The client should not repeat the request without modifications.</p>
</td>
</tr>
<tr id="css_03_0018_row8972103517147"><td class="cellrowborder" valign="top" width="15.939999999999998%" headers="mcps1.2.4.1.1 "><p id="css_03_0018_p75841441191410"><a name="css_03_0018_p75841441191410"></a><a name="css_03_0018_p75841441191410"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="31.04%" headers="mcps1.2.4.1.2 "><p id="css_03_0018_p258716416142"><a name="css_03_0018_p258716416142"></a><a name="css_03_0018_p258716416142"></a>NotFound</p>
</td>
<td class="cellrowborder" valign="top" width="53.02%" headers="mcps1.2.4.1.3 "><p id="css_03_0018_p15589154118141"><a name="css_03_0018_p15589154118141"></a><a name="css_03_0018_p15589154118141"></a>The requested resource cannot be found.</p>
<p id="css_03_0018_p14590164151410"><a name="css_03_0018_p14590164151410"></a><a name="css_03_0018_p14590164151410"></a>The client should not repeat the request without modifications.</p>
</td>
</tr>
<tr id="css_03_0018_row297223511416"><td class="cellrowborder" valign="top" width="15.939999999999998%" headers="mcps1.2.4.1.1 "><p id="css_03_0018_p13595164131416"><a name="css_03_0018_p13595164131416"></a><a name="css_03_0018_p13595164131416"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="31.04%" headers="mcps1.2.4.1.2 "><p id="css_03_0018_p9598741131416"><a name="css_03_0018_p9598741131416"></a><a name="css_03_0018_p9598741131416"></a>OK</p>
</td>
<td class="cellrowborder" valign="top" width="53.02%" headers="mcps1.2.4.1.3 "><p id="css_03_0018_p659994115146"><a name="css_03_0018_p659994115146"></a><a name="css_03_0018_p659994115146"></a>The request is processed successfully.</p>
</td>
</tr>
</tbody>
</table>

