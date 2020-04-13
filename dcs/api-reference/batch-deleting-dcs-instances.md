# Batch Deleting DCS Instances<a name="EN-US_TOPIC_0237964389"></a>

## Function<a name="section848378"></a>

This API is used to delete multiple DCS instances at a time.

## URI<a name="section7635405"></a>

-   URI format:

    DELETE /v1.0/\{project\_id\}/instances?allFailure=\{allFailure\}

-   Parameter description:

    [Table 1](#d0e1909)  describes the parameters of this API.


**Table  1**  Parameter description

<a name="d0e1909"></a>
<table><thead align="left"><tr id="row25964774"><th class="cellrowborder" valign="top" width="25.252525252525253%" id="mcps1.2.5.1.1"><p id="p22771929"><a name="p22771929"></a><a name="p22771929"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="14.14141414141414%" id="mcps1.2.5.1.2"><p id="p32586932"><a name="p32586932"></a><a name="p32586932"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="23.232323232323232%" id="mcps1.2.5.1.3"><p id="p22295840"><a name="p22295840"></a><a name="p22295840"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="37.37373737373738%" id="mcps1.2.5.1.4"><p id="p61132612"><a name="p61132612"></a><a name="p61132612"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row52794569"><td class="cellrowborder" valign="top" width="25.252525252525253%" headers="mcps1.2.5.1.1 "><p id="p48501719"><a name="p48501719"></a><a name="p48501719"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.2 "><p id="p36325141"><a name="p36325141"></a><a name="p36325141"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="23.232323232323232%" headers="mcps1.2.5.1.3 "><p id="p56655275"><a name="p56655275"></a><a name="p56655275"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="37.37373737373738%" headers="mcps1.2.5.1.4 "><p id="p25674562"><a name="p25674562"></a><a name="p25674562"></a>Project ID.</p>
</td>
</tr>
<tr id="row29744469"><td class="cellrowborder" valign="top" width="25.252525252525253%" headers="mcps1.2.5.1.1 "><p id="p60491792"><a name="p60491792"></a><a name="p60491792"></a>allFailure</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.2 "><p id="p888095"><a name="p888095"></a><a name="p888095"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="23.232323232323232%" headers="mcps1.2.5.1.3 "><p id="p4826859"><a name="p4826859"></a><a name="p4826859"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="37.37373737373738%" headers="mcps1.2.5.1.4 "><p id="p55431259"><a name="p55431259"></a><a name="p55431259"></a>An indicator of whether all DCS instances that failed to be created will be deleted.</p>
<p id="p29119284"><a name="p29119284"></a><a name="p29119284"></a>Options:</p>
<a name="ul60746967"></a><a name="ul60746967"></a><ul id="ul60746967"><li><strong id="b21557320"><a name="b21557320"></a><a name="b21557320"></a>true</strong>: All DCS instances that the tenant specified by <strong id="b59798160"><a name="b59798160"></a><a name="b59798160"></a>project_id</strong> failed to create will be deleted without a need to specify the <strong id="b1312534"><a name="b1312534"></a><a name="b1312534"></a>instances</strong> parameter in the API request.</li><li><strong id="b39206440"><a name="b39206440"></a><a name="b39206440"></a>false</strong> or others: The DCS instances specified by the <strong id="b17313647"><a name="b17313647"></a><a name="b17313647"></a>instances</strong> parameter in the API request will be deleted.</li></ul>
</td>
</tr>
</tbody>
</table>

## Request<a name="section1609783"></a>

-   Request parameter:

    [Table 2](#table1511573511014)  describes request parameters.


**Table  2**  Parameter description

<a name="table1511573511014"></a>
<table><thead align="left"><tr id="row48086644"><th class="cellrowborder" valign="top" width="19.387755102040817%" id="mcps1.2.5.1.1"><p id="p2704124"><a name="p2704124"></a><a name="p2704124"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="14.285714285714285%" id="mcps1.2.5.1.2"><p id="p17707476"><a name="p17707476"></a><a name="p17707476"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="19.387755102040817%" id="mcps1.2.5.1.3"><p id="p25019428"><a name="p25019428"></a><a name="p25019428"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="46.93877551020408%" id="mcps1.2.5.1.4"><p id="p13307797"><a name="p13307797"></a><a name="p13307797"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row4189774"><td class="cellrowborder" valign="top" width="19.387755102040817%" headers="mcps1.2.5.1.1 "><p id="p3827448"><a name="p3827448"></a><a name="p3827448"></a>instances</p>
</td>
<td class="cellrowborder" valign="top" width="14.285714285714285%" headers="mcps1.2.5.1.2 "><p id="p41587899"><a name="p41587899"></a><a name="p41587899"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="19.387755102040817%" headers="mcps1.2.5.1.3 "><p id="p13176638"><a name="p13176638"></a><a name="p13176638"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="46.93877551020408%" headers="mcps1.2.5.1.4 "><p id="p60674729"><a name="p60674729"></a><a name="p60674729"></a>IDs of DCS instances to be deleted.</p>
<p id="p9201653"><a name="p9201653"></a><a name="p9201653"></a>This parameter needs to be set only when the <strong id="b15706021"><a name="b15706021"></a><a name="b15706021"></a>allFailure</strong> parameter in the URI is set to <strong id="b7136465"><a name="b7136465"></a><a name="b7136465"></a>false</strong> or another value.</p>
</td>
</tr>
</tbody>
</table>

-   Example request with  **allFailure** set to  **false**:

    ```
    { 
     "instances": [ 
            "54602a9d-5e22-4239-9123-77e350df4a34", 
            "7166cdea-dbad-4d79-9610-7163e6f8b640" 
     ] 
    }
    ```


## Response<a name="section14488049"></a>

-   Status code:

    If status code "200 OK" is returned, the DCS instances specified by the  **instances**  parameter in the API request have been deleted

    If status code "204 No Content" is returned, all DCS instances that the tenant specified by  **project\_id**  failed to create have been deleted.

    For description of other status codes, see  [API Usage Guidelines](api-usage-guidelines.md).

-   Response parameter:

    If the value of the  **allFailure**  parameter in the URI is  **true**, all DCS instances that the tenant specified by  **project\_id**  failed to create are deleted and an empty response is then returned.

    If the value of the  **allFailure**  parameter in the URI is  **false**, the DCS instances specified by the  **instances**  parameter in the API request are deleted and a response containing the parameter in  [Table 3](#table4881539111717)  is then returned.


**Table  3**  Parameter description

<a name="table4881539111717"></a>
<table><thead align="left"><tr id="row47829735"><th class="cellrowborder" valign="top" width="19.19191919191919%" id="mcps1.2.4.1.1"><p id="p49003335"><a name="p49003335"></a><a name="p49003335"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p9847179"><a name="p9847179"></a><a name="p9847179"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="47.474747474747474%" id="mcps1.2.4.1.3"><p id="p59424028"><a name="p59424028"></a><a name="p59424028"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row48616929"><td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.2.4.1.1 "><p id="p45657154"><a name="p45657154"></a><a name="p45657154"></a>results</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p7242025"><a name="p7242025"></a><a name="p7242025"></a>Array.</p>
<p id="p65178225"><a name="p65178225"></a><a name="p65178225"></a>For more information, see <a href="#table2090183919176">Table 4</a>.</p>
</td>
<td class="cellrowborder" valign="top" width="47.474747474747474%" headers="mcps1.2.4.1.3 "><p id="p1850530"><a name="p1850530"></a><a name="p1850530"></a>Instance deletion result.</p>
</td>
</tr>
</tbody>
</table>

**Table  4**  Parameter description of the results array

<a name="table2090183919176"></a>
<table><thead align="left"><tr id="row56815916"><th class="cellrowborder" valign="top" width="19%" id="mcps1.2.4.1.1"><p id="p38686482"><a name="p38686482"></a><a name="p38686482"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="26%" id="mcps1.2.4.1.2"><p id="p46597308"><a name="p46597308"></a><a name="p46597308"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="55.00000000000001%" id="mcps1.2.4.1.3"><p id="p16285586"><a name="p16285586"></a><a name="p16285586"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row44064126"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="p12424421"><a name="p12424421"></a><a name="p12424421"></a>instance</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="p66854065"><a name="p66854065"></a><a name="p66854065"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p46470218"><a name="p46470218"></a><a name="p46470218"></a>DCS instance ID.</p>
</td>
</tr>
<tr id="row15578783"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="p53921877"><a name="p53921877"></a><a name="p53921877"></a>result</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="p5595916"><a name="p5595916"></a><a name="p5595916"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p50616043"><a name="p50616043"></a><a name="p50616043"></a>Instance deletion result.</p>
<p id="p52891210"><a name="p52891210"></a><a name="p52891210"></a>Value: <strong id="b6258843"><a name="b6258843"></a><a name="b6258843"></a>success</strong> or <strong id="b56329593"><a name="b56329593"></a><a name="b56329593"></a>failed</strong></p>
</td>
</tr>
</tbody>
</table>

-   Example response:

    ```
    { 
     "results": [ 
            { 
                "instance": "54602a9d-5e22-4239-9123-77e350df4a34", 
                "result": "success" 
            }, 
            { 
                "instance": "7166cdea-dbad-4d79-9610-7163e6f8b640", 
                "result": "success" 
            } 
     ] 
    }
    ```


