# Obtaining an Automated Backup Policy<a name="rds_09_0003"></a>

## Function<a name="section117711820496"></a>

This API is used to obtain an automated backup policy.

-   Learn how to  [authorize and authenticate](authentication.md)  this API before using it.
-   Before calling this API, obtain the required  [region and endpoint](https://docs.otc.t-systems.com/en-us/endpoint/index.html).

## URI<a name="section12081471012"></a>

-   URI format

    GET https://\{_Endpoint_\}/v3/\{project\_id\}/instances/\{instance\_id\}/backups/policy

-   Example

    https://rds.eu-de.otc.t-systems.com/v3/0483b6b16e954cb88930a360d2c4e663/instances/dsfae23fsfdsae3435in01/backups/policy

-   Parameter description

    **Table  1**  Parameter description

    <a name="table65777232"></a>
    <table><thead align="left"><tr id="row46529701"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p10809459"><a name="p10809459"></a><a name="p10809459"></a><strong>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p3150961"><a name="p3150961"></a><a name="p3150961"></a><strong>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p53901255"><a name="p53901255"></a><a name="p53901255"></a><strong>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3925534"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p49532829"><a name="p49532829"></a><a name="p49532829"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p52736237"><a name="p52736237"></a><a name="p52736237"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p43776822"><a name="p43776822"></a><a name="p43776822"></a>Specifies the project ID of a tenant in a region.</p>
    <p id="p75911521266"><a name="p75911521266"></a><a name="p75911521266"></a>For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="row5911165722911"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p41557789155220"><a name="p41557789155220"></a><a name="p41557789155220"></a>instance_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p10737742155220"><a name="p10737742155220"></a><a name="p10737742155220"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p64450739155220"><a name="p64450739155220"></a><a name="p64450739155220"></a>Specifies the DB instance ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section420839121019"></a>

None

## Response<a name="section1229512143106"></a>

-   Normal response

    **Table  2**  Parameter description

    <a name="table6426756154514"></a>
    <table><thead align="left"><tr id="row142645664510"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p17490046"><a name="p17490046"></a><a name="p17490046"></a><strong>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p63149496"><a name="p63149496"></a><a name="p63149496"></a><strong>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p14835533"><a name="p14835533"></a><a name="p14835533"></a><strong>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row34264566458"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p28083633"><a name="p28083633"></a><a name="p28083633"></a>backup_policy</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p42890904"><a name="p42890904"></a><a name="p42890904"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p61847473"><a name="p61847473"></a><a name="p61847473"></a>Indicates the backup policy objects, including the backup retention period (days) and backup start time.</p>
    <p id="p9587110124113"><a name="p9587110124113"></a><a name="p9587110124113"></a>For details, see <a href="#table163715367507">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  backup\_policy field data structure description

    <a name="table163715367507"></a>
    <table><thead align="left"><tr id="row9637103616501"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p6927161055116"><a name="p6927161055116"></a><a name="p6927161055116"></a><strong>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p1792911005118"><a name="p1792911005118"></a><a name="p1792911005118"></a><strong>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p16930810145119"><a name="p16930810145119"></a><a name="p16930810145119"></a><strong>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1863793617509"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p22303345174853"><a name="p22303345174853"></a><a name="p22303345174853"></a>keep_days</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p34927138174853"><a name="p34927138174853"></a><a name="p34927138174853"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p30482871191015"><a name="p30482871191015"></a><a name="p30482871191015"></a>Indicates the number of days to retain the backup files.</p>
    </td>
    </tr>
    <tr id="row1637173618507"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p8056259175641"><a name="p8056259175641"></a><a name="p8056259175641"></a>start_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p42443136175641"><a name="p42443136175641"></a><a name="p42443136175641"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p8983181183415"><a name="p8983181183415"></a><a name="p8983181183415"></a>Indicates the backup time window. Automated backups will be triggered during the backup time window.</p>
    </td>
    </tr>
    <tr id="row166371436195010"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p146385361506"><a name="p146385361506"></a><a name="p146385361506"></a>period</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1363812362509"><a name="p1363812362509"></a><a name="p1363812362509"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p11638173615018"><a name="p11638173615018"></a><a name="p11638173615018"></a>Indicates the backup cycle configuration. Data will be automatically backed up on the selected days every week.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example normal response

    When the automated backup policy is disabled:

    ```
    {
    	"backup_policy": {
    		"keep_days": 0
    	}
    }
    ```

    When the automated backup policy is enabled:

    ```
    {
    	"backup_policy": {
    		"keep_days": 7,
    		"start_time": "19:00-20:00",
    		"period": "1,2"
    	}
    }
    ```

-   Abnormal Response

    For details, see  [Abnormal Request Results](abnormal-request-results.md).


## Status Code<a name="section4778540915440"></a>

For details, see  [Status Codes](status-codes.md).

## Error Code<a name="section946032144017"></a>

For details, see  [Error Codes](error-codes.md).

