# What Are the Differences Between Data Formats Supported by an OBS Foreign Table?<a name="dws_03_0018"></a>

An OBS foreign table supports CSV and TEXT. The two formats differ from each other in the following aspects:

-   CSV
    -   Consists of records, which are separated as fields by separators. Each piece of record has the same field sequence.
    -   Efficiently manages the linefeed in fields, but performs moderately in processing special characters.

-   TEXT

    Efficiently manages special characters, but performs moderately in processing the linefeed in fields.


