# README

## Introduction 

This Git repository provides you with Open Telekom Cloud (OTC) service
documents, including user guides and API references, to help you better
understand and use OTC services.

## Directory structure 

Documents are stored according to the following rules:
- The level-1 directory (github.com/opentelekomcloud/docs/doc/source) is the
  main entry for OTC service documents.
- Level-2 directories are named after service abbreviations such as "ecs" and
  "vpc".
- Level-3 directories are named after document names such as "user-guide" and
  "api-reference".
- Level-4 and sub -directories contain topics and graphs of a document. Files
  are grouped in subfolders in the desired structuring of the results (i.e. for
the api reference files are grouped on the resource bases). Basic documentation
tree is handled as .rst documentation to improve flexibility. Final
documentation content might be placed in markdown format and must be
correspondignly included in the index file. Project validation jobs will try to
build project in each PR and will request changes if the build fails (i.e. file
contain broken links, file not included in the index or otherwise index points
to not existing file. This helps keeping directories small and avoid file name
collisions.

Pictures (icons) common to all services are located under doc/source/images and
are included from there, instead of copying them in each individual service.


## Document contribution 

We appreciate contributed documents from all OTC users, partners, developers,
and document engineers, which enrich our repository and help us improve
continuously.  To make a contribution, you need to register with GitHub. Then
you can log in to GitHub to find the wanted document in a Git repository. If
you need to download PDF documents or preview a full document online, go to the
help center of OTC at https://docs.otc.t-systems.com/

Using the index.rst file in the Git repository (doc/source/index.rst) can help
you quickly locate the topic that you want to read. If you want to make changes
to a topic, submit the content to the project owner of OTC by forking and
proposing a pull requests with the change.

## Language restrictions 

All documents in the GitHub community must be written in the
RestructuredText/Markdown language. For more information about writing and
formatting on GitHub, visit
https://help.github.com/articles/getting-started-with-writing-and-formatting-on-github/


## LICENSE 

For details, see the LICENSE file.  Apache-2.0 License
