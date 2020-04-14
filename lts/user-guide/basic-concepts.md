# Basic Concepts<a name="lts_01_0003"></a>

## Log Groups<a name="section153271638165116"></a>

A log group is a collection of logs and a basic unit for managing logs. You can transfer logs to log groups for storage to facilitate log queries.

## Log Topics<a name="section13775650103317"></a>

A log topic is the basic unit of a log group. Each log group contains a maximum of 100 log topics.

Logs are distinguished by log topic. Before logs are written, you can specify a log topic to facilitate future queries. For example, you can name log topics as different IDs, thus quickly finding out the logs you need by entering a log topic.

## Agent<a name="section19224193115371"></a>

Agent is a tool used by Log Tank Service \(LTS\) to collect logs. It runs on the server where logs are collected. If you use LTS to collect logs for the first time, you need to install the Agent. If you need to collect logs of multiple hosts, you can also install the Agent in batches. You can view the running status of the Agent in real time on the LTS console.

