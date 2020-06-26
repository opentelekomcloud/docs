# Querying SSH Key Pairs<a name="EN-US_TOPIC_0020212676"></a>

## Function<a name="section66325402"></a>

This API is used to query SSH key pairs.

## URI<a name="section60057706"></a>

GET /v2/\{project\_id\}/os-keypairs

GET /v2.1/\{project\_id\}/os-keypairs

[Table 1](#table38623499)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="table38623499"></a>
<table><thead align="left"><tr id="row59671974"><th class="cellrowborder" valign="top" width="16.79%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.169999999999998%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="66.03999999999999%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row53887795"><td class="cellrowborder" valign="top" width="16.79%" headers="mcps1.2.4.1.1 "><p id="p2835298"><a name="p2835298"></a><a name="p2835298"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.2.4.1.2 "><p id="p28332581"><a name="p28332581"></a><a name="p28332581"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="66.03999999999999%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section3648444"></a>

None

## Response<a name="section32836002"></a>

[Table 2](#table46959463)  describes the response parameters.

**Table  2**  Response parameters

<a name="table46959463"></a>
<table><thead align="left"><tr id="row9766180"><th class="cellrowborder" valign="top" width="16.79%" id="mcps1.2.4.1.1"><p id="p52863116"><a name="p52863116"></a><a name="p52863116"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.23%" id="mcps1.2.4.1.2"><p id="p16299242"><a name="p16299242"></a><a name="p16299242"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="66.97999999999999%" id="mcps1.2.4.1.3"><p id="p45170224"><a name="p45170224"></a><a name="p45170224"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row34909498"><td class="cellrowborder" valign="top" width="16.79%" headers="mcps1.2.4.1.1 "><p id="p9097072"><a name="p9097072"></a><a name="p9097072"></a>keypairs</p>
</td>
<td class="cellrowborder" valign="top" width="16.23%" headers="mcps1.2.4.1.2 "><p id="p26115459"><a name="p26115459"></a><a name="p26115459"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="66.97999999999999%" headers="mcps1.2.4.1.3 "><p id="p46361647"><a name="p46361647"></a><a name="p46361647"></a>Specifies key pairs. For details, see <a href="#table41882197">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **keypairs**  field description

<a name="table41882197"></a>
<table><thead align="left"><tr id="row19241577"><th class="cellrowborder" valign="top" width="16.79%" id="mcps1.2.4.1.1"><p id="p564410811336"><a name="p564410811336"></a><a name="p564410811336"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.05%" id="mcps1.2.4.1.2"><p id="p2064412853319"><a name="p2064412853319"></a><a name="p2064412853319"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="67.16%" id="mcps1.2.4.1.3"><p id="p166444810334"><a name="p166444810334"></a><a name="p166444810334"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row34772456"><td class="cellrowborder" valign="top" width="16.79%" headers="mcps1.2.4.1.1 "><p id="p65105571"><a name="p65105571"></a><a name="p65105571"></a>keypair</p>
</td>
<td class="cellrowborder" valign="top" width="16.05%" headers="mcps1.2.4.1.2 "><p id="p9736186"><a name="p9736186"></a><a name="p9736186"></a>Obejct</p>
</td>
<td class="cellrowborder" valign="top" width="67.16%" headers="mcps1.2.4.1.3 "><p id="p51249570"><a name="p51249570"></a><a name="p51249570"></a>Specifies details about a key pair. For details, see <a href="#table48408329">Table 4</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **keypair**  field description

<a name="table48408329"></a>
<table><thead align="left"><tr id="row27259828"><th class="cellrowborder" valign="top" width="16.78%" id="mcps1.2.4.1.1"><p id="p956121163317"><a name="p956121163317"></a><a name="p956121163317"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.04%" id="mcps1.2.4.1.2"><p id="p656110113337"><a name="p656110113337"></a><a name="p656110113337"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="67.17999999999999%" id="mcps1.2.4.1.3"><p id="p1256131103312"><a name="p1256131103312"></a><a name="p1256131103312"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row37982174"><td class="cellrowborder" valign="top" width="16.78%" headers="mcps1.2.4.1.1 "><p id="p56657239"><a name="p56657239"></a><a name="p56657239"></a>fingerprint</p>
</td>
<td class="cellrowborder" valign="top" width="16.04%" headers="mcps1.2.4.1.2 "><p id="p12150471"><a name="p12150471"></a><a name="p12150471"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67.17999999999999%" headers="mcps1.2.4.1.3 "><p id="p66432381"><a name="p66432381"></a><a name="p66432381"></a>Specifies fingerprint information about the key pair.</p>
</td>
</tr>
<tr id="row61020521"><td class="cellrowborder" valign="top" width="16.78%" headers="mcps1.2.4.1.1 "><p id="p43715136"><a name="p43715136"></a><a name="p43715136"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="16.04%" headers="mcps1.2.4.1.2 "><p id="p58836357"><a name="p58836357"></a><a name="p58836357"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67.17999999999999%" headers="mcps1.2.4.1.3 "><p id="p9140568"><a name="p9140568"></a><a name="p9140568"></a>Specifies the key pair name.</p>
</td>
</tr>
<tr id="row199744112018"><td class="cellrowborder" valign="top" width="16.78%" headers="mcps1.2.4.1.1 "><p id="p199751011803"><a name="p199751011803"></a><a name="p199751011803"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="16.04%" headers="mcps1.2.4.1.2 "><p id="p139751111204"><a name="p139751111204"></a><a name="p139751111204"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67.17999999999999%" headers="mcps1.2.4.1.3 "><p id="p1097512112013"><a name="p1097512112013"></a><a name="p1097512112013"></a>Specifies the key type, which is <strong id="b84235270619443"><a name="b84235270619443"></a><a name="b84235270619443"></a>ssh</strong> by default.</p>
<p id="p144811212011"><a name="p144811212011"></a><a name="p144811212011"></a>This field is supported in microversions later than 2.2.</p>
</td>
</tr>
<tr id="row15156252"><td class="cellrowborder" valign="top" width="16.78%" headers="mcps1.2.4.1.1 "><p id="p19696890"><a name="p19696890"></a><a name="p19696890"></a>public_key</p>
</td>
<td class="cellrowborder" valign="top" width="16.04%" headers="mcps1.2.4.1.2 "><p id="p46735588"><a name="p46735588"></a><a name="p46735588"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67.17999999999999%" headers="mcps1.2.4.1.3 "><p id="p46049856"><a name="p46049856"></a><a name="p46049856"></a>Specifies information about the public key.</p>
</td>
</tr>
</tbody>
</table>

## Example Request<a name="section13755153085015"></a>

```
GET https://{endpoint}/v2/{project_id}/os-keypairs
GET https://{endpoint}/v2.1/{project_id}/os-keypairs
```

## Example Response<a name="section4713102134415"></a>

```
{
    "keypairs": [
        {
            "keypair": {
                "fingerprint": "15:b0:f8:b3:f9:48:63:71:cf:7b:5b:38:6d:44:2d:4a",
                "name": "keypair-601a2305-4f25-41ed-89c6-2a966fc8027a",
                "type": "ssh",
                "public_key": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAAgQC+Eo/RZRngaGTkFs7I62ZjsIlO79KklKbMXi8F+KITD4bVQHHn+kV+4gRgkgCRbdoDqoGfpaDFs877DYX9n4z6FrAIZ4PES8TNKhatifpn9NdQYWA+IkU8CuvlEKGuFpKRi/k7JLos/gHi2hy7QUwgtRvcefvD/vgQZOVw/mGR9Q== Generated-by-Nova\n"
            }
        }
    ]
}
```

## Returned Values<a name="section27088563"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

