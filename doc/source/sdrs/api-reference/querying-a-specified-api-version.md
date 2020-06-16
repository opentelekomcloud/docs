# Querying a Specified API Version<a name="sdrs_05_0202"></a>

## Function<a name="section1593161881114"></a>

This interface is used to query a specified API version.

## Constraints and Limitations<a name="section165931918141120"></a>

None

## URI<a name="section13593518191116"></a>

-   URI format

    GET /\{api\_version\}

-   Parameter description

    <a name="table186092189116"></a>
    <table><thead align="left"><tr id="row4202191910113"><th class="cellrowborder" valign="top" width="29.59%" id="mcps1.1.4.1.1"><p id="p1020271916119"><a name="p1020271916119"></a><a name="p1020271916119"></a><strong id="b84235270615443"><a name="b84235270615443"></a><a name="b84235270615443"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.33%" id="mcps1.1.4.1.2"><p id="p1620211981114"><a name="p1620211981114"></a><a name="p1620211981114"></a><strong id="b84235270615447"><a name="b84235270615447"></a><a name="b84235270615447"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="54.08%" id="mcps1.1.4.1.3"><p id="p5202151951112"><a name="p5202151951112"></a><a name="p5202151951112"></a><strong id="b84235270615457"><a name="b84235270615457"></a><a name="b84235270615457"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row10202719151120"><td class="cellrowborder" valign="top" width="29.59%" headers="mcps1.1.4.1.1 "><p id="p620241931117"><a name="p620241931117"></a><a name="p620241931117"></a>api_version</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.33%" headers="mcps1.1.4.1.2 "><p id="p1920261913115"><a name="p1920261913115"></a><a name="p1920261913115"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.08%" headers="mcps1.1.4.1.3 "><p id="p22026196116"><a name="p22026196116"></a><a name="p22026196116"></a>Specifies the API version, for example, <strong id="b84235270619258"><a name="b84235270619258"></a><a name="b84235270619258"></a>v1</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section11625111891113"></a>

-   Request parameters

    None

-   Example request

    GET https://\{endpoint\}/v1


## Response<a name="section196251718101117"></a>

-   Parameter description

    <a name="table1265715185111"></a>
    <table><thead align="left"><tr id="row16202121991119"><th class="cellrowborder" valign="top" width="29.07%" id="mcps1.1.4.1.1"><p id="p1220211191119"><a name="p1220211191119"></a><a name="p1220211191119"></a><strong id="b842352706151210"><a name="b842352706151210"></a><a name="b842352706151210"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.44%" id="mcps1.1.4.1.2"><p id="p13202919161115"><a name="p13202919161115"></a><a name="p13202919161115"></a><strong id="b84235270615453"><a name="b84235270615453"></a><a name="b84235270615453"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53.49%" id="mcps1.1.4.1.3"><p id="p1720241911117"><a name="p1720241911117"></a><a name="p1720241911117"></a><strong id="b84235270615457_1"><a name="b84235270615457_1"></a><a name="b84235270615457_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row20202171919110"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.1.4.1.1 "><p id="p1320281917114"><a name="p1320281917114"></a><a name="p1320281917114"></a>version</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.1.4.1.2 "><p id="p162021819121111"><a name="p162021819121111"></a><a name="p162021819121111"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.1.4.1.3 "><p id="p10202121911111"><a name="p10202121911111"></a><a name="p10202121911111"></a>Specifies the version of an API.</p>
    <p id="p19242375287"><a name="p19242375287"></a><a name="p19242375287"></a>For details, see <a href="#table14672161881114">Table 1</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  1**  Description of field  **version**

    <a name="table14672161881114"></a>
    <table><thead align="left"><tr id="row020212196111"><th class="cellrowborder" valign="top" width="29.07%" id="mcps1.2.4.1.1"><p id="p720210196118"><a name="p720210196118"></a><a name="p720210196118"></a><strong id="b842352706151210_1"><a name="b842352706151210_1"></a><a name="b842352706151210_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.44%" id="mcps1.2.4.1.2"><p id="p1920271915118"><a name="p1920271915118"></a><a name="p1920271915118"></a><strong id="b84235270615453_1"><a name="b84235270615453_1"></a><a name="b84235270615453_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53.49%" id="mcps1.2.4.1.3"><p id="p8202219121112"><a name="p8202219121112"></a><a name="p8202219121112"></a><strong id="b84235270615457_2"><a name="b84235270615457_2"></a><a name="b84235270615457_2"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row22021319181119"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p9202161913115"><a name="p9202161913115"></a><a name="p9202161913115"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p52021199111"><a name="p52021199111"></a><a name="p52021199111"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p0202161941117"><a name="p0202161941117"></a><a name="p0202161941117"></a>Specifies the version ID, for example, <strong id="b84235270619258_1"><a name="b84235270619258_1"></a><a name="b84235270619258_1"></a>v1</strong>.</p>
    </td>
    </tr>
    <tr id="row152021419121113"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p42021819141117"><a name="p42021819141117"></a><a name="p42021819141117"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p320213193119"><a name="p320213193119"></a><a name="p320213193119"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p520218195117"><a name="p520218195117"></a><a name="p520218195117"></a>Specifies the API URL.</p>
    <p id="p14541184611292"><a name="p14541184611292"></a><a name="p14541184611292"></a>For details, see <a href="#table122284216266">Table 2</a>.</p>
    </td>
    </tr>
    <tr id="row420214194116"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p2202191914110"><a name="p2202191914110"></a><a name="p2202191914110"></a>version</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p16202171919111"><a name="p16202171919111"></a><a name="p16202171919111"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p5202919181115"><a name="p5202919181115"></a><a name="p5202919181115"></a>Specifies the version. If the APIs of this version support microversions, the system returns the supported maximum microversion. If the microversion is not supported, the system returns an empty value. </p>
    </td>
    </tr>
    <tr id="row1720261915113"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p12021619151117"><a name="p12021619151117"></a><a name="p12021619151117"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p1218111991115"><a name="p1218111991115"></a><a name="p1218111991115"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p1421871991115"><a name="p1421871991115"></a><a name="p1421871991115"></a>Specifies the version status. Values are as follows:</p>
    <p id="p13218101961111"><a name="p13218101961111"></a><a name="p13218101961111"></a><strong>CURRENT</strong>: widely used version</p>
    <p id="p8218619201113"><a name="p8218619201113"></a><a name="p8218619201113"></a><strong>SUPPORT</strong>: earlier version which is still supported</p>
    <p id="p821891911116"><a name="p821891911116"></a><a name="p821891911116"></a><strong>DEPRECATED</strong>: deprecated version which may be deleted later</p>
    </td>
    </tr>
    <tr id="row1621811911114"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p7218171951115"><a name="p7218171951115"></a><a name="p7218171951115"></a>updated</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p721841914112"><a name="p721841914112"></a><a name="p721841914112"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p192181619151111"><a name="p192181619151111"></a><a name="p192181619151111"></a>Specifies the version release time, which must be the UTC time. For example, the release time of v1 is 2018-05-30T15:00:00Z.</p>
    </td>
    </tr>
    <tr id="row1221831916112"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p172181619101116"><a name="p172181619101116"></a><a name="p172181619101116"></a>min_version</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p4218919111111"><a name="p4218919111111"></a><a name="p4218919111111"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p10218619131113"><a name="p10218619131113"></a><a name="p10218619131113"></a>Specifies the microversion. If APIs of a version support microversions, the system returns the supported minimum microversion. If microversions are not supported, the system returns an empty value. </p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2** **links**  parameters

    <a name="table122284216266"></a>
    <table><thead align="left"><tr id="row0222174292613"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.1"><p id="p1522204215262"><a name="p1522204215262"></a><a name="p1522204215262"></a><strong id="b84235270615443_1"><a name="b84235270615443_1"></a><a name="b84235270615443_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="22.35%" id="mcps1.2.4.1.2"><p id="p1822294232612"><a name="p1822294232612"></a><a name="p1822294232612"></a><strong id="b84235270615453_2"><a name="b84235270615453_2"></a><a name="b84235270615453_2"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="57.65%" id="mcps1.2.4.1.3"><p id="p15222164218261"><a name="p15222164218261"></a><a name="p15222164218261"></a><strong id="b84235270615457_3"><a name="b84235270615457_3"></a><a name="b84235270615457_3"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row20222144212611"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p5222242202619"><a name="p5222242202619"></a><a name="p5222242202619"></a>rel</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.2.4.1.2 "><p id="p10222114212268"><a name="p10222114212268"></a><a name="p10222114212268"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.65%" headers="mcps1.2.4.1.3 "><p id="p142221942192619"><a name="p142221942192619"></a><a name="p142221942192619"></a>Describes a link.</p>
    </td>
    </tr>
    <tr id="row722294217261"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p622254262619"><a name="p622254262619"></a><a name="p622254262619"></a>href</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.2.4.1.2 "><p id="p022224232615"><a name="p022224232615"></a><a name="p022224232615"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.65%" headers="mcps1.2.4.1.3 "><p id="p19222124210263"><a name="p19222124210263"></a><a name="p19222124210263"></a>Specifies the version query link.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "version": {
            "id": "v1",
            "links": [
                {
                    "href": "https://sdrs.localdomain.com/v1",
                    "rel": "self"
                }
            ],
            "status": "CURRENT",
            "updated": "2018-05-30T00:00:00Z",
            "version": "",
            "min_version": ""
        }
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


## **Returned Value**<a name="section137651118151119"></a>

-   Normal

    <a name="table47815180118"></a>
    <table><thead align="left"><tr id="row2021871915114"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p4218171912116"><a name="p4218171912116"></a><a name="p4218171912116"></a><strong id="b842352706175024_1"><a name="b842352706175024_1"></a><a name="b842352706175024_1"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p17218171901115"><a name="p17218171901115"></a><a name="p17218171901115"></a><strong id="b84235270615457_4"><a name="b84235270615457_4"></a><a name="b84235270615457_4"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row22187190113"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p921861921119"><a name="p921861921119"></a><a name="p921861921119"></a>200</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p72184190118"><a name="p72184190118"></a><a name="p72184190118"></a>The server has accepted the request.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Abnormal

    <a name="table2781151816113"></a>
    <table><thead align="left"><tr id="row32181419141115"><th class="cellrowborder" valign="top" width="43.43%" id="mcps1.1.3.1.1"><p id="p2218191916115"><a name="p2218191916115"></a><a name="p2218191916115"></a><strong id="b842352706175024_2"><a name="b842352706175024_2"></a><a name="b842352706175024_2"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="56.57%" id="mcps1.1.3.1.2"><p id="p42181719201113"><a name="p42181719201113"></a><a name="p42181719201113"></a><strong id="b84235270615457_5"><a name="b84235270615457_5"></a><a name="b84235270615457_5"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row182185197119"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p321831961112"><a name="p321831961112"></a><a name="p321831961112"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p1321821981115"><a name="p1321821981115"></a><a name="p1321821981115"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row19218161918116"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p7218151921111"><a name="p7218151921111"></a><a name="p7218151921111"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p112182191113"><a name="p112182191113"></a><a name="p112182191113"></a>You must enter a username and the password to access the requested page.</p>
    </td>
    </tr>
    <tr id="row18218121921120"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p17218171918111"><a name="p17218171918111"></a><a name="p17218171918111"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p15218131981117"><a name="p15218131981117"></a><a name="p15218131981117"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="row521811913111"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p20218181913113"><a name="p20218181913113"></a><a name="p20218181913113"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p18218101971117"><a name="p18218101971117"></a><a name="p18218101971117"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="row1821816197114"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p921817196119"><a name="p921817196119"></a><a name="p921817196119"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p4218171991118"><a name="p4218171991118"></a><a name="p4218171991118"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="row20218151921115"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p5218519181114"><a name="p5218519181114"></a><a name="p5218519181114"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p182189191114"><a name="p182189191114"></a><a name="p182189191114"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="row172182198112"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p22184191112"><a name="p22184191112"></a><a name="p22184191112"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p192181419141118"><a name="p192181419141118"></a><a name="p192181419141118"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="row32185197110"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p1721891911120"><a name="p1721891911120"></a><a name="p1721891911120"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p17218131971114"><a name="p17218131971114"></a><a name="p17218131971114"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row62181319191115"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p921831911118"><a name="p921831911118"></a><a name="p921831911118"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p162181619201111"><a name="p162181619201111"></a><a name="p162181619201111"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="row1021820196115"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p18218141920118"><a name="p18218141920118"></a><a name="p18218141920118"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p52181219191119"><a name="p52181219191119"></a><a name="p52181219191119"></a>Failed to complete the request because of a service error.</p>
    </td>
    </tr>
    <tr id="row1421811911112"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p2021819197116"><a name="p2021819197116"></a><a name="p2021819197116"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p1821851941119"><a name="p1821851941119"></a><a name="p1821851941119"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="row13218219151119"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p22183198114"><a name="p22183198114"></a><a name="p22183198114"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p2021811913118"><a name="p2021811913118"></a><a name="p2021811913118"></a>Failed to complete the request because the server receives an invalid response from an upstream server.</p>
    </td>
    </tr>
    <tr id="row192180191118"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p921831991110"><a name="p921831991110"></a><a name="p921831991110"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p22181196111"><a name="p22181196111"></a><a name="p22181196111"></a>Failed to complete the request because the system is unavailable.</p>
    </td>
    </tr>
    <tr id="row8218119181114"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p1321814199113"><a name="p1321814199113"></a><a name="p1321814199113"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p02181319141114"><a name="p02181319141114"></a><a name="p02181319141114"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


