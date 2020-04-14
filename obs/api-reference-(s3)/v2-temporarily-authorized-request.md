# V2 Temporarily Authorized Request<a name="EN-US_TOPIC_0125560431"></a>

Requests for temporarily authorized operations are authenticated using the query-string parameters instead of the  **authorization**  header.

In OBS, a registered and activated user can use its account to create a URL that contains authentication information. In addition, any user that obtains the URL can perform the operation specified by the URL.

For example, during temporarily authorized Get Object request, a specific URL is created and any user obtaining this URL can get the specified object before the expired time.

```
GET /ObjectKey?AWSAccessKeyId=AccessKeyID&Expires=ExpiresValue&Signature=signature HTTP/ 1.1
Host: bucketname.obs.example.com
```

The required authentication elements are specified as query string parameters detailed in  [Table 1](#table38455150).

**Table  1**  Request parameters

<a name="table38455150"></a>
<table><tbody><tr id="row39330387"><td class="cellrowborder" valign="top" width="23.18%"><p id="p31644779"><a name="p31644779"></a><a name="p31644779"></a>Parameter</p>
</td>
<td class="cellrowborder" valign="top" width="56.830000000000005%"><p id="p13090320"><a name="p13090320"></a><a name="p13090320"></a>Description</p>
</td>
<td class="cellrowborder" valign="top" width="19.99%"><p id="p53682985"><a name="p53682985"></a><a name="p53682985"></a>Remarks</p>
</td>
</tr>
<tr id="row13384821"><td class="cellrowborder" valign="top" width="23.18%"><p id="p10428696"><a name="p10428696"></a><a name="p10428696"></a>AWSAccessKeyId</p>
</td>
<td class="cellrowborder" valign="top" width="56.830000000000005%"><p id="p39418019"><a name="p39418019"></a><a name="p39418019"></a>Indicates the AK of the permission grantor.</p>
<p id="p19217855"><a name="p19217855"></a><a name="p19217855"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="19.99%"><p id="p13142459"><a name="p13142459"></a><a name="p13142459"></a>Mandatory</p>
</td>
</tr>
<tr id="row51173267"><td class="cellrowborder" valign="top" width="23.18%"><p id="p51393992"><a name="p51393992"></a><a name="p51393992"></a>Expires</p>
</td>
<td class="cellrowborder" valign="top" width="56.830000000000005%"><p id="p2163846"><a name="p2163846"></a><a name="p2163846"></a>Indicates the time (expressed in seconds) when the temporarily authorized URL expires. The time must be in Coordinated Universal Time (UTC) format and later than 00:00:00 on January 1, 1970.</p>
<p id="p19474615"><a name="p19474615"></a><a name="p19474615"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="19.99%"><p id="p33939988"><a name="p33939988"></a><a name="p33939988"></a>Mandatory</p>
</td>
</tr>
<tr id="row37024442"><td class="cellrowborder" valign="top" width="23.18%"><p id="p46189825"><a name="p46189825"></a><a name="p46189825"></a>Signature</p>
</td>
<td class="cellrowborder" valign="top" width="56.830000000000005%"><p id="p50388336"><a name="p50388336"></a><a name="p50388336"></a>Indicates the signature generated using the SK and parameter <strong id="b50841847"><a name="b50841847"></a><a name="b50841847"></a>Expires</strong>.</p>
<p id="p54923440"><a name="p54923440"></a><a name="p54923440"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="19.99%"><p id="p19613673"><a name="p19613673"></a><a name="p19613673"></a>Mandatory</p>
</td>
</tr>
</tbody>
</table>

The query-string authentication differs from the authorization header authentication in the following aspects:

-   The signature is both Base64 and URL encoded.
-   **Expires** in **StringToSign** corresponds to **Date**  in authorization information.

```
StringToSign = HTTP-Verb + "\n" + Content-MD5 + "\n" + Content-Type + "\n" + Expire + "\n" + CanonicalizedOBSHeaders + CanonicalizedResource.

 Signature = URL-Encode(Base64( HMAC-SHA1( UTF-8-Encoding-Of(YourSecretAccessKeyID, StringToSign ) ) )).
```

