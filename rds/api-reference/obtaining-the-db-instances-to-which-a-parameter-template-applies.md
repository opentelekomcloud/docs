# Obtaining the DB Instances to Which a Parameter Template Applies<a name="en-us_topic_0056890262"></a>

## Function<a name="section9132197102930"></a>

This API is used to obtain the DB instances to which a specified parameter template applies.

## URI<a name="section13594659102930"></a>

-   URI format

    PATH: /v1.0/\{project\_id\}/configurations/\{id\}/instances

    Method: GET

-   Parameter description

    **Table  1**  Parameter description

    <a name="table49253498102930"></a>
    <table><thead align="left"><tr id="row6101675102930"><th class="cellrowborder" valign="top" width="21.25%" id="mcps1.2.4.1.1"><p id="p24473662102930"><a name="p24473662102930"></a><a name="p24473662102930"></a><strong id="b84235270691445_1"><a name="b84235270691445_1"></a><a name="b84235270691445_1"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.88%" id="mcps1.2.4.1.2"><p id="p36209614102930"><a name="p36209614102930"></a><a name="p36209614102930"></a><strong id="b842352706102346_1"><a name="b842352706102346_1"></a><a name="b842352706102346_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="49.87%" id="mcps1.2.4.1.3"><p id="p47297602102930"><a name="p47297602102930"></a><a name="p47297602102930"></a><strong id="b842352706163417_1"><a name="b842352706163417_1"></a><a name="b842352706163417_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row5900547102930"><td class="cellrowborder" valign="top" width="21.25%" headers="mcps1.2.4.1.1 "><p id="p66477586145432"><a name="p66477586145432"></a><a name="p66477586145432"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.88%" headers="mcps1.2.4.1.2 "><p id="p15984606145432"><a name="p15984606145432"></a><a name="p15984606145432"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.87%" headers="mcps1.2.4.1.3 "><p id="p62134500145432"><a name="p62134500145432"></a><a name="p62134500145432"></a>Specifies the project ID of a tenant in a region.</p>
    </td>
    </tr>
    <tr id="row37808032102930"><td class="cellrowborder" valign="top" width="21.25%" headers="mcps1.2.4.1.1 "><p id="p36091923145432"><a name="p36091923145432"></a><a name="p36091923145432"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.88%" headers="mcps1.2.4.1.2 "><p id="p49613608145432"><a name="p49613608145432"></a><a name="p49613608145432"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.87%" headers="mcps1.2.4.1.3 "><p id="p42126365145432"><a name="p42126365145432"></a><a name="p42126365145432"></a>Specifies the parameter template ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Restrictions

    Currently, the DB engines MySQL and PostgreSQL support obtaining DB instances to which the specified parameter template applies.


## Request<a name="section64614201102930"></a>

None

## Normal Response<a name="section60439435102930"></a>

-   Parameter description

    **Table  2**  Parameter description

    <a name="table63970789102930"></a>
    <table><thead align="left"><tr id="row53030790102930"><th class="cellrowborder" valign="top" width="25.509999999999998%" id="mcps1.2.4.1.1"><p id="p526765102930"><a name="p526765102930"></a><a name="p526765102930"></a><strong id="b84235270691445_5"><a name="b84235270691445_5"></a><a name="b84235270691445_5"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="40.82%" id="mcps1.2.4.1.2"><p id="p42667967102930"><a name="p42667967102930"></a><a name="p42667967102930"></a><strong id="b842352706164541_1"><a name="b842352706164541_1"></a><a name="b842352706164541_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.67%" id="mcps1.2.4.1.3"><p id="p33553318102930"><a name="p33553318102930"></a><a name="p33553318102930"></a><strong id="b842352706163417_5"><a name="b842352706163417_5"></a><a name="b842352706163417_5"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row33464266102930"><td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.4.1.1 "><p id="p26251026102930"><a name="p26251026102930"></a><a name="p26251026102930"></a>instances</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.82%" headers="mcps1.2.4.1.2 "><p id="p45958375102930"><a name="p45958375102930"></a><a name="p45958375102930"></a>List data structure. For details, see <a href="#table47861511102930">Table 3</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.67%" headers="mcps1.2.4.1.3 "><p id="p16332468102930"><a name="p16332468102930"></a><a name="p16332468102930"></a>Indicates the DB instance list information.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  instances field data structure description

    <a name="table47861511102930"></a>
    <table><thead align="left"><tr id="row44932905102930"><th class="cellrowborder" valign="top" width="26.939999999999998%" id="mcps1.2.4.1.1"><p id="p15686709102930"><a name="p15686709102930"></a><a name="p15686709102930"></a><strong id="b84235270691445_7"><a name="b84235270691445_7"></a><a name="b84235270691445_7"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39.35%" id="mcps1.2.4.1.2"><p id="p62663950102930"><a name="p62663950102930"></a><a name="p62663950102930"></a><strong id="b842352706164541_3"><a name="b842352706164541_3"></a><a name="b842352706164541_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.71%" id="mcps1.2.4.1.3"><p id="p42615195102930"><a name="p42615195102930"></a><a name="p42615195102930"></a><strong id="b842352706163417_7"><a name="b842352706163417_7"></a><a name="b842352706163417_7"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row29278789102930"><td class="cellrowborder" valign="top" width="26.939999999999998%" headers="mcps1.2.4.1.1 "><p id="p22771699102930"><a name="p22771699102930"></a><a name="p22771699102930"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.35%" headers="mcps1.2.4.1.2 "><p id="p32568334102930"><a name="p32568334102930"></a><a name="p32568334102930"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.71%" headers="mcps1.2.4.1.3 "><p id="p20789373102930"><a name="p20789373102930"></a><a name="p20789373102930"></a>Indicates the DB instance ID.</p>
    </td>
    </tr>
    <tr id="row52886632102930"><td class="cellrowborder" valign="top" width="26.939999999999998%" headers="mcps1.2.4.1.1 "><p id="p55958769102930"><a name="p55958769102930"></a><a name="p55958769102930"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.35%" headers="mcps1.2.4.1.2 "><p id="p36366402102930"><a name="p36366402102930"></a><a name="p36366402102930"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.71%" headers="mcps1.2.4.1.3 "><p id="p59997444102930"><a name="p59997444102930"></a><a name="p59997444102930"></a>Indicates the DB instance name.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Response example

    ```
    {
      "instances": [
        {
          "id": "53754eff-3f95-4da8-a908-a88e6ea2f65a",
          "name": "instances_test_1"
    },    
    {
          "id": "53754eff-3f95-4da8-a908-a88e6ea2f65b",
          "name": "instances_test_2"
        }
      ]
    }
    ```


## Abnormal Response<a name="section36958885102930"></a>

For details, see  [Abnormal Request Results](abnormal-request-results.md).

