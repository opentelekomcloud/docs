# Adding or Deleting Protected Instance Tags in Batches<a name="sdrs_05_0802"></a>

## Function<a name="section11743182514464"></a>

This API is used to add or delete protected instance tags for a specified protected instance in batches.

You can add a maximum of 20 tags to a protected instance.

This API is idempotent.

-   If there are duplicate keys in the request body when you add tags, an error is reported.
-   During tag creation, duplicate keys are not allowed. If a key exists in the database, its value will be overwritten.
-   During tag deletion, if some tags do not exist, the operation is considered to be successful by default. The character set of the tags will not be checked. When you delete tags, the tag structure cannot be missing, and the key cannot be left blank or be an empty string.

## URI<a name="section1775552564615"></a>

-   URI format

    POST /v1/\{project\_id\}/protected-instances/\{protected\_instance\_id\}/tags/action


-   Parameter description

    <a name="table14756192511463"></a>
    <table><thead align="left"><tr id="row189891125114611"><th class="cellrowborder" valign="top" width="19.39%" id="mcps1.1.5.1.1"><p id="p9989625134619"><a name="p9989625134619"></a><a name="p9989625134619"></a><strong id="b842352706162023"><a name="b842352706162023"></a><a name="b842352706162023"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="23.47%" id="mcps1.1.5.1.2"><p id="p199892258468"><a name="p199892258468"></a><a name="p199892258468"></a><strong id="b84235270615447"><a name="b84235270615447"></a><a name="b84235270615447"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="12.24%" id="mcps1.1.5.1.3"><p id="p298916253464"><a name="p298916253464"></a><a name="p298916253464"></a><strong id="b84235270615453"><a name="b84235270615453"></a><a name="b84235270615453"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.9%" id="mcps1.1.5.1.4"><p id="p8989225134620"><a name="p8989225134620"></a><a name="p8989225134620"></a><strong id="b84235270615457"><a name="b84235270615457"></a><a name="b84235270615457"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row998942594616"><td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.1 "><p id="p198982554613"><a name="p198982554613"></a><a name="p198982554613"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.47%" headers="mcps1.1.5.1.2 "><p id="p1298915253466"><a name="p1298915253466"></a><a name="p1298915253466"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.24%" headers="mcps1.1.5.1.3 "><p id="p898962594617"><a name="p898962594617"></a><a name="p898962594617"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.9%" headers="mcps1.1.5.1.4 "><p id="p398915254462"><a name="p398915254462"></a><a name="p398915254462"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row13989162512469"><td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.1 "><p id="p89891925134615"><a name="p89891925134615"></a><a name="p89891925134615"></a>protected_instance_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.47%" headers="mcps1.1.5.1.2 "><p id="p20989152518462"><a name="p20989152518462"></a><a name="p20989152518462"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.24%" headers="mcps1.1.5.1.3 "><p id="p10989102518465"><a name="p10989102518465"></a><a name="p10989102518465"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.9%" headers="mcps1.1.5.1.4 "><p id="p1798962564612"><a name="p1798962564612"></a><a name="p1798962564612"></a>Specifies the ID of a protected instance.</p>
    <p id="p167524401505"><a name="p167524401505"></a><a name="p167524401505"></a>For details, see <a href="querying-protected-instances.md">Querying Protected Instances</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section1877562518469"></a>

-   Parameter description

    <a name="table0779825104611"></a>
    <table><thead align="left"><tr id="row798917257464"><th class="cellrowborder" valign="top" width="12.12121212121212%" id="mcps1.1.5.1.1"><p id="p10989112574616"><a name="p10989112574616"></a><a name="p10989112574616"></a><strong id="b842352706162023_1"><a name="b842352706162023_1"></a><a name="b842352706162023_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.2020202020202%" id="mcps1.1.5.1.2"><p id="p13989102564611"><a name="p13989102564611"></a><a name="p13989102564611"></a><strong id="b84235270615447_1"><a name="b84235270615447_1"></a><a name="b84235270615447_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25.25252525252525%" id="mcps1.1.5.1.3"><p id="p2989162513468"><a name="p2989162513468"></a><a name="p2989162513468"></a><strong id="b84235270615453_1"><a name="b84235270615453_1"></a><a name="b84235270615453_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="42.42424242424242%" id="mcps1.1.5.1.4"><p id="p2098952584613"><a name="p2098952584613"></a><a name="p2098952584613"></a><strong id="b84235270615457_1"><a name="b84235270615457_1"></a><a name="b84235270615457_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row9989725114615"><td class="cellrowborder" valign="top" width="12.12121212121212%" headers="mcps1.1.5.1.1 "><p id="p698952514619"><a name="p698952514619"></a><a name="p698952514619"></a>action</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.2020202020202%" headers="mcps1.1.5.1.2 "><p id="p14989152514460"><a name="p14989152514460"></a><a name="p14989152514460"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.25252525252525%" headers="mcps1.1.5.1.3 "><p id="p1598982514461"><a name="p1598982514461"></a><a name="p1598982514461"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.1.5.1.4 "><p id="p134981385164"><a name="p134981385164"></a><a name="p134981385164"></a>Identifies the operation. The value can be <strong id="b842352706112823"><a name="b842352706112823"></a><a name="b842352706112823"></a>create</strong> or <strong id="b842352706112836"><a name="b842352706112836"></a><a name="b842352706112836"></a>delete</strong>.</p>
    <a name="ul1313055620166"></a><a name="ul1313055620166"></a><ul id="ul1313055620166"><li><strong id="b842352706104918"><a name="b842352706104918"></a><a name="b842352706104918"></a>create</strong>: indicates to create a tag.</li><li><strong id="b339018611414"><a name="b339018611414"></a><a name="b339018611414"></a>delete</strong>: indicates to delete a tag.</li></ul>
    </td>
    </tr>
    <tr id="row1255715497467"><td class="cellrowborder" valign="top" width="12.12121212121212%" headers="mcps1.1.5.1.1 "><p id="p2098952554610"><a name="p2098952554610"></a><a name="p2098952554610"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.2020202020202%" headers="mcps1.1.5.1.2 "><p id="p15989325194612"><a name="p15989325194612"></a><a name="p15989325194612"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.25252525252525%" headers="mcps1.1.5.1.3 "><p id="p18989825144619"><a name="p18989825144619"></a><a name="p18989825144619"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.1.5.1.4 "><p id="p199891025184612"><a name="p199891025184612"></a><a name="p199891025184612"></a>Specifies the tag list.</p>
    <p id="p5238016101319"><a name="p5238016101319"></a><a name="p5238016101319"></a>For details, see <a href="#table6785202564616">Table 1</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  1**  Data structure of the  **resource\_tag**  field

    <a name="table6785202564616"></a>
    <table><thead align="left"><tr id="row8989112518468"><th class="cellrowborder" valign="top" width="11%" id="mcps1.2.5.1.1"><p id="p3989152544617"><a name="p3989152544617"></a><a name="p3989152544617"></a><strong id="b842352706162023_2"><a name="b842352706162023_2"></a><a name="b842352706162023_2"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="34%" id="mcps1.2.5.1.2"><p id="p69891253464"><a name="p69891253464"></a><a name="p69891253464"></a><strong id="b84235270615447_2"><a name="b84235270615447_2"></a><a name="b84235270615447_2"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="12%" id="mcps1.2.5.1.3"><p id="p1298910251462"><a name="p1298910251462"></a><a name="p1298910251462"></a><strong id="b84235270615453_2"><a name="b84235270615453_2"></a><a name="b84235270615453_2"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="43%" id="mcps1.2.5.1.4"><p id="p1798918259466"><a name="p1798918259466"></a><a name="p1798918259466"></a><strong id="b84235270615457_2"><a name="b84235270615457_2"></a><a name="b84235270615457_2"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1998918251468"><td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.5.1.1 "><p id="p16989225134616"><a name="p16989225134616"></a><a name="p16989225134616"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.5.1.2 "><p id="p16989122518462"><a name="p16989122518462"></a><a name="p16989122518462"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.3 "><p id="p0989102514466"><a name="p0989102514466"></a><a name="p0989102514466"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43%" headers="mcps1.2.5.1.4 "><p id="p20255101518620"><a name="p20255101518620"></a><a name="p20255101518620"></a>Specifies the tag key. The tag key of a resource must be unique.</p>
    </td>
    </tr>
    <tr id="row1399152510466"><td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.5.1.1 "><p id="p17991725204610"><a name="p17991725204610"></a><a name="p17991725204610"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.5.1.2 "><p id="p6871542154817"><a name="p6871542154817"></a><a name="p6871542154817"></a>This parameter is mandatory when <strong id="b842352706143922"><a name="b842352706143922"></a><a name="b842352706143922"></a>action</strong> is set to <strong id="b18668156302"><a name="b18668156302"></a><a name="b18668156302"></a>create</strong> and optional when <strong id="b787512312113"><a name="b787512312113"></a><a name="b787512312113"></a>action</strong> is set to <strong id="b3772566115"><a name="b3772566115"></a><a name="b3772566115"></a>delete</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.3 "><p id="p899142564618"><a name="p899142564618"></a><a name="p899142564618"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43%" headers="mcps1.2.5.1.4 "><p id="p14973122115616"><a name="p14973122115616"></a><a name="p14973122115616"></a>Specifies the tag value.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    POST https://\{Endpoint\}/v1/\{project\_id\}/protected-instances/67a2cc7e-fb87-41a8-ba28-9c032abcaee1/tags/action

    ```
    {
        "action": "create",
        "tags": [
            {
                "key": "key1",
                "value": "value1"
            },
            {
                "key": "key",
                "value": "value3"
            }
        ]
    }
    ```

    Or

    ```
    {
        "action": "delete",
        "tags": [
            {
                "key": "key1"
            },
            {
                "key": "key2",
                "value": "value3"
            }
        ]
    }
    ```


## Response<a name="section58051725144613"></a>

-   Parameter description

    None


## **Returned Value**<a name="section4805102564610"></a>

-   Normal

    <a name="table1380817254462"></a>
    <table><thead align="left"><tr id="row10991425114619"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p1199113253468"><a name="p1199113253468"></a><a name="p1199113253468"></a><strong id="b842352706175024_1"><a name="b842352706175024_1"></a><a name="b842352706175024_1"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p39911625134616"><a name="p39911625134616"></a><a name="p39911625134616"></a><strong id="b84235270615457_3"><a name="b84235270615457_3"></a><a name="b84235270615457_3"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1099111252461"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p12991162510464"><a name="p12991162510464"></a><a name="p12991162510464"></a>204</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p1299152510469"><a name="p1299152510469"></a><a name="p1299152510469"></a>No Content</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Abnormal

    <a name="table19809152512466"></a>
    <table><thead align="left"><tr id="row99913253465"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p1699162564617"><a name="p1699162564617"></a><a name="p1699162564617"></a><strong id="b842352706175024_2"><a name="b842352706175024_2"></a><a name="b842352706175024_2"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p09911125194610"><a name="p09911125194610"></a><a name="p09911125194610"></a><strong id="b84235270615457_4"><a name="b84235270615457_4"></a><a name="b84235270615457_4"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row18991925164617"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p7991225144614"><a name="p7991225144614"></a><a name="p7991225144614"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p199192514463"><a name="p199192514463"></a><a name="p199192514463"></a>Invalid parameters.</p>
    </td>
    </tr>
    <tr id="row1799162534618"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p9991725124620"><a name="p9991725124620"></a><a name="p9991725124620"></a>401</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p119911825194616"><a name="p119911825194616"></a><a name="p119911825194616"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="row10991132515466"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p9991122514466"><a name="p9991122514466"></a><a name="p9991122514466"></a>403</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p20991152574610"><a name="p20991152574610"></a><a name="p20991152574610"></a>Insufficient permission.</p>
    </td>
    </tr>
    <tr id="row19911251467"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p79918251467"><a name="p79918251467"></a><a name="p79918251467"></a>404</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p6991172504612"><a name="p6991172504612"></a><a name="p6991172504612"></a>The requested resource was not found.</p>
    </td>
    </tr>
    <tr id="row199142515468"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p49911425194615"><a name="p49911425194615"></a><a name="p49911425194615"></a>500</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p1299192504619"><a name="p1299192504619"></a><a name="p1299192504619"></a>Internal service error.</p>
    </td>
    </tr>
    </tbody>
    </table>


