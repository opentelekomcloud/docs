# Querying the Quota of a User<a name="kms_02_0025"></a>

## Function<a name="en-us_topic_0112992292_section27849192112353"></a>

This API is used to query the quota of a user, that is, the allocated total number of CMKs that can be created by a user and the number of CMKs that has been created by the user.

>![](/images/icon-note.gif) **NOTE:**   
>The quota does not include Default Master Keys.  

## URI<a name="en-us_topic_0112992292_section35184599112353"></a>

-   URI format

    GET /v1.0/\{project\_id\}/kms/user-quotas

-   Parameter description

    **Table  1**  Parameter description

    <a name="en-us_topic_0112992292_table63109676112353"></a>
    <table><thead align="left"><tr id="en-us_topic_0112992292_row49827042112353"><th class="cellrowborder" valign="top" width="22.74%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992292_p9458563112353"><a name="en-us_topic_0112992292_p9458563112353"></a><a name="en-us_topic_0112992292_p9458563112353"></a><strong id="en-us_topic_0112992292_b8423527061924"><a name="en-us_topic_0112992292_b8423527061924"></a><a name="en-us_topic_0112992292_b8423527061924"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.919999999999998%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992292_p27946133112353"><a name="en-us_topic_0112992292_p27946133112353"></a><a name="en-us_topic_0112992292_p27946133112353"></a><strong id="en-us_topic_0112992292_b84235270619210"><a name="en-us_topic_0112992292_b84235270619210"></a><a name="en-us_topic_0112992292_b84235270619210"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.55%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992292_p49044287112353"><a name="en-us_topic_0112992292_p49044287112353"></a><a name="en-us_topic_0112992292_p49044287112353"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="40.79%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992292_p13164330112353"><a name="en-us_topic_0112992292_p13164330112353"></a><a name="en-us_topic_0112992292_p13164330112353"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0112992292_row59677822112353"><td class="cellrowborder" valign="top" width="22.74%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992292_p2065377112353"><a name="en-us_topic_0112992292_p2065377112353"></a><a name="en-us_topic_0112992292_p2065377112353"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992292_p33077886112353"><a name="en-us_topic_0112992292_p33077886112353"></a><a name="en-us_topic_0112992292_p33077886112353"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.55%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992292_p62063099112353"><a name="en-us_topic_0112992292_p62063099112353"></a><a name="en-us_topic_0112992292_p62063099112353"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.79%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992292_p61055104112353"><a name="en-us_topic_0112992292_p61055104112353"></a><a name="en-us_topic_0112992292_p61055104112353"></a>Project ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Requests<a name="en-us_topic_0112992292_section12625030112353"></a>

None

## Responses<a name="en-us_topic_0112992292_section15686020"></a>

**Table  2**  Response parameters

<a name="en-us_topic_0112992292_table57089888113143"></a>
<table><thead align="left"><tr id="en-us_topic_0112992292_row44406426113143"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992292_p40150733113143"><a name="en-us_topic_0112992292_p40150733113143"></a><a name="en-us_topic_0112992292_p40150733113143"></a><strong id="en-us_topic_0112992292_b84235270619232"><a name="en-us_topic_0112992292_b84235270619232"></a><a name="en-us_topic_0112992292_b84235270619232"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992292_p26668948113143"><a name="en-us_topic_0112992292_p26668948113143"></a><a name="en-us_topic_0112992292_p26668948113143"></a><strong id="en-us_topic_0112992292_b84235270619240"><a name="en-us_topic_0112992292_b84235270619240"></a><a name="en-us_topic_0112992292_b84235270619240"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992292_p30983912113143"><a name="en-us_topic_0112992292_p30983912113143"></a><a name="en-us_topic_0112992292_p30983912113143"></a><strong id="en-us_topic_0112992292_b84235270619236"><a name="en-us_topic_0112992292_b84235270619236"></a><a name="en-us_topic_0112992292_b84235270619236"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992292_p12701176113143"><a name="en-us_topic_0112992292_p12701176113143"></a><a name="en-us_topic_0112992292_p12701176113143"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992292_row22162365113143"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992292_p50321163113143"><a name="en-us_topic_0112992292_p50321163113143"></a><a name="en-us_topic_0112992292_p50321163113143"></a>quotas</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992292_p48649567113143"><a name="en-us_topic_0112992292_p48649567113143"></a><a name="en-us_topic_0112992292_p48649567113143"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992292_p49482377113143"><a name="en-us_topic_0112992292_p49482377113143"></a><a name="en-us_topic_0112992292_p49482377113143"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992292_p48300854113143"><a name="en-us_topic_0112992292_p48300854113143"></a><a name="en-us_topic_0112992292_p48300854113143"></a>Quota list. For details, see <a href="#en-us_topic_0112992292_table91213810301">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **quotas**  field description

<a name="en-us_topic_0112992292_table91213810301"></a>
<table><thead align="left"><tr id="en-us_topic_0112992292_row1812219893014"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992292_p270818432314"><a name="en-us_topic_0112992292_p270818432314"></a><a name="en-us_topic_0112992292_p270818432314"></a><strong id="en-us_topic_0112992292_b138440703"><a name="en-us_topic_0112992292_b138440703"></a><a name="en-us_topic_0112992292_b138440703"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992292_p0708144373116"><a name="en-us_topic_0112992292_p0708144373116"></a><a name="en-us_topic_0112992292_p0708144373116"></a><strong id="en-us_topic_0112992292_b1740257363"><a name="en-us_topic_0112992292_b1740257363"></a><a name="en-us_topic_0112992292_b1740257363"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992292_p37081843133115"><a name="en-us_topic_0112992292_p37081843133115"></a><a name="en-us_topic_0112992292_p37081843133115"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992292_p10708204343110"><a name="en-us_topic_0112992292_p10708204343110"></a><a name="en-us_topic_0112992292_p10708204343110"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992292_row1212288203011"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992292_p158526571311"><a name="en-us_topic_0112992292_p158526571311"></a><a name="en-us_topic_0112992292_p158526571311"></a>resources</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992292_p385275711314"><a name="en-us_topic_0112992292_p385275711314"></a><a name="en-us_topic_0112992292_p385275711314"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992292_p1852105712316"><a name="en-us_topic_0112992292_p1852105712316"></a><a name="en-us_topic_0112992292_p1852105712316"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992292_p188521457103115"><a name="en-us_topic_0112992292_p188521457103115"></a><a name="en-us_topic_0112992292_p188521457103115"></a>Resource quota list. For details, see <a href="#en-us_topic_0112992292_table167809412315">Table 4</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **resources**  field description

<a name="en-us_topic_0112992292_table167809412315"></a>
<table><thead align="left"><tr id="en-us_topic_0112992292_row1278094143119"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992292_p9231545143120"><a name="en-us_topic_0112992292_p9231545143120"></a><a name="en-us_topic_0112992292_p9231545143120"></a><strong id="en-us_topic_0112992292_b1900110896"><a name="en-us_topic_0112992292_b1900110896"></a><a name="en-us_topic_0112992292_b1900110896"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992292_p1523245183111"><a name="en-us_topic_0112992292_p1523245183111"></a><a name="en-us_topic_0112992292_p1523245183111"></a><strong id="en-us_topic_0112992292_b2128767927"><a name="en-us_topic_0112992292_b2128767927"></a><a name="en-us_topic_0112992292_b2128767927"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992292_p1823545193118"><a name="en-us_topic_0112992292_p1823545193118"></a><a name="en-us_topic_0112992292_p1823545193118"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992292_p19231145193119"><a name="en-us_topic_0112992292_p19231145193119"></a><a name="en-us_topic_0112992292_p19231145193119"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992292_row10780154133117"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992292_p04621010163215"><a name="en-us_topic_0112992292_p04621010163215"></a><a name="en-us_topic_0112992292_p04621010163215"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992292_p1462181053214"><a name="en-us_topic_0112992292_p1462181053214"></a><a name="en-us_topic_0112992292_p1462181053214"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992292_p746261063219"><a name="en-us_topic_0112992292_p746261063219"></a><a name="en-us_topic_0112992292_p746261063219"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992292_p16462210163219"><a name="en-us_topic_0112992292_p16462210163219"></a><a name="en-us_topic_0112992292_p16462210163219"></a>Quota type.</p>
<p id="en-us_topic_0112992292_p1246201014323"><a name="en-us_topic_0112992292_p1246201014323"></a><a name="en-us_topic_0112992292_p1246201014323"></a>Enumerated values:</p>
<a name="en-us_topic_0112992292_ul446210103324"></a><a name="en-us_topic_0112992292_ul446210103324"></a><ul id="en-us_topic_0112992292_ul446210103324"><li><strong id="en-us_topic_0112992292_b775316212144618"><a name="en-us_topic_0112992292_b775316212144618"></a><a name="en-us_topic_0112992292_b775316212144618"></a>CMK</strong> indicates a Customer Master Key.</li><li><strong id="en-us_topic_0112992292_b84235270614475"><a name="en-us_topic_0112992292_b84235270614475"></a><a name="en-us_topic_0112992292_b84235270614475"></a>grant_per_CMK</strong> indicates the number of grants that can be created on a CMK.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0112992292_row1978119418318"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992292_p2463201083213"><a name="en-us_topic_0112992292_p2463201083213"></a><a name="en-us_topic_0112992292_p2463201083213"></a>used</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992292_p1446331012321"><a name="en-us_topic_0112992292_p1446331012321"></a><a name="en-us_topic_0112992292_p1446331012321"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992292_p11463181019323"><a name="en-us_topic_0112992292_p11463181019323"></a><a name="en-us_topic_0112992292_p11463181019323"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992292_p1046331043211"><a name="en-us_topic_0112992292_p1046331043211"></a><a name="en-us_topic_0112992292_p1046331043211"></a>Used quota</p>
</td>
</tr>
<tr id="en-us_topic_0112992292_row978111473112"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992292_p15463210143211"><a name="en-us_topic_0112992292_p15463210143211"></a><a name="en-us_topic_0112992292_p15463210143211"></a>quota</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992292_p114631210113216"><a name="en-us_topic_0112992292_p114631210113216"></a><a name="en-us_topic_0112992292_p114631210113216"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992292_p10463131063212"><a name="en-us_topic_0112992292_p10463131063212"></a><a name="en-us_topic_0112992292_p10463131063212"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992292_p1146351023210"><a name="en-us_topic_0112992292_p1146351023210"></a><a name="en-us_topic_0112992292_p1146351023210"></a>Total quota</p>
</td>
</tr>
</tbody>
</table>

## Examples<a name="en-us_topic_0112992292_section169469372415"></a>

-   Example request

    None

-   Example response

    ```
    {
        "quotas": {
            "resources": [
                {
                    "type": "CMK",
                    "used": 15,
                    "quota": 20
                },
                {
                    "type": "grant_per_CMK",
                    "used": 15,
                    "quota": 100
                }
    
            ]
        }
    }
    ```

    or

    ```
    {
        "error": {
            "error_code": "KMS.XXXX",
            "error_msg": "XXX"
        }
    }
    ```


## Status Codes<a name="en-us_topic_0112992292_section3454223421"></a>

[Table 5](#en-us_topic_0112992292_en-us_topic_0112992294_en-us_topic_0079615001_table20596071)  lists the normal status code returned by the response.

**Table  5**  Status codes

<a name="en-us_topic_0112992292_en-us_topic_0112992294_en-us_topic_0079615001_table20596071"></a>
<table><thead align="left"><tr id="en-us_topic_0112992292_en-us_topic_0112992294_en-us_topic_0079615001_row9746163"><th class="cellrowborder" valign="top" width="22%" id="mcps1.2.4.1.1"><p id="en-us_topic_0112992292_en-us_topic_0112992294_p57545694203043"><a name="en-us_topic_0112992292_en-us_topic_0112992294_p57545694203043"></a><a name="en-us_topic_0112992292_en-us_topic_0112992294_p57545694203043"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="32%" id="mcps1.2.4.1.2"><p id="en-us_topic_0112992292_en-us_topic_0112992294_p4531342288"><a name="en-us_topic_0112992292_en-us_topic_0112992294_p4531342288"></a><a name="en-us_topic_0112992292_en-us_topic_0112992294_p4531342288"></a>Status</p>
</th>
<th class="cellrowborder" valign="top" width="46%" id="mcps1.2.4.1.3"><p id="en-us_topic_0112992292_en-us_topic_0112992294_p30689603203043"><a name="en-us_topic_0112992292_en-us_topic_0112992294_p30689603203043"></a><a name="en-us_topic_0112992292_en-us_topic_0112992294_p30689603203043"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992292_en-us_topic_0112992294_en-us_topic_0079615001_row48621261"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0112992292_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"><a name="en-us_topic_0112992292_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"></a><a name="en-us_topic_0112992292_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0112992292_en-us_topic_0112992294_p7538425819"><a name="en-us_topic_0112992292_en-us_topic_0112992294_p7538425819"></a><a name="en-us_topic_0112992292_en-us_topic_0112992294_p7538425819"></a>OK</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0112992292_en-us_topic_0112992294_p1885682315512"><a name="en-us_topic_0112992292_en-us_topic_0112992294_p1885682315512"></a><a name="en-us_topic_0112992292_en-us_topic_0112992294_p1885682315512"></a>Request processed successfully.</p>
</td>
</tr>
</tbody>
</table>

Exception status code. For details, see  [Status Codes](status-codes.md#kms_02_0301).

