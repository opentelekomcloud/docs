# Querying API Versions<a name="sdrs_05_0201"></a>

## Function<a name="section15202175015916"></a>

This API is used to query all available API versions of SDRS.

## Constraints<a name="section2218250892"></a>

None

## URI<a name="section102186501492"></a>

-   URI format

    GET  /


## Request<a name="section122189507911"></a>

-   Parameter description

    None

-   Example request

    GET https://\{endpoint\}/


## Response<a name="section1921820506915"></a>

-   Parameter description

    <a name="table182331050591"></a>
    <table><thead align="left"><tr id="row175301150797"><th class="cellrowborder" valign="top" width="29.07%" id="mcps1.1.4.1.1"><p id="p65303501498"><a name="p65303501498"></a><a name="p65303501498"></a><strong id="b842352706151210"><a name="b842352706151210"></a><a name="b842352706151210"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.44%" id="mcps1.1.4.1.2"><p id="p195302503918"><a name="p195302503918"></a><a name="p195302503918"></a><strong id="b84235270615453"><a name="b84235270615453"></a><a name="b84235270615453"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53.49%" id="mcps1.1.4.1.3"><p id="p35303501793"><a name="p35303501793"></a><a name="p35303501793"></a><strong id="b84235270615457"><a name="b84235270615457"></a><a name="b84235270615457"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1153012501194"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.1.4.1.1 "><p id="p19530550193"><a name="p19530550193"></a><a name="p19530550193"></a>versions</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.1.4.1.2 "><p id="p175301150093"><a name="p175301150093"></a><a name="p175301150093"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.1.4.1.3 "><p id="p12530250298"><a name="p12530250298"></a><a name="p12530250298"></a>Specifies the API version list.</p>
    <p id="p1292113616103"><a name="p1292113616103"></a><a name="p1292113616103"></a>For details, see <a href="#table11250550892">Table 1</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  1** **versions**  field description

    <a name="table11250550892"></a>
    <table><thead align="left"><tr id="row195307501295"><th class="cellrowborder" valign="top" width="29.07%" id="mcps1.2.4.1.1"><p id="p65307506917"><a name="p65307506917"></a><a name="p65307506917"></a><strong id="b842352706151210_1"><a name="b842352706151210_1"></a><a name="b842352706151210_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.44%" id="mcps1.2.4.1.2"><p id="p653045013912"><a name="p653045013912"></a><a name="p653045013912"></a><strong id="b84235270615453_1"><a name="b84235270615453_1"></a><a name="b84235270615453_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53.49%" id="mcps1.2.4.1.3"><p id="p253035016913"><a name="p253035016913"></a><a name="p253035016913"></a><strong id="b84235270615457_1"><a name="b84235270615457_1"></a><a name="b84235270615457_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row553075018919"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p165302507919"><a name="p165302507919"></a><a name="p165302507919"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p1853012503910"><a name="p1853012503910"></a><a name="p1853012503910"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p65307507916"><a name="p65307507916"></a><a name="p65307507916"></a>Specifies the version ID, for example, <strong id="b84235270619258"><a name="b84235270619258"></a><a name="b84235270619258"></a>v1</strong>.</p>
    </td>
    </tr>
    <tr id="row1953016501699"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p953010504914"><a name="p953010504914"></a><a name="p953010504914"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p9530155016912"><a name="p9530155016912"></a><a name="p9530155016912"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p165306504911"><a name="p165306504911"></a><a name="p165306504911"></a>Specifies the API URL.</p>
    <p id="p79618574411"><a name="p79618574411"></a><a name="p79618574411"></a>For details, see <a href="#en-us_topic_0060111075_table35183803523">Table 2</a>.</p>
    </td>
    </tr>
    <tr id="row55302504916"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p0530115017910"><a name="p0530115017910"></a><a name="p0530115017910"></a>version</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p17530115019910"><a name="p17530115019910"></a><a name="p17530115019910"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p853015501918"><a name="p853015501918"></a><a name="p853015501918"></a>Specifies the version. If the APIs of this version support microversions, the system returns the supported maximum microversion. If the microversion is not supported, the system returns an empty value.</p>
    </td>
    </tr>
    <tr id="row1153012501910"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p55301850595"><a name="p55301850595"></a><a name="p55301850595"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p25301501498"><a name="p25301501498"></a><a name="p25301501498"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p85304501993"><a name="p85304501993"></a><a name="p85304501993"></a>Specifies the version status. Values are as follows:</p>
    <p id="p853015502920"><a name="p853015502920"></a><a name="p853015502920"></a><strong>CURRENT</strong>: widely used version</p>
    <p id="p3530350293"><a name="p3530350293"></a><a name="p3530350293"></a><strong>SUPPORT</strong>: earlier version which is still supported</p>
    <p id="p35306503917"><a name="p35306503917"></a><a name="p35306503917"></a><strong>DEPRECATED</strong>: deprecated version which may be deleted later</p>
    </td>
    </tr>
    <tr id="row115307500919"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p15308501693"><a name="p15308501693"></a><a name="p15308501693"></a>updated</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p1530950391"><a name="p1530950391"></a><a name="p1530950391"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p75306505917"><a name="p75306505917"></a><a name="p75306505917"></a>Specifies the version release time in UTC format. For example, the release time of v1 is 2018-05-30T15:00:00Z.</p>
    </td>
    </tr>
    <tr id="row1530250795"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p205307501896"><a name="p205307501896"></a><a name="p205307501896"></a>min_version</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p1153014501496"><a name="p1153014501496"></a><a name="p1153014501496"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p1653013501091"><a name="p1653013501091"></a><a name="p1653013501091"></a>Specifies the microversion. If APIs of a version support microversions, the system returns the supported minimum microversion. If microversions are not supported, the system returns an empty value.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2** **links**  parameters

    <a name="en-us_topic_0060111075_table35183803523"></a>
    <table><thead align="left"><tr id="en-us_topic_0060111075_row1099838503523"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.1"><p id="en-us_topic_0060111075_p1845402603523"><a name="en-us_topic_0060111075_p1845402603523"></a><a name="en-us_topic_0060111075_p1845402603523"></a><strong id="b84235270615443"><a name="b84235270615443"></a><a name="b84235270615443"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="22.35%" id="mcps1.2.4.1.2"><p id="en-us_topic_0060111075_p1838114303523"><a name="en-us_topic_0060111075_p1838114303523"></a><a name="en-us_topic_0060111075_p1838114303523"></a><strong id="b84235270615453_2"><a name="b84235270615453_2"></a><a name="b84235270615453_2"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="57.65%" id="mcps1.2.4.1.3"><p id="en-us_topic_0060111075_p405534303523"><a name="en-us_topic_0060111075_p405534303523"></a><a name="en-us_topic_0060111075_p405534303523"></a><strong id="b84235270615457_2"><a name="b84235270615457_2"></a><a name="b84235270615457_2"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0060111075_row3649809103523"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0060111075_p355541903523"><a name="en-us_topic_0060111075_p355541903523"></a><a name="en-us_topic_0060111075_p355541903523"></a>rel</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0060111075_p1955354003523"><a name="en-us_topic_0060111075_p1955354003523"></a><a name="en-us_topic_0060111075_p1955354003523"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.65%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0060111075_p4573756603523"><a name="en-us_topic_0060111075_p4573756603523"></a><a name="en-us_topic_0060111075_p4573756603523"></a>Describes a link.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0060111075_row898491303523"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0060111075_p5668937803523"><a name="en-us_topic_0060111075_p5668937803523"></a><a name="en-us_topic_0060111075_p5668937803523"></a>href</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0060111075_p2843694403523"><a name="en-us_topic_0060111075_p2843694403523"></a><a name="en-us_topic_0060111075_p2843694403523"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.65%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0060111075_p1215177703523"><a name="en-us_topic_0060111075_p1215177703523"></a><a name="en-us_topic_0060111075_p1215177703523"></a>Specifies the version query link.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "versions": [
            {
                "id": "v1",
                "links": [
                    {
                        "href": "https://sdrs.localdomain.com/v1",
                        "rel": "self"
                    }
                ],
                "status": "CURRENT",
                "updated": "2018-05-30T15:00:00Z",
                "version": "",
                "min_version": ""
            }
        ]
    }            
    ```

    Or

    ```
    {  
          "error": {  
              "message": "XXXX",   
              "code": "XXX"  
          }  
      }
    ```

    In the preceding example,  **error**  indicates a general error, for example,  **badrequest**  or  **itemNotFound**. An example is provided as follows:

    ```
    {  
          "badrequest": {  
              "message": "XXXX",   
              "code": "XXX"  
          }  
      }
    ```


## **Returned Value**<a name="section1280175013910"></a>

-   Normal

    <a name="table1328075020914"></a>
    <table><thead align="left"><tr id="row353013501299"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p4530350292"><a name="p4530350292"></a><a name="p4530350292"></a><strong id="b842352706175024_1"><a name="b842352706175024_1"></a><a name="b842352706175024_1"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p175301750497"><a name="p175301750497"></a><a name="p175301750497"></a><strong id="b84235270615457_3"><a name="b84235270615457_3"></a><a name="b84235270615457_3"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row553055014912"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p553005012910"><a name="p553005012910"></a><a name="p553005012910"></a>200</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p95306501392"><a name="p95306501392"></a><a name="p95306501392"></a>The server has accepted the request.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Abnormal

    <a name="table182801579913"></a>
    <table><thead align="left"><tr id="row128011579913"><th class="cellrowborder" valign="top" width="43.43%" id="mcps1.1.3.1.1"><p id="p1328016571695"><a name="p1328016571695"></a><a name="p1328016571695"></a><strong id="b842352706175024_2"><a name="b842352706175024_2"></a><a name="b842352706175024_2"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="56.57%" id="mcps1.1.3.1.2"><p id="p02801757990"><a name="p02801757990"></a><a name="p02801757990"></a><strong id="b84235270615457_4"><a name="b84235270615457_4"></a><a name="b84235270615457_4"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row628045712912"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p22809571991"><a name="p22809571991"></a><a name="p22809571991"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p2028019571694"><a name="p2028019571694"></a><a name="p2028019571694"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row10280105719915"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p182805576911"><a name="p182805576911"></a><a name="p182805576911"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p728019575910"><a name="p728019575910"></a><a name="p728019575910"></a>You must enter a username and the password to access the requested page.</p>
    </td>
    </tr>
    <tr id="row152801571496"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p428013579918"><a name="p428013579918"></a><a name="p428013579918"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p192801157095"><a name="p192801157095"></a><a name="p192801157095"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="row14280165716912"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p32801157596"><a name="p32801157596"></a><a name="p32801157596"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p428012575913"><a name="p428012575913"></a><a name="p428012575913"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="row152806579910"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p12280157491"><a name="p12280157491"></a><a name="p12280157491"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p14280957992"><a name="p14280957992"></a><a name="p14280957992"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="row828015570910"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p92803570912"><a name="p92803570912"></a><a name="p92803570912"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p2280457991"><a name="p2280457991"></a><a name="p2280457991"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="row828014573910"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p172801357397"><a name="p172801357397"></a><a name="p172801357397"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p182804578913"><a name="p182804578913"></a><a name="p182804578913"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="row02801857196"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p182801757394"><a name="p182801757394"></a><a name="p182801757394"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p1228014575913"><a name="p1228014575913"></a><a name="p1228014575913"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row228035715917"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p1928019575911"><a name="p1928019575911"></a><a name="p1928019575911"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p11280135715913"><a name="p11280135715913"></a><a name="p11280135715913"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="row192806571191"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p9280145719917"><a name="p9280145719917"></a><a name="p9280145719917"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p42806574918"><a name="p42806574918"></a><a name="p42806574918"></a>Failed to complete the request because of a service error.</p>
    </td>
    </tr>
    <tr id="row52801557997"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p1728016571298"><a name="p1728016571298"></a><a name="p1728016571298"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p4280857797"><a name="p4280857797"></a><a name="p4280857797"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="row112801057893"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p192801571095"><a name="p192801571095"></a><a name="p192801571095"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p328045716919"><a name="p328045716919"></a><a name="p328045716919"></a>Failed to complete the request because the server receives an invalid response from an upstream server.</p>
    </td>
    </tr>
    <tr id="row728015571697"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p42801757490"><a name="p42801757490"></a><a name="p42801757490"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p728015720916"><a name="p728015720916"></a><a name="p728015720916"></a>Failed to complete the request because the system is unavailable.</p>
    </td>
    </tr>
    <tr id="row928075714911"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p12807571690"><a name="p12807571690"></a><a name="p12807571690"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p12804571095"><a name="p12804571095"></a><a name="p12804571095"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


