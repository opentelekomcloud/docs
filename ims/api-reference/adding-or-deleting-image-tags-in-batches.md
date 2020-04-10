# Adding or Deleting Image Tags in Batches<a name="EN-US_TOPIC_0102682862"></a>

## Function<a name="section49664599183533"></a>

This API is used to add tags to, update tags of, or delete tags from an image in batches.

## Constraints<a name="section33815340183533"></a>

-   Each tag consists of a key and a value. The key contains at most 36 characters, and the value contains at most 43 characters. The key cannot be left blank or an empty character string. The value cannot be left blank but can be an empty character string.
-   An image can have a maximum of 10 tags.
-   The keys of multiple tags in the request body must be unique.
-   This API is an idempotent one.

    If a tag to be added has the same key as an existing tag, but the tag values are different, this tag will be added and overwrite the existing one. If a tag to be added has the same key and value as an existing tag, this tag will not be added.

    If the specified tag does not exist, the deletion is considered successful by default.


-   Restrictions on tag keys and values during batch deletion

    During the deletion, the system will not verify the character set range of the key and value. The key cannot be left blank or an empty character string. The value is optional and will not be not verified. If the tag to be deleted does not exist, the deletion is considered successful and no error is reported. Also, the system will not verify the length of both the key and value. The key can contain a maximum of 127 characters, and the value contains a maximum of 255 characters.


## URI<a name="section11906898183533"></a>

POST /v2/\{project\_id\}/images/\{image\_id\}/tags/action

[Table 1](#table1543205183533)  lists the parameters in the URI.

**Table  1**  Parameter description

<a name="table1543205183533"></a>
<table><thead align="left"><tr id="row928566183533"><th class="cellrowborder" valign="top" width="18.55814418558144%" id="mcps1.2.5.1.1"><p id="p8104982183533"><a name="p8104982183533"></a><a name="p8104982183533"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19.58804119588041%" id="mcps1.2.5.1.2"><p id="p52523778183533"><a name="p52523778183533"></a><a name="p52523778183533"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="30.926907309269076%" id="mcps1.2.5.1.3"><p id="p26567651183533"><a name="p26567651183533"></a><a name="p26567651183533"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="30.926907309269076%" id="mcps1.2.5.1.4"><p id="p4496161183533"><a name="p4496161183533"></a><a name="p4496161183533"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row28644771183533"><td class="cellrowborder" valign="top" width="18.55814418558144%" headers="mcps1.2.5.1.1 "><p id="p38525138183533"><a name="p38525138183533"></a><a name="p38525138183533"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.58804119588041%" headers="mcps1.2.5.1.2 "><p id="p33528469183533"><a name="p33528469183533"></a><a name="p33528469183533"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="30.926907309269076%" headers="mcps1.2.5.1.3 "><p id="p31451477183533"><a name="p31451477183533"></a><a name="p31451477183533"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="30.926907309269076%" headers="mcps1.2.5.1.4 "><p id="p64541689183533"><a name="p64541689183533"></a><a name="p64541689183533"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row44004292183533"><td class="cellrowborder" valign="top" width="18.55814418558144%" headers="mcps1.2.5.1.1 "><p id="p7577914183533"><a name="p7577914183533"></a><a name="p7577914183533"></a>image_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.58804119588041%" headers="mcps1.2.5.1.2 "><p id="p9831304183533"><a name="p9831304183533"></a><a name="p9831304183533"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="30.926907309269076%" headers="mcps1.2.5.1.3 "><p id="p58138199183533"><a name="p58138199183533"></a><a name="p58138199183533"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="30.926907309269076%" headers="mcps1.2.5.1.4 "><p id="p11573711183533"><a name="p11573711183533"></a><a name="p11573711183533"></a>Specifies the image ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section37054537183533"></a>

-   Request parameters

    <a name="table46516372183533"></a>
    <table><thead align="left"><tr id="row15305774183533"><th class="cellrowborder" valign="top" width="18.55814418558144%" id="mcps1.1.5.1.1"><p id="p31808161183533"><a name="p31808161183533"></a><a name="p31808161183533"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.58804119588041%" id="mcps1.1.5.1.2"><p id="p26324220183533"><a name="p26324220183533"></a><a name="p26324220183533"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="30.926907309269076%" id="mcps1.1.5.1.3"><p id="p51887080183533"><a name="p51887080183533"></a><a name="p51887080183533"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="30.926907309269076%" id="mcps1.1.5.1.4"><p id="p42103948183533"><a name="p42103948183533"></a><a name="p42103948183533"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row54976657183533"><td class="cellrowborder" valign="top" width="18.55814418558144%" headers="mcps1.1.5.1.1 "><p id="p23924255183533"><a name="p23924255183533"></a><a name="p23924255183533"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.58804119588041%" headers="mcps1.1.5.1.2 "><p id="p58816477183533"><a name="p58816477183533"></a><a name="p58816477183533"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.926907309269076%" headers="mcps1.1.5.1.3 "><p id="p66514163183533"><a name="p66514163183533"></a><a name="p66514163183533"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.926907309269076%" headers="mcps1.1.5.1.4 "><p id="p18938122183533"><a name="p18938122183533"></a><a name="p18938122183533"></a>Lists the tags you want to operate.</p>
    </td>
    </tr>
    <tr id="row36225373183533"><td class="cellrowborder" valign="top" width="18.55814418558144%" headers="mcps1.1.5.1.1 "><p id="p48574104183533"><a name="p48574104183533"></a><a name="p48574104183533"></a>action</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.58804119588041%" headers="mcps1.1.5.1.2 "><p id="p42188327183533"><a name="p42188327183533"></a><a name="p42188327183533"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.926907309269076%" headers="mcps1.1.5.1.3 "><p id="p61811315183533"><a name="p61811315183533"></a><a name="p61811315183533"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.926907309269076%" headers="mcps1.1.5.1.4 "><p id="p40660579183533"><a name="p40660579183533"></a><a name="p40660579183533"></a>Specifies the tag operation to be performed. The value is case sensitive and can be <strong id="b842352706145313"><a name="b842352706145313"></a><a name="b842352706145313"></a>create</strong> or <strong id="b842352706145317"><a name="b842352706145317"></a><a name="b842352706145317"></a>delete</strong>. <strong id="b605074693145454"><a name="b605074693145454"></a><a name="b605074693145454"></a>create</strong> indicates that tags will be added or updated, while <strong id="b1812124538145535"><a name="b1812124538145535"></a><a name="b1812124538145535"></a>delete</strong> indicates that tags will be deleted.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2**  Data structure description of the  **resource\_tag**  field

    <a name="table107083563918"></a>
    <table><thead align="left"><tr id="row137071156390"><th class="cellrowborder" valign="top" width="31.626837316268368%" id="mcps1.2.5.1.1"><p id="p1070717566915"><a name="p1070717566915"></a><a name="p1070717566915"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885708%" id="mcps1.2.5.1.2"><p id="p57073568916"><a name="p57073568916"></a><a name="p57073568916"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885708%" id="mcps1.2.5.1.3"><p id="p870735611915"><a name="p870735611915"></a><a name="p870735611915"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="39.7960203979602%" id="mcps1.2.5.1.4"><p id="p570713560920"><a name="p570713560920"></a><a name="p570713560920"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row470845617914"><td class="cellrowborder" valign="top" width="31.626837316268368%" headers="mcps1.2.5.1.1 "><p id="p12708556598"><a name="p12708556598"></a><a name="p12708556598"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885708%" headers="mcps1.2.5.1.2 "><p id="p470816561594"><a name="p470816561594"></a><a name="p470816561594"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885708%" headers="mcps1.2.5.1.3 "><p id="p370814561393"><a name="p370814561393"></a><a name="p370814561393"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.5.1.4 "><p id="p1470814561497"><a name="p1470814561497"></a><a name="p1470814561497"></a>Specifies the tag key. The tag key cannot be left blank.</p>
    </td>
    </tr>
    <tr id="row870810563916"><td class="cellrowborder" valign="top" width="31.626837316268368%" headers="mcps1.2.5.1.1 "><p id="p10708105612918"><a name="p10708105612918"></a><a name="p10708105612918"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885708%" headers="mcps1.2.5.1.2 "><p id="p67087568918"><a name="p67087568918"></a><a name="p67087568918"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885708%" headers="mcps1.2.5.1.3 "><p id="p20708195618914"><a name="p20708195618914"></a><a name="p20708195618914"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.5.1.4 "><p id="p870814565914"><a name="p870814565914"></a><a name="p870814565914"></a>Specifies the tag value. This parameter is optional.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request
    -   Adding image tags in batches

        ```
        POST https://{Endpoint}/v2/fd73a4a14a4a4dfb9771a8475e5198ea/images/67e17426-359e-49fb-aa12-0bd1756ec240/tags/action
        ```

        ```
        {
           "tags": [{
              "value": "value1",
              "key": "key1"
           },
           {
              "value": "value2",
              "key": "key2"
           },
           {
              "value": "",
              "key": "key3"
           }],
           "action": "create"
        }
        ```

    -   Deleting image tags in batches

        ```
        POST https://{Endpoint}/v2/fd73a4a14a4a4dfb9771a8475e5198ea/images/67e17426-359e-49fb-aa12-0bd1756ec240/tags/action
        ```

        ```
        {
           "tags": [{
              "value": "value1",
              "key": "key1"
           },
           {
              "value": "value2",
              "key": "key2"
           },
           {
              "value": "",
              "key": "key3"
           }],
              "action": "delete"
        }
        ```



## Response<a name="section935919183533"></a>

-   Response parameters

    None

-   Example response

    ```
    STATUS CODE 204
    ```


## Returned Values<a name="section11196745183533"></a>

-   Normal

    204

-   Abnormal

    <a name="table748594183533"></a>
    <table><thead align="left"><tr id="row46152835183533"><th class="cellrowborder" valign="top" width="46.46%" id="mcps1.1.3.1.1"><p id="p47392170183533"><a name="p47392170183533"></a><a name="p47392170183533"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.54%" id="mcps1.1.3.1.2"><p id="p13560590183533"><a name="p13560590183533"></a><a name="p13560590183533"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row24666006183533"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.1.3.1.1 "><p id="p51789483183533"><a name="p51789483183533"></a><a name="p51789483183533"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.1.3.1.2 "><p id="p34198580183533"><a name="p34198580183533"></a><a name="p34198580183533"></a>Request error.</p>
    </td>
    </tr>
    <tr id="row39351768183533"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.1.3.1.1 "><p id="p33376619183533"><a name="p33376619183533"></a><a name="p33376619183533"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.1.3.1.2 "><p id="p19151590183533"><a name="p19151590183533"></a><a name="p19151590183533"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="row38146586183533"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.1.3.1.1 "><p id="p2865798183533"><a name="p2865798183533"></a><a name="p2865798183533"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.1.3.1.2 "><p id="p30803053183533"><a name="p30803053183533"></a><a name="p30803053183533"></a>You do not have the rights to perform the operation.</p>
    </td>
    </tr>
    <tr id="row8792027183533"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.1.3.1.1 "><p id="p41065609183533"><a name="p41065609183533"></a><a name="p41065609183533"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.1.3.1.2 "><p id="p37980007183533"><a name="p37980007183533"></a><a name="p37980007183533"></a>The requested resource was not found.</p>
    </td>
    </tr>
    <tr id="row6275743183533"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.1.3.1.1 "><p id="p38573193183533"><a name="p38573193183533"></a><a name="p38573193183533"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.1.3.1.2 "><p id="p37420919183533"><a name="p37420919183533"></a><a name="p37420919183533"></a>Internal service error.</p>
    </td>
    </tr>
    <tr id="row1243955183533"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.1.3.1.1 "><p id="p33651555183533"><a name="p33651555183533"></a><a name="p33651555183533"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.1.3.1.2 "><p id="p41421452183533"><a name="p41421452183533"></a><a name="p41421452183533"></a>The service is unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


