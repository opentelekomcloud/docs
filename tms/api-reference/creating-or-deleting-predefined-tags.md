# Creating or Deleting Predefined Tags<a name="EN-US_TOPIC_0170553617"></a>

## Function<a name="s3ca7a6682f2f40adb92fc2535fc27c71"></a>

This API is used to create or delete predefined tags. Users can add tags to resources using the predefined tags.

This API supports idempotency and batch processing.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>Idempotent operations refer to invoking the same API for multiple times by using the same parameters, which have the same impact on the system.  

## URI<a name="sd093810dcf9f49f9a9ac3f0addd993aa"></a>

POST /v1.0/predefine\_tags/action

## Request<a name="s0080d9bf95db45a999db8ca7195660ca"></a>

-   Parameter description

    **Table  1**  Parameters in the request

    <a name="en-us_topic_0056765542_table10523083"></a>
    <table><thead align="left"><tr id="en-us_topic_0056765542_row3226198"><th class="cellrowborder" valign="top" width="18.58%" id="mcps1.2.5.1.1"><p id="en-us_topic_0056765542_p59995477"><a name="en-us_topic_0056765542_p59995477"></a><a name="en-us_topic_0056765542_p59995477"></a><strong id="b410197072043"><a name="b410197072043"></a><a name="b410197072043"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.36%" id="mcps1.2.5.1.2"><p id="en-us_topic_0056765542_p27795493"><a name="en-us_topic_0056765542_p27795493"></a><a name="en-us_topic_0056765542_p27795493"></a><strong id="b342619932043"><a name="b342619932043"></a><a name="b342619932043"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="29.89%" id="mcps1.2.5.1.3"><p id="en-us_topic_0056765542_p36842478"><a name="en-us_topic_0056765542_p36842478"></a><a name="en-us_topic_0056765542_p36842478"></a><strong id="b237580232043"><a name="b237580232043"></a><a name="b237580232043"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="34.17%" id="mcps1.2.5.1.4"><p id="en-us_topic_0056765542_p31450711"><a name="en-us_topic_0056765542_p31450711"></a><a name="en-us_topic_0056765542_p31450711"></a><strong id="b453516772043"><a name="b453516772043"></a><a name="b453516772043"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0056765542_row5166299"><td class="cellrowborder" valign="top" width="18.58%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0056765542_p15817070"><a name="en-us_topic_0056765542_p15817070"></a><a name="en-us_topic_0056765542_p15817070"></a>action</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0056765542_p6114302"><a name="en-us_topic_0056765542_p6114302"></a><a name="en-us_topic_0056765542_p6114302"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.89%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0056765542_p25496434"><a name="en-us_topic_0056765542_p25496434"></a><a name="en-us_topic_0056765542_p25496434"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.17%" headers="mcps1.2.5.1.4 "><p id="p22800527164128"><a name="p22800527164128"></a><a name="p22800527164128"></a>Specifies the operation identifier.</p>
    <p id="en-us_topic_0056765542_p51945267"><a name="en-us_topic_0056765542_p51945267"></a><a name="en-us_topic_0056765542_p51945267"></a>This parameter value is case sensitive and can be <strong id="b842352706163653"><a name="b842352706163653"></a><a name="b842352706163653"></a>create</strong> or <strong id="b842352706163656"><a name="b842352706163656"></a><a name="b842352706163656"></a>delete</strong>.</p>
    </td>
    </tr>
    <tr id="row3768776719376"><td class="cellrowborder" valign="top" width="18.58%" headers="mcps1.2.5.1.1 "><p id="p3295480193712"><a name="p3295480193712"></a><a name="p3295480193712"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.5.1.2 "><p id="p65607343193712"><a name="p65607343193712"></a><a name="p65607343193712"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.89%" headers="mcps1.2.5.1.3 "><p id="p4388405218398"><a name="p4388405218398"></a><a name="p4388405218398"></a>List&lt;predefine_tag_request&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.17%" headers="mcps1.2.5.1.4 "><p id="p13529275193712"><a name="p13529275193712"></a><a name="p13529275193712"></a>Specifies the tag list.</p>
    <p id="p6301124715121"><a name="p6301124715121"></a><a name="p6301124715121"></a>For details, see <a href="#en-us_topic_0056765542_table46817064">Table 2</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   **predefine\_tag\_request**  data structure

    **Table  2** **predefine\_tag\_request**  data structure description

    <a name="en-us_topic_0056765542_table46817064"></a>
    <table><thead align="left"><tr id="en-us_topic_0056765542_row4410728"><th class="cellrowborder" valign="top" width="19.01980198019802%" id="mcps1.2.5.1.1"><p id="en-us_topic_0056765542_p21724664"><a name="en-us_topic_0056765542_p21724664"></a><a name="en-us_topic_0056765542_p21724664"></a><strong id="b3685747820628"><a name="b3685747820628"></a><a name="b3685747820628"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.752475247524753%" id="mcps1.2.5.1.2"><p id="en-us_topic_0056765542_p14867369"><a name="en-us_topic_0056765542_p14867369"></a><a name="en-us_topic_0056765542_p14867369"></a><strong id="b3266572720628"><a name="b3266572720628"></a><a name="b3266572720628"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21.871287128712872%" id="mcps1.2.5.1.3"><p id="en-us_topic_0056765542_p63406242"><a name="en-us_topic_0056765542_p63406242"></a><a name="en-us_topic_0056765542_p63406242"></a><strong id="b2867822920628"><a name="b2867822920628"></a><a name="b2867822920628"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="40.35643564356436%" id="mcps1.2.5.1.4"><p id="en-us_topic_0056765542_p35632012"><a name="en-us_topic_0056765542_p35632012"></a><a name="en-us_topic_0056765542_p35632012"></a><strong id="b4123518320628"><a name="b4123518320628"></a><a name="b4123518320628"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0056765542_row511887"><td class="cellrowborder" valign="top" width="19.01980198019802%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0056765542_p41462866"><a name="en-us_topic_0056765542_p41462866"></a><a name="en-us_topic_0056765542_p41462866"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.752475247524753%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0056765542_p3048957"><a name="en-us_topic_0056765542_p3048957"></a><a name="en-us_topic_0056765542_p3048957"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.871287128712872%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0056765542_p45638969"><a name="en-us_topic_0056765542_p45638969"></a><a name="en-us_topic_0056765542_p45638969"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.35643564356436%" headers="mcps1.2.5.1.4 "><p id="p108587120631"><a name="p108587120631"></a><a name="p108587120631"></a>Specifies the key.</p>
    <p id="p16424462153146"><a name="p16424462153146"></a><a name="p16424462153146"></a>It cannot be left blank and can contain a maximum of 36 Unicode characters. Can contain only digits, letters, hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    <tr id="en-us_topic_0056765542_row51921052"><td class="cellrowborder" valign="top" width="19.01980198019802%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0056765542_p44855704"><a name="en-us_topic_0056765542_p44855704"></a><a name="en-us_topic_0056765542_p44855704"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.752475247524753%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0056765542_p9433441"><a name="en-us_topic_0056765542_p9433441"></a><a name="en-us_topic_0056765542_p9433441"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.871287128712872%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0056765542_p25911262"><a name="en-us_topic_0056765542_p25911262"></a><a name="en-us_topic_0056765542_p25911262"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.35643564356436%" headers="mcps1.2.5.1.4 "><p id="p2486891184110"><a name="p2486891184110"></a><a name="p2486891184110"></a>Specifies the value.</p>
    <p id="p10159585153243"><a name="p10159585153243"></a><a name="p10159585153243"></a>Each value contains a maximum of 43 Unicode characters and can be an empty string. Can contain only digits, letters, hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    ```
    POST https://TMS endpoint/v1.0/predefine_tags/action
    ```

    ```
    {
        "action": "create",
        "tags": [
            {
                "key": "ENV1",
                "value": "DEV1"
            },
            {
                "key": "ENV2",
                "value": "DEV2"
            }
        ]
    }
    ```


## Response<a name="s8f10435686924c5ca93a27ff7fbeacb2"></a>

-   Parameter description

    None


-   Example response

    None


## Status Codes<a name="section17789101582315"></a>

For details, see  [Status Code](status-code.md).

## Error Codes<a name="section18604165622519"></a>

For details, see  [Error Code Description](error-code-description.md).

