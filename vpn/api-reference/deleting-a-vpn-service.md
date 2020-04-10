# Deleting a VPN Service<a name="en_topic_0093011502"></a>

## **Function**<a name="section28812104"></a>

This interface is used to delete a VPN service.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>This interface cannot be used to delete a VPN service in the active-active VPN scenarios.  

## URI<a name="section57982344"></a>

DELETE /v2.0/vpn/vpnservices/\{service\_id\}

**Table  1**  Parameter description

<a name="table184162115335"></a>
<table><thead align="left"><tr id="row984914219336"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p8849921163313"><a name="p8849921163313"></a><a name="p8849921163313"></a><strong id="b842352706172115"><a name="b842352706172115"></a><a name="b842352706172115"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p384918214339"><a name="p384918214339"></a><a name="p384918214339"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p208493212330"><a name="p208493212330"></a><a name="p208493212330"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p1185732118339"><a name="p1185732118339"></a><a name="p1185732118339"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row10857162110332"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p17857142117336"><a name="p17857142117336"></a><a name="p17857142117336"></a>service_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p18857152173311"><a name="p18857152173311"></a><a name="p18857152173311"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p385772133310"><a name="p385772133310"></a><a name="p385772133310"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p28642214334"><a name="p28642214334"></a><a name="p28642214334"></a>Specifies the VPN service ID.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section66058249"></a>

None

## Response Message<a name="section57653332"></a>

None

## Example<a name="section49117947"></a>

-   Example Request

```
DELETE v2.0/vpn/vpnservices/{service_id}
```

-   Example Response

    None


## Returned Values<a name="section6578292"></a>

For details, see section  [Common Returned Values](common-returned-values.md).

