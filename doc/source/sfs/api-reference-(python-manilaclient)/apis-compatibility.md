# APIs Compatibility<a name="EN-US_TOPIC_0119194395"></a>

Currently, SFS provides only interfaces related to basic share provisioning, share capacity expansion/reduction, share access rules, quota management, and API version querying, as well as python-manilaclient commands corresponding to these interfaces. For details, see  [APIs Overview](apis-overview.md). SFS does not support commands not relating to preceding functions, such as commands about snapshots, share types, shared networks, and migration.

>![](/images/icon-notice.gif) **NOTICE:**   
>If you run commands that are not listed in  [APIs Overview](apis-overview.md)  for SFS, an error message will be displayed or an exception may occur during command execution.  

>![](/images/icon-notice.gif) **NOTICE:**   
>In some manila commands provided by python-manilaclient, setting certain parameters may invoke interfaces that are not opened by SFS. If you run such commands with such parameters set, command execution will fail. For example, running the  **manila list --share-type default**  command will fail because SFS does not open the interface for querying the share type.  

>![](/images/icon-notice.gif) **NOTICE:**   
>The latest version of manila APIs supported by current SFS is 2.28. For details about how to query the supported versions, see  [Querying All Major Versions](querying-all-major-versions.md). Therefore, in the latest version of python-manilaclient, some parameters requiring the version of manila APIs to be later than 2.28 are not supported by SFS. This document does not describe such parameters. For example, in python-manilaclient-1.23.0, the  **--count <True|False\>**  parameter in the  **manila list**  command requires that the version of manila APIs must be 2.42 or later. As a result, SFS does not support  **--count <True|False\>**  and this parameter is not described in this document.  

