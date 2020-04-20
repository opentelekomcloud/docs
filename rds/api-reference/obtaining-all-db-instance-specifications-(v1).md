# Obtaining All DB Instance Specifications<a name="en-us_topic_0056890255"></a>

## Function<a name="section6335675610813"></a>

This API is used to obtain all DB instance specifications.

## URI<a name="section1617705710813"></a>

-   URI format

    PATH: /v1.0/\{project\_id\}/flavors

    Method: GET

-   Parameter description

    **Table  1**  Parameter description

    <a name="table6096138610813"></a>
    <table><thead align="left"><tr id="row1654305710813"><th class="cellrowborder" valign="top" width="21.240000000000002%" id="mcps1.2.4.1.1"><p id="p6491926310813"><a name="p6491926310813"></a><a name="p6491926310813"></a><strong id="b84235270691445"><a name="b84235270691445"></a><a name="b84235270691445"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.96%" id="mcps1.2.4.1.2"><p id="p2396892510813"><a name="p2396892510813"></a><a name="p2396892510813"></a><strong id="b842352706102346"><a name="b842352706102346"></a><a name="b842352706102346"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="49.8%" id="mcps1.2.4.1.3"><p id="p6243473910813"><a name="p6243473910813"></a><a name="p6243473910813"></a><strong id="b842352706163417"><a name="b842352706163417"></a><a name="b842352706163417"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2404909810813"><td class="cellrowborder" valign="top" width="21.240000000000002%" headers="mcps1.2.4.1.1 "><p id="p181991310813"><a name="p181991310813"></a><a name="p181991310813"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.96%" headers="mcps1.2.4.1.2 "><p id="p1319528910813"><a name="p1319528910813"></a><a name="p1319528910813"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.8%" headers="mcps1.2.4.1.3 "><p id="p6218550610813"><a name="p6218550610813"></a><a name="p6218550610813"></a>Specifies the project ID of a tenant in a region.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Restrictions

    Currently, only the DB engines MySQL and PostgreSQL are supported by the API.


## Request<a name="section43437110813"></a>

None

## Normal Response<a name="section4822117510813"></a>

-   Parameter description

    **Table  2**  Parameter description

    <a name="table2794613710813"></a>
    <table><thead align="left"><tr id="row1824035410813"><th class="cellrowborder" valign="top" width="21.07210721072107%" id="mcps1.2.4.1.1"><p id="p107367210813"><a name="p107367210813"></a><a name="p107367210813"></a><strong id="b645303894"><a name="b645303894"></a><a name="b645303894"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="29.05290529052905%" id="mcps1.2.4.1.2"><p id="p1985860710813"><a name="p1985860710813"></a><a name="p1985860710813"></a><strong id="b842352706164541"><a name="b842352706164541"></a><a name="b842352706164541"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="49.874987498749874%" id="mcps1.2.4.1.3"><p id="p6504332610813"><a name="p6504332610813"></a><a name="p6504332610813"></a><strong id="b820055573"><a name="b820055573"></a><a name="b820055573"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3401807810813"><td class="cellrowborder" valign="top" width="21.07210721072107%" headers="mcps1.2.4.1.1 "><p id="p400095110813"><a name="p400095110813"></a><a name="p400095110813"></a>flavors</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.05290529052905%" headers="mcps1.2.4.1.2 "><p id="p5564158410813"><a name="p5564158410813"></a><a name="p5564158410813"></a>List data structure. For details, see <a href="#table5932144310813">Table 3</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.874987498749874%" headers="mcps1.2.4.1.3 "><p id="p2896089210813"><a name="p2896089210813"></a><a name="p2896089210813"></a>Indicates the specification information.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  flavors field data structure description

    <a name="table5932144310813"></a>
    <table><thead align="left"><tr id="row3847854010813"><th class="cellrowborder" valign="top" width="21.07%" id="mcps1.2.4.1.1"><p id="p2975403110813"><a name="p2975403110813"></a><a name="p2975403110813"></a><strong id="b615228827"><a name="b615228827"></a><a name="b615228827"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="29.299999999999997%" id="mcps1.2.4.1.2"><p id="p6126631910813"><a name="p6126631910813"></a><a name="p6126631910813"></a><strong id="b1390943255"><a name="b1390943255"></a><a name="b1390943255"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="49.63%" id="mcps1.2.4.1.3"><p id="p6362478710813"><a name="p6362478710813"></a><a name="p6362478710813"></a><strong id="b1389121196"><a name="b1389121196"></a><a name="b1389121196"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row198232910813"><td class="cellrowborder" valign="top" width="21.07%" headers="mcps1.2.4.1.1 "><p id="p2635094510813"><a name="p2635094510813"></a><a name="p2635094510813"></a>ram</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.299999999999997%" headers="mcps1.2.4.1.2 "><p id="p5405177710813"><a name="p5405177710813"></a><a name="p5405177710813"></a>Int</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.63%" headers="mcps1.2.4.1.3 "><p id="p1611782610813"><a name="p1611782610813"></a><a name="p1611782610813"></a>Indicates the memory specifications in megabytes (MB).</p>
    </td>
    </tr>
    <tr id="row1084271010813"><td class="cellrowborder" valign="top" width="21.07%" headers="mcps1.2.4.1.1 "><p id="p584433110813"><a name="p584433110813"></a><a name="p584433110813"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.299999999999997%" headers="mcps1.2.4.1.2 "><p id="p362878810813"><a name="p362878810813"></a><a name="p362878810813"></a>Int</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.63%" headers="mcps1.2.4.1.3 "><p id="p2549641010813"><a name="p2549641010813"></a><a name="p2549641010813"></a>Indicates the specification ID (Int type). Its default value is <strong id="b842352706114710"><a name="b842352706114710"></a><a name="b842352706114710"></a>1</strong> because RDS uses UUID to store the specification ID and cannot convert it to the Int type.</p>
    </td>
    </tr>
    <tr id="row2814109910813"><td class="cellrowborder" valign="top" width="21.07%" headers="mcps1.2.4.1.1 "><p id="p6483651810813"><a name="p6483651810813"></a><a name="p6483651810813"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.299999999999997%" headers="mcps1.2.4.1.2 "><p id="p1726661010813"><a name="p1726661010813"></a><a name="p1726661010813"></a>List data structure. For details, see <a href="#table2591008910813">Table 4</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.63%" headers="mcps1.2.4.1.3 "><p id="p5641816610813"><a name="p5641816610813"></a><a name="p5641816610813"></a>Indicates the link address.</p>
    </td>
    </tr>
    <tr id="row646876310813"><td class="cellrowborder" valign="top" width="21.07%" headers="mcps1.2.4.1.1 "><p id="p5420781710813"><a name="p5420781710813"></a><a name="p5420781710813"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.299999999999997%" headers="mcps1.2.4.1.2 "><p id="p2875703110813"><a name="p2875703110813"></a><a name="p2875703110813"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.63%" headers="mcps1.2.4.1.3 "><p id="p4761814110813"><a name="p4761814110813"></a><a name="p4761814110813"></a>Indicates the specification item name.</p>
    </td>
    </tr>
    <tr id="row54300797114538"><td class="cellrowborder" valign="top" width="21.07%" headers="mcps1.2.4.1.1 "><p id="p21700115114541"><a name="p21700115114541"></a><a name="p21700115114541"></a>str_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.299999999999997%" headers="mcps1.2.4.1.2 "><p id="p12878889114541"><a name="p12878889114541"></a><a name="p12878889114541"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.63%" headers="mcps1.2.4.1.3 "><p id="p36557059114541"><a name="p36557059114541"></a><a name="p36557059114541"></a>Indicates the specification ID (String type).</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4**  links field data structure description

    <a name="table2591008910813"></a>
    <table><thead align="left"><tr id="row3370068410813"><th class="cellrowborder" valign="top" width="20.47%" id="mcps1.2.4.1.1"><p id="p4540085310813"><a name="p4540085310813"></a><a name="p4540085310813"></a><strong id="b9314487"><a name="b9314487"></a><a name="b9314487"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="29.709999999999997%" id="mcps1.2.4.1.2"><p id="p5359043810813"><a name="p5359043810813"></a><a name="p5359043810813"></a><strong id="b98040100"><a name="b98040100"></a><a name="b98040100"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="49.82%" id="mcps1.2.4.1.3"><p id="p4585821610813"><a name="p4585821610813"></a><a name="p4585821610813"></a><strong id="b37245340"><a name="b37245340"></a><a name="b37245340"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row10564639114448"><td class="cellrowborder" valign="top" width="20.47%" headers="mcps1.2.4.1.1 "><p id="p64824342114457"><a name="p64824342114457"></a><a name="p64824342114457"></a>rel</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.709999999999997%" headers="mcps1.2.4.1.2 "><p id="p16280358114457"><a name="p16280358114457"></a><a name="p16280358114457"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.82%" headers="mcps1.2.4.1.3 "><p id="p43640602114457"><a name="p43640602114457"></a><a name="p43640602114457"></a>Indicates the link property.</p>
    </td>
    </tr>
    <tr id="row2352800210813"><td class="cellrowborder" valign="top" width="20.47%" headers="mcps1.2.4.1.1 "><p id="p2672002910813"><a name="p2672002910813"></a><a name="p2672002910813"></a>href</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.709999999999997%" headers="mcps1.2.4.1.2 "><p id="p1683875310813"><a name="p1683875310813"></a><a name="p1683875310813"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.82%" headers="mcps1.2.4.1.3 "><p id="p2176171610813"><a name="p2176171610813"></a><a name="p2176171610813"></a>Indicates the API link. Its value is <strong id="b842352706182645"><a name="b842352706182645"></a><a name="b842352706182645"></a>""</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Response example

    ```
    {
      "flavors": [
        {
          "ram": 2048,
          "id": 1,
          "links": [
            {
              "rel": "self",
              "href": ""
            },
            {
              "rel": "bookmark",
              "href": ""
            }
          ],
          "name": "rds.pg.c2.medium",
          "str_id": "9ff2a3a5-c859-bbc0-67f7-86ce59432b1d"
        },
        {
          "ram": 4096,
          "id": 1,
          "links": [
            {
              "rel": "self",
              "href": ""
            },
            {
              "rel": "bookmark",
              "href": ""
            }
          ],
          "name": "rds.pg.c2.large",
          "str_id": "b77b5b7e-f572-dfd9-57af-910547fe0883"
        }
      ]
    }
    ```


## Abnormal Response<a name="section639248310813"></a>

For details, see  [Abnormal Request Results](abnormal-request-results.md).

