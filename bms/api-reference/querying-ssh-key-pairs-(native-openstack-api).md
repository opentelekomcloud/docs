# Querying SSH Key Pairs \(Native OpenStack API\)<a name="EN-US_TOPIC_0060384658"></a>

## Function<a name="section17769131"></a>

This interface is used to query SSH key pairs and to display the query results in a list.

## Constraints<a name="section25186711103718"></a>

Pagination query is not supported.

## URI<a name="section40393097103718"></a>

GET /v2.1/\{project\_id\}/os-keypairs

[Table 1](#table875418115417)  lists the parameters.

**Table  1**  Parameter description

<a name="table875418115417"></a>
<table><thead align="left"><tr id="row20751518135416"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p67050730103718"><a name="p67050730103718"></a><a name="p67050730103718"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p62400032103718"><a name="p62400032103718"></a><a name="p62400032103718"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p21237868103718"><a name="p21237868103718"></a><a name="p21237868103718"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row675161812542"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p23650911103718"><a name="p23650911103718"></a><a name="p23650911103718"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p36675672103718"><a name="p36675672103718"></a><a name="p36675672103718"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p17939461103718"><a name="p17939461103718"></a><a name="p17939461103718"></a>Specifies the project ID.</p>
<p id="p9141450142010"><a name="p9141450142010"></a><a name="p9141450142010"></a>For how to obtain the project ID, see <a href="https://docs.otc.t-systems.com/en-us/api/apiug/apig-en-api-180328009.html" target="_blank" rel="noopener noreferrer">Obtaining Required Information</a>.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section43810255103718"></a>

-   Request parameters

    None

-   Example request

    ```
    GET https://{ECS Endpoint}/v2.1/bbf1946d374b44a0a2a95533562ba954/os-keypairs
    ```


## Response Message<a name="section60965769103718"></a>

-   Response parameters

    <a name="table27586210103718"></a>
    <table><thead align="left"><tr id="row41984926103718"><th class="cellrowborder" valign="top" width="22.48224822482248%" id="mcps1.1.4.1.1"><p id="p19987085"><a name="p19987085"></a><a name="p19987085"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="28.722872287228725%" id="mcps1.1.4.1.2"><p id="p4546697"><a name="p4546697"></a><a name="p4546697"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="48.7948794879488%" id="mcps1.1.4.1.3"><p id="p32738149"><a name="p32738149"></a><a name="p32738149"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row30149674103718"><td class="cellrowborder" valign="top" width="22.48224822482248%" headers="mcps1.1.4.1.1 "><p id="p26204567103718"><a name="p26204567103718"></a><a name="p26204567103718"></a>keypairs</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.722872287228725%" headers="mcps1.1.4.1.2 "><p id="p42195172103718"><a name="p42195172103718"></a><a name="p42195172103718"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.7948794879488%" headers="mcps1.1.4.1.3 "><p id="p62365753103718"><a name="p62365753103718"></a><a name="p62365753103718"></a>Specifies key pairs. For details, see <a href="#table31933500103718">Table 2</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2** **keypairs**  field data structure description

    <a name="table31933500103718"></a>
    <table><thead align="left"><tr id="row13327014103718"><th class="cellrowborder" valign="top" width="22.509999999999998%" id="mcps1.2.4.1.1"><p id="p898483610238"><a name="p898483610238"></a><a name="p898483610238"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="28.77%" id="mcps1.2.4.1.2"><p id="p398620365236"><a name="p398620365236"></a><a name="p398620365236"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="48.72%" id="mcps1.2.4.1.3"><p id="p69881436202319"><a name="p69881436202319"></a><a name="p69881436202319"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row65555086103718"><td class="cellrowborder" valign="top" width="22.509999999999998%" headers="mcps1.2.4.1.1 "><p id="p8361735103718"><a name="p8361735103718"></a><a name="p8361735103718"></a>keypair</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.77%" headers="mcps1.2.4.1.2 "><p id="p6211933103718"><a name="p6211933103718"></a><a name="p6211933103718"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.72%" headers="mcps1.2.4.1.3 "><p id="p33404535103718"><a name="p33404535103718"></a><a name="p33404535103718"></a>Specifies details about a key pair. For details, see <a href="#table58497453103718">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **keypair**  field data structure description

    <a name="table58497453103718"></a>
    <table><thead align="left"><tr id="row32349076103718"><th class="cellrowborder" valign="top" width="22.830000000000002%" id="mcps1.2.4.1.1"><p id="p97199488231"><a name="p97199488231"></a><a name="p97199488231"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="28.89%" id="mcps1.2.4.1.2"><p id="p20720548142312"><a name="p20720548142312"></a><a name="p20720548142312"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="48.28%" id="mcps1.2.4.1.3"><p id="p14724548132319"><a name="p14724548132319"></a><a name="p14724548132319"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row45087230103718"><td class="cellrowborder" valign="top" width="22.830000000000002%" headers="mcps1.2.4.1.1 "><p id="p28187038103718"><a name="p28187038103718"></a><a name="p28187038103718"></a>fingerprint</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.89%" headers="mcps1.2.4.1.2 "><p id="p1448759103718"><a name="p1448759103718"></a><a name="p1448759103718"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.28%" headers="mcps1.2.4.1.3 "><p id="p50240624103718"><a name="p50240624103718"></a><a name="p50240624103718"></a>Specifies fingerprint information about the key pair.</p>
    </td>
    </tr>
    <tr id="row49512432103718"><td class="cellrowborder" valign="top" width="22.830000000000002%" headers="mcps1.2.4.1.1 "><p id="p51084028103718"><a name="p51084028103718"></a><a name="p51084028103718"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.89%" headers="mcps1.2.4.1.2 "><p id="p44165629103718"><a name="p44165629103718"></a><a name="p44165629103718"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.28%" headers="mcps1.2.4.1.3 "><p id="p20646235103718"><a name="p20646235103718"></a><a name="p20646235103718"></a>Specifies the key pair name.</p>
    </td>
    </tr>
    <tr id="row5652164133420"><td class="cellrowborder" valign="top" width="22.830000000000002%" headers="mcps1.2.4.1.1 "><p id="p565314113349"><a name="p565314113349"></a><a name="p565314113349"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.89%" headers="mcps1.2.4.1.2 "><p id="p865354117348"><a name="p865354117348"></a><a name="p865354117348"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.28%" headers="mcps1.2.4.1.3 "><p id="p765344153418"><a name="p765344153418"></a><a name="p765344153418"></a>Specifies the key type, which is <strong id="b84235270619443"><a name="b84235270619443"></a><a name="b84235270619443"></a>ssh</strong> by default.</p>
    <p id="p2049715618353"><a name="p2049715618353"></a><a name="p2049715618353"></a>This field is supported in microversions later than 2.2.</p>
    </td>
    </tr>
    <tr id="row51598392103718"><td class="cellrowborder" valign="top" width="22.830000000000002%" headers="mcps1.2.4.1.1 "><p id="p18720236103718"><a name="p18720236103718"></a><a name="p18720236103718"></a>public_key</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.89%" headers="mcps1.2.4.1.2 "><p id="p39944111103718"><a name="p39944111103718"></a><a name="p39944111103718"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.28%" headers="mcps1.2.4.1.3 "><p id="p14247596103718"><a name="p14247596103718"></a><a name="p14247596103718"></a>Specifies information about the public key in the key pair.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "keypairs": [
            {
                "keypair": {
                    "fingerprint": "15:b0:f8:b3:f9:48:63:71:cf:7b:5b:38:6d:44:2d:4a",
                    "name": "keypair-test",
                    "type": "ssh",
                    "public_key": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAAgQC+Eo/RZRngaGTkFs7I62ZjsIlO79KklKbMXi8F+KITD4bVQHHn+kV+4gRgkgCRbdoDqoGfpaDFs877DYX9n4z6FrAIZ4PES8TNKhatifpn9NdQYWA+IkU8CuvlEKGuFpKRi/k7JLos/gHi2hy7QUwgtRvcefvD/vgQZOVw/mGR9Q== Generated-by-Nova"
                }
            }
        ]
    }
    ```


## Returned Values<a name="section7610951"></a>

Normal values

<a name="en-us_topic_0106040941_table753804619176"></a>
<table><thead align="left"><tr id="en-us_topic_0106040941_row10735134615172"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="en-us_topic_0106040941_p19735204616177"><a name="en-us_topic_0106040941_p19735204616177"></a><a name="en-us_topic_0106040941_p19735204616177"></a>Returned Values</p>
</th>
<th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="en-us_topic_0106040941_p207355465176"><a name="en-us_topic_0106040941_p207355465176"></a><a name="en-us_topic_0106040941_p207355465176"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0106040941_row1473514621713"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0106040941_p13735144611178"><a name="en-us_topic_0106040941_p13735144611178"></a><a name="en-us_topic_0106040941_p13735144611178"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0106040941_p207351246161711"><a name="en-us_topic_0106040941_p207351246161711"></a><a name="en-us_topic_0106040941_p207351246161711"></a>The server has successfully processed the request.</p>
</td>
</tr>
</tbody>
</table>

For details about other returned values, see  [Status Codes](status-codes.md).

## Error Codes<a name="section14752650154917"></a>

See  [Error Codes](error-codes.md).

