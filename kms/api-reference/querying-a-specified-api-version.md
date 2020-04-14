# Querying a Specified API Version<a name="kms_02_0049"></a>

## Function<a name="en-us_topic_0133150654_section27849192112353"></a>

This API is used to query the version of an API.

## URI<a name="en-us_topic_0133150654_section35184599112353"></a>

-   URI format

    GET /\{version\_id\}

-   Parameter description

    **Table  1**  Parameter description

    <a name="en-us_topic_0133150654_table63109676112353"></a>
    <table><thead align="left"><tr id="en-us_topic_0133150654_row49827042112353"><th class="cellrowborder" valign="top" width="22.74%" id="mcps1.2.5.1.1"><p id="en-us_topic_0133150654_p1577110425210"><a name="en-us_topic_0133150654_p1577110425210"></a><a name="en-us_topic_0133150654_p1577110425210"></a><strong id="en-us_topic_0133150654_b15692163216618"><a name="en-us_topic_0133150654_b15692163216618"></a><a name="en-us_topic_0133150654_b15692163216618"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.919999999999998%" id="mcps1.2.5.1.2"><p id="en-us_topic_0133150654_p167751142326"><a name="en-us_topic_0133150654_p167751142326"></a><a name="en-us_topic_0133150654_p167751142326"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.55%" id="mcps1.2.5.1.3"><p id="en-us_topic_0133150654_p157711420214"><a name="en-us_topic_0133150654_p157711420214"></a><a name="en-us_topic_0133150654_p157711420214"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="40.79%" id="mcps1.2.5.1.4"><p id="en-us_topic_0133150654_p1877644212217"><a name="en-us_topic_0133150654_p1877644212217"></a><a name="en-us_topic_0133150654_p1877644212217"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0133150654_row1533688409"><td class="cellrowborder" valign="top" width="22.74%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0133150654_p12534488409"><a name="en-us_topic_0133150654_p12534488409"></a><a name="en-us_topic_0133150654_p12534488409"></a>version_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0133150654_p9535198184015"><a name="en-us_topic_0133150654_p9535198184015"></a><a name="en-us_topic_0133150654_p9535198184015"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.55%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0133150654_p105353804019"><a name="en-us_topic_0133150654_p105353804019"></a><a name="en-us_topic_0133150654_p105353804019"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.79%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0133150654_p17984943124012"><a name="en-us_topic_0133150654_p17984943124012"></a><a name="en-us_topic_0133150654_p17984943124012"></a>Version ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Requests<a name="en-us_topic_0133150654_section12625030112353"></a>

None

## Responses<a name="en-us_topic_0133150654_section15686020"></a>

**Table  2**  Response parameters

<a name="en-us_topic_0133150654_table5963155810121"></a>
<table><thead align="left"><tr id="en-us_topic_0133150654_row14964195819121"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="en-us_topic_0133150654_p209641586129"><a name="en-us_topic_0133150654_p209641586129"></a><a name="en-us_topic_0133150654_p209641586129"></a><strong id="en-us_topic_0133150654_b743438474"><a name="en-us_topic_0133150654_b743438474"></a><a name="en-us_topic_0133150654_b743438474"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="en-us_topic_0133150654_p10964185816121"><a name="en-us_topic_0133150654_p10964185816121"></a><a name="en-us_topic_0133150654_p10964185816121"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.3"><p id="en-us_topic_0133150654_p7964205821210"><a name="en-us_topic_0133150654_p7964205821210"></a><a name="en-us_topic_0133150654_p7964205821210"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.5.1.4"><p id="en-us_topic_0133150654_p1896414586120"><a name="en-us_topic_0133150654_p1896414586120"></a><a name="en-us_topic_0133150654_p1896414586120"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0133150654_row996417582128"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0133150654_p69642058131212"><a name="en-us_topic_0133150654_p69642058131212"></a><a name="en-us_topic_0133150654_p69642058131212"></a>version</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0133150654_p1964165811218"><a name="en-us_topic_0133150654_p1964165811218"></a><a name="en-us_topic_0133150654_p1964165811218"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0133150654_p13964185810124"><a name="en-us_topic_0133150654_p13964185810124"></a><a name="en-us_topic_0133150654_p13964185810124"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0133150654_p2096565813122"><a name="en-us_topic_0133150654_p2096565813122"></a><a name="en-us_topic_0133150654_p2096565813122"></a>Version information. For details, see <a href="#en-us_topic_0133150654_table5856932152840">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **version**  field data structure description

<a name="en-us_topic_0133150654_table5856932152840"></a>
<table><thead align="left"><tr id="en-us_topic_0133150654_row5206426152840"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="en-us_topic_0133150654_p2059315101761"><a name="en-us_topic_0133150654_p2059315101761"></a><a name="en-us_topic_0133150654_p2059315101761"></a><strong id="en-us_topic_0133150654_b1385415364"><a name="en-us_topic_0133150654_b1385415364"></a><a name="en-us_topic_0133150654_b1385415364"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="en-us_topic_0133150654_p6593610867"><a name="en-us_topic_0133150654_p6593610867"></a><a name="en-us_topic_0133150654_p6593610867"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.3"><p id="en-us_topic_0133150654_p6593101011614"><a name="en-us_topic_0133150654_p6593101011614"></a><a name="en-us_topic_0133150654_p6593101011614"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.5.1.4"><p id="en-us_topic_0133150654_p135931109617"><a name="en-us_topic_0133150654_p135931109617"></a><a name="en-us_topic_0133150654_p135931109617"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0133150654_row1168105801813"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0133150654_p17673853131911"><a name="en-us_topic_0133150654_p17673853131911"></a><a name="en-us_topic_0133150654_p17673853131911"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0133150654_p18673753141918"><a name="en-us_topic_0133150654_p18673753141918"></a><a name="en-us_topic_0133150654_p18673753141918"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0133150654_p9673653111917"><a name="en-us_topic_0133150654_p9673653111917"></a><a name="en-us_topic_0133150654_p9673653111917"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0133150654_p8673205341913"><a name="en-us_topic_0133150654_p8673205341913"></a><a name="en-us_topic_0133150654_p8673205341913"></a>Version number, for example, <span class="parmvalue" id="en-us_topic_0133150654_parmvalue14343434714"><a name="en-us_topic_0133150654_parmvalue14343434714"></a><a name="en-us_topic_0133150654_parmvalue14343434714"></a><b>v1.0</b></span></p>
</td>
</tr>
<tr id="en-us_topic_0133150654_row5394312194"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0133150654_p1167305319192"><a name="en-us_topic_0133150654_p1167305319192"></a><a name="en-us_topic_0133150654_p1167305319192"></a>links</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0133150654_p8673453181912"><a name="en-us_topic_0133150654_p8673453181912"></a><a name="en-us_topic_0133150654_p8673453181912"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0133150654_p10673195361910"><a name="en-us_topic_0133150654_p10673195361910"></a><a name="en-us_topic_0133150654_p10673195361910"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0133150654_p96731653201918"><a name="en-us_topic_0133150654_p96731653201918"></a><a name="en-us_topic_0133150654_p96731653201918"></a>JSON object. For details, see <a href="#en-us_topic_0133150654_table525011561381">Table 4</a>.</p>
</td>
</tr>
<tr id="en-us_topic_0133150654_row1927121716191"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0133150654_p667314532194"><a name="en-us_topic_0133150654_p667314532194"></a><a name="en-us_topic_0133150654_p667314532194"></a>version</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0133150654_p17673105321917"><a name="en-us_topic_0133150654_p17673105321917"></a><a name="en-us_topic_0133150654_p17673105321917"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0133150654_p867375310190"><a name="en-us_topic_0133150654_p867375310190"></a><a name="en-us_topic_0133150654_p867375310190"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0133150654_p1067317537197"><a name="en-us_topic_0133150654_p1067317537197"></a><a name="en-us_topic_0133150654_p1067317537197"></a>If the APIs of this version support microversions, the supported maximum microversion is returned. If the microversion is not supported, empty character string is returned.</p>
</td>
</tr>
<tr id="en-us_topic_0133150654_row1327861351913"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0133150654_p9673185320198"><a name="en-us_topic_0133150654_p9673185320198"></a><a name="en-us_topic_0133150654_p9673185320198"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0133150654_p56732538195"><a name="en-us_topic_0133150654_p56732538195"></a><a name="en-us_topic_0133150654_p56732538195"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0133150654_p9673165315195"><a name="en-us_topic_0133150654_p9673165315195"></a><a name="en-us_topic_0133150654_p9673165315195"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0133150654_p1267335320191"><a name="en-us_topic_0133150654_p1267335320191"></a><a name="en-us_topic_0133150654_p1267335320191"></a>Version status. Valid values are as follows:</p>
<a name="en-us_topic_0133150654_ul386312155239"></a><a name="en-us_topic_0133150654_ul386312155239"></a><ul id="en-us_topic_0133150654_ul386312155239"><li><strong id="en-us_topic_0133150654_b744814358717"><a name="en-us_topic_0133150654_b744814358717"></a><a name="en-us_topic_0133150654_b744814358717"></a>CURRENT</strong>: widely used version</li><li><strong id="en-us_topic_0133150654_b842352706115419"><a name="en-us_topic_0133150654_b842352706115419"></a><a name="en-us_topic_0133150654_b842352706115419"></a>SUPPORTED</strong>: earlier version which is still supported</li><li><strong id="en-us_topic_0133150654_b59714208716"><a name="en-us_topic_0133150654_b59714208716"></a><a name="en-us_topic_0133150654_b59714208716"></a>DEPRECATED</strong>: deprecated version which may be deleted later</li></ul>
</td>
</tr>
<tr id="en-us_topic_0133150654_row45580661911"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0133150654_p1267355310197"><a name="en-us_topic_0133150654_p1267355310197"></a><a name="en-us_topic_0133150654_p1267355310197"></a>updated</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0133150654_p0673155313192"><a name="en-us_topic_0133150654_p0673155313192"></a><a name="en-us_topic_0133150654_p0673155313192"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0133150654_p16673253121920"><a name="en-us_topic_0133150654_p16673253121920"></a><a name="en-us_topic_0133150654_p16673253121920"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0133150654_p196732531193"><a name="en-us_topic_0133150654_p196732531193"></a><a name="en-us_topic_0133150654_p196732531193"></a>Version release time, which must be UTC time. For example, the release time of v1.0 is 2014-06-28T12:20:21Z.</p>
</td>
</tr>
<tr id="en-us_topic_0133150654_row14719199199"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0133150654_p8673553121919"><a name="en-us_topic_0133150654_p8673553121919"></a><a name="en-us_topic_0133150654_p8673553121919"></a>min_version</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0133150654_p4673155321911"><a name="en-us_topic_0133150654_p4673155321911"></a><a name="en-us_topic_0133150654_p4673155321911"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0133150654_p4673453111915"><a name="en-us_topic_0133150654_p4673453111915"></a><a name="en-us_topic_0133150654_p4673453111915"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0133150654_p136732530199"><a name="en-us_topic_0133150654_p136732530199"></a><a name="en-us_topic_0133150654_p136732530199"></a>If the APIs of this version support microversions, the supported minimum microversion is returned. If the microversion is not supported, empty character string is returned.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **links**  field data structure description

<a name="en-us_topic_0133150654_table525011561381"></a>
<table><thead align="left"><tr id="en-us_topic_0133150654_row132503561082"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="en-us_topic_0133150654_p1625015615811"><a name="en-us_topic_0133150654_p1625015615811"></a><a name="en-us_topic_0133150654_p1625015615811"></a><strong id="en-us_topic_0133150654_b693792758"><a name="en-us_topic_0133150654_b693792758"></a><a name="en-us_topic_0133150654_b693792758"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="en-us_topic_0133150654_p125113569815"><a name="en-us_topic_0133150654_p125113569815"></a><a name="en-us_topic_0133150654_p125113569815"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.3"><p id="en-us_topic_0133150654_p925105618816"><a name="en-us_topic_0133150654_p925105618816"></a><a name="en-us_topic_0133150654_p925105618816"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.5.1.4"><p id="en-us_topic_0133150654_p1325155614816"><a name="en-us_topic_0133150654_p1325155614816"></a><a name="en-us_topic_0133150654_p1325155614816"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0133150654_row202512562089"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0133150654_p1425115564818"><a name="en-us_topic_0133150654_p1425115564818"></a><a name="en-us_topic_0133150654_p1425115564818"></a>href</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0133150654_p92512056884"><a name="en-us_topic_0133150654_p92512056884"></a><a name="en-us_topic_0133150654_p92512056884"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0133150654_p62518561389"><a name="en-us_topic_0133150654_p62518561389"></a><a name="en-us_topic_0133150654_p62518561389"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0133150654_p12511566810"><a name="en-us_topic_0133150654_p12511566810"></a><a name="en-us_topic_0133150654_p12511566810"></a>API URL</p>
</td>
</tr>
<tr id="en-us_topic_0133150654_row142511456987"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0133150654_p2251165613814"><a name="en-us_topic_0133150654_p2251165613814"></a><a name="en-us_topic_0133150654_p2251165613814"></a>rel</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0133150654_p62522566811"><a name="en-us_topic_0133150654_p62522566811"></a><a name="en-us_topic_0133150654_p62522566811"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0133150654_p2252145610820"><a name="en-us_topic_0133150654_p2252145610820"></a><a name="en-us_topic_0133150654_p2252145610820"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0133150654_p225212561985"><a name="en-us_topic_0133150654_p225212561985"></a><a name="en-us_topic_0133150654_p225212561985"></a>The default value is <strong id="en-us_topic_0133150654_b555016171571"><a name="en-us_topic_0133150654_b555016171571"></a><a name="en-us_topic_0133150654_b555016171571"></a>self</strong>.</p>
</td>
</tr>
</tbody>
</table>

## Examples<a name="en-us_topic_0133150654_section12491816289"></a>

The following uses the  **v1.0**  version as an example.

-   Example request

    None

-   Example response

    ```
    { 
       "version":
            {
                "id":"v1.0",
                "links":
                [
                    {
                        
                        "href":"https://kms.eu-de.otc.t-systems.com/v1.0/",
                        "rel":"self"
                    }
                ],
                "min_version":"",
                "status":"CURRENT",
                "version":"",
                "updated":"2018-09-05T08:18:05Z"
            }
    }
    ```

    or

    ```
    {
        "error": {
            "error_code": "KMS.XXXX",
            "error_msg": "XXX"
        }
    }
    ```


## Status Codes<a name="en-us_topic_0133150654_section3454223421"></a>

[Table 5](#en-us_topic_0133150654_en-us_topic_0112992294_en-us_topic_0079615001_table20596071)  lists the normal status code returned by the response.

**Table  5**  Status codes

<a name="en-us_topic_0133150654_en-us_topic_0112992294_en-us_topic_0079615001_table20596071"></a>
<table><thead align="left"><tr id="en-us_topic_0133150654_en-us_topic_0112992294_en-us_topic_0079615001_row9746163"><th class="cellrowborder" valign="top" width="22%" id="mcps1.2.4.1.1"><p id="en-us_topic_0133150654_en-us_topic_0112992294_p57545694203043"><a name="en-us_topic_0133150654_en-us_topic_0112992294_p57545694203043"></a><a name="en-us_topic_0133150654_en-us_topic_0112992294_p57545694203043"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="32%" id="mcps1.2.4.1.2"><p id="en-us_topic_0133150654_en-us_topic_0112992294_p4531342288"><a name="en-us_topic_0133150654_en-us_topic_0112992294_p4531342288"></a><a name="en-us_topic_0133150654_en-us_topic_0112992294_p4531342288"></a>Status</p>
</th>
<th class="cellrowborder" valign="top" width="46%" id="mcps1.2.4.1.3"><p id="en-us_topic_0133150654_en-us_topic_0112992294_p30689603203043"><a name="en-us_topic_0133150654_en-us_topic_0112992294_p30689603203043"></a><a name="en-us_topic_0133150654_en-us_topic_0112992294_p30689603203043"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0133150654_en-us_topic_0112992294_en-us_topic_0079615001_row48621261"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0133150654_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"><a name="en-us_topic_0133150654_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"></a><a name="en-us_topic_0133150654_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0133150654_en-us_topic_0112992294_p7538425819"><a name="en-us_topic_0133150654_en-us_topic_0112992294_p7538425819"></a><a name="en-us_topic_0133150654_en-us_topic_0112992294_p7538425819"></a>OK</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0133150654_en-us_topic_0112992294_p1885682315512"><a name="en-us_topic_0133150654_en-us_topic_0112992294_p1885682315512"></a><a name="en-us_topic_0133150654_en-us_topic_0112992294_p1885682315512"></a>Request processed successfully.</p>
</td>
</tr>
</tbody>
</table>

Exception status code. For details, see  [Status Codes](status-codes.md#kms_02_0301).

