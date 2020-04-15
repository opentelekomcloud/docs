# Querying All API Versions<a name="EN-US_TOPIC_0134546378"></a>

## Function<a name="section3280114143010"></a>

This API is used to query all API versions of ELB.

## URI<a name="section1029091414304"></a>

GET /

## Request<a name="section192941514193013"></a>

-   Request parameters

    None

-   Example request

    None


## Response<a name="section12951814123017"></a>

-   Response parameters

    **Table  1**  Response parameters

    <a name="table1829981433014"></a>
    <table><thead align="left"><tr id="row13525171413019"><th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.4.1.1"><p id="p15256149305"><a name="p15256149305"></a><a name="p15256149305"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15%" id="mcps1.2.4.1.2"><p id="p165251714123013"><a name="p165251714123013"></a><a name="p165251714123013"></a><strong id="b842352706145623"><a name="b842352706145623"></a><a name="b842352706145623"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="71%" id="mcps1.2.4.1.3"><p id="p4448384817"><a name="p4448384817"></a><a name="p4448384817"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1452511417307"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="p052513142301"><a name="p052513142301"></a><a name="p052513142301"></a>versions</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="p7525131413016"><a name="p7525131413016"></a><a name="p7525131413016"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="p55251814193016"><a name="p55251814193016"></a><a name="p55251814193016"></a>Lists all API versions.</p>
    </td>
    </tr>
    <tr id="row85258147302"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="p15525131473014"><a name="p15525131473014"></a><a name="p15525131473014"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="p1752591416309"><a name="p1752591416309"></a><a name="p1752591416309"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="p6525814133015"><a name="p6525814133015"></a><a name="p6525814133015"></a>Specifies the version ID, for example, <strong id="b84235270619258"><a name="b84235270619258"></a><a name="b84235270619258"></a>v1</strong>.</p>
    </td>
    </tr>
    <tr id="row185251714173016"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="p35258147305"><a name="p35258147305"></a><a name="p35258147305"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="p552511411306"><a name="p552511411306"></a><a name="p552511411306"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="p1552541433016"><a name="p1552541433016"></a><a name="p1552541433016"></a>Specifies the API URL.</p>
    </td>
    </tr>
    <tr id="row55255149303"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="p152514149305"><a name="p152514149305"></a><a name="p152514149305"></a>href</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="p19777202015503"><a name="p19777202015503"></a><a name="p19777202015503"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="p1952661418305"><a name="p1952661418305"></a><a name="p1952661418305"></a>Specifies the reference address of the current API version.</p>
    </td>
    </tr>
    <tr id="row1952661413303"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="p13526121413010"><a name="p13526121413010"></a><a name="p13526121413010"></a>rel</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="p1994962395012"><a name="p1994962395012"></a><a name="p1994962395012"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="p10526131410307"><a name="p10526131410307"></a><a name="p10526131410307"></a>Specifies the relationship between the current API version and the referenced address.</p>
    </td>
    </tr>
    <tr id="row2052611443013"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="p55263143301"><a name="p55263143301"></a><a name="p55263143301"></a>version</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="p1152601413307"><a name="p1152601413307"></a><a name="p1152601413307"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="p14526514183016"><a name="p14526514183016"></a><a name="p14526514183016"></a>Specifies the version. If minor versions are supported, set this parameter to the latest minor version. If minor versions are not supported, leave this parameter blank.</p>
    </td>
    </tr>
    <tr id="row1352681415300"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="p1252631416307"><a name="p1252631416307"></a><a name="p1252631416307"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="p16526414193010"><a name="p16526414193010"></a><a name="p16526414193010"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="p1952616141302"><a name="p1952616141302"></a><a name="p1952616141302"></a>Specifies the version status. Options are as follows:</p>
    <a name="ul169821627114814"></a><a name="ul169821627114814"></a><ul id="ul169821627114814"><li><strong id="b6982172718489"><a name="b6982172718489"></a><a name="b6982172718489"></a>CURRENT</strong>: indicates the major version.</li><li><strong id="b196351729194820"><a name="b196351729194820"></a><a name="b196351729194820"></a>SUPPORTED</strong>: indicates that the version is an old one, but it is still supported.</li><li><strong id="b659213164818"><a name="b659213164818"></a><a name="b659213164818"></a>DEPRECATED</strong>: indicates a deprecated version which may be deleted later.</li></ul>
    </td>
    </tr>
    <tr id="row17526914113012"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="p352611418308"><a name="p352611418308"></a><a name="p352611418308"></a>updated</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="p8526121414305"><a name="p8526121414305"></a><a name="p8526121414305"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="p1526181453010"><a name="p1526181453010"></a><a name="p1526181453010"></a>Specifies the version release time, which must be the UTC time. For example, the release time of v1 is 2014-06-28T12:20:21Z.</p>
    </td>
    </tr>
    <tr id="row852612147307"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.1 "><p id="p952651415305"><a name="p952651415305"></a><a name="p952651415305"></a>min_version</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="p6189633115014"><a name="p6189633115014"></a><a name="p6189633115014"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="p16526914193017"><a name="p16526914193017"></a><a name="p16526914193017"></a>Specifies the minor version. If minor versions are supported, set this parameter to the earliest minor version. If minor versions are not supported, leave this parameter blank.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    { 
       "versions": [ 
         { 
           "id": "v1.0", 
           "links": [ 
             { 
               "href": "https://{elb_endpoint}/v1.0/", 
               "rel": "self" 
             } 
           ], 
           "min_version": "", 
           "status": "CURRENT", 
           "updated": "2018-09-30T00:00:00Z", 
           "version": "" 
         } 
       ] 
     }
    ```


## Status Code<a name="section163541714123020"></a>

-   Normal

    200

-   Abnormal

    <a name="table835781418301"></a>
    <table><thead align="left"><tr id="row9526214113014"><th class="cellrowborder" valign="top" width="12.13%" id="mcps1.1.4.1.1"><p id="p1352614149300"><a name="p1352614149300"></a><a name="p1352614149300"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="52.38%" id="mcps1.1.4.1.2"><p id="p522343074810"><a name="p522343074810"></a><a name="p522343074810"></a>Message</p>
    </th>
    <th class="cellrowborder" valign="top" width="35.49%" id="mcps1.1.4.1.3"><p id="p1952681473010"><a name="p1952681473010"></a><a name="p1952681473010"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1752691483011"><td class="cellrowborder" valign="top" width="12.13%" headers="mcps1.1.4.1.1 "><p id="p1052641493017"><a name="p1052641493017"></a><a name="p1052641493017"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.38%" headers="mcps1.1.4.1.2 "><p id="p5421540134813"><a name="p5421540134813"></a><a name="p5421540134813"></a>Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.49%" headers="mcps1.1.4.1.3 "><p id="p125261414183017"><a name="p125261414183017"></a><a name="p125261414183017"></a>Request error.</p>
    </td>
    </tr>
    <tr id="row1352613145300"><td class="cellrowborder" valign="top" width="12.13%" headers="mcps1.1.4.1.1 "><p id="p16526314133013"><a name="p16526314133013"></a><a name="p16526314133013"></a>401</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.38%" headers="mcps1.1.4.1.2 "><p id="p104212040164813"><a name="p104212040164813"></a><a name="p104212040164813"></a>Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.49%" headers="mcps1.1.4.1.3 "><p id="p85261914163019"><a name="p85261914163019"></a><a name="p85261914163019"></a>The authentication information is not provided or is incorrect.</p>
    </td>
    </tr>
    <tr id="row135261014163016"><td class="cellrowborder" valign="top" width="12.13%" headers="mcps1.1.4.1.1 "><p id="p352611140306"><a name="p352611140306"></a><a name="p352611140306"></a>403</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.38%" headers="mcps1.1.4.1.2 "><p id="p74211540154810"><a name="p74211540154810"></a><a name="p74211540154810"></a>Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.49%" headers="mcps1.1.4.1.3 "><p id="p552681412306"><a name="p552681412306"></a><a name="p552681412306"></a>The request was forbidden.</p>
    </td>
    </tr>
    <tr id="row18526414193016"><td class="cellrowborder" valign="top" width="12.13%" headers="mcps1.1.4.1.1 "><p id="p3526914183011"><a name="p3526914183011"></a><a name="p3526914183011"></a>404</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.38%" headers="mcps1.1.4.1.2 "><p id="p4421104084819"><a name="p4421104084819"></a><a name="p4421104084819"></a>Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.49%" headers="mcps1.1.4.1.3 "><p id="p13526161419305"><a name="p13526161419305"></a><a name="p13526161419305"></a>The requested resource does not exist.</p>
    </td>
    </tr>
    <tr id="row55268146301"><td class="cellrowborder" valign="top" width="12.13%" headers="mcps1.1.4.1.1 "><p id="p1852613141307"><a name="p1852613141307"></a><a name="p1852613141307"></a>408</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.38%" headers="mcps1.1.4.1.2 "><p id="p142174084820"><a name="p142174084820"></a><a name="p142174084820"></a>Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.49%" headers="mcps1.1.4.1.3 "><p id="p11526171443016"><a name="p11526171443016"></a><a name="p11526171443016"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row195266148306"><td class="cellrowborder" valign="top" width="12.13%" headers="mcps1.1.4.1.1 "><p id="p1152611410307"><a name="p1152611410307"></a><a name="p1152611410307"></a>429</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.38%" headers="mcps1.1.4.1.2 "><p id="p6421184013488"><a name="p6421184013488"></a><a name="p6421184013488"></a>Too Many Requests</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.49%" headers="mcps1.1.4.1.3 "><p id="p1952651416303"><a name="p1952651416303"></a><a name="p1952651416303"></a>The number requests exceeded the upper limit.</p>
    </td>
    </tr>
    <tr id="row452671473019"><td class="cellrowborder" valign="top" width="12.13%" headers="mcps1.1.4.1.1 "><p id="p4526214123016"><a name="p4526214123016"></a><a name="p4526214123016"></a>500</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.38%" headers="mcps1.1.4.1.2 "><p id="p8421940124817"><a name="p8421940124817"></a><a name="p8421940124817"></a>Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.49%" headers="mcps1.1.4.1.3 "><p id="p14528101418306"><a name="p14528101418306"></a><a name="p14528101418306"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row18528201420300"><td class="cellrowborder" valign="top" width="12.13%" headers="mcps1.1.4.1.1 "><p id="p352851417307"><a name="p352851417307"></a><a name="p352851417307"></a>503</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.38%" headers="mcps1.1.4.1.2 "><p id="p164211440114815"><a name="p164211440114815"></a><a name="p164211440114815"></a>Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.49%" headers="mcps1.1.4.1.3 "><p id="p1852851403019"><a name="p1852851403019"></a><a name="p1852851403019"></a>The service is currently unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


