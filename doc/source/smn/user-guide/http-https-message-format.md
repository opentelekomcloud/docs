# HTTP/HTTPS Message Format<a name="smn_ug_a9002"></a>

## Scenario<a name="section32651219144241"></a>

This section describes the format of messages sent to HTTP or HTTPS endpoints. You can identify messages based on message types in the headers. HTTP/HTTPS message types include: subscription confirmation messages, notification messages, and subscription cancellation messages.

The header of an SMN HTTP/HTTPS message contains the following parameters:  **X-SMN-TOPIC-URN**,  **X-SMN-MESSAGE-ID**,  **X-SMN-MESSAGE-TYPE**, and  **X-SMN-SUBSCRIPTION-URN**.

**Table  1**  HTTP/HTTPS header parameters

<a name="table59304739144241"></a>
<table><thead align="left"><tr id="row30468244144241"><th class="cellrowborder" valign="top" width="45.15%" id="mcps1.2.3.1.1"><p id="p52008685144241"><a name="p52008685144241"></a><a name="p52008685144241"></a><strong id="b17331199153917"><a name="b17331199153917"></a><a name="b17331199153917"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="54.85%" id="mcps1.2.3.1.2"><p id="p51953955144241"><a name="p51953955144241"></a><a name="p51953955144241"></a><strong id="b61649860153917"><a name="b61649860153917"></a><a name="b61649860153917"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row47520797144241"><td class="cellrowborder" valign="top" width="45.15%" headers="mcps1.2.3.1.1 "><p id="p23979331144241"><a name="p23979331144241"></a><a name="p23979331144241"></a>X-SMN-MESSAGE-TYPE</p>
</td>
<td class="cellrowborder" valign="top" width="54.85%" headers="mcps1.2.3.1.2 "><p id="p63277695144241"><a name="p63277695144241"></a><a name="p63277695144241"></a>Indicates the message type, which can be:</p>
<a name="ul32628343144241"></a><a name="ul32628343144241"></a><ul id="ul32628343144241"><li>SubscriptionConfirmation</li><li>Notification</li><li>UnsubscribeConfirmation</li></ul>
</td>
</tr>
<tr id="row64396778144241"><td class="cellrowborder" valign="top" width="45.15%" headers="mcps1.2.3.1.1 "><p id="p48756504144241"><a name="p48756504144241"></a><a name="p48756504144241"></a>X-SMN-MESSAGE-ID</p>
</td>
<td class="cellrowborder" valign="top" width="54.85%" headers="mcps1.2.3.1.2 "><p id="p56962718144241"><a name="p56962718144241"></a><a name="p56962718144241"></a>Indicates the unique message ID.</p>
</td>
</tr>
<tr id="row42902418144241"><td class="cellrowborder" valign="top" width="45.15%" headers="mcps1.2.3.1.1 "><p id="p52543824144241"><a name="p52543824144241"></a><a name="p52543824144241"></a>X-SMN-TOPIC-URN</p>
</td>
<td class="cellrowborder" valign="top" width="54.85%" headers="mcps1.2.3.1.2 "><p id="p28191355144241"><a name="p28191355144241"></a><a name="p28191355144241"></a>Indicates the URN of the topic to which the message belongs.</p>
</td>
</tr>
<tr id="row52395604144241"><td class="cellrowborder" valign="top" width="45.15%" headers="mcps1.2.3.1.1 "><p id="p16185549144241"><a name="p16185549144241"></a><a name="p16185549144241"></a>X-SMN-SUBSCRIPTION-URN</p>
</td>
<td class="cellrowborder" valign="top" width="54.85%" headers="mcps1.2.3.1.2 "><p id="p35961062144241"><a name="p35961062144241"></a><a name="p35961062144241"></a>Identifies the subscription endpoint.</p>
</td>
</tr>
</tbody>
</table>

## HTTP/HTTPS Subscription Confirmation Message Format<a name="section55214102144241"></a>

After you add an HTTP/HTTPS endpoint, SMN sends a subscription confirmation message to the subscriber. The message body is composed of JSON character strings. The subscriber must obtain the subscription URL \(**subscribe\_url**\) to confirm the subscription.  [Table 2](#table52870937144241)  describes the JSON strings in detail.

**Table  2**  HTTP/HTTPS subscription confirmation message body

<a name="table52870937144241"></a>
<table><thead align="left"><tr id="row40646338144241"><th class="cellrowborder" valign="top" width="30.3%" id="mcps1.2.3.1.1"><p id="p4019045144241"><a name="p4019045144241"></a><a name="p4019045144241"></a><strong id="b982317815399"><a name="b982317815399"></a><a name="b982317815399"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="69.69999999999999%" id="mcps1.2.3.1.2"><p id="p57107266144241"><a name="p57107266144241"></a><a name="p57107266144241"></a><strong id="b5747991715399"><a name="b5747991715399"></a><a name="b5747991715399"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row62285823144241"><td class="cellrowborder" valign="top" width="30.3%" headers="mcps1.2.3.1.1 "><p id="p11986884144241"><a name="p11986884144241"></a><a name="p11986884144241"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="69.69999999999999%" headers="mcps1.2.3.1.2 "><p id="p31413562144241"><a name="p31413562144241"></a><a name="p31413562144241"></a>Indicates the message type, the value of which is <strong id="b842352706153316"><a name="b842352706153316"></a><a name="b842352706153316"></a>SubscriptionConfirmation</strong>.</p>
</td>
</tr>
<tr id="row1552519559188"><td class="cellrowborder" valign="top" width="30.3%" headers="mcps1.2.3.1.1 "><p id="p40184032144241"><a name="p40184032144241"></a><a name="p40184032144241"></a>signature</p>
</td>
<td class="cellrowborder" valign="top" width="69.69999999999999%" headers="mcps1.2.3.1.2 "><p id="p33681196144241"><a name="p33681196144241"></a><a name="p33681196144241"></a>Indicates the signature information.</p>
<p id="p34695308144241"><a name="p34695308144241"></a><a name="p34695308144241"></a>The signature includes the <strong id="b842352706154239"><a name="b842352706154239"></a><a name="b842352706154239"></a>message</strong>, <strong id="b842352706154245"><a name="b842352706154245"></a><a name="b842352706154245"></a>message_id</strong>, <strong id="b842352706154252"><a name="b842352706154252"></a><a name="b842352706154252"></a>subscribe_url</strong>, <strong id="b842352706154258"><a name="b842352706154258"></a><a name="b842352706154258"></a>timestamp</strong>, <strong id="b84235270615438"><a name="b84235270615438"></a><a name="b84235270615438"></a>topic_urn</strong>, and <strong id="b842352706154321"><a name="b842352706154321"></a><a name="b842352706154321"></a>type</strong> fields. For details about signature verification, see <a href="message-signature-verification.md">Message Signature Verification</a>.</p>
</td>
</tr>
<tr id="row152615551813"><td class="cellrowborder" valign="top" width="30.3%" headers="mcps1.2.3.1.1 "><p id="p6643351144241"><a name="p6643351144241"></a><a name="p6643351144241"></a>topic_urn</p>
</td>
<td class="cellrowborder" valign="top" width="69.69999999999999%" headers="mcps1.2.3.1.2 "><p id="p1240535144241"><a name="p1240535144241"></a><a name="p1240535144241"></a>Indicates the URN of the topic to which the message belongs.</p>
</td>
</tr>
<tr id="row2526555141811"><td class="cellrowborder" valign="top" width="30.3%" headers="mcps1.2.3.1.1 "><p id="p31935228144241"><a name="p31935228144241"></a><a name="p31935228144241"></a>message_id</p>
</td>
<td class="cellrowborder" valign="top" width="69.69999999999999%" headers="mcps1.2.3.1.2 "><p id="p36616689144241"><a name="p36616689144241"></a><a name="p36616689144241"></a>Indicates the unique message ID.</p>
</td>
</tr>
<tr id="row852765513189"><td class="cellrowborder" valign="top" width="30.3%" headers="mcps1.2.3.1.1 "><p id="p59947295144241"><a name="p59947295144241"></a><a name="p59947295144241"></a>signature_version</p>
</td>
<td class="cellrowborder" valign="top" width="69.69999999999999%" headers="mcps1.2.3.1.2 "><p id="p23892760144241"><a name="p23892760144241"></a><a name="p23892760144241"></a>Indicates the signature version, which is currently <strong id="b842352706154631"><a name="b842352706154631"></a><a name="b842352706154631"></a>V1</strong>.</p>
</td>
</tr>
<tr id="row165271255201813"><td class="cellrowborder" valign="top" width="30.3%" headers="mcps1.2.3.1.1 "><p id="p51347502144241"><a name="p51347502144241"></a><a name="p51347502144241"></a>message</p>
</td>
<td class="cellrowborder" valign="top" width="69.69999999999999%" headers="mcps1.2.3.1.2 "><p id="p65506977144241"><a name="p65506977144241"></a><a name="p65506977144241"></a>Indicates the message content.</p>
</td>
</tr>
<tr id="row1528195511811"><td class="cellrowborder" valign="top" width="30.3%" headers="mcps1.2.3.1.1 "><p id="p16364496144241"><a name="p16364496144241"></a><a name="p16364496144241"></a>subscribe_url</p>
</td>
<td class="cellrowborder" valign="top" width="69.69999999999999%" headers="mcps1.2.3.1.2 "><p id="p50455831144241"><a name="p50455831144241"></a><a name="p50455831144241"></a>Indicates the URL to be accessed for subscription confirmation.</p>
</td>
</tr>
<tr id="row1552865521811"><td class="cellrowborder" valign="top" width="30.3%" headers="mcps1.2.3.1.1 "><p id="p36626675144241"><a name="p36626675144241"></a><a name="p36626675144241"></a>signing_cert_url</p>
</td>
<td class="cellrowborder" valign="top" width="69.69999999999999%" headers="mcps1.2.3.1.2 "><p id="p13970698144241"><a name="p13970698144241"></a><a name="p13970698144241"></a>Indicates the certificate URL for generating the message signature.</p>
</td>
</tr>
<tr id="row14529105511188"><td class="cellrowborder" valign="top" width="30.3%" headers="mcps1.2.3.1.1 "><p id="p51200664144241"><a name="p51200664144241"></a><a name="p51200664144241"></a>timestamp</p>
</td>
<td class="cellrowborder" valign="top" width="69.69999999999999%" headers="mcps1.2.3.1.2 "><p id="p53613095144241"><a name="p53613095144241"></a><a name="p53613095144241"></a>Indicates the time stamp when the message was initially sent.</p>
</td>
</tr>
</tbody>
</table>

The following is an example HTTP/HTTPS subscription confirmation message:

```
{
    "signature": "ViE96uGbBkl+S8eWqgebi5KdmRht2U8+Rs88yuyMHq1k4h3jUkcDZ6HCqTqdpJ8nrLcdqETyyEiOQyTszJdU05z+LhfE8jerCCdSbL4zeInVkydHh0kcCRWmORye0/EuQ/gLC1UIXwvUsqbUCPnBRhNFXOeXMOPPCzK+d04xjy4QHd1H/bHxgsY3AlTe0gCFT068Zru7OK6w9aQaY44mXnN3OWGmBmoHyFab5TRXLSQNz/9u/Vj646cQMMaI0PPQ30QzGYD0MtzgDZi12m8jMTHAnMkTEcbLaEgaqmaoEnATSpEcspFKNXv2skwk7rsVakMOISpMH3+qC6RzhETA2A==",
    "topic_urn": "urn:smn:region01:0553db98c800d5192f9bc01232b89622:vpc_status_report_topic",
    "message_id": "d86c201092574e71a3ca85826652c58b",
    "signature_version": "v1",
    "type": "SubscriptionConfirmation",
    "message": "{\"enterpriseProjectId\": \"0\", \"eventTime\": \"2019-08-12 22:40:55.040632\", \"chargingMode\": \"postPaid\", \"cloudserviceType\": \"hws.service.type.bandwidth\", \"eventType\": 1, \"regionId\": \"region01\", \"tenantId\": \"057eefe55400d2742f8cc0017870ceef\", \"resourceType\": \"hws.resource.type.bandwidth\", \"resourceSpecCode\": \"19_bgp\", \"resourceSize\": 10, \"resourceId\": \"e091f1b1-08ef-4e2b-a27e-f85e4c19026a\", \"resouceSizeMeasureId\": 15, \"resourceName\": \"elbauto_2019_08_13_06_40_46\"}",
    "subscribe_url": "https://console.xxx.com/smn/subscription/unsubscribe?subscription_urn=urn:smn:region01:0553db98c800d5192f9bc01232b89622:vpc_status_report_topic:653e212a43884f7188ca656c537e31ce",
    "signing_cert_url": "https://console.xxx.com/smn/SMN_region01_b3974c411807498bb532b3cd6cd65d91.pem",
    "timestamp": "2019-08-12T22:40:56Z"
}
```

## HTTP/HTTPS Notification Message Format<a name="section12755810144241"></a>

After an HTTP/HTTPS subscriber confirms the subscription, the subscriber can receive notification messages published to the topic. The notification message body is composed of JSON character strings, which are described in  [Table 3](#table37962339144241).

**Table  3**  HTTP/HTTPS notification message body

<a name="table37962339144241"></a>
<table><thead align="left"><tr id="row7026846144241"><th class="cellrowborder" valign="top" width="30.3%" id="mcps1.2.3.1.1"><p id="p32303664144241"><a name="p32303664144241"></a><a name="p32303664144241"></a><strong id="b1201045415393"><a name="b1201045415393"></a><a name="b1201045415393"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="69.69999999999999%" id="mcps1.2.3.1.2"><p id="p66460015144241"><a name="p66460015144241"></a><a name="p66460015144241"></a><strong id="b5747991715399_1"><a name="b5747991715399_1"></a><a name="b5747991715399_1"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row14552130144241"><td class="cellrowborder" valign="top" width="30.3%" headers="mcps1.2.3.1.1 "><p id="p37871890144241"><a name="p37871890144241"></a><a name="p37871890144241"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="69.69999999999999%" headers="mcps1.2.3.1.2 "><p id="p47724230144241"><a name="p47724230144241"></a><a name="p47724230144241"></a>Indicates the message type, the value of which is <strong id="b842352706153316_1"><a name="b842352706153316_1"></a><a name="b842352706153316_1"></a>Notification</strong>.</p>
</td>
</tr>
<tr id="row7564121282219"><td class="cellrowborder" valign="top" width="30.3%" headers="mcps1.2.3.1.1 "><p id="p6714630144241"><a name="p6714630144241"></a><a name="p6714630144241"></a>signature</p>
</td>
<td class="cellrowborder" valign="top" width="69.69999999999999%" headers="mcps1.2.3.1.2 "><p id="p7014129144241"><a name="p7014129144241"></a><a name="p7014129144241"></a>Indicates the signature information.</p>
<p id="p63127165144241"><a name="p63127165144241"></a><a name="p63127165144241"></a>The signature includes the <strong id="b208337332916012"><a name="b208337332916012"></a><a name="b208337332916012"></a>message</strong>, <strong id="b114633180716012"><a name="b114633180716012"></a><a name="b114633180716012"></a>message_id</strong>, <strong id="b90995432916012"><a name="b90995432916012"></a><a name="b90995432916012"></a>subject</strong>, <strong id="b191541930216012"><a name="b191541930216012"></a><a name="b191541930216012"></a>timestamp</strong>, <strong id="b147985341616012"><a name="b147985341616012"></a><a name="b147985341616012"></a>topic_urn</strong>, and <strong id="b184080830316012"><a name="b184080830316012"></a><a name="b184080830316012"></a>type</strong> fields. If the <strong id="b8423527061631"><a name="b8423527061631"></a><a name="b8423527061631"></a>subject</strong> field is empty, the signature is not verified. For details about signature verification, see <a href="message-signature-verification.md">Message Signature Verification</a>.</p>
</td>
</tr>
<tr id="row358016462275"><td class="cellrowborder" valign="top" width="30.3%" headers="mcps1.2.3.1.1 "><p id="p9739111242810"><a name="p9739111242810"></a><a name="p9739111242810"></a>subject</p>
</td>
<td class="cellrowborder" valign="top" width="69.69999999999999%" headers="mcps1.2.3.1.2 "><p id="p16739912122814"><a name="p16739912122814"></a><a name="p16739912122814"></a>Message subject</p>
</td>
</tr>
<tr id="row1514019818214"><td class="cellrowborder" valign="top" width="30.3%" headers="mcps1.2.3.1.1 "><p id="p28572415144241"><a name="p28572415144241"></a><a name="p28572415144241"></a>topic_urn</p>
</td>
<td class="cellrowborder" valign="top" width="69.69999999999999%" headers="mcps1.2.3.1.2 "><p id="p32664285144241"><a name="p32664285144241"></a><a name="p32664285144241"></a>Indicates the URN of the topic to which the message belongs.</p>
</td>
</tr>
<tr id="row14140982214"><td class="cellrowborder" valign="top" width="30.3%" headers="mcps1.2.3.1.1 "><p id="p55726628144241"><a name="p55726628144241"></a><a name="p55726628144241"></a>message_id</p>
</td>
<td class="cellrowborder" valign="top" width="69.69999999999999%" headers="mcps1.2.3.1.2 "><p id="p17562982144241"><a name="p17562982144241"></a><a name="p17562982144241"></a>Indicates the unique message ID.</p>
</td>
</tr>
<tr id="row01402818219"><td class="cellrowborder" valign="top" width="30.3%" headers="mcps1.2.3.1.1 "><p id="p50132129144241"><a name="p50132129144241"></a><a name="p50132129144241"></a>signature_version</p>
</td>
<td class="cellrowborder" valign="top" width="69.69999999999999%" headers="mcps1.2.3.1.2 "><p id="p34170678144241"><a name="p34170678144241"></a><a name="p34170678144241"></a>Indicates the signature version, which is currently <strong id="b28527649185211"><a name="b28527649185211"></a><a name="b28527649185211"></a>V1</strong>.</p>
</td>
</tr>
<tr id="row101401581219"><td class="cellrowborder" valign="top" width="30.3%" headers="mcps1.2.3.1.1 "><p id="p52730220144241"><a name="p52730220144241"></a><a name="p52730220144241"></a>message</p>
</td>
<td class="cellrowborder" valign="top" width="69.69999999999999%" headers="mcps1.2.3.1.2 "><p id="p43289437144241"><a name="p43289437144241"></a><a name="p43289437144241"></a>Indicates the message content.</p>
</td>
</tr>
<tr id="row18141148112119"><td class="cellrowborder" valign="top" width="30.3%" headers="mcps1.2.3.1.1 "><p id="p16833870144241"><a name="p16833870144241"></a><a name="p16833870144241"></a>unsubscribe_url</p>
</td>
<td class="cellrowborder" valign="top" width="69.69999999999999%" headers="mcps1.2.3.1.2 "><p id="p21366215144241"><a name="p21366215144241"></a><a name="p21366215144241"></a>Indicates the URL for canceling a subscription.</p>
</td>
</tr>
<tr id="row121410822111"><td class="cellrowborder" valign="top" width="30.3%" headers="mcps1.2.3.1.1 "><p id="p13036277144241"><a name="p13036277144241"></a><a name="p13036277144241"></a>signing_cert_url</p>
</td>
<td class="cellrowborder" valign="top" width="69.69999999999999%" headers="mcps1.2.3.1.2 "><p id="p49305522144241"><a name="p49305522144241"></a><a name="p49305522144241"></a>Indicates the certificate URL for generating the message signature.</p>
</td>
</tr>
<tr id="row1114128192119"><td class="cellrowborder" valign="top" width="30.3%" headers="mcps1.2.3.1.1 "><p id="p40483823144241"><a name="p40483823144241"></a><a name="p40483823144241"></a>timestamp</p>
</td>
<td class="cellrowborder" valign="top" width="69.69999999999999%" headers="mcps1.2.3.1.2 "><p id="p57964222144241"><a name="p57964222144241"></a><a name="p57964222144241"></a>Indicates the time stamp when the message was initially sent.</p>
</td>
</tr>
</tbody>
</table>

The following is an example HTTP\(S\) notification message:

```
{
    "signature": "ViE96uGbBkl+S8eWqgebi5KdmRht2U8+Rs88yuyMHq1k4h3jUkcDZ6HCqTqdpJ8nrLcdqETyyEiOQyTszJdU05z+LhfE8jerCCdSbL4zeInVkydHh0kcCRWmORye0/EuQ/gLC1UIXwvUsqbUCPnBRhNFXOeXMOPPCzK+d04xjy4QHd1H/bHxgsY3AlTe0gCFT068Zru7OK6w9aQaY44mXnN3OWGmBmoHyFab5TRXLSQNz/9u/Vj646cQMMaI0PPQ30QzGYD0MtzgDZi12m8jMTHAnMkTEcbLaEgaqmaoEnATSpEcspFKNXv2skwk7rsVakMOISpMH3+qC6RzhETA2A==",
    "topic_urn": "urn:smn:region01:0553db98c800d5192f9bc01232b89622:vpc_status_report_topic",
    "message_id": "d86c201092574e71a3ca85826652c58b",
    "signature_version": "v1",
    "type": "Notification",
    "message": "{\"enterpriseProjectId\": \"0\", \"eventTime\": \"2019-08-12 22:40:55.040632\", \"chargingMode\": \"postPaid\", \"cloudserviceType\": \"hws.service.type.bandwidth\", \"eventType\": 1, \"regionId\": \"region01\", \"tenantId\": \"057eefe55400d2742f8cc0017870ceef\", \"resourceType\": \"hws.resource.type.bandwidth\", \"resourceSpecCode\": \"19_bgp\", \"resourceSize\": 10, \"resourceId\": \"e091f1b1-08ef-4e2b-a27e-f85e4c19026a\", \"resouceSizeMeasureId\": 15, \"resourceName\": \"elbauto_2019_08_13_06_40_46\"}",
    "unsubscribe_url": "https://console.xxx.com/smn/subscription/unsubscribe?subscription_urn=urn:smn:region01:0553db98c800d5192f9bc01232b89622:vpc_status_report_topic:653e212a43884f7188ca656c537e31ce",
    "signing_cert_url": "https://console.xxx.com/smn/SMN_region01_b3974c411807498bb532b3cd6cd65d91.pem",
    "timestamp": "2019-08-12T22:40:56Z"
}
```

## HTTP/HTTPS Subscription Cancellation Message Format<a name="section51915957144241"></a>

After an HTTP/HTTPS subscription is canceled, the subscriber receives a subscription cancellation message sent by SMN. The message body is composed of JSON character strings, which are described in  [Table 4](#table64442359144241).

**Table  4**  HTTP/HTTPS subscription cancellation message body

<a name="table64442359144241"></a>
<table><thead align="left"><tr id="row47856547144241"><th class="cellrowborder" valign="top" width="30.3%" id="mcps1.2.3.1.1"><p id="p51175085144241"><a name="p51175085144241"></a><a name="p51175085144241"></a><strong id="b44234363153857"><a name="b44234363153857"></a><a name="b44234363153857"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="69.69999999999999%" id="mcps1.2.3.1.2"><p id="p51541240144241"><a name="p51541240144241"></a><a name="p51541240144241"></a><strong id="b5747991715399_2"><a name="b5747991715399_2"></a><a name="b5747991715399_2"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row14090924144241"><td class="cellrowborder" valign="top" width="30.3%" headers="mcps1.2.3.1.1 "><p id="p514159144241"><a name="p514159144241"></a><a name="p514159144241"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="69.69999999999999%" headers="mcps1.2.3.1.2 "><p id="p41646956144241"><a name="p41646956144241"></a><a name="p41646956144241"></a>Indicates the message type, the value of which is <strong id="b842352706153316_2"><a name="b842352706153316_2"></a><a name="b842352706153316_2"></a>UnsubscribeConfirmation</strong>.</p>
</td>
</tr>
<tr id="row15109115512224"><td class="cellrowborder" valign="top" width="30.3%" headers="mcps1.2.3.1.1 "><p id="p31795252144241"><a name="p31795252144241"></a><a name="p31795252144241"></a>signature</p>
</td>
<td class="cellrowborder" valign="top" width="69.69999999999999%" headers="mcps1.2.3.1.2 "><p id="p25278618144241"><a name="p25278618144241"></a><a name="p25278618144241"></a>Indicates the signature information.</p>
<p id="p26180971144241"><a name="p26180971144241"></a><a name="p26180971144241"></a>The signature includes the <strong id="b842352706154239_1"><a name="b842352706154239_1"></a><a name="b842352706154239_1"></a>message</strong>, <strong id="b842352706154245_1"><a name="b842352706154245_1"></a><a name="b842352706154245_1"></a>message_id</strong>, <strong id="b842352706154252_1"><a name="b842352706154252_1"></a><a name="b842352706154252_1"></a>subscribe_url</strong>, <strong id="b842352706154258_1"><a name="b842352706154258_1"></a><a name="b842352706154258_1"></a>timestamp</strong>, <strong id="b84235270615438_1"><a name="b84235270615438_1"></a><a name="b84235270615438_1"></a>topic_urn</strong>, and <strong id="b842352706154321_1"><a name="b842352706154321_1"></a><a name="b842352706154321_1"></a>type</strong> fields. For details about signature verification, see <a href="message-signature-verification.md">Message Signature Verification</a>.</p>
</td>
</tr>
<tr id="row171091555112219"><td class="cellrowborder" valign="top" width="30.3%" headers="mcps1.2.3.1.1 "><p id="p61825074144241"><a name="p61825074144241"></a><a name="p61825074144241"></a>topic_urn</p>
</td>
<td class="cellrowborder" valign="top" width="69.69999999999999%" headers="mcps1.2.3.1.2 "><p id="p41775137144241"><a name="p41775137144241"></a><a name="p41775137144241"></a>Indicates the URN of the topic to which the message belongs.</p>
</td>
</tr>
<tr id="row16109125502214"><td class="cellrowborder" valign="top" width="30.3%" headers="mcps1.2.3.1.1 "><p id="p53760131144241"><a name="p53760131144241"></a><a name="p53760131144241"></a>message_id</p>
</td>
<td class="cellrowborder" valign="top" width="69.69999999999999%" headers="mcps1.2.3.1.2 "><p id="p59603370144241"><a name="p59603370144241"></a><a name="p59603370144241"></a>Indicates the unique message ID.</p>
</td>
</tr>
<tr id="row811017551229"><td class="cellrowborder" valign="top" width="30.3%" headers="mcps1.2.3.1.1 "><p id="p27010586144241"><a name="p27010586144241"></a><a name="p27010586144241"></a>signature_version</p>
</td>
<td class="cellrowborder" valign="top" width="69.69999999999999%" headers="mcps1.2.3.1.2 "><p id="p40373894144241"><a name="p40373894144241"></a><a name="p40373894144241"></a>Indicates the signature version, which is currently <strong id="b7205736185211"><a name="b7205736185211"></a><a name="b7205736185211"></a>V1</strong>.</p>
</td>
</tr>
<tr id="row711055515224"><td class="cellrowborder" valign="top" width="30.3%" headers="mcps1.2.3.1.1 "><p id="p31422338144241"><a name="p31422338144241"></a><a name="p31422338144241"></a>message</p>
</td>
<td class="cellrowborder" valign="top" width="69.69999999999999%" headers="mcps1.2.3.1.2 "><p id="p62181451144241"><a name="p62181451144241"></a><a name="p62181451144241"></a>Indicates the message content.</p>
</td>
</tr>
<tr id="row11110125510228"><td class="cellrowborder" valign="top" width="30.3%" headers="mcps1.2.3.1.1 "><p id="p27424659144241"><a name="p27424659144241"></a><a name="p27424659144241"></a>subscribe_url</p>
</td>
<td class="cellrowborder" valign="top" width="69.69999999999999%" headers="mcps1.2.3.1.2 "><p id="p6804900144241"><a name="p6804900144241"></a><a name="p6804900144241"></a>Indicates the URL for a re-subscription.</p>
</td>
</tr>
<tr id="row11103555223"><td class="cellrowborder" valign="top" width="30.3%" headers="mcps1.2.3.1.1 "><p id="p38886363144241"><a name="p38886363144241"></a><a name="p38886363144241"></a>signing_cert_url</p>
</td>
<td class="cellrowborder" valign="top" width="69.69999999999999%" headers="mcps1.2.3.1.2 "><p id="p62787721144241"><a name="p62787721144241"></a><a name="p62787721144241"></a>Indicates the certificate URL for generating the message signature.</p>
</td>
</tr>
<tr id="row411018554224"><td class="cellrowborder" valign="top" width="30.3%" headers="mcps1.2.3.1.1 "><p id="p4003487144241"><a name="p4003487144241"></a><a name="p4003487144241"></a>timestamp</p>
</td>
<td class="cellrowborder" valign="top" width="69.69999999999999%" headers="mcps1.2.3.1.2 "><p id="p55847049144241"><a name="p55847049144241"></a><a name="p55847049144241"></a>Indicates the time stamp when the message was initially sent.</p>
</td>
</tr>
</tbody>
</table>

The following is an example HTTP\(S\) message for canceling a subscription:

```
{
    "signature": "ViE96uGbBkl+S8eWqgebi5KdmRht2U8+Rs88yuyMHq1k4h3jUkcDZ6HCqTqdpJ8nrLcdqETyyEiOQyTszJdU05z+LhfE8jerCCdSbL4zeInVkydHh0kcCRWmORye0/EuQ/gLC1UIXwvUsqbUCPnBRhNFXOeXMOPPCzK+d04xjy4QHd1H/bHxgsY3AlTe0gCFT068Zru7OK6w9aQaY44mXnN3OWGmBmoHyFab5TRXLSQNz/9u/Vj646cQMMaI0PPQ30QzGYD0MtzgDZi12m8jMTHAnMkTEcbLaEgaqmaoEnATSpEcspFKNXv2skwk7rsVakMOISpMH3+qC6RzhETA2A==",
    "topic_urn": "urn:smn:region01:0553db98c800d5192f9bc01232b89622:vpc_status_report_topic",
    "message_id": "d86c201092574e71a3ca85826652c58b",
    "signature_version": "v1",
    "type": "UnsubscribeConfirmation",
    "message": "{\"enterpriseProjectId\": \"0\", \"eventTime\": \"2019-08-12 22:40:55.040632\", \"chargingMode\": \"postPaid\", \"cloudserviceType\": \"hws.service.type.bandwidth\", \"eventType\": 1, \"regionId\": \"region01\", \"tenantId\": \"057eefe55400d2742f8cc0017870ceef\", \"resourceType\": \"hws.resource.type.bandwidth\", \"resourceSpecCode\": \"19_bgp\", \"resourceSize\": 10, \"resourceId\": \"e091f1b1-08ef-4e2b-a27e-f85e4c19026a\", \"resouceSizeMeasureId\": 15, \"resourceName\": \"elbauto_2019_08_13_06_40_46\"}",
    "subscribe_url": "https://console.xxx.com/smn/subscription/unsubscribe?subscription_urn=urn:smn:region01:0553db98c800d5192f9bc01232b89622:vpc_status_report_topic:653e212a43884f7188ca656c537e31ce",
    "signing_cert_url": "https://console.xxx.com/smn/SMN_region01_b3974c411807498bb532b3cd6cd65d91.pem",
    "timestamp": "2019-08-12T22:40:56Z"
}
```

