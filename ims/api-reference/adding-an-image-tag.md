# Adding an Image Tag<a name="EN-US_TOPIC_0102682863"></a>

## Function<a name="section10905330183640"></a>

This API is used to add a tag to an image or update a tag.

## Constraints<a name="section31140086183640"></a>

-   Each tag consists of a key and a value. The key contains at most 36 characters, and the value contains at most 43 characters. The key cannot be left blank or an empty character string. The value cannot be left blank but can be an empty character string.
-   An image can have a maximum of 10 tags.
-   This API is an idempotent API. If a tag to be added has the same key as an existing tag, but the tag values are different, this tag will be added and overwrite the existing one. If a tag to be added has the same key and value as an existing tag, this tag will not be added.

## URI<a name="section66183038183640"></a>

POST /v2/\{project\_id\}/images/\{image\_id\}/tags

[Table 1](#table51217005183640)  lists the parameters in the URI.

**Table  1**  Parameter description

<a name="table51217005183640"></a>
<table><thead align="left"><tr id="row52286949183640"><th class="cellrowborder" valign="top" width="18.55814418558144%" id="mcps1.2.5.1.1"><p id="p7384511183640"><a name="p7384511183640"></a><a name="p7384511183640"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19.58804119588041%" id="mcps1.2.5.1.2"><p id="p61274546183640"><a name="p61274546183640"></a><a name="p61274546183640"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="30.926907309269076%" id="mcps1.2.5.1.3"><p id="p64291173183640"><a name="p64291173183640"></a><a name="p64291173183640"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="30.926907309269076%" id="mcps1.2.5.1.4"><p id="p40202496183640"><a name="p40202496183640"></a><a name="p40202496183640"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row35176748183640"><td class="cellrowborder" valign="top" width="18.55814418558144%" headers="mcps1.2.5.1.1 "><p id="p30744336183640"><a name="p30744336183640"></a><a name="p30744336183640"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.58804119588041%" headers="mcps1.2.5.1.2 "><p id="p7263317183640"><a name="p7263317183640"></a><a name="p7263317183640"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="30.926907309269076%" headers="mcps1.2.5.1.3 "><p id="p51457827183640"><a name="p51457827183640"></a><a name="p51457827183640"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="30.926907309269076%" headers="mcps1.2.5.1.4 "><p id="p7334433183640"><a name="p7334433183640"></a><a name="p7334433183640"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row66009897183640"><td class="cellrowborder" valign="top" width="18.55814418558144%" headers="mcps1.2.5.1.1 "><p id="p45201459183640"><a name="p45201459183640"></a><a name="p45201459183640"></a>image_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.58804119588041%" headers="mcps1.2.5.1.2 "><p id="p37439553183640"><a name="p37439553183640"></a><a name="p37439553183640"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="30.926907309269076%" headers="mcps1.2.5.1.3 "><p id="p12704956183640"><a name="p12704956183640"></a><a name="p12704956183640"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="30.926907309269076%" headers="mcps1.2.5.1.4 "><p id="p22468491183640"><a name="p22468491183640"></a><a name="p22468491183640"></a>Specifies the image ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section889830183640"></a>

-   Request parameters

    <a name="table66813056183640"></a>
    <table><thead align="left"><tr id="row17712916183640"><th class="cellrowborder" valign="top" width="18.55814418558144%" id="mcps1.1.5.1.1"><p id="p25460115183640"><a name="p25460115183640"></a><a name="p25460115183640"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.58804119588041%" id="mcps1.1.5.1.2"><p id="p49003430183640"><a name="p49003430183640"></a><a name="p49003430183640"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="30.926907309269076%" id="mcps1.1.5.1.3"><p id="p9854902183640"><a name="p9854902183640"></a><a name="p9854902183640"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="30.926907309269076%" id="mcps1.1.5.1.4"><p id="p60049578183640"><a name="p60049578183640"></a><a name="p60049578183640"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row32177643183640"><td class="cellrowborder" valign="top" width="18.55814418558144%" headers="mcps1.1.5.1.1 "><p id="p56252256183640"><a name="p56252256183640"></a><a name="p56252256183640"></a>tag</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.58804119588041%" headers="mcps1.1.5.1.2 "><p id="p60138865183640"><a name="p60138865183640"></a><a name="p60138865183640"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.926907309269076%" headers="mcps1.1.5.1.3 "><p id="p3312363191641"><a name="p3312363191641"></a><a name="p3312363191641"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.926907309269076%" headers="mcps1.1.5.1.4 "><p id="p38087562183640"><a name="p38087562183640"></a><a name="p38087562183640"></a>Specifies the tag to be added or updated.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2**  Data structure description of the  **resource\_tag**  field

    <a name="table65193697183640"></a>
    <table><thead align="left"><tr id="row45372420183640"><th class="cellrowborder" valign="top" width="31.626837316268368%" id="mcps1.2.5.1.1"><p id="p51287431183640"><a name="p51287431183640"></a><a name="p51287431183640"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885708%" id="mcps1.2.5.1.2"><p id="p60641226183640"><a name="p60641226183640"></a><a name="p60641226183640"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885708%" id="mcps1.2.5.1.3"><p id="p12992245183640"><a name="p12992245183640"></a><a name="p12992245183640"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="39.7960203979602%" id="mcps1.2.5.1.4"><p id="p45738929183640"><a name="p45738929183640"></a><a name="p45738929183640"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row13865765183640"><td class="cellrowborder" valign="top" width="31.626837316268368%" headers="mcps1.2.5.1.1 "><p id="p49385210183640"><a name="p49385210183640"></a><a name="p49385210183640"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885708%" headers="mcps1.2.5.1.2 "><p id="p40779096183640"><a name="p40779096183640"></a><a name="p40779096183640"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885708%" headers="mcps1.2.5.1.3 "><p id="p14772454183640"><a name="p14772454183640"></a><a name="p14772454183640"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.5.1.4 "><p id="p55718092183640"><a name="p55718092183640"></a><a name="p55718092183640"></a>Specifies the tag key. The tag key cannot be left blank.</p>
    </td>
    </tr>
    <tr id="row31700784183640"><td class="cellrowborder" valign="top" width="31.626837316268368%" headers="mcps1.2.5.1.1 "><p id="p17626702183640"><a name="p17626702183640"></a><a name="p17626702183640"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885708%" headers="mcps1.2.5.1.2 "><p id="p18476761183640"><a name="p18476761183640"></a><a name="p18476761183640"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885708%" headers="mcps1.2.5.1.3 "><p id="p20222648183640"><a name="p20222648183640"></a><a name="p20222648183640"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.5.1.4 "><p id="p27421780183640"><a name="p27421780183640"></a><a name="p27421780183640"></a>Specifies the tag value.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    ```
    POST https://{Endpoint}/v2/fd73a4a14a4a4dfb9771a8475e5198ea/images/67e17426-359e-49fb-aa12-0bd1756ec240/tags
    ```

    ```
    {
       "tag": {
          "value": "value1",
          "key": "key1"
       }
    }
    ```


## Response<a name="section59059888183640"></a>

-   Response parameters

    None

-   Example response

    ```
    STATUS CODE 204
    ```


## Returned Value<a name="section37876563183640"></a>

-   Normal

    204

-   Abnormal

    <a name="table56403656183640"></a>
    <table><thead align="left"><tr id="row33675493183640"><th class="cellrowborder" valign="top" width="46.46%" id="mcps1.1.3.1.1"><p id="p43360445183640"><a name="p43360445183640"></a><a name="p43360445183640"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.54%" id="mcps1.1.3.1.2"><p id="p22535141183640"><a name="p22535141183640"></a><a name="p22535141183640"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row13407109183640"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.1.3.1.1 "><p id="p12234054183640"><a name="p12234054183640"></a><a name="p12234054183640"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.1.3.1.2 "><p id="p51434319183640"><a name="p51434319183640"></a><a name="p51434319183640"></a>Request error.</p>
    </td>
    </tr>
    <tr id="row60255695183640"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.1.3.1.1 "><p id="p48873112183640"><a name="p48873112183640"></a><a name="p48873112183640"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.1.3.1.2 "><p id="p66407998183640"><a name="p66407998183640"></a><a name="p66407998183640"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="row60801071183640"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.1.3.1.1 "><p id="p25939690183640"><a name="p25939690183640"></a><a name="p25939690183640"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.1.3.1.2 "><p id="p20740150183640"><a name="p20740150183640"></a><a name="p20740150183640"></a>You do not have the rights to perform the operation.</p>
    </td>
    </tr>
    <tr id="row52443626183640"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.1.3.1.1 "><p id="p20075281183640"><a name="p20075281183640"></a><a name="p20075281183640"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.1.3.1.2 "><p id="p15485085183640"><a name="p15485085183640"></a><a name="p15485085183640"></a>The requested resource was not found.</p>
    </td>
    </tr>
    <tr id="row5148045183640"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.1.3.1.1 "><p id="p14338475183640"><a name="p14338475183640"></a><a name="p14338475183640"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.1.3.1.2 "><p id="p20565793183640"><a name="p20565793183640"></a><a name="p20565793183640"></a>Internal service error.</p>
    </td>
    </tr>
    <tr id="row50874413183640"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.1.3.1.1 "><p id="p27186779183640"><a name="p27186779183640"></a><a name="p27186779183640"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.1.3.1.2 "><p id="p54645494183640"><a name="p54645494183640"></a><a name="p54645494183640"></a>The service is unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


