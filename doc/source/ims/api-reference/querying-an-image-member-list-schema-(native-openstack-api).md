# Querying an Image Member List Schema \(Native OpenStack API\)<a name="EN-US_TOPIC_0049147877"></a>

## Function<a name="section16441043104828"></a>

This API is used to query an image member list schema, which allows you to view image member attributes and their data types.

## URI<a name="section40142579104828"></a>

GET /v2/schemas/members

## Request<a name="section40279828104828"></a>

-   Request parameters

    None

-   Example request

    ```
    GET https://{Endpoint}/v2/schemas/members
    ```


## Response<a name="section1248471104828"></a>

-   Response parameters

    <a name="table3942269104828"></a>
    <table><thead align="left"><tr id="row39362799104828"><th class="cellrowborder" valign="top" width="30.486951304869514%" id="mcps1.1.4.1.1"><p id="p34270171104828"><a name="p34270171104828"></a><a name="p34270171104828"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.078292170782923%" id="mcps1.1.4.1.2"><p id="p31903489104828"><a name="p31903489104828"></a><a name="p31903489104828"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="52.434756524347556%" id="mcps1.1.4.1.3"><p id="p34045835104828"><a name="p34045835104828"></a><a name="p34045835104828"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row6249241104828"><td class="cellrowborder" valign="top" width="30.486951304869514%" headers="mcps1.1.4.1.1 "><p id="p36426516104828"><a name="p36426516104828"></a><a name="p36426516104828"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.078292170782923%" headers="mcps1.1.4.1.2 "><p id="p19708015104828"><a name="p19708015104828"></a><a name="p19708015104828"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.434756524347556%" headers="mcps1.1.4.1.3 "><p id="p52845343104828"><a name="p52845343104828"></a><a name="p52845343104828"></a>Specifies the schema name.</p>
    </td>
    </tr>
    <tr id="row5846040104828"><td class="cellrowborder" valign="top" width="30.486951304869514%" headers="mcps1.1.4.1.1 "><p id="p3767226104828"><a name="p3767226104828"></a><a name="p3767226104828"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.078292170782923%" headers="mcps1.1.4.1.2 "><p id="p20709999104828"><a name="p20709999104828"></a><a name="p20709999104828"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.434756524347556%" headers="mcps1.1.4.1.3 "><p id="p66897235104828"><a name="p66897235104828"></a><a name="p66897235104828"></a>Specifies the URL for accessing the schema.</p>
    <p id="p13897123335712"><a name="p13897123335712"></a><a name="p13897123335712"></a>For details, see <a href="#table15641103183416">Table 1</a>.</p>
    </td>
    </tr>
    <tr id="row65204203104828"><td class="cellrowborder" valign="top" width="30.486951304869514%" headers="mcps1.1.4.1.1 "><p id="p47049086104828"><a name="p47049086104828"></a><a name="p47049086104828"></a>properties</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.078292170782923%" headers="mcps1.1.4.1.2 "><p id="p55391618104828"><a name="p55391618104828"></a><a name="p55391618104828"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.434756524347556%" headers="mcps1.1.4.1.3 "><p id="p1582015495573"><a name="p1582015495573"></a><a name="p1582015495573"></a>Describes basic image attributes, including the type and usage of each attribute.</p>
    <p id="p4120204111445"><a name="p4120204111445"></a><a name="p4120204111445"></a>For details about the parameters, see <a href="image-attributes.md">Image Attributes</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  1**  LinkInfo parameter description

    <a name="table15641103183416"></a>
    <table><thead align="left"><tr id="row136411132345"><th class="cellrowborder" valign="top" width="30.646935306469352%" id="mcps1.2.4.1.1"><p id="p136411433347"><a name="p136411433347"></a><a name="p136411433347"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.18828117188281%" id="mcps1.2.4.1.2"><p id="p12641193183412"><a name="p12641193183412"></a><a name="p12641193183412"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="52.16478352164784%" id="mcps1.2.4.1.3"><p id="p164120311348"><a name="p164120311348"></a><a name="p164120311348"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row4641634345"><td class="cellrowborder" valign="top" width="30.646935306469352%" headers="mcps1.2.4.1.1 "><p id="p126411432347"><a name="p126411432347"></a><a name="p126411432347"></a>href</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.18828117188281%" headers="mcps1.2.4.1.2 "><p id="p1864133173419"><a name="p1864133173419"></a><a name="p1864133173419"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.16478352164784%" headers="mcps1.2.4.1.3 "><p id="p16411373420"><a name="p16411373420"></a><a name="p16411373420"></a>Specifies the domain name.</p>
    </td>
    </tr>
    <tr id="row146411238348"><td class="cellrowborder" valign="top" width="30.646935306469352%" headers="mcps1.2.4.1.1 "><p id="p156421039346"><a name="p156421039346"></a><a name="p156421039346"></a>rel</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.18828117188281%" headers="mcps1.2.4.1.2 "><p id="p196421736343"><a name="p196421736343"></a><a name="p196421736343"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.16478352164784%" headers="mcps1.2.4.1.3 "><p id="p1164263163416"><a name="p1164263163416"></a><a name="p1164263163416"></a>Specifies the domain name description.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    STATUS CODE 200
    ```

    ```
    {
        "name": "members",
        "links": [
            {
                "href": "{schema}",
                "rel": "describedby"
            }
        ],
        "properties": {
            "members": {
                "items": {
                    "name": "member",
                    "properties": {
                        "status": {
                            "enum": [
                                "pending",
                                "accepted",
                                "rejected"
                            ],
                            "type": "string",
                            "description": "The status of this image member"
                        },
                        "created_at": {
                            "type": "string",
                            "description": "Date and time of image member creation"
                        },
                        "updated_at": {
                            "type": "string",
                            "description": "Date and time of last modification of image member"
                        },
                        "image_id": {
                            "pattern": "^([0-9a-fA-F]){8}-([0-9a-fA-F]){4}-([0-9a-fA-F]){4}-([0-9a-fA-F]){4}-([0-9a-fA-F]){12}$",
                            "type": "string",
                            "description": "An identifier for the image"
                        },
                        "member_id": {
                            "type": "string",
                            "description": "An identifier for the image member (tenantId)"
                        },
                        "schema": {
                            "readOnly": true,
                            "type": "string"
                        }
                    }
                },
                "type": "array"
            },
            "schema": {
                "type": "string"
            }
        }
    }
    ```


## Returned Value<a name="section57883339104828"></a>

-   Normal

    200

-   Abnormal

    <a name="table17662154104828"></a>
    <table><thead align="left"><tr id="row60824774104828"><th class="cellrowborder" valign="top" width="46.46%" id="mcps1.1.3.1.1"><p id="p27859693104828"><a name="p27859693104828"></a><a name="p27859693104828"></a><strong id="b842352706202113"><a name="b842352706202113"></a><a name="b842352706202113"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53.54%" id="mcps1.1.3.1.2"><p id="p42042623104828"><a name="p42042623104828"></a><a name="p42042623104828"></a><strong id="b842352706104623"><a name="b842352706104623"></a><a name="b842352706104623"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row50009318104828"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.1.3.1.1 "><p id="p24222986104828"><a name="p24222986104828"></a><a name="p24222986104828"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.1.3.1.2 "><p id="p15904850104828"><a name="p15904850104828"></a><a name="p15904850104828"></a>Request error.</p>
    </td>
    </tr>
    <tr id="row8925927104828"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.1.3.1.1 "><p id="p51911521104828"><a name="p51911521104828"></a><a name="p51911521104828"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.1.3.1.2 "><p id="p44083700104828"><a name="p44083700104828"></a><a name="p44083700104828"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="row61208982104828"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.1.3.1.1 "><p id="p58980480104828"><a name="p58980480104828"></a><a name="p58980480104828"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.1.3.1.2 "><p id="p12689558104828"><a name="p12689558104828"></a><a name="p12689558104828"></a>You do not have the rights to perform the operation.</p>
    </td>
    </tr>
    <tr id="row47097166104828"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.1.3.1.1 "><p id="p56774098104828"><a name="p56774098104828"></a><a name="p56774098104828"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.1.3.1.2 "><p id="p35299255104828"><a name="p35299255104828"></a><a name="p35299255104828"></a>The requested resource was not found.</p>
    </td>
    </tr>
    <tr id="row49257845104828"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.1.3.1.1 "><p id="p30462542104828"><a name="p30462542104828"></a><a name="p30462542104828"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.1.3.1.2 "><p id="p51546843104828"><a name="p51546843104828"></a><a name="p51546843104828"></a>Internal service error.</p>
    </td>
    </tr>
    <tr id="row61268409104828"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.1.3.1.1 "><p id="p63794096104828"><a name="p63794096104828"></a><a name="p63794096104828"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.1.3.1.2 "><p id="p67048143104828"><a name="p67048143104828"></a><a name="p67048143104828"></a>The service is unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


