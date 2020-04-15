# Logging In to the CAS<a name="EN-US_TOPIC_0220024723"></a>

## Function<a name="en-us_topic_0125376251_section117081433155319"></a>

This API is used to submit a CAS login request. This API can be used only by security clusters that support Kerberos authentication.

## URI<a name="en-us_topic_0125376251_sdf9aaecf112841708e5dce8abfdb5ef4"></a>

POST /cas/login

## Request<a name="en-us_topic_0125376251_s5638694e0ef44845af6169cdd3eb9040"></a>

-   Example:

```
POST /cas/login HTTP/1.1
Host: example.com
Content-Type: application/json
Accept:application/json
username: String
password: String
lt: String
_eventId: String
Submit: String
```

-   Parameter description

<a name="en-us_topic_0125376251_en-us_topic_0110839907_table13129592"></a>
<table><thead align="left"><tr id="en-us_topic_0125376251_en-us_topic_0110839907_row45356064"><th class="cellrowborder" valign="top" width="20%" id="mcps1.1.4.1.1"><p id="en-us_topic_0125376251_en-us_topic_0110839907_p49962569"><a name="en-us_topic_0125376251_en-us_topic_0110839907_p49962569"></a><a name="en-us_topic_0125376251_en-us_topic_0110839907_p49962569"></a><strong id="en-us_topic_0125376251_b162774213314533_1"><a name="en-us_topic_0125376251_b162774213314533_1"></a><a name="en-us_topic_0125376251_b162774213314533_1"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="21%" id="mcps1.1.4.1.2"><p id="en-us_topic_0125376251_en-us_topic_0110839907_p20436323"><a name="en-us_topic_0125376251_en-us_topic_0110839907_p20436323"></a><a name="en-us_topic_0125376251_en-us_topic_0110839907_p20436323"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="59%" id="mcps1.1.4.1.3"><p id="en-us_topic_0125376251_en-us_topic_0110839907_p53775824"><a name="en-us_topic_0125376251_en-us_topic_0110839907_p53775824"></a><a name="en-us_topic_0125376251_en-us_topic_0110839907_p53775824"></a><strong id="en-us_topic_0125376251_b842352706134712"><a name="en-us_topic_0125376251_b842352706134712"></a><a name="en-us_topic_0125376251_b842352706134712"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0125376251_en-us_topic_0110839907_row60874484"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0125376251_en-us_topic_0110839907_p31886201"><a name="en-us_topic_0125376251_en-us_topic_0110839907_p31886201"></a><a name="en-us_topic_0125376251_en-us_topic_0110839907_p31886201"></a>username</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0125376251_en-us_topic_0110839907_p32645511"><a name="en-us_topic_0125376251_en-us_topic_0110839907_p32645511"></a><a name="en-us_topic_0125376251_en-us_topic_0110839907_p32645511"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0125376251_en-us_topic_0110839907_p10131777"><a name="en-us_topic_0125376251_en-us_topic_0110839907_p10131777"></a><a name="en-us_topic_0125376251_en-us_topic_0110839907_p10131777"></a>User name</p>
</td>
</tr>
<tr id="en-us_topic_0125376251_en-us_topic_0110839907_row24077135"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0125376251_en-us_topic_0110839907_p4090907"><a name="en-us_topic_0125376251_en-us_topic_0110839907_p4090907"></a><a name="en-us_topic_0125376251_en-us_topic_0110839907_p4090907"></a>password</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0125376251_en-us_topic_0110839907_p62928011"><a name="en-us_topic_0125376251_en-us_topic_0110839907_p62928011"></a><a name="en-us_topic_0125376251_en-us_topic_0110839907_p62928011"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0125376251_en-us_topic_0110839907_p26299090"><a name="en-us_topic_0125376251_en-us_topic_0110839907_p26299090"></a><a name="en-us_topic_0125376251_en-us_topic_0110839907_p26299090"></a>Password</p>
</td>
</tr>
<tr id="en-us_topic_0125376251_row0125122520168"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0125376251_p11125192518165"><a name="en-us_topic_0125376251_p11125192518165"></a><a name="en-us_topic_0125376251_p11125192518165"></a>lt</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0125376251_p212511253169"><a name="en-us_topic_0125376251_p212511253169"></a><a name="en-us_topic_0125376251_p212511253169"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0125376251_p15316853183015"><a name="en-us_topic_0125376251_p15316853183015"></a><a name="en-us_topic_0125376251_p15316853183015"></a>Login ticket. Follow instructions in step 1 in the <span class="parmname" id="en-us_topic_0125376251_parmname618076927165330"><a name="en-us_topic_0125376251_parmname618076927165330"></a><a name="en-us_topic_0125376251_parmname618076927165330"></a><b>Obtaining Request Authentication Information</b></span>&nbsp;part of the section&nbsp;<a href="api-calling-process.md#EN-US_TOPIC_0220024720">API Calling Process</a>&nbsp;to send a GET request to obtain&nbsp;<strong id="en-us_topic_0125376251_b842352706165534"><a name="en-us_topic_0125376251_b842352706165534"></a><a name="en-us_topic_0125376251_b842352706165534"></a>loginTicket</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0125376251_row8764725151619"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0125376251_p187641259167"><a name="en-us_topic_0125376251_p187641259167"></a><a name="en-us_topic_0125376251_p187641259167"></a>_eventId</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0125376251_p2076413254161"><a name="en-us_topic_0125376251_p2076413254161"></a><a name="en-us_topic_0125376251_p2076413254161"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0125376251_p97646253162"><a name="en-us_topic_0125376251_p97646253162"></a><a name="en-us_topic_0125376251_p97646253162"></a>Event type. The default value is <strong id="en-us_topic_0125376251_b842352706165548"><a name="en-us_topic_0125376251_b842352706165548"></a><a name="en-us_topic_0125376251_b842352706165548"></a>submit</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0125376251_row19185726191614"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0125376251_p10185152619161"><a name="en-us_topic_0125376251_p10185152619161"></a><a name="en-us_topic_0125376251_p10185152619161"></a>submit</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0125376251_p018517267166"><a name="en-us_topic_0125376251_p018517267166"></a><a name="en-us_topic_0125376251_p018517267166"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0125376251_p191851926151618"><a name="en-us_topic_0125376251_p191851926151618"></a><a name="en-us_topic_0125376251_p191851926151618"></a>Submission type. The default value is <strong id="en-us_topic_0125376251_b84235270616560"><a name="en-us_topic_0125376251_b84235270616560"></a><a name="en-us_topic_0125376251_b84235270616560"></a>Login</strong>.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="en-us_topic_0125376251_s1f994bcec3664deab9024db0ad17b4ca"></a>

-   Example

    ```
    HTTP/1.1 200 OK
    Data:Wed,02 May 2018 10:10:01 GMT
    Server: example-server
    Content-Type: application/json
    ```

-   Parameter description

    None


## Status Code<a name="en-us_topic_0125376251_section1090133331415"></a>

**Table  1**  Status code

<a name="en-us_topic_0125376251_table2979011121511"></a>
<table><thead align="left"><tr id="en-us_topic_0125376251_row3981161161515"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.3.1.1"><p id="en-us_topic_0125376251_p398115116158"><a name="en-us_topic_0125376251_p398115116158"></a><a name="en-us_topic_0125376251_p398115116158"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="83%" id="mcps1.2.3.1.2"><p id="en-us_topic_0125376251_p1798121191515"><a name="en-us_topic_0125376251_p1798121191515"></a><a name="en-us_topic_0125376251_p1798121191515"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0125376251_row69813112155"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0125376251_p698113117157"><a name="en-us_topic_0125376251_p698113117157"></a><a name="en-us_topic_0125376251_p698113117157"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="83%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0125376251_p7981131116153"><a name="en-us_topic_0125376251_p7981131116153"></a><a name="en-us_topic_0125376251_p7981131116153"></a>The login is successful.</p>
</td>
</tr>
</tbody>
</table>

For details about error status codes, see  [Status Codes](status-codes.md).

