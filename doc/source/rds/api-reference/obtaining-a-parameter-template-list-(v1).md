# Obtaining a Parameter Template List<a name="en-us_topic_0056890260"></a>

## Function<a name="section43822836102534"></a>

This API is used to obtain a parameter template list, including all databases' default and custom parameter templates.

## URI<a name="section3028329102534"></a>

-   URI format

    PATH: /v1.0/\{project\_id\}/configurations

    Method: GET

-   Parameter description

    **Table  1**  Parameter description

    <a name="table31577051102534"></a>
    <table><thead align="left"><tr id="row1972977102534"><th class="cellrowborder" valign="top" width="22.38%" id="mcps1.2.4.1.1"><p id="p25593416102534"><a name="p25593416102534"></a><a name="p25593416102534"></a><strong id="b84235270691445_1"><a name="b84235270691445_1"></a><a name="b84235270691445_1"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="27.62%" id="mcps1.2.4.1.2"><p id="p59800836102534"><a name="p59800836102534"></a><a name="p59800836102534"></a><strong id="b842352706102346_1"><a name="b842352706102346_1"></a><a name="b842352706102346_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="p12029581102534"><a name="p12029581102534"></a><a name="p12029581102534"></a><strong id="b842352706163417_1"><a name="b842352706163417_1"></a><a name="b842352706163417_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row34872010102534"><td class="cellrowborder" valign="top" width="22.38%" headers="mcps1.2.4.1.1 "><p id="p6060580102534"><a name="p6060580102534"></a><a name="p6060580102534"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.62%" headers="mcps1.2.4.1.2 "><p id="p21144962102534"><a name="p21144962102534"></a><a name="p21144962102534"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p35020365102534"><a name="p35020365102534"></a><a name="p35020365102534"></a>Specifies the project ID of a tenant in a region.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Restrictions

    Currently, the DB engines MySQL and PostgreSQL support obtaining parameter template lists.


## Request<a name="section5119069102534"></a>

None

## Normal Response<a name="section40814386102534"></a>

-   Parameter description

    **Table  2**  Parameter description

    <a name="table18820018102534"></a>
    <table><thead align="left"><tr id="row31964513102534"><th class="cellrowborder" valign="top" width="23.82%" id="mcps1.2.4.1.1"><p id="p38988735102534"><a name="p38988735102534"></a><a name="p38988735102534"></a><strong id="b84235270691445_5"><a name="b84235270691445_5"></a><a name="b84235270691445_5"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="31.61%" id="mcps1.2.4.1.2"><p id="p3970933102534"><a name="p3970933102534"></a><a name="p3970933102534"></a><strong id="b842352706164541_1"><a name="b842352706164541_1"></a><a name="b842352706164541_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.57%" id="mcps1.2.4.1.3"><p id="p53210156102534"><a name="p53210156102534"></a><a name="p53210156102534"></a><strong id="b842352706163417_5"><a name="b842352706163417_5"></a><a name="b842352706163417_5"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row15055371102534"><td class="cellrowborder" valign="top" width="23.82%" headers="mcps1.2.4.1.1 "><p id="p11525563102534"><a name="p11525563102534"></a><a name="p11525563102534"></a>configurations</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.61%" headers="mcps1.2.4.1.2 "><p id="p61155428102534"><a name="p61155428102534"></a><a name="p61155428102534"></a>List data structure. For details, see <a href="#table2172481102534">Table 3</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.57%" headers="mcps1.2.4.1.3 "><p id="p22021397102534"><a name="p22021397102534"></a><a name="p22021397102534"></a>Indicates the parameter template list.</p>
    </td>
    </tr>
    <tr id="row63974846102534"><td class="cellrowborder" valign="top" width="23.82%" headers="mcps1.2.4.1.1 "><p id="p14580032102534"><a name="p14580032102534"></a><a name="p14580032102534"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.61%" headers="mcps1.2.4.1.2 "><p id="p40131930102534"><a name="p40131930102534"></a><a name="p40131930102534"></a>List data structure. For details, see <a href="#table29317924102534">Table 4</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.57%" headers="mcps1.2.4.1.3 "><p id="p63821666102534"><a name="p63821666102534"></a><a name="p63821666102534"></a>Indicates the link compatible with OpenStack. Currently, this parameter functions as a placeholder.</p>
    </td>
    </tr>
    <tr id="row64526335143431"><td class="cellrowborder" valign="top" width="23.82%" headers="mcps1.2.4.1.1 "><p id="p59250621143431"><a name="p59250621143431"></a><a name="p59250621143431"></a>maxgrouplimit</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.61%" headers="mcps1.2.4.1.2 "><p id="p34570963143431"><a name="p34570963143431"></a><a name="p34570963143431"></a>Int</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.57%" headers="mcps1.2.4.1.3 "><p id="p48784618143431"><a name="p48784618143431"></a><a name="p48784618143431"></a>Indicates the maximum quota of custom parameter templates. All DB engines share this quota. Its default value is <strong id="b84235270617243"><a name="b84235270617243"></a><a name="b84235270617243"></a>1000</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  configurations field data structure description

    <a name="table2172481102534"></a>
    <table><thead align="left"><tr id="row43311675102534"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p18584801102534"><a name="p18584801102534"></a><a name="p18584801102534"></a><strong id="b84235270691445_7"><a name="b84235270691445_7"></a><a name="b84235270691445_7"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p28973919102534"><a name="p28973919102534"></a><a name="p28973919102534"></a><strong id="b842352706164541_3"><a name="b842352706164541_3"></a><a name="b842352706164541_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p65186142102534"><a name="p65186142102534"></a><a name="p65186142102534"></a><strong id="b842352706163417_7"><a name="b842352706163417_7"></a><a name="b842352706163417_7"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row45586182102534"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1493246102534"><a name="p1493246102534"></a><a name="p1493246102534"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p53844078102534"><a name="p53844078102534"></a><a name="p53844078102534"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p66403071102534"><a name="p66403071102534"></a><a name="p66403071102534"></a>Indicates the parameter template ID.</p>
    </td>
    </tr>
    <tr id="row60756731102534"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p22348192102534"><a name="p22348192102534"></a><a name="p22348192102534"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p65373113102534"><a name="p65373113102534"></a><a name="p65373113102534"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p60730799102534"><a name="p60730799102534"></a><a name="p60730799102534"></a>Indicates the parameter template name.</p>
    </td>
    </tr>
    <tr id="row44743265175923"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p55904883175924"><a name="p55904883175924"></a><a name="p55904883175924"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p32001680175924"><a name="p32001680175924"></a><a name="p32001680175924"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p41999306175924"><a name="p41999306175924"></a><a name="p41999306175924"></a>Specifies the parameter template description.</p>
    </td>
    </tr>
    <tr id="row9706280102534"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p48011187102534"><a name="p48011187102534"></a><a name="p48011187102534"></a>datastore_version_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p63700943102534"><a name="p63700943102534"></a><a name="p63700943102534"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p59502755102534"><a name="p59502755102534"></a><a name="p59502755102534"></a>Indicates the database version ID.</p>
    </td>
    </tr>
    <tr id="row65762754102534"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p25182878102534"><a name="p25182878102534"></a><a name="p25182878102534"></a>datastore_version_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p26547271102534"><a name="p26547271102534"></a><a name="p26547271102534"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p2845348102534"><a name="p2845348102534"></a><a name="p2845348102534"></a>Indicates the database version name.</p>
    </td>
    </tr>
    <tr id="row25608138102534"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p60993297102534"><a name="p60993297102534"></a><a name="p60993297102534"></a>datastore_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p41510016102534"><a name="p41510016102534"></a><a name="p41510016102534"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p6868160102534"><a name="p6868160102534"></a><a name="p6868160102534"></a>Indicates the database name.</p>
    </td>
    </tr>
    <tr id="row593206131809"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p6477101718017"><a name="p6477101718017"></a><a name="p6477101718017"></a>created</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1196099118017"><a name="p1196099118017"></a><a name="p1196099118017"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p2931621418017"><a name="p2931621418017"></a><a name="p2931621418017"></a>Indicates the parameter template creation time in the following format: yyyy-MM-ddTHH:mm:ss.</p>
    </td>
    </tr>
    <tr id="row682502118015"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p3090154018017"><a name="p3090154018017"></a><a name="p3090154018017"></a>updated</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1999678718017"><a name="p1999678718017"></a><a name="p1999678718017"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p912703918017"><a name="p912703918017"></a><a name="p912703918017"></a>Indicates the parameter template updated time in the following format: yyyy-MM-ddTHH:mm:ss.</p>
    </td>
    </tr>
    <tr id="row6315141102534"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p41764399102534"><a name="p41764399102534"></a><a name="p41764399102534"></a>allowed_updated</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p27473178102534"><a name="p27473178102534"></a><a name="p27473178102534"></a>Int</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p54172888194540"><a name="p54172888194540"></a><a name="p54172888194540"></a>Indicates whether the parameters in the obtained parameter template can be modified.</p>
    <a name="ul29769253194627"></a><a name="ul29769253194627"></a><ul id="ul29769253194627"><li><strong id="b84235270693047"><a name="b84235270693047"></a><a name="b84235270693047"></a>0</strong>: indicates the parameters cannot be modified. When a default parameter template is obtained, this parameter value is <strong id="b842352706213339"><a name="b842352706213339"></a><a name="b842352706213339"></a>0</strong>.</li><li><strong id="b2671175116415"><a name="b2671175116415"></a><a name="b2671175116415"></a>1</strong>: indicates the parameters can be modified.</li></ul>
    </td>
    </tr>
    <tr id="row29505758102534"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p41156193102534"><a name="p41156193102534"></a><a name="p41156193102534"></a>instance_count</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p45317345102534"><a name="p45317345102534"></a><a name="p45317345102534"></a>Int</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p46826309102534"><a name="p46826309102534"></a><a name="p46826309102534"></a>Indicates the number of associated DB instances.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4**  links field data structure description

    <a name="table29317924102534"></a>
    <table><thead align="left"><tr id="row1320492102534"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p39850998102534"><a name="p39850998102534"></a><a name="p39850998102534"></a><strong id="b84235270691445_9"><a name="b84235270691445_9"></a><a name="b84235270691445_9"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p6705388102534"><a name="p6705388102534"></a><a name="p6705388102534"></a><strong id="b842352706164541_5"><a name="b842352706164541_5"></a><a name="b842352706164541_5"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p6265592102534"><a name="p6265592102534"></a><a name="p6265592102534"></a><strong id="b842352706163417_9"><a name="b842352706163417_9"></a><a name="b842352706163417_9"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row37750911102534"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p37924971102534"><a name="p37924971102534"></a><a name="p37924971102534"></a>href</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p52023844102534"><a name="p52023844102534"></a><a name="p52023844102534"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p51734292145223"><a name="p51734292145223"></a><a name="p51734292145223"></a>Indicates the link URL. Currently, this parameter functions as a placeholder and its value is <strong id="b84235270619145"><a name="b84235270619145"></a><a name="b84235270619145"></a>""</strong>.</p>
    </td>
    </tr>
    <tr id="row8874527102534"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p47748086102534"><a name="p47748086102534"></a><a name="p47748086102534"></a>rel</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p42389749102534"><a name="p42389749102534"></a><a name="p42389749102534"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p13067152145223"><a name="p13067152145223"></a><a name="p13067152145223"></a>Indicates the link redirection. Currently, this parameter functions as a placeholder and its default value is <strong id="b842352706213853"><a name="b842352706213853"></a><a name="b842352706213853"></a>next</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Response example

    ```
    { 
      "configurations": [
        {
          "id": "07fc12a8e0e94df7a3fcf53d0b5e1605pr01",
          "name": "default-mysql-5.6",
          "description": "Default parameter group for mysql 5.6",
          "datastore_version_id": "",
          "datastore_version_name": "5.6",
          "datastore_name": "mysql",
          "created": "2017-01-01T10:00:00",
          "updated": "2017-01-01T10:00:00",
          "allowed_updated": 0,
          "instance_count": 0
    },
        {
          "id": "3bc1e9cc0d34404b9225ed7a58fb284epr01",
          "name": "test-mysql-5.6",
          "description": "test-mysql-5.6",
          "datastore_version_id": "",
          "datastore_version_name": "5.6",
          "datastore_name": "mysql",
          "created": "2017-02-01T10:00:00",
          "updated": "2017-02-01T10:00:00",
          "allowed_updated": 1,
          "instance_count": 2
        }
      ],
      "links": [
        {  
          "href": "",
          "rel": "next"
        }
      ],
      "maxgrouplimit": 100
    }
    ```


## Abnormal Response<a name="section34751554102534"></a>

For details, see  [Abnormal Request Results](abnormal-request-results.md).

