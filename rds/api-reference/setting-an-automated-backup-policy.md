# Setting an Automated Backup Policy<a name="rds_09_0002"></a>

## Function<a name="section117711820496"></a>

This API is used to set an automated backup policy.

-   Learn how to  [authorize and authenticate](authentication.md)  this API before using it.
-   Before calling this API, obtain the required  [region and endpoint](https://docs.otc.t-systems.com/en-us/endpoint/index.html).

## URI<a name="section12081471012"></a>

-   URI format

    PUT https://\{_Endpoint_\}/v3/\{project\_id\}/instances/\{instance\_id\}/backups/policy

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
    <p id="p186761044260"><a name="p186761044260"></a><a name="p186761044260"></a>For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="row19780235152911"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p41557789155220"><a name="p41557789155220"></a><a name="p41557789155220"></a>instance_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p10737742155220"><a name="p10737742155220"></a><a name="p10737742155220"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p64450739155220"><a name="p64450739155220"></a><a name="p64450739155220"></a>Specifies the DB instance ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section420839121019"></a>

-   Parameter description

    **Table  2**  Parameter description

    <a name="table6426756154514"></a>
    <table><thead align="left"><tr id="row142645664510"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p17490046"><a name="p17490046"></a><a name="p17490046"></a><strong>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p7407659"><a name="p7407659"></a><a name="p7407659"></a><strong>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p63149496"><a name="p63149496"></a><a name="p63149496"></a><strong>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p14835533"><a name="p14835533"></a><a name="p14835533"></a><strong>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row34264566458"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p28083633"><a name="p28083633"></a><a name="p28083633"></a>backup_policy</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p60181840"><a name="p60181840"></a><a name="p60181840"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p42890904"><a name="p42890904"></a><a name="p42890904"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p61847473"><a name="p61847473"></a><a name="p61847473"></a>Specifies the backup policy objects, including the backup retention period (days) and backup start time.</p>
    <p id="p11824922203914"><a name="p11824922203914"></a><a name="p11824922203914"></a>For details, see <a href="#table163715367507">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  backup\_policy field data structure description

    <a name="table163715367507"></a>
    <table><thead align="left"><tr id="row9637103616501"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p6927161055116"><a name="p6927161055116"></a><a name="p6927161055116"></a><strong>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p139288103515"><a name="p139288103515"></a><a name="p139288103515"></a><strong>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p1792911005118"><a name="p1792911005118"></a><a name="p1792911005118"></a><strong>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p16930810145119"><a name="p16930810145119"></a><a name="p16930810145119"></a><strong>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1863793617509"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p22303345174853"><a name="p22303345174853"></a><a name="p22303345174853"></a>keep_days</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p61740531174853"><a name="p61740531174853"></a><a name="p61740531174853"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p34927138174853"><a name="p34927138174853"></a><a name="p34927138174853"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p30482871191015"><a name="p30482871191015"></a><a name="p30482871191015"></a>Specifies the number of days to retain the generated backup files.</p>
    <p id="p5563313"><a name="p5563313"></a><a name="p5563313"></a>The value range is from 0 to 732. The value <strong id="b842352706115136"><a name="b842352706115136"></a><a name="b842352706115136"></a>0</strong> indicates that the automated backup policy is disabled. To extend the retention period, contact customer service. Automated backups can be retained for up to 2562 days.</p>
    <div class="notice" id="note25229308132657"><a name="note25229308132657"></a><a name="note25229308132657"></a><span class="noticetitle"> NOTICE: </span><div class="noticebody"><p id="p138964484163"><a name="p138964484163"></a><a name="p138964484163"></a>Once the automated backup policy is disabled, automated backups are no longer created and all incremental backups are deleted immediately. Operations related to the incremental backups, including downloads, replications, restorations, and rebuilds, may fail.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row1637173618507"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p8056259175641"><a name="p8056259175641"></a><a name="p8056259175641"></a>start_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p48577249175641"><a name="p48577249175641"></a><a name="p48577249175641"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p42443136175641"><a name="p42443136175641"></a><a name="p42443136175641"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p8983181183415"><a name="p8983181183415"></a><a name="p8983181183415"></a>Specifies the backup time window. Automated backups will be triggered during the backup time window. This parameter is mandatory except that the automated backup policy is disabled.</p>
    <p id="p144363282818"><a name="p144363282818"></a><a name="p144363282818"></a>The value must be a valid value in the "hh:mm-HH:MM" format. The current time is in the UTC format.</p>
    <a name="ul73551635192814"></a><a name="ul73551635192814"></a><ul id="ul73551635192814"><li>The <strong id="b1743121315413"><a name="b1743121315413"></a><a name="b1743121315413"></a>HH</strong> value must be 1 greater than the <strong id="b774310134416"><a name="b774310134416"></a><a name="b774310134416"></a>hh</strong> value.</li><li>The values of <strong id="b75708229414"><a name="b75708229414"></a><a name="b75708229414"></a>mm</strong> and <strong id="b19570822049"><a name="b19570822049"></a><a name="b19570822049"></a>MM</strong> must be the same and must be set to any of the following: <strong id="b1657215221947"><a name="b1657215221947"></a><a name="b1657215221947"></a>00</strong>, <strong id="b057210229411"><a name="b057210229411"></a><a name="b057210229411"></a>15</strong>, <strong id="b757310221742"><a name="b757310221742"></a><a name="b757310221742"></a>30</strong>, or <strong id="b457332211413"><a name="b457332211413"></a><a name="b457332211413"></a>45</strong>.</li></ul>
    <p id="p59342194324"><a name="p59342194324"></a><a name="p59342194324"></a>Example value:</p>
    <a name="ul1210322243217"></a><a name="ul1210322243217"></a><ul id="ul1210322243217"><li>08:15-09:15</li><li>23:00-00:00</li></ul>
    </td>
    </tr>
    <tr id="row166371436195010"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p146385361506"><a name="p146385361506"></a><a name="p146385361506"></a>period</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p6638736145019"><a name="p6638736145019"></a><a name="p6638736145019"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p1363812362509"><a name="p1363812362509"></a><a name="p1363812362509"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p11638173615018"><a name="p11638173615018"></a><a name="p11638173615018"></a>Specifies the backup cycle configuration. Data will be automatically backed up on the selected days every week. This parameter is mandatory except that the automated backup policy is disabled.</p>
    <p id="p79691359132716"><a name="p79691359132716"></a><a name="p79691359132716"></a>Value range: The value is digits separated by commas (,), indicating the day of the week and starting from Monday.</p>
    <p id="p185631411195613"><a name="p185631411195613"></a><a name="p185631411195613"></a>For example, the value <strong id="b13680142354411"><a name="b13680142354411"></a><a name="b13680142354411"></a>1,2,3,4</strong> indicates that the backup period is Monday, Tuesday, Wednesday, and Thursday.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Request example

    Modifying the automated backup policy:

    ```
    {
    	"backup_policy": {
    		"keep_days": 7,
    		"start_time": "19:00-20:00",
    		"period": "1,2"
    	}
    }
    ```

    Disabling the automated backup policy:

    ```
    {
    	"backup_policy": {
    		"keep_days": 0
    	}
    }
    ```


## Response<a name="section1229512143106"></a>

-   Normal response

    None

-   Abnormal Response

    For details, see  [Abnormal Request Results](abnormal-request-results.md).


## Status Code<a name="section4778540915440"></a>

For details, see  [Status Codes](status-codes.md).

## Error Code<a name="section946032144017"></a>

For details, see  [Error Codes](error-codes.md).

