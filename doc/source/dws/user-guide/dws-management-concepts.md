# DWS Management Concepts <a name="dws_01_0005"></a>

## Cluster<a name="section17248514161134"></a>

A cluster is a server group that consists of multiple nodes. DWS is organized using clusters. A data warehouse cluster contains nodes with the same flavors in the same subnet. Those nodes jointly provide services.

## Node<a name="section2062812517412"></a>

Each data warehouse cluster contains at least three nodes, all of which support data storage and analysis.

## Flavor<a name="section33777514161134"></a>

You need to specify the node flavors when you create a data warehouse cluster. CPU, memory, and storage resources vary depending on node flavors.

## Snapshot<a name="section17640691161134"></a>

You can create a snapshot to back up data warehouse cluster data so as to restore the cluster data from the snapshot. A snapshot is retained until you delete it on the management console. Automatic snapshots cannot be manually deleted. Snapshots will occupy your OBS quotas.

## Project<a name="section25776682114018"></a>

Projects are used to group and isolate OpenStack resources \(computing resources, storage resources, and network resources\). A project can be a department or a project team. Multiple projects can be created for one account.

