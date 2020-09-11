# Querying All API Versions<a name="EN-US_TOPIC_0171212585"></a>

## Function<a name="section66578044"></a>

This API is used to query all API versions supported by Cloud Eye.

## URI<a name="section62331491"></a>

GET /

## Request<a name="section24112512"></a>

Example request

```
GET https://{Cloud Eye endpoint}/
```

## Response<a name="section15686020"></a>

-   Response parameters

    **Table  1**  Response parameters

    <a name="table26246518152631"></a>
    <table><thead align="left"><tr id="row29602547152631"><th class="cellrowborder" valign="top" width="17.61%" id="mcps1.2.4.1.1"><p id="p1143665616354"><a name="p1143665616354"></a><a name="p1143665616354"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.23%" id="mcps1.2.4.1.2"><p id="p11440156143517"><a name="p11440156143517"></a><a name="p11440156143517"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="64.16%" id="mcps1.2.4.1.3"><p id="p244212561357"><a name="p244212561357"></a><a name="p244212561357"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row56174697152631"><td class="cellrowborder" valign="top" width="17.61%" headers="mcps1.2.4.1.1 "><p id="p4445556153516"><a name="p4445556153516"></a><a name="p4445556153516"></a>versions</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.23%" headers="mcps1.2.4.1.2 "><p id="p444855610353"><a name="p444855610353"></a><a name="p444855610353"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.16%" headers="mcps1.2.4.1.3 "><p id="p344911569354"><a name="p344911569354"></a><a name="p344911569354"></a>Specifies the list of all versions.</p>
    <p id="p76411522123610"><a name="p76411522123610"></a><a name="p76411522123610"></a><a href="#table11622191810339">Table 2</a> describes the parameters.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2** **versions**  field data structure description

    <a name="table11622191810339"></a>
    <table><thead align="left"><tr id="row4619181833318"><th class="cellrowborder" valign="top" width="17.61%" id="mcps1.2.4.1.1"><p id="p8618218183315"><a name="p8618218183315"></a><a name="p8618218183315"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.23%" id="mcps1.2.4.1.2"><p id="p46182182336"><a name="p46182182336"></a><a name="p46182182336"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="64.16%" id="mcps1.2.4.1.3"><p id="p1361819181337"><a name="p1361819181337"></a><a name="p1361819181337"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1261921810335"><td class="cellrowborder" valign="top" width="17.61%" headers="mcps1.2.4.1.1 "><p id="p1619718203313"><a name="p1619718203313"></a><a name="p1619718203313"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.23%" headers="mcps1.2.4.1.2 "><p id="p186194185335"><a name="p186194185335"></a><a name="p186194185335"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.16%" headers="mcps1.2.4.1.3 "><p id="p8619418123311"><a name="p8619418123311"></a><a name="p8619418123311"></a>Specifies the version ID, for example, v1.</p>
    </td>
    </tr>
    <tr id="row106201018103311"><td class="cellrowborder" valign="top" width="17.61%" headers="mcps1.2.4.1.1 "><p id="p12620181823313"><a name="p12620181823313"></a><a name="p12620181823313"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.23%" headers="mcps1.2.4.1.2 "><p id="p12620171823314"><a name="p12620171823314"></a><a name="p12620171823314"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.16%" headers="mcps1.2.4.1.3 "><p id="p46207186338"><a name="p46207186338"></a><a name="p46207186338"></a>Specifies the API URL.</p>
    <p id="p551085418378"><a name="p551085418378"></a><a name="p551085418378"></a>For details, see <a href="#table7157926103418">Table 3</a>.</p>
    </td>
    </tr>
    <tr id="row186211518163313"><td class="cellrowborder" valign="top" width="17.61%" headers="mcps1.2.4.1.1 "><p id="p1562111184330"><a name="p1562111184330"></a><a name="p1562111184330"></a>version</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.23%" headers="mcps1.2.4.1.2 "><p id="p762171863315"><a name="p762171863315"></a><a name="p762171863315"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.16%" headers="mcps1.2.4.1.3 "><p id="p196210182338"><a name="p196210182338"></a><a name="p196210182338"></a>Specifies the API version. If the APIs of this version support microversions, set this parameter to the supported maximum microversion. If the microversion is not supported, leave this parameter blank.</p>
    </td>
    </tr>
    <tr id="row862171813317"><td class="cellrowborder" valign="top" width="17.61%" headers="mcps1.2.4.1.1 "><p id="p262191883312"><a name="p262191883312"></a><a name="p262191883312"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.23%" headers="mcps1.2.4.1.2 "><p id="p20621118153312"><a name="p20621118153312"></a><a name="p20621118153312"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.16%" headers="mcps1.2.4.1.3 "><p id="p362121813335"><a name="p362121813335"></a><a name="p362121813335"></a>Specifies the version status. Possible values are as follows:</p>
    <p id="p10621201813316"><a name="p10621201813316"></a><a name="p10621201813316"></a><strong id="b842352706192132"><a name="b842352706192132"></a><a name="b842352706192132"></a>CURRENT</strong>: indicates a primary version.</p>
    <p id="p662112186338"><a name="p662112186338"></a><a name="p662112186338"></a><strong id="b1164542231713"><a name="b1164542231713"></a><a name="b1164542231713"></a>SUPPORTED</strong>: indicates an old version but is still supported.</p>
    <p id="p18621141813331"><a name="p18621141813331"></a><a name="p18621141813331"></a><strong id="b164043941413"><a name="b164043941413"></a><a name="b164043941413"></a>DEPRECATED</strong>: indicates a deprecated version which may be deleted later.</p>
    </td>
    </tr>
    <tr id="row16223181336"><td class="cellrowborder" valign="top" width="17.61%" headers="mcps1.2.4.1.1 "><p id="p1062261817332"><a name="p1062261817332"></a><a name="p1062261817332"></a>updated</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.23%" headers="mcps1.2.4.1.2 "><p id="p16228184334"><a name="p16228184334"></a><a name="p16228184334"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.16%" headers="mcps1.2.4.1.3 "><p id="p56220183330"><a name="p56220183330"></a><a name="p56220183330"></a>Specifies the version release time, which must be the UTC time. For example, the release time of v1 is 2014-06-28T12:20:21Z.</p>
    </td>
    </tr>
    <tr id="row206221018163316"><td class="cellrowborder" valign="top" width="17.61%" headers="mcps1.2.4.1.1 "><p id="p8622171816333"><a name="p8622171816333"></a><a name="p8622171816333"></a>min_version</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.23%" headers="mcps1.2.4.1.2 "><p id="p4622121819338"><a name="p4622121819338"></a><a name="p4622121819338"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.16%" headers="mcps1.2.4.1.3 "><p id="p16221118103315"><a name="p16221118103315"></a><a name="p16221118103315"></a>If the APIs of this version support microversions, set this parameter to the supported minimum microversion. If not, leave this parameter blank.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **links**  field data structure description

    <a name="table7157926103418"></a>
    <table><thead align="left"><tr id="row6157112653419"><th class="cellrowborder" valign="top" width="17.61%" id="mcps1.2.4.1.1"><p id="p1515711268345"><a name="p1515711268345"></a><a name="p1515711268345"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.23%" id="mcps1.2.4.1.2"><p id="p4157192614343"><a name="p4157192614343"></a><a name="p4157192614343"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="64.16%" id="mcps1.2.4.1.3"><p id="p7157102613346"><a name="p7157102613346"></a><a name="p7157102613346"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1915852612341"><td class="cellrowborder" valign="top" width="17.61%" headers="mcps1.2.4.1.1 "><p id="p1515872614346"><a name="p1515872614346"></a><a name="p1515872614346"></a>href</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.23%" headers="mcps1.2.4.1.2 "><p id="p2158162616349"><a name="p2158162616349"></a><a name="p2158162616349"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.16%" headers="mcps1.2.4.1.3 "><p id="p615813265341"><a name="p615813265341"></a><a name="p615813265341"></a>Specifies the reference address of the current API version.</p>
    </td>
    </tr>
    <tr id="row1158182615345"><td class="cellrowborder" valign="top" width="17.61%" headers="mcps1.2.4.1.1 "><p id="p4158162633414"><a name="p4158162633414"></a><a name="p4158162633414"></a>rel</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.23%" headers="mcps1.2.4.1.2 "><p id="p191584262345"><a name="p191584262345"></a><a name="p191584262345"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.16%" headers="mcps1.2.4.1.3 "><p id="p4158182603413"><a name="p4158182603413"></a><a name="p4158182603413"></a>Specifies the relationship between the current API version and the referenced address.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
      "versions": [
        {
          "id": "V1.0",
          "links": [
            {
              "href": "https://x.x.x.x/V1.0/",
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


## Returned Values<a name="section6956456"></a>

-   Normal

    200

-   Abnormal

    <a name="table46793998"></a>
    <table><thead align="left"><tr id="row65573909"><th class="cellrowborder" valign="top" width="30%" id="mcps1.1.3.1.1"><p id="p9886408"><a name="p9886408"></a><a name="p9886408"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="70%" id="mcps1.1.3.1.2"><p id="p62601592"><a name="p62601592"></a><a name="p62601592"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row37564172"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.3.1.1 "><p id="p22799085"><a name="p22799085"></a><a name="p22799085"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.1.3.1.2 "><p id="p44643603"><a name="p44643603"></a><a name="p44643603"></a>Request error</p>
    </td>
    </tr>
    <tr id="row66248115"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.3.1.1 "><p id="p64497130"><a name="p64497130"></a><a name="p64497130"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.1.3.1.2 "><p id="p42202994"><a name="p42202994"></a><a name="p42202994"></a>The authentication information is not provided or is incorrect.</p>
    </td>
    </tr>
    <tr id="row44282627"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.3.1.1 "><p id="p30123063"><a name="p30123063"></a><a name="p30123063"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.1.3.1.2 "><p id="p15114764"><a name="p15114764"></a><a name="p15114764"></a>You are forbidden to access the page requested.</p>
    </td>
    </tr>
    <tr id="row1815156"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.3.1.1 "><p id="p12809933"><a name="p12809933"></a><a name="p12809933"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.1.3.1.2 "><p id="p10309404"><a name="p10309404"></a><a name="p10309404"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row25675773"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.3.1.1 "><p id="p66471715"><a name="p66471715"></a><a name="p66471715"></a>429 Too Many Requests</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.1.3.1.2 "><p id="p5281111"><a name="p5281111"></a><a name="p5281111"></a>Concurrent requests are excessive.</p>
    </td>
    </tr>
    <tr id="row47530006"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.3.1.1 "><p id="p24725298"><a name="p24725298"></a><a name="p24725298"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.1.3.1.2 "><p id="p39567352"><a name="p39567352"></a><a name="p39567352"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row20561848"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.3.1.1 "><p id="p54897010"><a name="p54897010"></a><a name="p54897010"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.1.3.1.2 "><p id="p1451523117958"><a name="p1451523117958"></a><a name="p1451523117958"></a>The service is currently unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Code<a name="section137621219143417"></a>

For details, see  [Error Codes](error-codes.md).

