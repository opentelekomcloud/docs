# Querying Summary Information of EVS Disks<a name="evs_04_3046"></a>

## Function<a name="section13269437577"></a>

This API is used to query the summary information of EVS disks, including the disk quantity, total capacity, and metadata information.

>![](/images/icon-note.gif) **NOTE:**   
>The request version must be 3.12 or later.  

## URI<a name="section433454325717"></a>

-   URI format

    GET /v3/\{project\_id\}/volumes/summary

-   Parameter description

    <a name="table16338174335710"></a>
    <table><thead align="left"><tr id="row105031043115715"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="p25035437578"><a name="p25035437578"></a><a name="p25035437578"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="p1503643145710"><a name="p1503643145710"></a><a name="p1503643145710"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="p145031543165715"><a name="p145031543165715"></a><a name="p145031543165715"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1150310436576"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p165045438574"><a name="p165045438574"></a><a name="p165045438574"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p20504843175717"><a name="p20504843175717"></a><a name="p20504843175717"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p14504104315576"><a name="p14504104315576"></a><a name="p14504104315576"></a>Specifies the project ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section13354194317578"></a>

-   Example request

    ```
    GET https://{endpoint}/v3/{project_id}/volumes/summary
    ```


## Response<a name="section93541643195718"></a>

-   Parameter description

    <a name="table9790753204717"></a>
    <table><thead align="left"><tr id="row1379065318471"><th class="cellrowborder" valign="top" width="21.95%" id="mcps1.1.4.1.1"><p id="p67904536478"><a name="p67904536478"></a><a name="p67904536478"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="24.39%" id="mcps1.1.4.1.2"><p id="p11790165394719"><a name="p11790165394719"></a><a name="p11790165394719"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.66%" id="mcps1.1.4.1.3"><p id="p147902053104713"><a name="p147902053104713"></a><a name="p147902053104713"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row12790145304717"><td class="cellrowborder" valign="top" width="21.95%" headers="mcps1.1.4.1.1 "><p id="p147901753114712"><a name="p147901753114712"></a><a name="p147901753114712"></a>volume-summary</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.39%" headers="mcps1.1.4.1.2 "><p id="p12790115394719"><a name="p12790115394719"></a><a name="p12790115394719"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.66%" headers="mcps1.1.4.1.3 "><p id="p14791153134717"><a name="p14791153134717"></a><a name="p14791153134717"></a>Specifies the summary information of queried disks. For details, see <a href="#li10504143155718">Parameters in the volume-summary field</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   <a name="li10504143155718"></a>Parameters in the  **volume-summary**  field

    <a name="table0358124375716"></a>
    <table><thead align="left"><tr id="row55041443195713"><th class="cellrowborder" valign="top" width="21.95%" id="mcps1.1.4.1.1"><p id="p6504443115718"><a name="p6504443115718"></a><a name="p6504443115718"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="24.39%" id="mcps1.1.4.1.2"><p id="p185041743205719"><a name="p185041743205719"></a><a name="p185041743205719"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.66%" id="mcps1.1.4.1.3"><p id="p13504104314576"><a name="p13504104314576"></a><a name="p13504104314576"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row650434385716"><td class="cellrowborder" valign="top" width="21.95%" headers="mcps1.1.4.1.1 "><p id="p2504134315574"><a name="p2504134315574"></a><a name="p2504134315574"></a>total_size</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.39%" headers="mcps1.1.4.1.2 "><p id="p1750413434576"><a name="p1750413434576"></a><a name="p1750413434576"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.66%" headers="mcps1.1.4.1.3 "><p id="p16504124325719"><a name="p16504124325719"></a><a name="p16504124325719"></a>Specifies the total size of disks, in GB.</p>
    </td>
    </tr>
    <tr id="row950464345712"><td class="cellrowborder" valign="top" width="21.95%" headers="mcps1.1.4.1.1 "><p id="p95041543155718"><a name="p95041543155718"></a><a name="p95041543155718"></a>total_count</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.39%" headers="mcps1.1.4.1.2 "><p id="p95041643185717"><a name="p95041643185717"></a><a name="p95041643185717"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.66%" headers="mcps1.1.4.1.3 "><p id="p0504184385719"><a name="p0504184385719"></a><a name="p0504184385719"></a>Specifies the total quantity of disks.</p>
    </td>
    </tr>
    <tr id="row250411433578"><td class="cellrowborder" valign="top" width="21.95%" headers="mcps1.1.4.1.1 "><p id="p1950417435579"><a name="p1950417435579"></a><a name="p1950417435579"></a>metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.39%" headers="mcps1.1.4.1.2 "><p id="p1050513439578"><a name="p1050513439578"></a><a name="p1050513439578"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.66%" headers="mcps1.1.4.1.3 "><p id="p6505114318572"><a name="p6505114318572"></a><a name="p6505114318572"></a>Specifies the disk metadata information. This parameter is supported when the request version is 3.36 or later.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "volume-summary": {
            "total_size": 83, 
            "total_count": 8, 
            "metadata": {}
        }
    }
    ```

    or

    ```
    { 
        "error": { 
            "message": "XXXX",  
            "code": "XXX" 
        } 
    }
    ```

    In the preceding example,  **error**  indicates a general error, for example,  **badRequest**  or  **itemNotFound**. An example is provided as follows:

    ```
    {  
        "badRequest": {  
            "message": "XXXX",  
            "code": "XXX"  
        }  
    }
    ```


## Status Codes<a name="section1378194317577"></a>

-   Normal

    200


## Error Codes<a name="section431317151242"></a>

For details, see  [Error Codes](error-codes.md).

