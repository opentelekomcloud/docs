# Querying a Specified API Version<a name="EN-US_TOPIC_0134546379"></a>

## Function<a name="section9828101517313"></a>

This API is used to query a specified API version of ELB.

## URI<a name="section13830201510315"></a>

GET /\{api\_version\}

**Table  1**  Parameter description

<a name="table383815150316"></a>
<table><thead align="left"><tr id="row1614121683114"><th class="cellrowborder" valign="top" width="16.161616161616163%" id="mcps1.2.4.1.1"><p id="p111411516173117"><a name="p111411516173117"></a><a name="p111411516173117"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.161616161616163%" id="mcps1.2.4.1.2"><p id="p2014121613110"><a name="p2014121613110"></a><a name="p2014121613110"></a><strong id="b842352706192244"><a name="b842352706192244"></a><a name="b842352706192244"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="67.67676767676768%" id="mcps1.2.4.1.3"><p id="p81411416113111"><a name="p81411416113111"></a><a name="p81411416113111"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row2142716173114"><td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.4.1.1 "><p id="p11142121613118"><a name="p11142121613118"></a><a name="p11142121613118"></a>api_version</p>
</td>
<td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.4.1.2 "><p id="p17142191619318"><a name="p17142191619318"></a><a name="p17142191619318"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="67.67676767676768%" headers="mcps1.2.4.1.3 "><p id="p1914201643118"><a name="p1914201643118"></a><a name="p1914201643118"></a>Specifies the API version.</p>
</td>
</tr>
</tbody>
</table>

-   **Example**

    /v1.0


## Request<a name="section9847121516313"></a>

-   Request parameters

    None

-   Example request

    None


## Response<a name="section884711159311"></a>

-   Response parameters

    **Table  2**  Response parameters

    <a name="table14855415113115"></a>
    <table><thead align="left"><tr id="row10142191613119"><th class="cellrowborder" valign="top" width="15%" id="mcps1.2.4.1.1"><p id="p181421162310"><a name="p181421162310"></a><a name="p181421162310"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16%" id="mcps1.2.4.1.2"><p id="p17142181683113"><a name="p17142181683113"></a><a name="p17142181683113"></a><strong id="b842352706145623"><a name="b842352706145623"></a><a name="b842352706145623"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="69%" id="mcps1.2.4.1.3"><p id="p1614215167317"><a name="p1614215167317"></a><a name="p1614215167317"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1914316163317"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.1 "><p id="p814319169314"><a name="p814319169314"></a><a name="p814319169314"></a>version</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p3143151663113"><a name="p3143151663113"></a><a name="p3143151663113"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="69%" headers="mcps1.2.4.1.3 "><p id="p17143116143116"><a name="p17143116143116"></a><a name="p17143116143116"></a>Specifies the API version.</p>
    </td>
    </tr>
    <tr id="row201431116183115"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.1 "><p id="p1514341613117"><a name="p1514341613117"></a><a name="p1514341613117"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p1650194025018"><a name="p1650194025018"></a><a name="p1650194025018"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="69%" headers="mcps1.2.4.1.3 "><p id="p8143161603116"><a name="p8143161603116"></a><a name="p8143161603116"></a>Specifies the version ID, for example, <strong id="b84235270619258"><a name="b84235270619258"></a><a name="b84235270619258"></a>v1</strong>.</p>
    </td>
    </tr>
    <tr id="row1314318166312"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.1 "><p id="p1514351683110"><a name="p1514351683110"></a><a name="p1514351683110"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p998517393811"><a name="p998517393811"></a><a name="p998517393811"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="69%" headers="mcps1.2.4.1.3 "><p id="p131431416103116"><a name="p131431416103116"></a><a name="p131431416103116"></a>Specifies the API URL.</p>
    </td>
    </tr>
    <tr id="row71431616123117"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.1 "><p id="p17144216173119"><a name="p17144216173119"></a><a name="p17144216173119"></a>href</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p61444162310"><a name="p61444162310"></a><a name="p61444162310"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="69%" headers="mcps1.2.4.1.3 "><p id="p16144131619312"><a name="p16144131619312"></a><a name="p16144131619312"></a>Specifies the reference address of the current API version.</p>
    </td>
    </tr>
    <tr id="row0144141615318"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.1 "><p id="p114471623115"><a name="p114471623115"></a><a name="p114471623115"></a>rel</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p11444164317"><a name="p11444164317"></a><a name="p11444164317"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="69%" headers="mcps1.2.4.1.3 "><p id="p13144416113118"><a name="p13144416113118"></a><a name="p13144416113118"></a>Specifies the relationship between the current API version and the referenced address.</p>
    </td>
    </tr>
    <tr id="row15144101663113"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.1 "><p id="p0144151653113"><a name="p0144151653113"></a><a name="p0144151653113"></a>version</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p191441816153116"><a name="p191441816153116"></a><a name="p191441816153116"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="69%" headers="mcps1.2.4.1.3 "><p id="p10144316163113"><a name="p10144316163113"></a><a name="p10144316163113"></a>Specifies the version. If minor versions are supported, set this parameter to the latest minor version. If minor versions are not supported, leave this parameter blank.</p>
    </td>
    </tr>
    <tr id="row1014481653115"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.1 "><p id="p51448168312"><a name="p51448168312"></a><a name="p51448168312"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p238824715508"><a name="p238824715508"></a><a name="p238824715508"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="69%" headers="mcps1.2.4.1.3 "><p id="p1414441612319"><a name="p1414441612319"></a><a name="p1414441612319"></a>Specifies the version status. Options are as follows:</p>
    <a name="ul495925113499"></a><a name="ul495925113499"></a><ul id="ul495925113499"><li><strong id="b1595975124915"><a name="b1595975124915"></a><a name="b1595975124915"></a>CURRENT</strong>: indicates the major version.</li><li><strong id="b1590985317492"><a name="b1590985317492"></a><a name="b1590985317492"></a>SUPPORTED</strong>: indicates that the version is an old one, but it is still supported.</li><li><strong id="b11764355174919"><a name="b11764355174919"></a><a name="b11764355174919"></a>DEPRECATED</strong>: indicates a deprecated version which may be deleted later.</li></ul>
    </td>
    </tr>
    <tr id="row1714401617318"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.1 "><p id="p131441316163111"><a name="p131441316163111"></a><a name="p131441316163111"></a>updated</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p19144101617317"><a name="p19144101617317"></a><a name="p19144101617317"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="69%" headers="mcps1.2.4.1.3 "><p id="p141449168315"><a name="p141449168315"></a><a name="p141449168315"></a>Specifies the version release time, which must be the UTC time. For example, the release time of v1 is 2014-06-28T12:20:21Z.</p>
    </td>
    </tr>
    <tr id="row15144316203118"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.1 "><p id="p17144716183112"><a name="p17144716183112"></a><a name="p17144716183112"></a>min_version</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p91441316193117"><a name="p91441316193117"></a><a name="p91441316193117"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="69%" headers="mcps1.2.4.1.3 "><p id="p514413164311"><a name="p514413164311"></a><a name="p514413164311"></a>Specifies the minor version. If minor versions are supported, set this parameter to the earliest minor version. If minor versions are not supported, leave this parameter blank.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {  
       "version": {  
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
     }
    ```


## Status Code<a name="section1792221513312"></a>

-   Normal

    200

-   Abnormal

    <a name="table792881519311"></a>
    <table><thead align="left"><tr id="row1114621620318"><th class="cellrowborder" valign="top" width="10.040000000000001%" id="mcps1.1.4.1.1"><p id="p81466162315"><a name="p81466162315"></a><a name="p81466162315"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="54.47%" id="mcps1.1.4.1.2"><p id="p4515643155516"><a name="p4515643155516"></a><a name="p4515643155516"></a>Message</p>
    </th>
    <th class="cellrowborder" valign="top" width="35.49%" id="mcps1.1.4.1.3"><p id="p1714611611311"><a name="p1714611611311"></a><a name="p1714611611311"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row10146141643115"><td class="cellrowborder" valign="top" width="10.040000000000001%" headers="mcps1.1.4.1.1 "><p id="p2146716183117"><a name="p2146716183117"></a><a name="p2146716183117"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.47%" headers="mcps1.1.4.1.2 "><p id="p2040805665518"><a name="p2040805665518"></a><a name="p2040805665518"></a>Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.49%" headers="mcps1.1.4.1.3 "><p id="p8146121673119"><a name="p8146121673119"></a><a name="p8146121673119"></a>Request error.</p>
    </td>
    </tr>
    <tr id="row714611614312"><td class="cellrowborder" valign="top" width="10.040000000000001%" headers="mcps1.1.4.1.1 "><p id="p181461516163118"><a name="p181461516163118"></a><a name="p181461516163118"></a>401</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.47%" headers="mcps1.1.4.1.2 "><p id="p10409556105516"><a name="p10409556105516"></a><a name="p10409556105516"></a>Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.49%" headers="mcps1.1.4.1.3 "><p id="p18146111643116"><a name="p18146111643116"></a><a name="p18146111643116"></a>The authentication information is not provided or is incorrect.</p>
    </td>
    </tr>
    <tr id="row16146316103114"><td class="cellrowborder" valign="top" width="10.040000000000001%" headers="mcps1.1.4.1.1 "><p id="p12146516113114"><a name="p12146516113114"></a><a name="p12146516113114"></a>403</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.47%" headers="mcps1.1.4.1.2 "><p id="p104095561552"><a name="p104095561552"></a><a name="p104095561552"></a>Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.49%" headers="mcps1.1.4.1.3 "><p id="p1814621615316"><a name="p1814621615316"></a><a name="p1814621615316"></a>The request was forbidden.</p>
    </td>
    </tr>
    <tr id="row10146191663115"><td class="cellrowborder" valign="top" width="10.040000000000001%" headers="mcps1.1.4.1.1 "><p id="p191461016143116"><a name="p191461016143116"></a><a name="p191461016143116"></a>404</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.47%" headers="mcps1.1.4.1.2 "><p id="p4409165613553"><a name="p4409165613553"></a><a name="p4409165613553"></a>Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.49%" headers="mcps1.1.4.1.3 "><p id="p121462165314"><a name="p121462165314"></a><a name="p121462165314"></a>The requested resource does not exist.</p>
    </td>
    </tr>
    <tr id="row1146151613111"><td class="cellrowborder" valign="top" width="10.040000000000001%" headers="mcps1.1.4.1.1 "><p id="p7146201603114"><a name="p7146201603114"></a><a name="p7146201603114"></a>408</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.47%" headers="mcps1.1.4.1.2 "><p id="p12409115645514"><a name="p12409115645514"></a><a name="p12409115645514"></a>Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.49%" headers="mcps1.1.4.1.3 "><p id="p71475166314"><a name="p71475166314"></a><a name="p71475166314"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row514710169314"><td class="cellrowborder" valign="top" width="10.040000000000001%" headers="mcps1.1.4.1.1 "><p id="p161471416173110"><a name="p161471416173110"></a><a name="p161471416173110"></a>429</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.47%" headers="mcps1.1.4.1.2 "><p id="p1040914561558"><a name="p1040914561558"></a><a name="p1040914561558"></a>Too Many Requests</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.49%" headers="mcps1.1.4.1.3 "><p id="p31471116103115"><a name="p31471116103115"></a><a name="p31471116103115"></a>The number requests exceeded the upper limit.</p>
    </td>
    </tr>
    <tr id="row11147141610314"><td class="cellrowborder" valign="top" width="10.040000000000001%" headers="mcps1.1.4.1.1 "><p id="p1814731615311"><a name="p1814731615311"></a><a name="p1814731615311"></a>500</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.47%" headers="mcps1.1.4.1.2 "><p id="p17409185610558"><a name="p17409185610558"></a><a name="p17409185610558"></a>Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.49%" headers="mcps1.1.4.1.3 "><p id="p214715161310"><a name="p214715161310"></a><a name="p214715161310"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row714701613314"><td class="cellrowborder" valign="top" width="10.040000000000001%" headers="mcps1.1.4.1.1 "><p id="p01474166312"><a name="p01474166312"></a><a name="p01474166312"></a>503</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.47%" headers="mcps1.1.4.1.2 "><p id="p84091256155518"><a name="p84091256155518"></a><a name="p84091256155518"></a>Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.49%" headers="mcps1.1.4.1.3 "><p id="p1014717162317"><a name="p1014717162317"></a><a name="p1014717162317"></a>The service is currently unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


