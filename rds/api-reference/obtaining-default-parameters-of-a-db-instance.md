# Obtaining Default Parameters of a DB Instance<a name="en-us_topic_0056890259"></a>

## Function<a name="section21968845102411"></a>

This API is used to obtain default parameters of a specified DB instance.

## URI<a name="section43378670102411"></a>

-   URI format

    PATH: /v1.0/\{project\_id\}/instances/\{instanceId\}/configuration

    Method: GET

-   Parameter description

    **Table  1**  Parameter description

    <a name="table39538525102411"></a>
    <table><thead align="left"><tr id="row38994773102411"><th class="cellrowborder" valign="top" width="20.68%" id="mcps1.2.4.1.1"><p id="p4460079102411"><a name="p4460079102411"></a><a name="p4460079102411"></a><strong id="b84235270691445"><a name="b84235270691445"></a><a name="b84235270691445"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="29.330000000000002%" id="mcps1.2.4.1.2"><p id="p25722146102411"><a name="p25722146102411"></a><a name="p25722146102411"></a><strong id="b842352706102346"><a name="b842352706102346"></a><a name="b842352706102346"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="49.99%" id="mcps1.2.4.1.3"><p id="p3119061102411"><a name="p3119061102411"></a><a name="p3119061102411"></a><strong id="b842352706163417"><a name="b842352706163417"></a><a name="b842352706163417"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row51317360102411"><td class="cellrowborder" valign="top" width="20.68%" headers="mcps1.2.4.1.1 "><p id="p63065500102411"><a name="p63065500102411"></a><a name="p63065500102411"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p8031872102411"><a name="p8031872102411"></a><a name="p8031872102411"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.99%" headers="mcps1.2.4.1.3 "><p id="p46601925102411"><a name="p46601925102411"></a><a name="p46601925102411"></a>Specifies the project ID of a tenant in a region.</p>
    </td>
    </tr>
    <tr id="row16764147102411"><td class="cellrowborder" valign="top" width="20.68%" headers="mcps1.2.4.1.1 "><p id="p15718700102411"><a name="p15718700102411"></a><a name="p15718700102411"></a>instanceId</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p65255193102411"><a name="p65255193102411"></a><a name="p65255193102411"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.99%" headers="mcps1.2.4.1.3 "><p id="p51179299102411"><a name="p51179299102411"></a><a name="p51179299102411"></a>Specifies the DB instance ID.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Restrictions

    Currently, only the DB engines MySQL and PostgreSQL are supported by the API.


## Request<a name="section589521102411"></a>

None

## Normal Response<a name="section27108241102411"></a>

-   Parameter description

    **Table  2**  Parameter description

    <a name="table18682996102411"></a>
    <table><thead align="left"><tr id="row44628881102411"><th class="cellrowborder" valign="top" width="21.07210721072107%" id="mcps1.2.4.1.1"><p id="p58169645102411"><a name="p58169645102411"></a><a name="p58169645102411"></a><strong id="b281227480"><a name="b281227480"></a><a name="b281227480"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="29.05290529052905%" id="mcps1.2.4.1.2"><p id="p14120772102411"><a name="p14120772102411"></a><a name="p14120772102411"></a><strong id="b842352706164541"><a name="b842352706164541"></a><a name="b842352706164541"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="49.874987498749874%" id="mcps1.2.4.1.3"><p id="p2931904102411"><a name="p2931904102411"></a><a name="p2931904102411"></a><strong id="b1044129591"><a name="b1044129591"></a><a name="b1044129591"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row36157705102411"><td class="cellrowborder" valign="top" width="21.07210721072107%" headers="mcps1.2.4.1.1 "><p id="p43092998102411"><a name="p43092998102411"></a><a name="p43092998102411"></a>instance</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.05290529052905%" headers="mcps1.2.4.1.2 "><p id="p871968102411"><a name="p871968102411"></a><a name="p871968102411"></a>List data structure. For details, see <a href="#table16731081102411">Table 3</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.874987498749874%" headers="mcps1.2.4.1.3 "><p id="p31685170102411"><a name="p31685170102411"></a><a name="p31685170102411"></a>Indicates the parameter information of the specified DB instance.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  instance field data structure description

    <a name="table16731081102411"></a>
    <table><thead align="left"><tr id="row9353381102411"><th class="cellrowborder" valign="top" width="21.07%" id="mcps1.2.4.1.1"><p id="p19426391102411"><a name="p19426391102411"></a><a name="p19426391102411"></a><strong id="b462833301"><a name="b462833301"></a><a name="b462833301"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="29.29%" id="mcps1.2.4.1.2"><p id="p30033825102411"><a name="p30033825102411"></a><a name="p30033825102411"></a><strong id="b43067388"><a name="b43067388"></a><a name="b43067388"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="49.64%" id="mcps1.2.4.1.3"><p id="p16820780102411"><a name="p16820780102411"></a><a name="p16820780102411"></a><strong id="b1503867310"><a name="b1503867310"></a><a name="b1503867310"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row20305952102411"><td class="cellrowborder" valign="top" width="21.07%" headers="mcps1.2.4.1.1 "><p id="p34169379102411"><a name="p34169379102411"></a><a name="p34169379102411"></a>configuration</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.29%" headers="mcps1.2.4.1.2 "><p id="p16256352102411"><a name="p16256352102411"></a><a name="p16256352102411"></a>Dictionary data structure. For details, see <a href="#table39720807102411">Table 4</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.64%" headers="mcps1.2.4.1.3 "><p id="p41696125102411"><a name="p41696125102411"></a><a name="p41696125102411"></a>Indicates the default parameter value.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4**  configuration field data structure description

    <a name="table39720807102411"></a>
    <table><thead align="left"><tr id="row8443733102411"><th class="cellrowborder" valign="top" width="20.880000000000003%" id="mcps1.2.4.1.1"><p id="p12853805102411"><a name="p12853805102411"></a><a name="p12853805102411"></a><strong id="b791909733"><a name="b791909733"></a><a name="b791909733"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="29.86%" id="mcps1.2.4.1.2"><p id="p34525269102411"><a name="p34525269102411"></a><a name="p34525269102411"></a><strong id="b1078079530"><a name="b1078079530"></a><a name="b1078079530"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="49.26%" id="mcps1.2.4.1.3"><p id="p45083381102411"><a name="p45083381102411"></a><a name="p45083381102411"></a><strong id="b1545396945"><a name="b1545396945"></a><a name="b1545396945"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row27875254102411"><td class="cellrowborder" valign="top" width="20.880000000000003%" headers="mcps1.2.4.1.1 "><p id="p43303103102411"><a name="p43303103102411"></a><a name="p43303103102411"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.86%" headers="mcps1.2.4.1.2 "><p id="p17890489102411"><a name="p17890489102411"></a><a name="p17890489102411"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.26%" headers="mcps1.2.4.1.3 "><p id="p48244396202445"><a name="p48244396202445"></a><a name="p48244396202445"></a>Indicates the parameter name. For example, in <strong id="b84235270621563"><a name="b84235270621563"></a><a name="b84235270621563"></a>"max_connections": "10"</strong>, the key is <strong id="b842352706215241"><a name="b842352706215241"></a><a name="b842352706215241"></a>max_connections</strong>.</p>
    </td>
    </tr>
    <tr id="row6100639102411"><td class="cellrowborder" valign="top" width="20.880000000000003%" headers="mcps1.2.4.1.1 "><p id="p24389722102411"><a name="p24389722102411"></a><a name="p24389722102411"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.86%" headers="mcps1.2.4.1.2 "><p id="p29410470102411"><a name="p29410470102411"></a><a name="p29410470102411"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.26%" headers="mcps1.2.4.1.3 "><p id="p5120154202445"><a name="p5120154202445"></a><a name="p5120154202445"></a>Indicates the parameter value. For example, in <strong id="b953814020215624"><a name="b953814020215624"></a><a name="b953814020215624"></a>"max_connections": "10"</strong>, the value is <strong id="b842352706215633"><a name="b842352706215633"></a><a name="b842352706215633"></a>10</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Response example

    ```
    {
        "instance": {
            "configuration": {
                "basedir": "/usr",
                "connect_timeout": "15",
                "datadir": "/var/lib/mysql",
                "default_storage_engine": "innodb",
                "innodb_buffer_pool_size": "600M",
                "innodb_data_file_path": "ibdata1:10M:autoextend",
                "innodb_file_per_table": "1",
                "innodb_log_buffer_size": "25M",
                "innodb_log_file_size": "50M",
                "innodb_log_files_in_group": "2",
                "join_buffer_size": "1M",
                "key_buffer_size": "200M",
                "local-infile": "0",
                "max_allowed_packet": "4096K",
                "max_connections": "400",
                "max_heap_table_size": "64M",
                "max_user_connections": "400",
                "myisam-recover": "BACKUP",
                "open_files_limit": "2048",
                "pid_file": "/var/run/mysqld/mysqld.pid",
                "port": "3306",
                "query_cache_limit": "1M",
                "query_cache_size": "32M",
                "query_cache_type": "1",
                "read_buffer_size": "512K",
                "read_rnd_buffer_size": "512K",
                "server_id": "334596",
                "skip-external-locking": "1",
                "sort_buffer_size": "1M",
                "table_definition_cache": "1024",
                "table_open_cache": "1024",
                "thread_cache_size": "16",
                "thread_stack": "192K",
                "tmp_table_size": "64M",
                "tmpdir": "/var/tmp",
                "user": "mysql",
                "wait_timeout": "120"
            }
    }
    }
    ```


## Abnormal Response<a name="section8839348102411"></a>

For details, see  [Abnormal Request Results](abnormal-request-results.md).

