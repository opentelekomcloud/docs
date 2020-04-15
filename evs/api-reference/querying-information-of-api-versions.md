# Querying Information of API Versions<a name="evs_04_0020"></a>

## Function<a name="section19390540"></a>

This API is used to query information of API versions.

## URI<a name="section40297137"></a>

-   URI format

    GET /


## Request<a name="section27129916"></a>

-   Example request

    ```
    GET https://{endpoint}/
    ```


## Response<a name="section42842654"></a>

-   Parameter description

    <a name="table1244631181217"></a>
    <table><thead align="left"><tr id="row644717114128"><th class="cellrowborder" valign="top" width="20%" id="mcps1.1.4.1.1"><p id="p1044711171210"><a name="p1044711171210"></a><a name="p1044711171210"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.21%" id="mcps1.1.4.1.2"><p id="p1844716114129"><a name="p1844716114129"></a><a name="p1844716114129"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="58.79%" id="mcps1.1.4.1.3"><p id="p4447510123"><a name="p4447510123"></a><a name="p4447510123"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1244711120123"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p1744719113124"><a name="p1744719113124"></a><a name="p1744719113124"></a>versions</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21%" headers="mcps1.1.4.1.2 "><p id="p74479101218"><a name="p74479101218"></a><a name="p74479101218"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.79%" headers="mcps1.1.4.1.3 "><p id="p1144717181219"><a name="p1144717181219"></a><a name="p1144717181219"></a>Specifies the API versions. For details, see <a href="#li8787321201856">Parameters in the versions field</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="li8787321201856"></a>Parameters in the  **versions**  field

    <a name="table49541177222812"></a>
    <table><thead align="left"><tr id="row31307356222812"><th class="cellrowborder" valign="top" width="20%" id="mcps1.1.4.1.1"><p id="p52867918222812"><a name="p52867918222812"></a><a name="p52867918222812"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.18%" id="mcps1.1.4.1.2"><p id="p54442989222812"><a name="p54442989222812"></a><a name="p54442989222812"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="58.81999999999999%" id="mcps1.1.4.1.3"><p id="p47079504222812"><a name="p47079504222812"></a><a name="p47079504222812"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row49897554222812"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p31318845143243"><a name="p31318845143243"></a><a name="p31318845143243"></a>min_version</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.2 "><p id="p53798498143243"><a name="p53798498143243"></a><a name="p53798498143243"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.81999999999999%" headers="mcps1.1.4.1.3 "><p id="p46434022143243"><a name="p46434022143243"></a><a name="p46434022143243"></a>Specifies the minimum microversion supported. If this version does not support microversions, the value is an empty string.</p>
    </td>
    </tr>
    <tr id="row15692876222812"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p27535301143243"><a name="p27535301143243"></a><a name="p27535301143243"></a>media-types</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.2 "><p id="p15766871143243"><a name="p15766871143243"></a><a name="p15766871143243"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.81999999999999%" headers="mcps1.1.4.1.3 "><p id="p31685730143243"><a name="p31685730143243"></a><a name="p31685730143243"></a>Specifies the request message type of the API version. For details, see <a href="#li16162726152446">Parameters in the media-types field</a>.</p>
    </td>
    </tr>
    <tr id="row54402779222812"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p13448319143243"><a name="p13448319143243"></a><a name="p13448319143243"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.2 "><p id="p3173993219137"><a name="p3173993219137"></a><a name="p3173993219137"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.81999999999999%" headers="mcps1.1.4.1.3 "><p id="p28790367143243"><a name="p28790367143243"></a><a name="p28790367143243"></a>Specifies the URI of the API version. For details, see <a href="#li2542907152450">Parameters in the links field</a>.</p>
    </td>
    </tr>
    <tr id="row23073040222812"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p50212078143243"><a name="p50212078143243"></a><a name="p50212078143243"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.2 "><p id="p40646554143243"><a name="p40646554143243"></a><a name="p40646554143243"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.81999999999999%" headers="mcps1.1.4.1.3 "><p id="p58524749143243"><a name="p58524749143243"></a><a name="p58524749143243"></a>Specifies the ID of the API version.</p>
    </td>
    </tr>
    <tr id="row52652485222812"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p50414043143243"><a name="p50414043143243"></a><a name="p50414043143243"></a>updated</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.2 "><p id="p57005649143243"><a name="p57005649143243"></a><a name="p57005649143243"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.81999999999999%" headers="mcps1.1.4.1.3 "><p id="p16367207143243"><a name="p16367207143243"></a><a name="p16367207143243"></a>Specifies the last time when the API version was updated.</p>
    <p id="p2841328201815"><a name="p2841328201815"></a><a name="p2841328201815"></a><span id="text11514509197"><a name="text11514509197"></a><a name="text11514509197"></a>Time format: UTC YYYY-MM-DDTHH:MM:SS.XXXXXX</span></p>
    </td>
    </tr>
    <tr id="row2625553314335"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p35634222143315"><a name="p35634222143315"></a><a name="p35634222143315"></a>version</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.2 "><p id="p690833143315"><a name="p690833143315"></a><a name="p690833143315"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.81999999999999%" headers="mcps1.1.4.1.3 "><p id="p36267691143315"><a name="p36267691143315"></a><a name="p36267691143315"></a>Specifies the maximum microversion supported. If this version does not support microversions, the value is an empty string.</p>
    </td>
    </tr>
    <tr id="row3428178414338"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p65363382143315"><a name="p65363382143315"></a><a name="p65363382143315"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.2 "><p id="p59942555143315"><a name="p59942555143315"></a><a name="p59942555143315"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.81999999999999%" headers="mcps1.1.4.1.3 "><div class="p" id="p25161763143315"><a name="p25161763143315"></a><a name="p25161763143315"></a>Specifies the API version status. The value can be as follows:<a name="ul52099355205"></a><a name="ul52099355205"></a><ul id="ul52099355205"><li><strong id="b9283195613329"><a name="b9283195613329"></a><a name="b9283195613329"></a>CURRENT</strong>: indicates a major version.</li><li><strong id="b8470857123214"><a name="b8470857123214"></a><a name="b8470857123214"></a>SUPPORTED</strong>: indicates an earlier version which is still supported.</li><li><strong id="b1447319585329"><a name="b1447319585329"></a><a name="b1447319585329"></a>DEPRECATED</strong>: indicates a deprecated version that may be deleted later.</li></ul>
    </div>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="li16162726152446"></a>Parameters in the  **media-types**  field

    <a name="table1723912303523"></a>
    <table><thead align="left"><tr id="row1572605203523"><th class="cellrowborder" valign="top" width="20%" id="mcps1.1.4.1.1"><p id="p4956457303630"><a name="p4956457303630"></a><a name="p4956457303630"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.18%" id="mcps1.1.4.1.2"><p id="p5530748603630"><a name="p5530748603630"></a><a name="p5530748603630"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="58.81999999999999%" id="mcps1.1.4.1.3"><p id="p1479139303630"><a name="p1479139303630"></a><a name="p1479139303630"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row4241971403523"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p1344484103523"><a name="p1344484103523"></a><a name="p1344484103523"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.2 "><p id="p1529029903523"><a name="p1529029903523"></a><a name="p1529029903523"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.81999999999999%" headers="mcps1.1.4.1.3 "><p id="p5901344603523"><a name="p5901344603523"></a><a name="p5901344603523"></a>Specifies the response type.</p>
    </td>
    </tr>
    <tr id="row6135897003523"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p402067503523"><a name="p402067503523"></a><a name="p402067503523"></a>base</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.2 "><p id="p5723929303523"><a name="p5723929303523"></a><a name="p5723929303523"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.81999999999999%" headers="mcps1.1.4.1.3 "><p id="p580387503523"><a name="p580387503523"></a><a name="p580387503523"></a>Specifies the text type.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   <a name="li2542907152450"></a>Parameters in the  **links**  field

    <a name="table35183803523"></a>
    <table><thead align="left"><tr id="row1099838503523"><th class="cellrowborder" valign="top" width="20%" id="mcps1.1.4.1.1"><p id="p1845402603523"><a name="p1845402603523"></a><a name="p1845402603523"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.35%" id="mcps1.1.4.1.2"><p id="p1838114303523"><a name="p1838114303523"></a><a name="p1838114303523"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.65%" id="mcps1.1.4.1.3"><p id="p405534303523"><a name="p405534303523"></a><a name="p405534303523"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3649809103523"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p355541903523"><a name="p355541903523"></a><a name="p355541903523"></a>rel</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="p1955354003523"><a name="p1955354003523"></a><a name="p1955354003523"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.65%" headers="mcps1.1.4.1.3 "><p id="p4573756603523"><a name="p4573756603523"></a><a name="p4573756603523"></a>Specifies the domain name description.</p>
    </td>
    </tr>
    <tr id="row898491303523"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p5668937803523"><a name="p5668937803523"></a><a name="p5668937803523"></a>href</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="p2843694403523"><a name="p2843694403523"></a><a name="p2843694403523"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.65%" headers="mcps1.1.4.1.3 "><p id="p1215177703523"><a name="p1215177703523"></a><a name="p1215177703523"></a>Specifies the domain name.</p>
    </td>
    </tr>
    <tr id="row4225713203523"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p27570503523"><a name="p27570503523"></a><a name="p27570503523"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="p2233213403523"><a name="p2233213403523"></a><a name="p2233213403523"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.65%" headers="mcps1.1.4.1.3 "><p id="p2248281703523"><a name="p2248281703523"></a><a name="p2248281703523"></a>Specifies the response type.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "versions": [
            {
                "min_version": "", 
                "media-types": [
                    {
                        "type": "application/vnd.openstack.volume+json;version=1", 
                        "base": "application/json"
                    }, 
                    {
                        "type": "application/vnd.openstack.volume+xml;version=1", 
                        "base": "application/xml"
                    }
                ], 
                "links": [
                    {
                        "rel": "describedby", 
                        "href": "http://docs.openstack.org/", 
                        "type": "text/html"
                    }, 
                    {
                        "rel": "self", 
                        "href": "https://evs.localdomain.com/v1"
                    }
                ], 
                "id": "v1.0", 
                "updated": "2014-06-28T12:20:21Z", 
                "version": "", 
                "status": "SUPPORTED"
            }, 
            {
                "min_version": "", 
                "media-types": [
                    {
                        "type": "application/vnd.openstack.volume+json;version=1", 
                        "base": "application/json"
                    }, 
                    {
                        "type": "application/vnd.openstack.volume+xml;version=1", 
                        "base": "application/xml"
                    }
                ], 
                "links": [
                    {
                        "rel": "describedby", 
                        "href": "http://docs.openstack.org/", 
                        "type": "text/html"
                    }, 
                    {
                        "rel": "self", 
                        "href": "https://evs.localdomain.com/v2"
                    }
                ], 
                "id": "v2.0", 
                "updated": "2014-06-28T12:20:21Z", 
                "version": "", 
                "status": "SUPPORTED"
            }, 
            {
                "min_version": "3.0", 
                "media-types": [
                    {
                        "type": "application/vnd.openstack.volume+json;version=1", 
                        "base": "application/json"
                    }, 
                    {
                        "type": "application/vnd.openstack.volume+xml;version=1", 
                        "base": "application/xml"
                    }
                ], 
                "links": [
                    {
                        "rel": "describedby", 
                        "href": "http://docs.openstack.org/", 
                        "type": "text/html"
                    }, 
                    {
                        "rel": "self", 
                        "href": "https://evs.localdomain.com/v3"
                    }
                ], 
                "id": "v3.0", 
                "updated": "2016-02-08T12:20:21Z", 
                "version": "3.0", 
                "status": "CURRENT"
            }
        ]
    }
    ```


## Status Codes<a name="section50039568"></a>

-   Normal

    300


## Error Codes<a name="section431317151242"></a>

For details, see  [Error Codes](error-codes.md).

