Snowflake.Core
==============

Snowflake.Core is a system that acts as a backend for emulator frontends. Snowflake handles such things like scraping games, maintaining a database of games/roms, and handling media for the game. Frontends can connect to an instance through JSONRPC or XMLRPC and obtain data from the running instance. Snowflake is written in Python and is easily moddable for your purposes. As well, one can write wrappers around the Python methods to expose the methods to another language, but for now, the best way to access this data is through Snowflake's RPC servers.

Architecture
============
Snowflake uses a client-server model. Snowflake runs as a local server and frontends can connect to this instance to obtain data to display to the end user. This way, many frontends can have a standardized way of accessing this data, making interoperability extremely easy. 