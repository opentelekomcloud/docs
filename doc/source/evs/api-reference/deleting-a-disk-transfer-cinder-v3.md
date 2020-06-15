# Deleting a Disk Transfer<a name="evs_04_3071"></a>

## Function<a name="en-us_topic_0092902034_section44805042171914"></a>

This API is used to delete a disk transfer. A disk transfer can be deleted if it is not accepted. Accepted disk transfers cannot be deleted.

## URI<a name="en-us_topic_0092887872_section21748494171940"></a>

-   URI format

    DELETE /v3/\{project\_id\}/os-volume-transfer/\{transfer\_id\}

-   Parameter description

    <a name="table5162674110529"></a>
    <table><thead align="left"><tr id="row4741724810529"><th class="cellrowborder" valign="top" width="28.57%" id="mcps1.1.4.1.1"><p id="p1559190910529"><a name="p1559190910529"></a><a name="p1559190910529"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="26.529999999999998%" id="mcps1.1.4.1.2"><p id="p5498513910529"><a name="p5498513910529"></a><a name="p5498513910529"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="44.9%" id="mcps1.1.4.1.3"><p id="p2461124910529"><a name="p2461124910529"></a><a name="p2461124910529"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row4735411910529"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p18428135952510"><a name="p18428135952510"></a><a name="p18428135952510"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.1.4.1.2 "><p id="p4344649310529"><a name="p4344649310529"></a><a name="p4344649310529"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.9%" headers="mcps1.1.4.1.3 "><p id="p2950506910529"><a name="p2950506910529"></a><a name="p2950506910529"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row22943135111210"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p52246671151847"><a name="p52246671151847"></a><a name="p52246671151847"></a>transfer_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.1.4.1.2 "><p id="p4121938151847"><a name="p4121938151847"></a><a name="p4121938151847"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.9%" headers="mcps1.1.4.1.3 "><p id="p65441533151847"><a name="p65441533151847"></a><a name="p65441533151847"></a>Specifies the disk transfer ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="en-us_topic_0092902034_section3832507172056"></a>

-   Example request

    ```
    DELETE https://{endpoint}/v3/{project_id}/os-volume-transfer/cac5c677-73a9-4288-bb9c-b2ebfb547377
    ```


## Response<a name="en-us_topic_0092902034_section23586530172122"></a>

None

## Status Codes<a name="en-us_topic_0092902034_section10353980172239"></a>

-   Normal

    202


## Error Codes<a name="section431317151242"></a>

For details, see  [Error Codes](error-codes.md).

