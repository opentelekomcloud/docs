# Querying an API Version List \(Compatible with OpenStack\)<a name="en-us_topic_0057306831"></a>

## Function<a name="s527f618a3631437897927385613272af"></a>

This API is used to query the currently supported RDS API version list.

-   Learn how to  [authorize and authenticate](authentication.md)  this API before using it.
-   Before calling this API, obtain the required  [region and endpoint](https://docs.otc.t-systems.com/en-us/endpoint/index.html).

## URI<a name="s74ec19de10d34f1687b2179083d744ae"></a>

-   URI format

    PATH: /

    Method: GET

-   Parameter description

    None


## Request<a name="s01687545134d465baa4b5d6c8a28dde0"></a>

None

## Response<a name="s5ed2134cd7254287b6982b404afe1af5"></a>

-   Normal response

    **Table  1**  Parameter description

    <a name="tcf7775a6be1b47b5aa5297975d4256bb"></a>
    <table><thead align="left"><tr id="r017d023a16ac47b486b0a3ac66422d15"><th class="cellrowborder" valign="top" width="26.26262626262626%" id="mcps1.2.4.1.1"><p id="a7505c1daa195443fb47e22863245e80c"><a name="a7505c1daa195443fb47e22863245e80c"></a><a name="a7505c1daa195443fb47e22863245e80c"></a><strong id="en-us_topic_0032347778_b842352706102328"><a name="en-us_topic_0032347778_b842352706102328"></a><a name="en-us_topic_0032347778_b842352706102328"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="40.40404040404041%" id="mcps1.2.4.1.2"><p id="ac3a2b3811f064157a423119cf6bd8c05"><a name="ac3a2b3811f064157a423119cf6bd8c05"></a><a name="ac3a2b3811f064157a423119cf6bd8c05"></a><strong id="en-us_topic_0032347778_b842352706164541"><a name="en-us_topic_0032347778_b842352706164541"></a><a name="en-us_topic_0032347778_b842352706164541"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="a0d6afecd4b3744bc90bf9cc05e79c155"><a name="a0d6afecd4b3744bc90bf9cc05e79c155"></a><a name="a0d6afecd4b3744bc90bf9cc05e79c155"></a><strong id="en-us_topic_0032347778_b842352706163417"><a name="en-us_topic_0032347778_b842352706163417"></a><a name="en-us_topic_0032347778_b842352706163417"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r99baa6ed92f646b1846b461cf99bd4d8"><td class="cellrowborder" valign="top" width="26.26262626262626%" headers="mcps1.2.4.1.1 "><p id="a231101d576064625a2b6cc7c44720e2a"><a name="a231101d576064625a2b6cc7c44720e2a"></a><a name="a231101d576064625a2b6cc7c44720e2a"></a>versions</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.40404040404041%" headers="mcps1.2.4.1.2 "><p id="ab6e71f44fc8e4442b7c2b97464beebe5"><a name="ab6e71f44fc8e4442b7c2b97464beebe5"></a><a name="ab6e71f44fc8e4442b7c2b97464beebe5"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0032347778_p476126915440"><a name="en-us_topic_0032347778_p476126915440"></a><a name="en-us_topic_0032347778_p476126915440"></a>Indicates the list of detailed API version information.</p>
    <p id="p12971510123511"><a name="p12971510123511"></a><a name="p12971510123511"></a>For details, see <a href="#t597bb32ec3694c8e917e7b92cbcc8b18">Table 2</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2**  versions field data structure description

    <a name="t597bb32ec3694c8e917e7b92cbcc8b18"></a>
    <table><thead align="left"><tr id="r66a50d84290f4eccb889a0d8e54c51f6"><th class="cellrowborder" valign="top" width="26.529999999999998%" id="mcps1.2.4.1.1"><p id="a6ba6d0001fd44bd09ff25243bd4bb001"><a name="a6ba6d0001fd44bd09ff25243bd4bb001"></a><a name="a6ba6d0001fd44bd09ff25243bd4bb001"></a><strong id="b156741737"><a name="b156741737"></a><a name="b156741737"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39.800000000000004%" id="mcps1.2.4.1.2"><p id="a472d09f2c2624e15ad2662ea2214715b"><a name="a472d09f2c2624e15ad2662ea2214715b"></a><a name="a472d09f2c2624e15ad2662ea2214715b"></a><strong id="b1006960847"><a name="b1006960847"></a><a name="b1006960847"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.67%" id="mcps1.2.4.1.3"><p id="a02decdae0686467e82cb981d833cb370"><a name="a02decdae0686467e82cb981d833cb370"></a><a name="a02decdae0686467e82cb981d833cb370"></a><strong id="b1058882153"><a name="b1058882153"></a><a name="b1058882153"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r78c0afe5c849497a876f19c14a9ed4ee"><td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.1 "><p id="a4fe5e70b5fc4446c984112261ead63d3"><a name="a4fe5e70b5fc4446c984112261ead63d3"></a><a name="a4fe5e70b5fc4446c984112261ead63d3"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.4.1.2 "><p id="a11baa203faf04d838774d196d2c3d9fd"><a name="a11baa203faf04d838774d196d2c3d9fd"></a><a name="a11baa203faf04d838774d196d2c3d9fd"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.67%" headers="mcps1.2.4.1.3 "><p id="aac437d22b5bc49a5b75d163018e29121"><a name="aac437d22b5bc49a5b75d163018e29121"></a><a name="aac437d22b5bc49a5b75d163018e29121"></a>Indicates the API version.</p>
    <a name="ul1725315498237"></a><a name="ul1725315498237"></a><ul id="ul1725315498237"><li><strong id="b7261534541"><a name="b7261534541"></a><a name="b7261534541"></a>v1</strong>: indicates the API v1 version.</li><li><strong id="b0450103510410"><a name="b0450103510410"></a><a name="b0450103510410"></a>v1.0</strong>: indicates the OpenStack trove API v1.0.</li><li><strong id="b1134023611419"><a name="b1134023611419"></a><a name="b1134023611419"></a>v3</strong>: indicates the API v3 version.</li></ul>
    </td>
    </tr>
    <tr id="row42577582121025"><td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.1 "><p id="p33971472121032"><a name="p33971472121032"></a><a name="p33971472121032"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.4.1.2 "><p id="p871263121310"><a name="p871263121310"></a><a name="p871263121310"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.67%" headers="mcps1.2.4.1.3 "><p id="p30425021121032"><a name="p30425021121032"></a><a name="p30425021121032"></a>Indicates the API link information. The value is empty when the version is <strong id="b9972193716411"><a name="b9972193716411"></a><a name="b9972193716411"></a>v1</strong> or <strong id="b7661412057"><a name="b7661412057"></a><a name="b7661412057"></a>v3</strong>.</p>
    <p id="p93631481916"><a name="p93631481916"></a><a name="p93631481916"></a>For details, see <a href="#t645d6d81bf2f42a18f1a65676a7219d7">Table 3</a>.</p>
    </td>
    </tr>
    <tr id="r2f9163942c1647dba639a5cacea9613b"><td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.1 "><p id="ab6b2affa0c10471c99c0c271c505bffe"><a name="ab6b2affa0c10471c99c0c271c505bffe"></a><a name="ab6b2affa0c10471c99c0c271c505bffe"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.4.1.2 "><p id="afc828afd7db94565ab0e74b64b7e3e59"><a name="afc828afd7db94565ab0e74b64b7e3e59"></a><a name="afc828afd7db94565ab0e74b64b7e3e59"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.67%" headers="mcps1.2.4.1.3 "><p id="p32916607104653"><a name="p32916607104653"></a><a name="p32916607104653"></a>Indicates the version status.</p>
    <p id="p1835621415265"><a name="p1835621415265"></a><a name="p1835621415265"></a>The value <span class="parmvalue" id="parmvalue645211820517"><a name="parmvalue645211820517"></a><a name="parmvalue645211820517"></a><b>CURRENT</b></span> indicates that the version has been released.</p>
    </td>
    </tr>
    <tr id="rd1c8f00b419b468aa92c34291577c1cc"><td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.1 "><p id="a8894d2ac89ff4fb2a8d634c42bb0f208"><a name="a8894d2ac89ff4fb2a8d634c42bb0f208"></a><a name="a8894d2ac89ff4fb2a8d634c42bb0f208"></a>updated</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.4.1.2 "><p id="ac1128a30986c441b92aa3c5cfcd56e05"><a name="ac1128a30986c441b92aa3c5cfcd56e05"></a><a name="ac1128a30986c441b92aa3c5cfcd56e05"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.67%" headers="mcps1.2.4.1.3 "><p id="acae232520194469a9accb354a7948c6d"><a name="acae232520194469a9accb354a7948c6d"></a><a name="acae232520194469a9accb354a7948c6d"></a>Indicates the version update time.</p>
    <p id="a3944e8a22ca2484086ec90b72cda3a8a"><a name="a3944e8a22ca2484086ec90b72cda3a8a"></a><a name="a3944e8a22ca2484086ec90b72cda3a8a"></a>The format is yyyy-mm-dd Thh:mm:ssZ.</p>
    <p id="a28bcdc5cc276482a8f0bd4b90cb9b23e"><a name="a28bcdc5cc276482a8f0bd4b90cb9b23e"></a><a name="a28bcdc5cc276482a8f0bd4b90cb9b23e"></a><strong id="b842352706104536"><a name="b842352706104536"></a><a name="b842352706104536"></a>T</strong> is the separator between the calendar and the hourly notation of time. <strong id="b842352706161738"><a name="b842352706161738"></a><a name="b842352706161738"></a>Z</strong> indicates the UTC.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  links field data structure description \(dedicated for OpenStack v1.0\)

    <a name="t645d6d81bf2f42a18f1a65676a7219d7"></a>
    <table><thead align="left"><tr id="ra07a00bcadf64ad387c2dd75b4557e42"><th class="cellrowborder" valign="top" width="26.529999999999998%" id="mcps1.2.4.1.1"><p id="a5ea8fa3edfac44d887658822c2d57b26"><a name="a5ea8fa3edfac44d887658822c2d57b26"></a><a name="a5ea8fa3edfac44d887658822c2d57b26"></a><strong id="b2002039592"><a name="b2002039592"></a><a name="b2002039592"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39.800000000000004%" id="mcps1.2.4.1.2"><p id="af15dfe6143894935a69dfad224e01197"><a name="af15dfe6143894935a69dfad224e01197"></a><a name="af15dfe6143894935a69dfad224e01197"></a><strong id="b997947024"><a name="b997947024"></a><a name="b997947024"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.67%" id="mcps1.2.4.1.3"><p id="a27c6f07346604234b91ad6ad5d31c701"><a name="a27c6f07346604234b91ad6ad5d31c701"></a><a name="a27c6f07346604234b91ad6ad5d31c701"></a><strong id="b1609678968"><a name="b1609678968"></a><a name="b1609678968"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r913f5e29affb484da3f97eef6547e87e"><td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.1 "><p id="a61a58fd6166641d5aa9ef785fc475ae2"><a name="a61a58fd6166641d5aa9ef785fc475ae2"></a><a name="a61a58fd6166641d5aa9ef785fc475ae2"></a>href</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.4.1.2 "><p id="a571a52216e81461e928ecad12b114b19"><a name="a571a52216e81461e928ecad12b114b19"></a><a name="a571a52216e81461e928ecad12b114b19"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.67%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0032347778_p619568715440"><a name="en-us_topic_0032347778_p619568715440"></a><a name="en-us_topic_0032347778_p619568715440"></a>Indicates the API URL and the value is <strong id="b84235270618633"><a name="b84235270618633"></a><a name="b84235270618633"></a>""</strong>.</p>
    </td>
    </tr>
    <tr id="r9a2191a6f9a7465a983ac80b4c143dcd"><td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.1 "><p id="aa37bc9bde57b42dca72babbca6d4ef86"><a name="aa37bc9bde57b42dca72babbca6d4ef86"></a><a name="aa37bc9bde57b42dca72babbca6d4ef86"></a>rel</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.800000000000004%" headers="mcps1.2.4.1.2 "><p id="a601c1b6c0d3c410482bebe332656f0bc"><a name="a601c1b6c0d3c410482bebe332656f0bc"></a><a name="a601c1b6c0d3c410482bebe332656f0bc"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.67%" headers="mcps1.2.4.1.3 "><p id="ab2d6dd6fb61a4c46bedffa06052c155d"><a name="ab2d6dd6fb61a4c46bedffa06052c155d"></a><a name="ab2d6dd6fb61a4c46bedffa06052c155d"></a>Its value is <strong id="b84235270616818"><a name="b84235270616818"></a><a name="b84235270616818"></a>self</strong>, indicating that <strong id="b84235270616856"><a name="b84235270616856"></a><a name="b84235270616856"></a>href</strong> is a local link.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example normal response

    ```
    {      
     "versions": [
            {
               "id": "v1",
               "links": [],
               "status": "CURRENT",
               "updated": "2017-02-07T17:34:02Z"
            },      
            {         
                "id": "v1.0", 
                "links": [
                     {
                         "href": "",
                         "rel": "self"
                     }  
                ],               
                "status": "CURRENT",               
                "updated": "2017-03-23T17:34:02Z"
            } ,
         {
               "id": "v3",
               "links": [],
               "status": "CURRENT",
               "updated": "2019-01-15T12:00:00Z"
            }
        ]  
    }
    ```

-   Abnormal Response

    For details, see  [Abnormal Request Results](abnormal-request-results.md).


## Status Code<a name="section4778540915440"></a>

For details, see  [Status Codes](status-codes.md).

## Error Code<a name="section1183074220016"></a>

For details, see  [Error Codes](error-codes.md).

