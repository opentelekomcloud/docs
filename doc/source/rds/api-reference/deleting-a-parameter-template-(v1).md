# Deleting a Parameter Template<a name="en-us_topic_0056890266"></a>

## Function<a name="section10152443103714"></a>

This API is used to delete a specified parameter template.

## URI<a name="section19156261103714"></a>

-   URI format

    PATH: /v1.0/\{project\_id\}/configurations/\{id\}

    Method: DELETE

-   Parameter description

    **Table  1**  Parameter description

    <a name="table5941139103714"></a>
    <table><thead align="left"><tr id="row41917926103714"><th class="cellrowborder" valign="top" width="21.25%" id="mcps1.2.4.1.1"><p id="p39908856103714"><a name="p39908856103714"></a><a name="p39908856103714"></a><strong id="b84235270691445_1"><a name="b84235270691445_1"></a><a name="b84235270691445_1"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.77%" id="mcps1.2.4.1.2"><p id="p11391927103714"><a name="p11391927103714"></a><a name="p11391927103714"></a><strong id="b842352706102346_1"><a name="b842352706102346_1"></a><a name="b842352706102346_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="49.980000000000004%" id="mcps1.2.4.1.3"><p id="p50330890103714"><a name="p50330890103714"></a><a name="p50330890103714"></a><strong id="b842352706163417_1"><a name="b842352706163417_1"></a><a name="b842352706163417_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row50270298103714"><td class="cellrowborder" valign="top" width="21.25%" headers="mcps1.2.4.1.1 "><p id="p28863461145718"><a name="p28863461145718"></a><a name="p28863461145718"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.77%" headers="mcps1.2.4.1.2 "><p id="p56238989145718"><a name="p56238989145718"></a><a name="p56238989145718"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.980000000000004%" headers="mcps1.2.4.1.3 "><p id="p59064237145718"><a name="p59064237145718"></a><a name="p59064237145718"></a>Specifies the project ID of a tenant in a region.</p>
    </td>
    </tr>
    <tr id="row16341989103714"><td class="cellrowborder" valign="top" width="21.25%" headers="mcps1.2.4.1.1 "><p id="p48632772103714"><a name="p48632772103714"></a><a name="p48632772103714"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.77%" headers="mcps1.2.4.1.2 "><p id="p46940492103714"><a name="p46940492103714"></a><a name="p46940492103714"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.980000000000004%" headers="mcps1.2.4.1.3 "><p id="p44083492103714"><a name="p44083492103714"></a><a name="p44083492103714"></a>Specifies the parameter template ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Restrictions
    -   Currently, the DB engines MySQL and PostgreSQL support deleting parameter templates.
    -   Parameter templates being applied to DB instances cannot be deleted.
    -   Default parameter templates cannot be deleted.


## Request<a name="section23123072103714"></a>

None

## Normal Response<a name="section12395092103714"></a>

```
{
  "errCode": "RDS.0041",
  "externalMessage": "Operation successful."
}
```

## Abnormal Response<a name="section43434612103714"></a>

For details, see  [Abnormal Request Results](abnormal-request-results.md).

