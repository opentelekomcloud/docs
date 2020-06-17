# Configuration Examples<a name="EN-US_TOPIC_0161727556"></a>

## Example 1: Denying Access from Specific Ports<a name="section968441113166"></a>

In this example, you need to prevent WannaCry ransomware attacks and deny access from the port that can be exploited by WannaCry, for example TCP 445. You can add a user-defined network ACL rule to deny all incoming traffic from TCP port 445.

[Table 1](#table12372132313177)  lists the inbound rule required.

**Table  1**  User-defined network ACL rule

<a name="table12372132313177"></a>
<table><thead align="left"><tr id="row83726235174"><th class="cellrowborder" valign="top" width="9.46%" id="mcps1.2.9.1.1"><p id="p1437292312171"><a name="p1437292312171"></a><a name="p1437292312171"></a>Direction</p>
</th>
<th class="cellrowborder" valign="top" width="9.19%" id="mcps1.2.9.1.2"><p id="p33736237172"><a name="p33736237172"></a><a name="p33736237172"></a>Policy</p>
</th>
<th class="cellrowborder" valign="top" width="10.05%" id="mcps1.2.9.1.3"><p id="p1337319234177"><a name="p1337319234177"></a><a name="p1337319234177"></a>Protocol</p>
</th>
<th class="cellrowborder" valign="top" width="12.2%" id="mcps1.2.9.1.4"><p id="p183731023121717"><a name="p183731023121717"></a><a name="p183731023121717"></a>Source</p>
</th>
<th class="cellrowborder" valign="top" width="12.379999999999999%" id="mcps1.2.9.1.5"><p id="p11373102315176"><a name="p11373102315176"></a><a name="p11373102315176"></a>Source Port Range</p>
</th>
<th class="cellrowborder" valign="top" width="13.459999999999999%" id="mcps1.2.9.1.6"><p id="p17373162318179"><a name="p17373162318179"></a><a name="p17373162318179"></a>Destination</p>
</th>
<th class="cellrowborder" valign="top" width="12.91%" id="mcps1.2.9.1.7"><p id="p03731323181712"><a name="p03731323181712"></a><a name="p03731323181712"></a>Destination Port Range</p>
</th>
<th class="cellrowborder" valign="top" width="20.349999999999998%" id="mcps1.2.9.1.8"><p id="p837342317172"><a name="p837342317172"></a><a name="p837342317172"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row9373142313177"><td class="cellrowborder" valign="top" width="9.46%" headers="mcps1.2.9.1.1 "><p id="p16373172310178"><a name="p16373172310178"></a><a name="p16373172310178"></a>Inbound</p>
</td>
<td class="cellrowborder" valign="top" width="9.19%" headers="mcps1.2.9.1.2 "><p id="p037322321718"><a name="p037322321718"></a><a name="p037322321718"></a>Deny</p>
</td>
<td class="cellrowborder" valign="top" width="10.05%" headers="mcps1.2.9.1.3 "><p id="p173730232176"><a name="p173730232176"></a><a name="p173730232176"></a>TCP</p>
</td>
<td class="cellrowborder" valign="top" width="12.2%" headers="mcps1.2.9.1.4 "><p id="p6373132317170"><a name="p6373132317170"></a><a name="p6373132317170"></a>0.0.0.0/0</p>
</td>
<td class="cellrowborder" valign="top" width="12.379999999999999%" headers="mcps1.2.9.1.5 "><p id="p63731623101716"><a name="p63731623101716"></a><a name="p63731623101716"></a>1-65535</p>
</td>
<td class="cellrowborder" valign="top" width="13.459999999999999%" headers="mcps1.2.9.1.6 "><p id="p14373423171710"><a name="p14373423171710"></a><a name="p14373423171710"></a>0.0.0.0/0</p>
</td>
<td class="cellrowborder" valign="top" width="12.91%" headers="mcps1.2.9.1.7 "><p id="p137372391717"><a name="p137372391717"></a><a name="p137372391717"></a>445</p>
</td>
<td class="cellrowborder" valign="top" width="20.349999999999998%" headers="mcps1.2.9.1.8 "><p id="p133731523171712"><a name="p133731523171712"></a><a name="p133731523171712"></a>Denies inbound traffic from any IP address through TCP port 445.</p>
</td>
</tr>
</tbody>
</table>

## Example 2: Allowing Access from Specific Ports and Protocols<a name="section19692296209"></a>

In this example, a BMS in a user-defined subnet is used as the web server, and you must allow inbound traffic from HTTP port 80 and HTTPS port 443 and allow all outbound traffic.

[Table 2](#table1798617588250)  lists the inbound and outbound user-defined network ACL rules required.

**Table  2**  User-defined network ACL rules

<a name="table1798617588250"></a>
<table><thead align="left"><tr id="row0986658132512"><th class="cellrowborder" valign="top" width="9.46%" id="mcps1.2.9.1.1"><p id="p1398619580258"><a name="p1398619580258"></a><a name="p1398619580258"></a>Direction</p>
</th>
<th class="cellrowborder" valign="top" width="9.19%" id="mcps1.2.9.1.2"><p id="p10986185892511"><a name="p10986185892511"></a><a name="p10986185892511"></a>Policy</p>
</th>
<th class="cellrowborder" valign="top" width="10.05%" id="mcps1.2.9.1.3"><p id="p29863585250"><a name="p29863585250"></a><a name="p29863585250"></a>Protocol</p>
</th>
<th class="cellrowborder" valign="top" width="12.2%" id="mcps1.2.9.1.4"><p id="p69861582256"><a name="p69861582256"></a><a name="p69861582256"></a>Source</p>
</th>
<th class="cellrowborder" valign="top" width="12.379999999999999%" id="mcps1.2.9.1.5"><p id="p13986558122519"><a name="p13986558122519"></a><a name="p13986558122519"></a>Source Port Range</p>
</th>
<th class="cellrowborder" valign="top" width="13.459999999999999%" id="mcps1.2.9.1.6"><p id="p198735802514"><a name="p198735802514"></a><a name="p198735802514"></a>Destination</p>
</th>
<th class="cellrowborder" valign="top" width="12.91%" id="mcps1.2.9.1.7"><p id="p79871558162513"><a name="p79871558162513"></a><a name="p79871558162513"></a>Destination Port Range</p>
</th>
<th class="cellrowborder" valign="top" width="20.349999999999998%" id="mcps1.2.9.1.8"><p id="p498795816253"><a name="p498795816253"></a><a name="p498795816253"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row59871558172518"><td class="cellrowborder" valign="top" width="9.46%" headers="mcps1.2.9.1.1 "><p id="p11987185852511"><a name="p11987185852511"></a><a name="p11987185852511"></a>Inbound</p>
</td>
<td class="cellrowborder" valign="top" width="9.19%" headers="mcps1.2.9.1.2 "><p id="p1498775892511"><a name="p1498775892511"></a><a name="p1498775892511"></a>Permit</p>
</td>
<td class="cellrowborder" valign="top" width="10.05%" headers="mcps1.2.9.1.3 "><p id="p298712587258"><a name="p298712587258"></a><a name="p298712587258"></a>TCP</p>
</td>
<td class="cellrowborder" valign="top" width="12.2%" headers="mcps1.2.9.1.4 "><p id="p129879584259"><a name="p129879584259"></a><a name="p129879584259"></a>0.0.0.0/0</p>
</td>
<td class="cellrowborder" valign="top" width="12.379999999999999%" headers="mcps1.2.9.1.5 "><p id="p49879588252"><a name="p49879588252"></a><a name="p49879588252"></a>1-65535</p>
</td>
<td class="cellrowborder" valign="top" width="13.459999999999999%" headers="mcps1.2.9.1.6 "><p id="p298718586252"><a name="p298718586252"></a><a name="p298718586252"></a>0.0.0.0/0</p>
</td>
<td class="cellrowborder" valign="top" width="12.91%" headers="mcps1.2.9.1.7 "><p id="p1898735819257"><a name="p1898735819257"></a><a name="p1898735819257"></a>80</p>
</td>
<td class="cellrowborder" valign="top" width="20.349999999999998%" headers="mcps1.2.9.1.8 "><p id="p1598765812512"><a name="p1598765812512"></a><a name="p1598765812512"></a>Allows inbound HTTP traffic from any IP address to BMSs in the user-defined subnet through port 80.</p>
</td>
</tr>
<tr id="row252217255268"><td class="cellrowborder" valign="top" width="9.46%" headers="mcps1.2.9.1.1 "><p id="p2052382542610"><a name="p2052382542610"></a><a name="p2052382542610"></a>Inbound</p>
</td>
<td class="cellrowborder" valign="top" width="9.19%" headers="mcps1.2.9.1.2 "><p id="p152316259268"><a name="p152316259268"></a><a name="p152316259268"></a>Permit</p>
</td>
<td class="cellrowborder" valign="top" width="10.05%" headers="mcps1.2.9.1.3 "><p id="p16523132592620"><a name="p16523132592620"></a><a name="p16523132592620"></a>TCP</p>
</td>
<td class="cellrowborder" valign="top" width="12.2%" headers="mcps1.2.9.1.4 "><p id="p652317257266"><a name="p652317257266"></a><a name="p652317257266"></a>0.0.0.0/0</p>
</td>
<td class="cellrowborder" valign="top" width="12.379999999999999%" headers="mcps1.2.9.1.5 "><p id="p55237256260"><a name="p55237256260"></a><a name="p55237256260"></a>1-65535</p>
</td>
<td class="cellrowborder" valign="top" width="13.459999999999999%" headers="mcps1.2.9.1.6 "><p id="p65231225132611"><a name="p65231225132611"></a><a name="p65231225132611"></a>0.0.0.0/0</p>
</td>
<td class="cellrowborder" valign="top" width="12.91%" headers="mcps1.2.9.1.7 "><p id="p12523122519269"><a name="p12523122519269"></a><a name="p12523122519269"></a>443</p>
</td>
<td class="cellrowborder" valign="top" width="20.349999999999998%" headers="mcps1.2.9.1.8 "><p id="p185231252265"><a name="p185231252265"></a><a name="p185231252265"></a>Allows inbound HTTP traffic from any IP address to BMSs in the user-defined subnet through port 443.</p>
</td>
</tr>
<tr id="row2623172910269"><td class="cellrowborder" valign="top" width="9.46%" headers="mcps1.2.9.1.1 "><p id="p20623162917265"><a name="p20623162917265"></a><a name="p20623162917265"></a>Outbound</p>
</td>
<td class="cellrowborder" valign="top" width="9.19%" headers="mcps1.2.9.1.2 "><p id="p6623129202613"><a name="p6623129202613"></a><a name="p6623129202613"></a>Permit</p>
</td>
<td class="cellrowborder" valign="top" width="10.05%" headers="mcps1.2.9.1.3 "><p id="p1762311295265"><a name="p1762311295265"></a><a name="p1762311295265"></a>All</p>
</td>
<td class="cellrowborder" valign="top" width="12.2%" headers="mcps1.2.9.1.4 "><p id="p76231529132618"><a name="p76231529132618"></a><a name="p76231529132618"></a>0.0.0.0/0</p>
</td>
<td class="cellrowborder" valign="top" width="12.379999999999999%" headers="mcps1.2.9.1.5 "><p id="p66231129162614"><a name="p66231129162614"></a><a name="p66231129162614"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="13.459999999999999%" headers="mcps1.2.9.1.6 "><p id="p12623182932613"><a name="p12623182932613"></a><a name="p12623182932613"></a>0.0.0.0/0</p>
</td>
<td class="cellrowborder" valign="top" width="12.91%" headers="mcps1.2.9.1.7 "><p id="p262382916267"><a name="p262382916267"></a><a name="p262382916267"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="20.349999999999998%" headers="mcps1.2.9.1.8 "><p id="p106231294268"><a name="p106231294268"></a><a name="p106231294268"></a>Allow all outbound traffic from the user-defined subnet.</p>
</td>
</tr>
</tbody>
</table>

