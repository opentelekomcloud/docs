# Importing CMK Material<a name="kms_02_0036"></a>

## Function<a name="en-us_topic_0112992337_section2809137816511"></a>

This API allows you to import CMK material.

## URI<a name="en-us_topic_0112992337_section3802320916511"></a>

-   URI format

    POST /v1.0/\{project\_id\}/kms/import-key-material

-   Parameter description

    **Table  1**  Parameter description

    <a name="en-us_topic_0112992337_table964209216511"></a>
    <table><thead align="left"><tr id="en-us_topic_0112992337_row1607974516511"><th class="cellrowborder" valign="top" width="22.74%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992337_p2739096916511"><a name="en-us_topic_0112992337_p2739096916511"></a><a name="en-us_topic_0112992337_p2739096916511"></a><strong id="en-us_topic_0112992337_b842352706195551"><a name="en-us_topic_0112992337_b842352706195551"></a><a name="en-us_topic_0112992337_b842352706195551"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.919999999999998%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992337_p407603016511"><a name="en-us_topic_0112992337_p407603016511"></a><a name="en-us_topic_0112992337_p407603016511"></a><strong id="en-us_topic_0112992337_b842352706195553"><a name="en-us_topic_0112992337_b842352706195553"></a><a name="en-us_topic_0112992337_b842352706195553"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.55%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992337_p6172299916511"><a name="en-us_topic_0112992337_p6172299916511"></a><a name="en-us_topic_0112992337_p6172299916511"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="40.79%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992337_p3350702116511"><a name="en-us_topic_0112992337_p3350702116511"></a><a name="en-us_topic_0112992337_p3350702116511"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0112992337_row2971415116511"><td class="cellrowborder" valign="top" width="22.74%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992337_p5803601316511"><a name="en-us_topic_0112992337_p5803601316511"></a><a name="en-us_topic_0112992337_p5803601316511"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992337_p329664916511"><a name="en-us_topic_0112992337_p329664916511"></a><a name="en-us_topic_0112992337_p329664916511"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.55%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992337_p4386100291125"><a name="en-us_topic_0112992337_p4386100291125"></a><a name="en-us_topic_0112992337_p4386100291125"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.79%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992337_p2026050816511"><a name="en-us_topic_0112992337_p2026050816511"></a><a name="en-us_topic_0112992337_p2026050816511"></a>Project ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Requests<a name="en-us_topic_0112992337_section4812685216511"></a>

**Table  2**  Request parameters

<a name="en-us_topic_0112992337_table1307199216511"></a>
<table><thead align="left"><tr id="en-us_topic_0112992337_row2216064416511"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992337_p16445506549"><a name="en-us_topic_0112992337_p16445506549"></a><a name="en-us_topic_0112992337_p16445506549"></a><strong id="en-us_topic_0112992337_b1531119383"><a name="en-us_topic_0112992337_b1531119383"></a><a name="en-us_topic_0112992337_b1531119383"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992337_p19645165016541"><a name="en-us_topic_0112992337_p19645165016541"></a><a name="en-us_topic_0112992337_p19645165016541"></a><strong id="en-us_topic_0112992337_b1965255946"><a name="en-us_topic_0112992337_b1965255946"></a><a name="en-us_topic_0112992337_b1965255946"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992337_p26451450155411"><a name="en-us_topic_0112992337_p26451450155411"></a><a name="en-us_topic_0112992337_p26451450155411"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992337_p126453508548"><a name="en-us_topic_0112992337_p126453508548"></a><a name="en-us_topic_0112992337_p126453508548"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992337_row990996316511"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992337_p6450954916511"><a name="en-us_topic_0112992337_p6450954916511"></a><a name="en-us_topic_0112992337_p6450954916511"></a>key_id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992337_p5865974316511"><a name="en-us_topic_0112992337_p5865974316511"></a><a name="en-us_topic_0112992337_p5865974316511"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992337_p739071615716"><a name="en-us_topic_0112992337_p739071615716"></a><a name="en-us_topic_0112992337_p739071615716"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992337_p5381875116511"><a name="en-us_topic_0112992337_p5381875116511"></a><a name="en-us_topic_0112992337_p5381875116511"></a>36-byte ID of a CMK that matches the regular expression <span class="parmvalue" id="en-us_topic_0112992337_parmvalue80435593163333"><a name="en-us_topic_0112992337_parmvalue80435593163333"></a><a name="en-us_topic_0112992337_parmvalue80435593163333"></a><b>^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$</b></span></p>
<p id="en-us_topic_0112992337_p4509346016511"><a name="en-us_topic_0112992337_p4509346016511"></a><a name="en-us_topic_0112992337_p4509346016511"></a>Example: 0d0466b0-e727-4d9c-b35d-f84bb474a37f</p>
</td>
</tr>
<tr id="en-us_topic_0112992337_row2869160916511"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992337_p1322852165315"><a name="en-us_topic_0112992337_p1322852165315"></a><a name="en-us_topic_0112992337_p1322852165315"></a>import_token</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992337_p2539755516511"><a name="en-us_topic_0112992337_p2539755516511"></a><a name="en-us_topic_0112992337_p2539755516511"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992337_p1839414165712"><a name="en-us_topic_0112992337_p1839414165712"></a><a name="en-us_topic_0112992337_p1839414165712"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992337_p43447950172527"><a name="en-us_topic_0112992337_p43447950172527"></a><a name="en-us_topic_0112992337_p43447950172527"></a>CMK import token in Base64 format that matches the regular expression <strong id="en-us_topic_0112992337_b84235270616524"><a name="en-us_topic_0112992337_b84235270616524"></a><a name="en-us_topic_0112992337_b84235270616524"></a>^[0-9a-zA-Z+/=]{200,6144}$</strong></p>
</td>
</tr>
<tr id="en-us_topic_0112992337_row4675342116511"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992337_p35037151172738"><a name="en-us_topic_0112992337_p35037151172738"></a><a name="en-us_topic_0112992337_p35037151172738"></a>encrypted_key_material</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992337_p3090833716511"><a name="en-us_topic_0112992337_p3090833716511"></a><a name="en-us_topic_0112992337_p3090833716511"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992337_p1139612168718"><a name="en-us_topic_0112992337_p1139612168718"></a><a name="en-us_topic_0112992337_p1139612168718"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992337_p79390172758"><a name="en-us_topic_0112992337_p79390172758"></a><a name="en-us_topic_0112992337_p79390172758"></a>Encrypted CMK material in Base64 format that matches the regular expression ^[0-9a-zA-Z+/=]{344,360}$</p>
</td>
</tr>
<tr id="en-us_topic_0112992337_row19978824172316"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992337_p35515283172331"><a name="en-us_topic_0112992337_p35515283172331"></a><a name="en-us_topic_0112992337_p35515283172331"></a>expiration_time</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992337_p45942097172315"><a name="en-us_topic_0112992337_p45942097172315"></a><a name="en-us_topic_0112992337_p45942097172315"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992337_p22936807172315"><a name="en-us_topic_0112992337_p22936807172315"></a><a name="en-us_topic_0112992337_p22936807172315"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992337_p6745480102415"><a name="en-us_topic_0112992337_p6745480102415"></a><a name="en-us_topic_0112992337_p6745480102415"></a>Expiration time of the key material. The value is a timestamp expressed in the number of seconds since 00:00:00 UTC on January 1, 1970. KMS will delete the key material within 24 hours after the expiration.</p>
<p id="en-us_topic_0112992337_p4189223172358"><a name="en-us_topic_0112992337_p4189223172358"></a><a name="en-us_topic_0112992337_p4189223172358"></a>Example: 1550291833</p>
</td>
</tr>
<tr id="en-us_topic_0112992337_row32405724172319"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992337_p43470570172317"><a name="en-us_topic_0112992337_p43470570172317"></a><a name="en-us_topic_0112992337_p43470570172317"></a>sequence</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992337_p64847261172317"><a name="en-us_topic_0112992337_p64847261172317"></a><a name="en-us_topic_0112992337_p64847261172317"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992337_p16911172712717"><a name="en-us_topic_0112992337_p16911172712717"></a><a name="en-us_topic_0112992337_p16911172712717"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992337_p3371101522920"><a name="en-us_topic_0112992337_p3371101522920"></a><a name="en-us_topic_0112992337_p3371101522920"></a>36-byte serial number of a request message</p>
<p id="en-us_topic_0112992337_p18136822172317"><a name="en-us_topic_0112992337_p18136822172317"></a><a name="en-us_topic_0112992337_p18136822172317"></a>Example: 919c82d4-8046-4722-9094-35c3c6524cff</p>
</td>
</tr>
</tbody>
</table>

## Responses<a name="en-us_topic_0112992337_section5661868116511"></a>

None

## Examples<a name="en-us_topic_0112992337_section1169411326275"></a>

The following example describes how to import the CMK material and the import-token to the CMK whose ID is  **bb6a3d22-dc93-47ac-b5bd-88df7ad35f1e**, and set the expiration time of the CMK material to  **1521578672**.

-   Example request

    ```
    {      
        "key_id": "bb6a3d22-dc93-47ac-b5bd-88df7ad35f1e",
        "import_token":"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",
        "encrypted_key_material":"K+ixymtl90e+B5Rdan89KjDslBIoOexrIwzkYHGz3odS7FDXDkogqbWwwJg5wQ6zjUbEvsR/+Fi+A0SSkhhqtijivOKHu4Z86RWjOCBdrr9es+ZhJ0zYBNMN+7Rf2fd9vxbb873Q7VBkJRyH1hi3Wh+kLmDW4rpWZm4+YGCtWylz7ZKbV1KBlhSNLDtZzT4nxUra0p7Die4HgUUxSjZTOr/0s71yF6o2eysreIzIl+GbpCft0WpRsxN2Ng++ntgOcwOf2zOC9o/tjraxeAvgGw+Dwt4cjF4znnFf0LPQ2YvpNUo248LjAGxdFvzUABNzfYSj3RZ0K3wQCNAcXU3HYw==",
        "expiration_time":1521578672
    }
    ```

-   Example response

    ```
    {
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


## Status Codes<a name="en-us_topic_0112992337_section655115613254"></a>

[Table 3](#en-us_topic_0112992337_en-us_topic_0112992294_en-us_topic_0079615001_table20596071)  lists the normal status code returned by the response.

**Table  3**  Status codes

<a name="en-us_topic_0112992337_en-us_topic_0112992294_en-us_topic_0079615001_table20596071"></a>
<table><thead align="left"><tr id="en-us_topic_0112992337_en-us_topic_0112992294_en-us_topic_0079615001_row9746163"><th class="cellrowborder" valign="top" width="22%" id="mcps1.2.4.1.1"><p id="en-us_topic_0112992337_en-us_topic_0112992294_p57545694203043"><a name="en-us_topic_0112992337_en-us_topic_0112992294_p57545694203043"></a><a name="en-us_topic_0112992337_en-us_topic_0112992294_p57545694203043"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="32%" id="mcps1.2.4.1.2"><p id="en-us_topic_0112992337_en-us_topic_0112992294_p4531342288"><a name="en-us_topic_0112992337_en-us_topic_0112992294_p4531342288"></a><a name="en-us_topic_0112992337_en-us_topic_0112992294_p4531342288"></a>Status</p>
</th>
<th class="cellrowborder" valign="top" width="46%" id="mcps1.2.4.1.3"><p id="en-us_topic_0112992337_en-us_topic_0112992294_p30689603203043"><a name="en-us_topic_0112992337_en-us_topic_0112992294_p30689603203043"></a><a name="en-us_topic_0112992337_en-us_topic_0112992294_p30689603203043"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992337_en-us_topic_0112992294_en-us_topic_0079615001_row48621261"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0112992337_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"><a name="en-us_topic_0112992337_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"></a><a name="en-us_topic_0112992337_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0112992337_en-us_topic_0112992294_p7538425819"><a name="en-us_topic_0112992337_en-us_topic_0112992294_p7538425819"></a><a name="en-us_topic_0112992337_en-us_topic_0112992294_p7538425819"></a>OK</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0112992337_en-us_topic_0112992294_p1885682315512"><a name="en-us_topic_0112992337_en-us_topic_0112992294_p1885682315512"></a><a name="en-us_topic_0112992337_en-us_topic_0112992294_p1885682315512"></a>Request processed successfully.</p>
</td>
</tr>
</tbody>
</table>

Exception status code. For details, see  [Status Codes](status-codes.md#kms_02_0301).

