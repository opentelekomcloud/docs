# Trace Files<a name="en-us_topic_0043877298"></a>

A trace file is a collection of traces. CTS automatically generates multiple trace files by service and dump interval and then synchronizes these files to the OBS bucket that you have specified.

Generally, all traces of a service generated during a dump interval are compressed into one trace file. However, if there are a large number of traces, the system will adjust the number of traces contained in each trace file as needed.

Trace files are in JSON format.

For details about how to obtain trace files, see  [Querying Archived Traces](querying-archived-traces.md). For details about key fields in the structure of a trace, see  [Trace Structure](trace-structure.md).

