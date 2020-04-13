# Deleting Backup Files<a name="EN-US_TOPIC_0237964373"></a>

## Function<a name="section10488826"></a>

This API is used to delete the files backed up by a DCS instance.

## URI<a name="section27290576"></a>

-   URI format:

    DELETE /v1.0/\{project\_id\}/instances/\{instance\_id\}/backups/\{backup\_id\}

-   Parameter description:

    [Table 1](#d0e5777)  describes the parameters of this API.


**Table  1**  Parameter description

<a name="d0e5777"></a>
<table><thead align="left"><tr id="row45170876"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p34962352"><a name="p34962352"></a><a name="p34962352"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p13378227"><a name="p13378227"></a><a name="p13378227"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p9894640"><a name="p9894640"></a><a name="p9894640"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p63268365"><a name="p63268365"></a><a name="p63268365"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row24463922"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p35420680"><a name="p35420680"></a><a name="p35420680"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p50502838"><a name="p50502838"></a><a name="p50502838"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p64198117"><a name="p64198117"></a><a name="p64198117"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p32665021"><a name="p32665021"></a><a name="p32665021"></a>Project ID.</p>
</td>
</tr>
<tr id="row25549735"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p56262670"><a name="p56262670"></a><a name="p56262670"></a>instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p60982450"><a name="p60982450"></a><a name="p60982450"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p40631418"><a name="p40631418"></a><a name="p40631418"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p2810575"><a name="p2810575"></a><a name="p2810575"></a>DCS instance ID.</p>
</td>
</tr>
<tr id="row25295177"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p35643484"><a name="p35643484"></a><a name="p35643484"></a>backup_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p1441071"><a name="p1441071"></a><a name="p1441071"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p49617898"><a name="p49617898"></a><a name="p49617898"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p59626806"><a name="p59626806"></a><a name="p59626806"></a>ID of the backup record.</p>
</td>
</tr>
</tbody>
</table>

-   Example URI:

    ```
    DELETE /v1.0/885cacf2d49d4bb6931ae668e9c07553/instances/e016385d-b9fa-4bf0-9f38-9379f4a5293f/backups/75509c85-50a6-4525-ad56-a1bb62e84570
    ```


## Request<a name="section44288600"></a>

None.

## Response<a name="section63053081"></a>

-   Status code:

    If status code "200 OK" is returned, this request is fulfilled. For description of other status codes, see  [API Usage Guidelines](api-usage-guidelines.md).

-   Response parameter:

    [Table 2](#table5929344419)describes the response parameters.


**Table  2**  Parameter description

<a name="table5929344419"></a>
<table><thead align="left"><tr id="row64354785"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p45355069"><a name="p45355069"></a><a name="p45355069"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="12%" id="mcps1.2.4.1.2"><p id="p49881998"><a name="p49881998"></a><a name="p49881998"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="63%" id="mcps1.2.4.1.3"><p id="p13910076"><a name="p13910076"></a><a name="p13910076"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row52974382"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p63066573"><a name="p63066573"></a><a name="p63066573"></a>message</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p8118784"><a name="p8118784"></a><a name="p8118784"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p53641776"><a name="p53641776"></a><a name="p53641776"></a>Description of the result of deleting backup files.</p>
</td>
</tr>
</tbody>
</table>

-   Example response:

    ```
    { 
     "message": "" 
    }
    ```


