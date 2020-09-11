# Batch Adding or Deleting Whitelist Records<a name="vpcep_06_0209"></a>

## Function<a name="section1779922"></a>

This API is used to batch add to or delete whitelist records from a VPC endpoint service.

>![](/images/icon-note.gif) **NOTE:** 
>Your domain ID is in the whitelist of your own VPC endpoint service by default.

## URI<a name="section16019298"></a>

POST /v1/\{project\_id\}/vpc-endpoint-services/\{vpc\_endpoint\_service\_id\}/permissions/action

[Table 1](#table16108480)  describes the required parameters.

**Table  1**  Parameters

<a name="table16108480"></a>
<table><thead align="left"><tr id="row34443075"><th class="cellrowborder" valign="top" width="32.65%" id="mcps1.2.4.1.1"><p id="p38425723"><a name="p38425723"></a><a name="p38425723"></a><strong id="b88821758165117"><a name="b88821758165117"></a><a name="b88821758165117"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26.529999999999998%" id="mcps1.2.4.1.2"><p id="p25475843"><a name="p25475843"></a><a name="p25475843"></a><strong id="b176481159175118"><a name="b176481159175118"></a><a name="b176481159175118"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="40.82%" id="mcps1.2.4.1.3"><p id="p50277379"><a name="p50277379"></a><a name="p50277379"></a><strong id="b16569305528"><a name="b16569305528"></a><a name="b16569305528"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row45935908"><td class="cellrowborder" valign="top" width="32.65%" headers="mcps1.2.4.1.1 "><p id="p29821069"><a name="p29821069"></a><a name="p29821069"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.2 "><p id="p66696423"><a name="p66696423"></a><a name="p66696423"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="40.82%" headers="mcps1.2.4.1.3 "><p id="p33701210"><a name="p33701210"></a><a name="p33701210"></a>Specifies the project ID. For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
</td>
</tr>
<tr id="row34875436"><td class="cellrowborder" valign="top" width="32.65%" headers="mcps1.2.4.1.1 "><p id="p6338038"><a name="p6338038"></a><a name="p6338038"></a>vpc_endpoint_service_id</p>
</td>
<td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.2 "><p id="p43619052"><a name="p43619052"></a><a name="p43619052"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="40.82%" headers="mcps1.2.4.1.3 "><p id="p43482360"><a name="p43482360"></a><a name="p43482360"></a>Specifies the ID of the VPC endpoint service.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section9955955"></a>

-   Parameter description

    **Table  2**  Request parameters

    <a name="table10758598"></a>
    <table><thead align="left"><tr id="row52439445"><th class="cellrowborder" valign="top" width="14.66%" id="mcps1.2.5.1.1"><p id="p19736666"><a name="p19736666"></a><a name="p19736666"></a><strong id="b487721515524"><a name="b487721515524"></a><a name="b487721515524"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="11.27%" id="mcps1.2.5.1.2"><p id="p20637053172113"><a name="p20637053172113"></a><a name="p20637053172113"></a><strong id="b11256164710358"><a name="b11256164710358"></a><a name="b11256164710358"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="15.75%" id="mcps1.2.5.1.3"><p id="p55166099"><a name="p55166099"></a><a name="p55166099"></a><strong id="b5530133416520"><a name="b5530133416520"></a><a name="b5530133416520"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="58.32000000000001%" id="mcps1.2.5.1.4"><p id="p39269033"><a name="p39269033"></a><a name="p39269033"></a><strong id="b1108187722"><a name="b1108187722"></a><a name="b1108187722"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row26675075"><td class="cellrowborder" valign="top" width="14.66%" headers="mcps1.2.5.1.1 "><p id="p13197449"><a name="p13197449"></a><a name="p13197449"></a>permissions</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.27%" headers="mcps1.2.5.1.2 "><p id="p176371453152114"><a name="p176371453152114"></a><a name="p176371453152114"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.75%" headers="mcps1.2.5.1.3 "><p id="p62360485"><a name="p62360485"></a><a name="p62360485"></a>Array of strings</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.32000000000001%" headers="mcps1.2.5.1.4 "><p id="p18034492"><a name="p18034492"></a><a name="p18034492"></a>Lists the whitelist records.</p>
    <p id="p397711547482"><a name="p397711547482"></a><a name="p397711547482"></a>The permission format is <strong id="b84961501159"><a name="b84961501159"></a><a name="b84961501159"></a>iam:domain:: 6e9dfd51d1124e8d8498dce894923a0d</strong> or <strong id="b104972017516"><a name="b104972017516"></a><a name="b104972017516"></a>*</strong>. <strong id="b54983012520"><a name="b54983012520"></a><a name="b54983012520"></a>*</strong> indicates all users can connect to the VPC endpoint service. <strong id="b6791154917557"><a name="b6791154917557"></a><a name="b6791154917557"></a>6e9dfd51d1124e8d8498dce894923a0d</strong> indicates the domain ID of the user.</p>
    </td>
    </tr>
    <tr id="row28092706"><td class="cellrowborder" valign="top" width="14.66%" headers="mcps1.2.5.1.1 "><p id="p60916736"><a name="p60916736"></a><a name="p60916736"></a>action</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.27%" headers="mcps1.2.5.1.2 "><p id="p15637165313211"><a name="p15637165313211"></a><a name="p15637165313211"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.75%" headers="mcps1.2.5.1.3 "><p id="p35308558"><a name="p35308558"></a><a name="p35308558"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.32000000000001%" headers="mcps1.2.5.1.4 "><p id="p183695194593"><a name="p183695194593"></a><a name="p183695194593"></a>Specifies the operation to be performed.</p>
    <p id="p41420916"><a name="p41420916"></a><a name="p41420916"></a>The value is <strong id="b129245133539"><a name="b129245133539"></a><a name="b129245133539"></a>add</strong> or <strong id="b260781915531"><a name="b260781915531"></a><a name="b260781915531"></a>remove</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    This request is to add a whitelist record to the VPC endpoint service whose ID is  **4189d3c2-8882-4871-a3c2-d380272eed88**.

    ```
    POST https://{endpoint}/v1/{project_id}/vpc-endpoint-services/4189d3c2-8882-4871-a3c2-d380272eed88/permissions/action
    ```

    ```
    {
        "permissions":
          [
            "iam:domain::5fc973eea581490997e82ea11a1d0101",
          ],
        "action":"add"
    } 
    ```

    This request is to delete a whitelist record from the VPC endpoint service whose ID is  **4189d3c2-8882-4871-a3c2-d380272eed88**.

    ```
    POST https://{endpoint}/v1/{project_id}/vpc-endpoint-services/4189d3c2-8882-4871-a3c2-d380272eed88/iam:domain::5fc973eea581490997e82ea11a1d0101/action
    ```

    ```
    {
      "permissions":
        [
          "iam:domain::5fc973eea581490997e82ea11a1d0101",
        ],
       "action":"remove"
    }
    ```


## Response<a name="section1126021"></a>

-   Parameter description

    **Table  3**  Response parameters

    <a name="table29718523"></a>
    <table><thead align="left"><tr id="row41415880"><th class="cellrowborder" valign="top" width="28.28282828282828%" id="mcps1.2.4.1.1"><p id="p66352009"><a name="p66352009"></a><a name="p66352009"></a><strong id="b109076159"><a name="b109076159"></a><a name="b109076159"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="30.303030303030305%" id="mcps1.2.4.1.2"><p id="p5803687"><a name="p5803687"></a><a name="p5803687"></a><strong id="b1738258915"><a name="b1738258915"></a><a name="b1738258915"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="41.41414141414141%" id="mcps1.2.4.1.3"><p id="p336649"><a name="p336649"></a><a name="p336649"></a><strong id="b1454753994"><a name="b1454753994"></a><a name="b1454753994"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row27268632"><td class="cellrowborder" valign="top" width="28.28282828282828%" headers="mcps1.2.4.1.1 "><p id="p61275579"><a name="p61275579"></a><a name="p61275579"></a>permissions</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.2 "><p id="p04210448589"><a name="p04210448589"></a><a name="p04210448589"></a>Array of strings</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.41414141414141%" headers="mcps1.2.4.1.3 "><p id="p8301318441"><a name="p8301318441"></a><a name="p8301318441"></a>Lists the whitelist records.</p>
    <p id="p12963317204216"><a name="p12963317204216"></a><a name="p12963317204216"></a>The permission format is <strong id="b1126124011505"><a name="b1126124011505"></a><a name="b1126124011505"></a>iam:domain:: 6e9dfd51d1124e8d8498dce894923a0d</strong> or <strong id="b4281740125018"><a name="b4281740125018"></a><a name="b4281740125018"></a>*</strong>. <strong id="b1028840105010"><a name="b1028840105010"></a><a name="b1028840105010"></a>*</strong> indicates all users can connect to the VPC endpoint service. <strong id="b1285813487500"><a name="b1285813487500"></a><a name="b1285813487500"></a>6e9dfd51d1124e8d8498dce894923a0d</strong> indicates the domain ID of the user.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
      "permissions":
        [
          "iam:domain::5fc973eea581490997e82ea11a1d0101",
          "iam:domain::5fc973eea581490997e82ea11a1d0102"
          ]
    }
    ```


## Status Code<a name="section24098863"></a>

For details about status codes, see  [Status Code](/vpcep/api-reference/common/status-code.md).

