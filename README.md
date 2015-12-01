# ace command line interface

**Command Line Client for ACE (the Adaptive Context Engine)**

#### Installation

	pip install Axilent-Ace

#### Usage

    ace <command> <subcommand> <args>
    
For example:

	ace graphstack add --name=dev --graphstack-type=developer

#### Initialization and Configuration

The ace-client needs to be initialized in order to work.  Initialization writes a hidden config file into the user's home directory, with the name `.acerc`.

	ace init

##### Global Config

To make the ace-client aware of an ACE project, you can add it:

	ace project add --project=My\ Project \
		--library-key=6a9bc6e0ce9a4d299a3fcc1d7702edf5
		--api-version=astoria

And to add access to a specific GraphStack, you can add it like this:

	ace graphstack add --graphstack=development \
		--api-key=1e73ed82c7bb4da4b3d6cb7ebcf2810a

##### Project Specific Config

Project specific config is localized to the current working directory, and stored in a file called `ace.cfg`.

To set the ACE project to use:

	ace project set --project=My\ Project

To get the current project:

	ace project current

To get the active API version:

	ace project apiversion

To set the default GraphStack

	ace graphstack set --graphstack=development

To see the Library key of the current project

	ace project librarykey

To see the API key of the current graphstack

	ace graphstack apikey

API and Library keys will never be stored in ace.cfg, so it's safe to check the file into version control if you want.

#### Project Serialization

If you want to store an entire project's configuration, you can dump it to a JSON file. The project will dump to standard out.

	ace project dump > myproject.json

To load a project from a dump file

	ace project load --data-file=myproject.json

#### Plugins

The ACE CLI can expand it's functionality by installing plugins.  Plugins add more commands to the CLI.

To install the *Triggerstorm* plugin:

	ace plugins install triggerstorm

To list the installed plugins

	ace plugins list

To uninstall a plugin

	ace plugins uninstall triggerstorm





