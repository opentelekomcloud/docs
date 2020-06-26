# OS::Heat::WaitConditionHandle<a name="EN-US_TOPIC_0088407103"></a>

Resource for managing instance signals.

The main points of this resource are:

-   have no dependencies \(so the instance can reference it\).
-   create credentials to allow for signaling from the instance.
-   handle signals from the instance, validate and store result.

## Optional Properties<a name="section159171352149"></a>

<a name="table317554691413"></a>
<table><thead align="left"><tr id="row48181228142619"><th class="cellrowborder" valign="top" width="30%" id="mcps1.1.3.1.1"><p id="p151771646131420"><a name="p151771646131420"></a><a name="p151771646131420"></a><strong id="b20819122811263"><a name="b20819122811263"></a><a name="b20819122811263"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="70%" id="mcps1.1.3.1.2"><p id="p1117784601411"><a name="p1117784601411"></a><a name="p1117784601411"></a><strong id="b20819102872612"><a name="b20819102872612"></a><a name="b20819102872612"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row78191828122615"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.3.1.1 "><p id="p1417714465144"><a name="p1417714465144"></a><a name="p1417714465144"></a>signal_transport</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.1.3.1.2 "><p id="p183784819433"><a name="p183784819433"></a><a name="p183784819433"></a>How the client will signal the wait condition.</p>
<a name="ul1124175414448"></a><a name="ul1124175414448"></a><ul id="ul1124175414448"><li>TOKEN_SIGNAL will allow and HTTP POST to a Heat API endpoint with the provided keystone token.</li><li>NO_SIGNAL will result in the resource going to a signalled state without waiting for any signal.</li></ul>
<p id="p20839629"><a name="p20839629"></a><a name="p20839629"></a>String value expected.</p>
<p id="p18441221171719"><a name="p18441221171719"></a><a name="p18441221171719"></a>Updates cause replacement.</p>
<p id="p52922567178"><a name="p52922567178"></a><a name="p52922567178"></a>Defaults to "TOKEN_SIGNAL".</p>
<p id="p15909102634810"><a name="p15909102634810"></a><a name="p15909102634810"></a>Allowed values: TOKEN_SIGNAL, NO_SIGNAL</p>
</td>
</tr>
</tbody>
</table>

## Attributes<a name="section1227271741510"></a>

<a name="table185461036171010"></a>
<table><thead align="left"><tr id="row1114217219275"><th class="cellrowborder" valign="top" width="30%" id="mcps1.1.3.1.1"><p id="p354718362102"><a name="p354718362102"></a><a name="p354718362102"></a><strong id="b16143824274"><a name="b16143824274"></a><a name="b16143824274"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="70%" id="mcps1.1.3.1.2"><p id="p13547183614105"><a name="p13547183614105"></a><a name="p13547183614105"></a><strong id="b1014418210273"><a name="b1014418210273"></a><a name="b1014418210273"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row19144112102711"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.3.1.1 "><p id="p3547163611017"><a name="p3547163611017"></a><a name="p3547163611017"></a>curl_cli</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.1.3.1.2 "><p id="p53338937"><a name="p53338937"></a><a name="p53338937"></a>Convenience attribute, provides curl CLI command prefix, which can be used for signaling handle completion or failure when signal_transport is set to TOKEN_SIGNAL. You can signal success by adding –data-binary {"status": "SUCCESS"} , or signal failure by adding –data-binary {"status": "FAILURE"}. This attribute is set to None for all other signal transports.</p>
</td>
</tr>
<tr id="row1862910314286"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.3.1.1 "><p id="p1654715368103"><a name="p1654715368103"></a><a name="p1654715368103"></a>endpoint</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.1.3.1.2 "><p id="p57716227"><a name="p57716227"></a><a name="p57716227"></a>Endpoint/url which can be used for signaling handle when signal_transport is set to TOKEN_SIGNAL. None for all other signal transports.</p>
</td>
</tr>
<tr id="row102111335112812"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.3.1.1 "><p id="p10378851101511"><a name="p10378851101511"></a><a name="p10378851101511"></a>token</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.1.3.1.2 "><p id="p1537815115154"><a name="p1537815115154"></a><a name="p1537815115154"></a>Token for stack-user which can be used for signaling handle when signal_transport is set to TOKEN_SIGNAL. None for all other signal transports.</p>
</td>
</tr>
</tbody>
</table>

## HOT Syntax<a name="section12583192691510"></a>

```
heat_template_version: 2014-10-16
...
resources:
  ...
  the_resource:
    type: OS::Heat::WaitConditionHandle
    properties:
      signal_transport: String
```

