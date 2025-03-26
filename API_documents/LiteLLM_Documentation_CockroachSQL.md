

## Synopsis [Anchor link for: synopsis](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql\#synopsis)

Start the interactive SQL shell:

```shell
cockroach sql <flags>

```

Execute SQL from the command line:

```shell
cockroach sql --execute="<sql statement>;<sql statement>" --execute="<sql-statement>" <flags>

```

```shell
echo "<sql statement>;<sql statement>" | cockroach sql <flags>

```

```shell
cockroach sql <flags> --file file-containing-statements.sql

```

Exit the interactive SQL shell:

```sql
\q

```

```sql
quit

```

```sql
exit

```

```shell

```

View help:

```shell
cockroach sql --help

```

## Flags [Anchor link for: flags](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql\#flags)

The `sql` command supports the following types of flags:

- [General Use](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#general)
- [Client Connection](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#client-connection)
- [Logging](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#logging)

### General [Anchor link for: general](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql\#general)

- To start an interactive SQL shell, run `cockroach sql` with all appropriate connection flags or use just the [`--url` flag](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#sql-flag-url), which includes [connection details](https://www.cockroachlabs.com/docs/v25.1/connection-parameters#connect-using-a-url).
- To execute SQL statements from the command line, use the [`--execute` flag](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#sql-flag-execute).

| Flag | Description |
| --- | --- |
| `--database`<br>`-d` | A database name to use as [current database](https://www.cockroachlabs.com/docs/v25.1/sql-name-resolution#current-database) in the newly created session. |
| `--embedded` | Minimizes the SQL shell [welcome text](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#welcome-message) to be appropriate for embedding in playground-type environments. Specifically, this flag removes details that users in an embedded environment have no control over (e.g., networking information). |
| `--echo-sql` | Reveal the SQL statements sent implicitly by the command-line utility. For a demonstration, see the [example](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#reveal-the-sql-statements-sent-implicitly-by-the-command-line-utility) below.<br>This can also be enabled within the interactive SQL shell via the `\set echo` [shell command](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#commands). |
| `--execute`<br>`-e` | Execute SQL statements directly from the command line, without opening a shell. This flag can be set multiple times, and each instance can contain one or more statements separated by semi-colons. If an error occurs in any statement, the command exits with a non-zero status code and further statements are not executed. The results of each statement are printed to the standard output (see `--format` for formatting options).<br>For a demonstration of this and other ways to execute SQL from the command line, see the [example](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#execute-sql-statements-from-the-command-line) below. |
| `--file <filename>`<br>`-f <filename>` | Read SQL statements from `<filename>`. |
| `--format` | How to display table rows printed to the standard output. Possible values: `tsv`, `csv`, `table`, `raw`, `records`, `sql`, `html`.<br>**Default:** `table` for sessions that [output on a terminal](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#session-and-output-types); `tsv` otherwise<br>This flag corresponds to the `display_format` [client-side option](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#client-side-options). |
| `--read-only` | Sets the `default_transaction_read_only` [session variable](https://www.cockroachlabs.com/docs/v25.1/show-vars#supported-variables) to `on` upon connecting. |
| `--safe-updates` | Disallow potentially unsafe SQL statements, including `DELETE` without a `WHERE` clause, `UPDATE` without a `WHERE` clause, and `ALTER TABLE ... DROP COLUMN`.<br>**Default:** `true` for [interactive sessions](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#session-and-output-types); `false` otherwise<br>Potentially unsafe SQL statements can also be allowed/disallowed for an entire session via the `sql_safe_updates` [session variable](https://www.cockroachlabs.com/docs/v25.1/set-vars). |
| `--set` | Set a [client-side option](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#client-side-options) before starting the SQL shell or executing SQL statements from the command line via `--execute`. This flag may be specified multiple times, once per option.<br>After starting the SQL shell, the `\set` and `unset` commands can be use to enable and disable client-side options as well. |
| `--watch` | Repeat the SQL statements specified with `--execute` or `-e` until a SQL error occurs or the process is terminated. `--watch` applies to all `--execute` or `-e` flags in use.<br>You must also specify an interval at which to repeat the statement, followed by a time unit. For example, to specify an interval of 5 seconds, use `5s`.<br> Note that this flag is intended for simple monitoring scenarios during development and testing. See the [example](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#repeat-a-sql-statement) below. |

### Client connection [Anchor link for: client connection](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql\#client-connection)

| Flag | Description |
| --- | --- |
| `--url` | A [connection URL](https://www.cockroachlabs.com/docs/v25.1/connection-parameters#connect-using-a-url) to use instead of the other arguments. To convert a connection URL to the syntax that works with your client driver, run [`cockroach convert-url`](https://www.cockroachlabs.com/docs/v25.1/connection-parameters#convert-a-url-for-different-drivers).<br>**Env Variable:** `COCKROACH_URL`<br>**Default:** no URL |
| `--host` | The server host and port number to connect to. This can be the address of any node in the cluster. <br>**Env Variable:** `COCKROACH_HOST`<br>**Default:** `localhost:26257` |
| `--port`<br>`-p` | The server port to connect to. Note: The port number can also be specified via `--host`. <br>**Env Variable:** `COCKROACH_PORT`<br>**Default:** `26257` |
| `--user`<br>`-u` | The [SQL user](https://www.cockroachlabs.com/docs/v25.1/create-user) that will own the client session.<br>**Env Variable:** `COCKROACH_USER`<br>**Default:** `root` |
| `--insecure` | Use an insecure connection.<br>**Env Variable:** `COCKROACH_INSECURE`<br>**Default:** `false` |
| `--cert-principal-map` | A comma-separated list of `<cert-principal>:<db-principal>` mappings. This allows mapping the principal in a cert to a DB principal such as `node` or `root` or any SQL user. This is intended for use in situations where the certificate management system places restrictions on the `Subject.CommonName` or `SubjectAlternateName` fields in the certificate (e.g., disallowing a `CommonName` like `node` or `root`). If multiple mappings are provided for the same `<cert-principal>`, the last one specified in the list takes precedence. A principal not specified in the map is passed through as-is via the identity function. A cert is allowed to authenticate a DB principal if the DB principal name is contained in the mapped `CommonName` or DNS-type `SubjectAlternateName` fields. |
| `--certs-dir` | The path to the [certificate directory](https://www.cockroachlabs.com/docs/v25.1/cockroach-cert) containing the CA and client certificates and client key.<br>**Env Variable:** `COCKROACH_CERTS_DIR`<br>**Default:** `${HOME}/.cockroach-certs/` |

See [Client Connection Parameters](https://www.cockroachlabs.com/docs/v25.1/connection-parameters) for more details.

### Logging [Anchor link for: logging](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql\#logging)

By default, this command logs messages to `stderr`. This includes events with `WARNING` [severity](https://www.cockroachlabs.com/docs/v25.1/logging#logging-levels-severities) and higher.

If you need to troubleshoot this command's behavior, you can [customize its logging behavior](https://www.cockroachlabs.com/docs/v25.1/configure-logs).

## Session and output types [Anchor link for: session and output types](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql\#session-and-output-types)

`cockroach sql` exhibits different behaviors depending on whether or not the session is interactive and/or whether or not the session outputs on a terminal.

- A session is **interactive** when `cockroach sql` is invoked without the `-e` or `-f` flag, and the input is a terminal. In such cases:


  - The [`errexit` option](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#sql-option-errexit) defaults to `false`.
  - The [`check_syntax` option](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#sql-option-check-syntax) defaults to `true` if supported by the CockroachDB server (this is checked when the shell starts up).
  - **Ctrl+C** at the prompt will only terminate the shell if no other input was entered on the same line already.
  - The shell will attempt to set the `safe_updates` [session variable](https://www.cockroachlabs.com/docs/v25.1/set-vars) to `true` on the server.
  - The shell continues to read input after the last command entered.
- A session **outputs on a terminal** when output is not redirected to a file. In such cases:


  - The [`--format` flag](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#sql-flag-format) and its corresponding [`display_format` option](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#sql-option-display-format) default to `table`. These default to `tsv` otherwise.
  - The `show_times` option defaults to `true`.

When a session is both interactive and outputs on a terminal, `cockroach sql` also activates the interactive prompt with a line editor that can be used to modify the current line of input. Also, command history becomes active.

## SQL shell [Anchor link for: sql shell](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql\#sql-shell)

### Welcome message [Anchor link for: welcome message](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql\#welcome-message)

When the SQL shell connects (or reconnects) to a CockroachDB node, it prints a welcome text with some tips and CockroachDB version and cluster details:

```shell
#
# Welcome to the CockroachDB SQL shell.
# All statements must be terminated by a semicolon.
# To exit, type: \q.
#
# Server version: CockroachDB CCL v25.1.0 (x86_64-apple-darwin17.7.0, built 2019/09/13 00:07:19, go1.12.6) (same version as client)
# Cluster ID: 7fb9f5b4-a801-4851-92e9-c0db292d03f1
#
# Enter \? for a brief introduction.
#

```

The **Version** and **Cluster ID** details are particularly noteworthy:

- When the client and server versions of CockroachDB are the same, the shell prints the `Server version` followed by `(same version as client)`.
- When the client and server versions are different, the shell prints both the `Client version` and `Server version`. In this case, you may want to [plan an upgrade](https://www.cockroachlabs.com/docs/v25.1/upgrade-cockroach-version) of older client or server versions.
- Since every CockroachDB cluster has a unique ID, you can use the `Cluster ID` field to verify that your client is always connecting to the correct cluster.



Note:



For clusters deployed in CockroachDB Cloud, do not use the cluster ID printed in the welcome message to verify the cluster your client is connected to. Instead, use the `ccloud cluster list` command to list the ID of each cluster in your CockroachDB Cloud organization to which you have access. To learn more about the `ccloud` command, refer to [Get Started with the `ccloud` CLI](https://www.cockroachlabs.com/docs/cockroachcloud/ccloud-get-started).


### Commands [Anchor link for: commands](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql\#commands)

The following commands can be used within the interactive SQL shell:

| Command | Usage |
| --- | --- |
| `\?`, `help` | View this help within the shell. |
| `\q`, `quit`, `exit`, `ctrl-d` | Exit the shell.<br>When no text follows the prompt, `ctrl-c` exits the shell as well; otherwise, `ctrl-c` clears the line. |
| `\!` | Run an external command and print its results to `stdout`. [See an example](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#run-external-commands-from-the-sql-shell). |
| `\|` | Run the output of an external command as SQL statements. [See an example](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#run-external-commands-from-the-sql-shell). |
| `\set <option>`, `\unset <option>` | Enable or disable a client-side option. For more details, see [Client-side options](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#client-side-options).<br>You can also use the [`--set` flag](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#general) to enable or disable client-side options before starting the SQL shell. |
| `\p`, `\show` | During a multi-line statement or transaction, show the SQL that has been entered but not yet executed.<br>`\show` was deprecated as of v21.1. Use `\p` instead. |
| `\h <statement>`, `\hf <function>` | View help for specific SQL statements or functions. See [SQL shell help](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#help) for more details. |
| `\c <option>`, `\connect <option>` | Display or change the current [connection parameters](https://www.cockroachlabs.com/docs/v25.1/connection-parameters). Using `\c` without an argument lists the current connection parameters. <br>To reuse the existing connection and change the current database, use `\c <dbname>`. This is equivalent to `SET <database>` and `USE <database>`. <br>To connect to a cluster using individual connection parameters, use `\c <dbname> <user> <host> <port>`. Use the dash character ( `-`) to omit one parameter. To reconnect to the cluster using the current connection parameters enter `\c -`. When using individual connection parameters, the TLS settings from the original connection are reused. To use different TLS settings, connect using a connection URL. <br>To connect to a cluster using a [connection URL](https://www.cockroachlabs.com/docs/v25.1/connection-parameters#connect-using-a-url) use `\c <url>` |
| `\l` | List all databases in the CockroachDB cluster. This command is equivalent to [`SHOW DATABASES`](https://www.cockroachlabs.com/docs/v25.1/show-databases). |
| `\d[S+] [<pattern>]` | Show details about the relations in the current database. By default this command will show all the user tables, indexes, views, materialized views, and sequences in the current database. Add the `S` modifier to also show all system objects. If you specify a relation or a [pattern](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#patterns), it will show the details of matching relations. Add the `+` modifier to show additional information. |
| `\dC[+] [<pattern>]` | Show the type casts. If you specify a type or a [pattern](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#patterns), it will show the details of matching types. Add the `+` modifier to show additional information. |
| `\dd[S] [<pattern>]` | Show the objects of type `constraint` in the current database. Add the `S` modifier to also show all system objects. If you specify a type or a [pattern](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#patterns), it will show the details of matching objects. |
| `\df[S+] [<pattern>]` | Show the [user-defined functions](https://www.cockroachlabs.com/docs/v25.1/user-defined-functions) of the current database. Add the `S` modifier to also show all [system functions](https://www.cockroachlabs.com/docs/v25.1/functions-and-operators). If you specify a function name or a [pattern](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#patterns), it will show the details of matching function. Add the `+` modifier to show additional information. |
| `\dg[S+] [<pattern>]` | Show the [roles](https://www.cockroachlabs.com/docs/v25.1/authorization) of the current database. Add the `S` modifier to also show all system objects. If you specify a role name or a [pattern](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#patterns), it will show the details of matching roles. Add the `+` modifier to show additional information. |
| `\di[S+] [<pattern>]` | Show the indexes of the current database. Add the `S` modifier to also show all system objects. If you specify an index name or a [pattern](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#patterns), it will show the details of matching indexes. Add the `+` modifier to show additional information. |
| `\dm[S+] [<pattern>]` | Show the materialized views of the current database. Add the `S` modifier to also show all system objects. If you specify a materialized view name or a [pattern](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#patterns), it will show the details of matching materialized views. Add the `+` modifier to show additional information. |
| `\dn[S+] [<pattern>]` | List all [schemas](https://www.cockroachlabs.com/docs/v25.1/sql-name-resolution#naming-hierarchy) in the current database. Add the `S` modifier to also show all system schemas. Add the `+` modifier to show the permissions of each schema. Specify a [pattern](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#patterns) to limit the output to schemas that match the pattern. These commands are equivalent to [`SHOW SCHEMAS`](https://www.cockroachlabs.com/docs/v25.1/show-schemas). |
| `\ds[S+] [<pattern>]` | Show the sequences of the current database. Add the `S` modifier to also show all system objects. If you specify a sequence name or a [pattern](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#patterns), it will show the details of matching sequences. Add the `+` modifier to show additional information. |
| `\dt[S+] [<pattern>]` | Show the tables of the current database. Add the `S` modifier to also show all system objects. If you specify a table name or a [pattern](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#patterns), it will show the details of matching tables. Add the `+` modifier to show additional information. |
| `\dT[S+] [<pattern>]` | Show the [user-defined types](https://www.cockroachlabs.com/docs/v25.1/enum) in the current database. Add the `S` modifier to also show all system objects. If you specify a type name or a [pattern](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#patterns), it will show the details of matching types. Add the `+` modifier to show additional information. |
| `\du[S+] [<pattern>]` | Show the [roles](https://www.cockroachlabs.com/docs/v25.1/authorization) of the current database. Add the `S` modifier to also show all system objects. If you specify a role name or a [pattern](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#patterns), it will show the details of matching roles. Add the `+` modifier to show additional information. |
| `\dv[S+] [<pattern>]` | Show the views of the current database. Add the `S` modifier to also show all system objects. If you specify a view name or a [pattern](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#patterns), it will show the details of matching views. Add the `+` modifier to show additional information. |
| `\r` | Resets the query input buffer, clearing all SQL statements that have been entered but not yet executed. |
| `\statement-diag list` | List available [diagnostic bundles](https://www.cockroachlabs.com/docs/v25.1/cockroach-statement-diag). |
| `\statement-diag download <bundle-id> [<filename>]` | Download diagnostic bundle. |
| `\i <filename>` | Reads and executes input from the file `<filename>`, in the current working directory. |
| `\ir <filename>` | Reads and executes input from the file `<filename>`.<br>When invoked in the interactive shell, `\i` and `\ir` behave identically (i.e., CockroachDB looks for `<filename>` in the current working directory). When invoked from a script, CockroachDB looks for `<filename>` relative to the directory in which the script is located. |
| `\echo <arguments>` | Evaluate the `<arguments>` and print the results to the standard output. |
| `\x <boolean>` | When `true`/ `on`/ `yes`/ `1`, [sets the display format](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#sql-flag-format) to `records`. When `false`/ `off`/ `no`/ `0`, sets the session's format to the default ( `table`/ `tsv`). |

#### Patterns [Anchor link for: patterns](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql\#patterns)

Commands use the SQL [`LIKE` syntax](https://www.cockroachlabs.com/docs/v25.1/scalar-expressions#string-pattern-matching) for string pattern matching, not POSIX regular expressions.

For example to list all schemas that begin with the letter "p" you'd use the following pattern:

icon/buttons/copy

```sql
\dn p%

```

```
List of schemas:
      Name     | Owner
---------------+--------
  pg_catalog   | NULL
  pg_extension | NULL
  public       | admin
(3 rows)

```

### Client-side options [Anchor link for: client side options](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql\#client-side-options)

- To view option descriptions and how they are currently set, use `\set` without any options.
- To enable or disable an option, use `\set <option> <value>` or `\unset <option> <value>`. You can also use the form `<option>=<value>`.
- If an option accepts a boolean value:

  - `\set <option>` without `<value>` is equivalent to `\set <option> true`, and `\unset <option>` without `<value>` is equivalent to `\set <option> false`.
  - `on`, `yes`, and `1` are aliases for `true`, and `off`, `no`, and `0` are aliases for `false`.

| Client Options | Description |
| --- | --- |
| `auto_trace` | For every statement executed, the shell also produces the trace for that statement in a separate result below. A trace is also produced in case the statement produces a SQL error.<br>**Default:** `off`<br>To enable this option, run `\set auto_trace on`. |
| `border` | Display a border around the output of the SQL statement when using the `table` display format. Set the level of borders using `border=<level>` to configure how many borders and lines are in the output, where `<level>` is an integer between 0 and 3. The higher the integer, the more borders and lines are in the output. <br>A level of `0` shows the output with no outer lines and no row line separators. <br>A level of `1` adds row line separators. A level of `2` adds an outside border and no row line separators. A level of `3` adds both an outside border and row line separators. <br>**Default:** `0`<br>To change this option, run `\set border=<level>`. [See an example](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#show-borders-around-the-statement-output-within-the-sql-shell). |
| `check_syntax` | Validate SQL syntax. This ensures that a typo or mistake during user entry does not inconveniently abort an ongoing transaction previously started from the interactive shell.<br>**Default:** `true` for [interactive sessions](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#session-and-output-types); `false` otherwise.<br>To disable this option, run `\unset check_syntax`. |
| `display_format` | How to display table rows printed within the interactive SQL shell. Possible values: `tsv`, `csv`, `table`, `raw`, `records`, `sql`, `html`.<br>**Default:** `table` for sessions that [output on a terminal](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#session-and-output-types); `tsv` otherwise<br>To change this option, run `\set display_format <format>`. [See an example](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#make-the-output-of-show-statements-selectable). |
| `echo` | Reveal the SQL statements sent implicitly by the SQL shell.<br>**Default:** `false`<br>To enable this option, run `\set echo`. [See an example](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#reveal-the-sql-statements-sent-implicitly-by-the-command-line-utility). |
| `errexit` | Exit the SQL shell upon encountering an error.<br>**Default:** `false` for [interactive sessions](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#session-and-output-types); `true` otherwise<br>To enable this option, run `\set errexit`. |
| `prompt1` | Customize the interactive prompt within the SQL shell. See [Customizing the prompt](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#customizing-the-prompt) for information on the available prompt variables. |
| `show_times` | Reveal the time a query takes to complete. Possible values:<br>- `execution` time refers to the time taken by the SQL execution engine to execute the query.<br>- `network` time refers to the network latency between the server and the SQL client command.<br>- `other` time refers to all other forms of latency affecting the total query completion time, including query planning.<br>**Default:** `true`<br>To disable this option, run `\unset show_times`. |

#### Customizing the prompt [Anchor link for: customizing the prompt](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql\#customizing-the-prompt)

The `\set prompt1` option allows you to customize the interactive prompt in the SQL shell. Use the following prompt variables to set a custom prompt.

| Prompt variable | Description |
| --- | --- |
| `%>` | The port of the node you are connected to. |
| `%/` | The current database name. |
| `%M` | The fully qualified host name and port of the node. |
| `%m` | The fully qualified host name of the node. |
| `%n` | The username of the connected SQL user. |
| `%x` | The transaction status of the current statement. |

For example, to change the prompt to just the user, host, and database:

icon/buttons/copy

```sql
\set prompt1 %n@%m/%/

```

```
maxroach@blue-dog-595.g95.cockroachlabs.cloud/defaultdb>

```

### Help [Anchor link for: help](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql\#help)

Within the SQL shell, you can get interactive help about statements and functions:

| Command | Usage |
| --- | --- |
| `\h`<br>`??` | List all available SQL statements, by category. |
| `\hf` | List all available SQL functions, in alphabetical order. |
| `\h <statement>`<br>`<statement> ?` | View help for a specific SQL statement. |
| `\hf <function>`<br>`<function> ?` | View help for a specific SQL function. |

#### Examples [Anchor link for: examples](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql\#examples)

```sql
\h UPDATE

```

```
Command:     UPDATE
Description: update rows of a table
Category:    data manipulation
Syntax:
UPDATE <tablename> [[AS] <name>] SET ... [WHERE <expr>] [RETURNING <exprs...>]

See also:
  SHOW TABLES
  INSERT
  UPSERT
  DELETE
  https://www.cockroachlabs.com/docs/v25.1/update.html

```

```sql
\hf uuid_v4

```

```
Function:    uuid_v4
Category:    built-in functions
Returns a UUID.

Signature          Category
uuid_v4() -> bytes [ID Generation]

See also:
  https://www.cockroachlabs.com/docs/v25.1/functions-and-operators.html

```

### Shortcuts [Anchor link for: shortcuts](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql\#shortcuts)

Note: macOS users may need to manually enable Alt-based shortcuts in their terminal configuration. See the section [macOS terminal configuration](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#macos-terminal-configuration) below for details.

| Shortcut | Description |
| --- | --- |
| Tab | Use [context-sensitive command completion](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#tab-completion). |
| Ctrl+C | Clear/cancel the input. |
| Ctrl+M, Enter | New line/enter. |
| Ctrl+O | Force a new line on the current statement, even if the statement has a semicolon. |
| Ctrl+F, Right arrow | Forward one character. |
| Ctrl+B, Left arrow | Backward one character. |
| Alt+F, Ctrl+Right arrow | Forward one word. |
| Alt+B, Ctrl+Left arrow | Backward one word. |
| Ctrl+L | Refresh the display. |
| Delete | Delete the next character. |
| Ctrl+H, Backspace | Delete the previous character. |
| Ctrl+D | Delete the next character, or terminate the input if the input is currently empty. |
| Alt+D, Alt+Delete | Delete next word. |
| Ctrl+W, Alt+Backspace | Delete previous word. |
| Ctrl+E, End | End of line. |
| Alt+>, Ctrl+End | Move cursor to the end of a multi-line statement. |
| Ctrl+A, Home | Move cursor to the beginning of the current line. |
| Alt+<, Ctrl+Home | Move cursor to the beginning of a multi-line statement. |
| Ctrl+T | Transpose current and next characters. |
| Ctrl+K | Delete from cursor position until end of line. |
| Ctrl+U | Delete from beginning of line to cursor position. |
| Alt+Q | Reflow/reformat the current line. |
| Alt+Shift+Q, Alt+\` | Reflow/reformat the entire input. |
| Alt+L | Convert the current word to lowercase. |
| Alt+U | Convert the current word to uppercase. |
| Alt+. | Toggle the visibility of the prompt. |
| Alt+2, Alt+F2 | Invoke external editor on current input. |
| Alt+P, Up arrow | Recall previous history entry. |
| Alt+N, Down arrow | Recall next history entry. |
| Ctrl+R | Start searching through input history. |

When searching for history entries, the following shortcuts are active:

| Shortcut | Description |
| --- | --- |
| Ctrl+C, Ctrl+G | Cancel the search, return to normal mode. |
| Ctrl+R | Recall next entry matching current search pattern. |
| Enter | Accept the current recalled entry. |
| Backspace | Delete previous character in search pattern. |
| Other | Add character to search pattern. |

#### Tab completion [Anchor link for: tab completion](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql\#tab-completion)

The SQL client offers context-sensitive tab completion when entering commands. Use the **Tab** key on your keyboard when entering a command to initiate the command completion interface. You can then navigate to database objects, keywords, and functions using the arrow keys. Press the **Tab** key again to select the object, function, or keyword from the command completion interface and return to the console.

### macOS terminal configuration [Anchor link for: macos terminal configuration](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql\#macos-terminal-configuration)

In **Apple Terminal**:

1. Navigate to "Preferences", then "Profiles", then "Keyboard".
2. Enable the checkbox "Use Option as Meta Key".

![Apple Terminal Alt key configuration](https://www.cockroachlabs.com/docs/images/v24.2/terminal-configuration.png)

In **iTerm2**:

1. Navigate to "Preferences", then "Profiles", then "Keys".
2. Select the radio button "Esc+" for the behavior of the Left Option Key.

![iTerm2 Alt key configuration](https://www.cockroachlabs.com/docs/images/v24.2/iterm2-configuration.png)

### Error messages and `SQLSTATE` codes [Anchor link for: error messages and sqlstate codes](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql\#error-messages-and-sqlstate-codes)

When CockroachDB encounters a SQL error, it returns the following information to the client (whether `cockroach-sql` or another [client application](https://www.cockroachlabs.com/docs/v25.1/developer-guide-overview)):

1. An error message, prefixed with [the "Severity" field of the PostgreSQL wire protocol](https://www.postgresql.org/docs/current/protocol-error-fields.html). For example, `ERROR: insert on table "shipments" violates foreign key constraint "fk_customers"`.
2. A [5-digit `SQLSTATE` error code](https://wikipedia.org/wiki/SQLSTATE) as defined by the SQL standard. For example, `SQLSTATE: 23503`.

For example, the following query (taken from [this example of adding multiple foreign key constraints](https://www.cockroachlabs.com/docs/v25.1/foreign-key#add-multiple-foreign-key-constraints-to-a-single-column)) results in a SQL error, and returns both an error message and a `SQLSTATE` code as described above.

icon/buttons/copy

```sql
INSERT INTO shipments (carrier, status, customer_id) VALUES ('DHL', 'At facility', 2000);

```

```
ERROR: insert on table "shipments" violates foreign key constraint "fk_customers"
SQLSTATE: 23503
DETAIL: Key (customer_id)=(2000) is not present in table "customers".

```

The [`SQLSTATE` code](https://wikipedia.org/wiki/SQLSTATE) in particular can be helpful in the following ways:

- It is a standard SQL error code that you can look up in documentation and search for on the web. For any given error state, CockroachDB tries to produce the same `SQLSTATE` code as PostgreSQL.
- If you are developing automation that uses the CockroachDB SQL shell, it is more reliable to check for `SQLSTATE` values than for error message strings, which are likely to change.

## Examples [Anchor link for: examples](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql\#examples)

### Start a SQL shell [Anchor link for: start a sql shell](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql\#start-a-sql-shell)

In these examples, we connect a SQL shell to a **secure cluster**.

icon/buttons/copy

```shell
# Using the --url flag:
cockroach-sql \
--url="postgresql://maxroach@12.345.67.89:26257/critterdb?sslcert=certs/client.maxroach.crt&sslkey=certs/client.maxroach.key&sslmode=verify-full&sslrootcert=certs/ca.crt"

```

icon/buttons/copy

```shell
# Using standard connection flags:
cockroach-sql \
--certs-dir=certs \
--user=maxroach \
--host=12.345.67.89 \
--database=critterdb

```

In these examples, we connect a SQL shell to an **insecure cluster**.

icon/buttons/copy

```shell
# Using the --url flag:
cockroach-sql \
--url="postgresql://maxroach@12.345.67.89:26257/critterdb?sslmode=disable"

```

icon/buttons/copy

```shell
# Using standard connection flags:
cockroach-sql --insecure \
--user=maxroach \
--host=12.345.67.89 \
--database=critterdb

```

### Execute SQL statement within the SQL shell [Anchor link for: execute sql statement within the sql shell](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql\#execute-sql-statement-within-the-sql-shell)

This example assumes that we have already started the SQL shell (see examples above).

icon/buttons/copy

```sql
CREATE TABLE animals (id INT PRIMARY KEY DEFAULT unique_rowid(), name STRING);

```

icon/buttons/copy

```sql
INSERT INTO animals (name) VALUES ('bobcat'), ('🐢 '), ('barn owl');

```

icon/buttons/copy

```sql
SELECT * FROM animals;

```

```
          id         |   name
---------------------+-----------
  710907071259213825 | bobcat
  710907071259279361 | 🐢
  710907071259312129 | barn owl
(3 rows)

```

### Execute SQL statements from the command line [Anchor link for: execute sql statements from the command line](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql\#execute-sql-statements-from-the-command-line)

In these examples, we use the `--execute` flag to execute statements from the command line:

icon/buttons/copy

```shell
# Statements with a single --execute flag:
cockroach-sql --insecure \
--execute="CREATE TABLE roaches (name STRING, country STRING); INSERT INTO roaches VALUES ('American Cockroach', 'United States'), ('Brownbanded Cockroach', 'United States')" \
--user=maxroach \
--host=12.345.67.89 \
--database=critterdb

```

```
CREATE TABLE
INSERT 2

```

icon/buttons/copy

```shell
# Statements with multiple --execute flags:
cockroach-sql --insecure \
--execute="CREATE TABLE roaches (name STRING, country STRING)" \
--execute="INSERT INTO roaches VALUES ('American Cockroach', 'United States'), ('Brownbanded Cockroach', 'United States')" \
--user=maxroach \
--host=12.345.67.89 \
--database=critterdb

```

```
CREATE TABLE
INSERT 2

```

In this example, we use the `echo` command to execute statements from the command line:

icon/buttons/copy

```shell
# Statements with the echo command:
echo "SHOW TABLES; SELECT * FROM roaches;" | cockroach-sql --insecure --user=maxroach --host=12.345.67.89 --database=critterdb

```

```
  schema_name | table_name | type  | owner | estimated_row_count | locality
--------------+------------+-------+-------+---------------------+-----------
  public      | animals    | table | demo  |                   0 | NULL
  public      | roaches    | table | demo  |                   0 | NULL
(2 rows)

          name          |    country
------------------------+----------------
  American Cockroach    | United States
  Brownbanded Cockroach | United States

```

### Control how table rows are printed [Anchor link for: control how table rows are printed](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql\#control-how-table-rows-are-printed)

In these examples, we show tables and special characters printed in various formats.

When the standard output is a terminal, `--format` defaults to `table` and tables are printed with ASCII art and special characters are not escaped for easy human consumption:

icon/buttons/copy

```shell
cockroach-sql --insecure \
--execute="SELECT '🐥' AS chick, '🐢' AS turtle" \
--user=maxroach \
--host=12.345.67.89 \
--database=critterdb

```

```
  chick | turtle
--------+---------
  🐥    | 🐢

```

However, you can explicitly set `--format` to another format (e.g., `tsv` or `html`):

icon/buttons/copy

```shell
cockroach-sql --insecure \
--format=tsv \
--execute="SELECT '🐥' AS chick, '🐢' AS turtle" \
--user=maxroach \
--host=12.345.67.89 \
--database=critterdb

```

```
chick   turtle
🐥    🐢

```

icon/buttons/copy

```shell
cockroach-sql --insecure \
--format=html \
--execute="SELECT '🐥' AS chick, '🐢' AS turtle" \
--user=maxroach \
--host=12.345.67.89 \
--database=critterdb

```

```
<table>
<thead><tr><th>row</th><th>chick</th><th>turtle</th></tr></thead>
<tbody>
<tr><td>1</td><td>🐥</td><td>🐢</td></tr>
</tbody>
<tfoot><tr><td colspan=3>1 row</td></tr></tfoot></table>

```

When piping output to another command or a file, `--format` defaults to `tsv`:

icon/buttons/copy

```shell
cockroach-sql --insecure \
--execute="SELECT '🐥' AS chick, '🐢' AS turtle" > out.txt \
--user=maxroach \
--host=12.345.67.89 \
--database=critterdb

```

icon/buttons/copy

```shell
cat out.txt

```

```
1 row
chick   turtle
🐥    🐢

```

However, you can explicitly set `--format` to another format (e.g., `table`):

icon/buttons/copy

```shell
cockroach-sql --insecure \
--format=table \
--execute="SELECT '🐥' AS chick, '🐢' AS turtle" > out.txt \
--user=maxroach \
--host=12.345.67.89 \
--database=critterdb

```

icon/buttons/copy

```shell
cat out.txt

```

```
  chick | turtle
--------+---------
  🐥    | 🐢
(1 row)

```

### Show borders around the statement output within the SQL shell [Anchor link for: show borders around the statement output within the sql shell](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql\#show-borders-around-the-statement-output-within-the-sql-shell)

To display outside and inside borders in the statement output, set the `border` [SQL shell option](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#client-side-options) to `3`.

icon/buttons/copy

```sql
\set border=3
SELECT * FROM animals;

```

```
+--------------------+----------+
|         id         |   name   |
+--------------------+----------+
| 710907071259213825 | bobcat   |
+--------------------+----------+
| 710907071259279361 | 🐢       |
+--------------------+----------+
| 710907071259312129 | barn owl |
+--------------------+----------+

```

### Make the output of `SHOW` statements selectable [Anchor link for: make the output of show statements selectable](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql\#make-the-output-of-show-statements-selectable)

To make it possible to select from the output of `SHOW` statements, set `--format` to `raw`:

icon/buttons/copy

```shell
cockroach-sql --insecure \
--format=raw \
--user=maxroach \
--host=12.345.67.89 \
--database=critterdb

```

icon/buttons/copy

```sql
SHOW CREATE customers;

```

```
# 2 columns
# row 1
## 14
test.customers
## 185
CREATE TABLE customers (
    id INT NOT NULL,
    email STRING NULL,
    CONSTRAINT "primary" PRIMARY KEY (id ASC),
    UNIQUE INDEX customers_email_key (email ASC),
    FAMILY "primary" (id, email)
)
# 1 row

```

When `--format` is not set to `raw`, you can use the `display_format` [SQL shell option](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#client-side-options) to change the output format within the interactive session:

icon/buttons/copy

```sql
\set display_format raw

```

```
# 2 columns
# row 1
## 14
test.customers
## 185
CREATE TABLE customers (
  id INT NOT NULL,
  email STRING NULL,
  CONSTRAINT "primary" PRIMARY KEY (id ASC),
  UNIQUE INDEX customers_email_key (email ASC),
  FAMILY "primary" (id, email)
)
# 1 row

```

### Execute SQL statements from a file [Anchor link for: execute sql statements from a file](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql\#execute-sql-statements-from-a-file)

In this example, we show and then execute the contents of a file containing SQL statements.

icon/buttons/copy

```shell
cat statements.sql

```

```
CREATE TABLE roaches (name STRING, country STRING);
INSERT INTO roaches VALUES ('American Cockroach', 'United States'), ('Brownbanded Cockroach', 'United States');

```

icon/buttons/copy

```shell
cockroach-sql --insecure \
--user=maxroach \
--host=12.345.67.89 \
--database=critterdb \
-f statements.sql

```

```
CREATE TABLE
INSERT 2

```

### Run external commands from the SQL shell [Anchor link for: run external commands from the sql shell](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql\#run-external-commands-from-the-sql-shell)

In this example, we use `\!` to look at the rows in a CSV file before creating a table and then using `\|` to insert those rows into the table.

Note:

This example works only if the values in the CSV file are numbers. For values in other formats, use an online CSV-to-SQL converter or make your own import program.

icon/buttons/copy

```sql
\! cat test.csv

```

```
12, 13, 14
10, 20, 30

```

icon/buttons/copy

```sql
CREATE TABLE csv (x INT, y INT, z INT);

```

icon/buttons/copy

```sql
\| IFS=","; while read a b c; do echo "insert into csv values ($a, $b, $c);"; done < test.csv;

```

icon/buttons/copy

```sql
SELECT * FROM csv;

```

```
  x  | y  | z
-----+----+-----
  12 | 13 | 14
  10 | 20 | 30

```

In this example, we create a table and then use `\|` to programmatically insert values.

icon/buttons/copy

```sql
CREATE TABLE for_loop (x INT);

```

icon/buttons/copy

```sql
\| for ((i=0;i<10;++i)); do echo "INSERT INTO for_loop VALUES ($i);"; done

```

icon/buttons/copy

```sql
SELECT * FROM for_loop;

```

```
  x
-----
  0
  1
  2
  3
  4
  5
  6
  7
  8
  9

```

### Allow potentially unsafe SQL statements [Anchor link for: allow potentially unsafe sql statements](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql\#allow-potentially-unsafe-sql-statements)

The `--safe-updates` flag defaults to `true`. This prevents SQL statements that may have broad, undesired side effects. For example, by default, we cannot use `DELETE` without a `WHERE` clause to delete all rows from a table:

icon/buttons/copy

```shell
cockroach-sql --insecure --execute="SELECT * FROM db1.t1"

```

```
  id | name
-----+-------
   1 | a
   2 | b
   3 | c
   4 | d
   5 | e
   6 | f
   7 | g
   8 | h
   9 | i
  10 | j
-----+-------
(10 rows)

```

icon/buttons/copy

```shell
cockroach-sql --insecure --execute="DELETE FROM db1.t1"

```

```
Error: pq: rejected: DELETE without WHERE clause (sql_safe_updates = true)
Failed running "sql"

```

However, to allow an "unsafe" statement, you can set `--safe-updates=false`:

icon/buttons/copy

```shell
cockroach-sql --insecure --safe-updates=false --execute="DELETE FROM db1.t1"

```

```
DELETE 10

```

Note:

Potentially unsafe SQL statements can also be allowed/disallowed for an entire session via the `sql_safe_updates` [session variable](https://www.cockroachlabs.com/docs/v25.1/set-vars).

### Reveal the SQL statements sent implicitly by the command-line utility [Anchor link for: reveal the sql statements sent implicitly by the command line utility](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql\#reveal-the-sql-statements-sent-implicitly-by-the-command-line-utility)

In this example, we use the `--execute` flag to execute statements from the command line and the `--echo-sql` flag to reveal SQL statements sent implicitly:

icon/buttons/copy

```shell
cockroach-sql --insecure \
--execute="CREATE TABLE t1 (id INT PRIMARY KEY, name STRING)" \
--execute="INSERT INTO t1 VALUES (1, 'a'), (2, 'b'), (3, 'c')" \
--user=maxroach \
--host=12.345.67.89 \
--database=db1
--echo-sql

```

```
# Server version: CockroachDB CCL f8f3c9317 (darwin amd64, built 2017/09/13 15:05:35, go1.8) (same version as client)
# Cluster ID: 847a4ba5-c78a-465a-b1a0-59fae3aab520
> SET sql_safe_updates = TRUE
> CREATE TABLE t1 (id INT PRIMARY KEY, name STRING)
CREATE TABLE
> INSERT INTO t1 VALUES (1, 'a'), (2, 'b'), (3, 'c')
INSERT 3

```

In this example, we start the interactive SQL shell and enable the `echo` shell option to reveal SQL statements sent implicitly:

icon/buttons/copy

```shell
cockroach-sql --insecure \
--user=maxroach \
--host=12.345.67.89 \
--database=db1

```

icon/buttons/copy

```sql
\set echo

```

icon/buttons/copy

```sql
INSERT INTO db1.t1 VALUES (4, 'd'), (5, 'e'), (6, 'f');

```

```
> INSERT INTO db1.t1 VALUES (4, 'd'), (5, 'e'), (6, 'f');
INSERT 3

Time: 2.426534ms

> SHOW TRANSACTION STATUS
> SHOW DATABASE

```

### Repeat a SQL statement [Anchor link for: repeat a sql statement](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql\#repeat-a-sql-statement)

Repeating SQL queries on a table can be useful for monitoring purposes. With the `--watch` flag, you can repeat the statements specified with a `--execute` or `-e` flag periodically, until a SQL error occurs or the process is terminated.

For example, if you want to monitor the number of queries running on the current node, you can use `cockroach-sql` with the `--watch` flag to query the node's `crdb_internal.node_statement_statistics` table for the query count:

icon/buttons/copy

```shell
cockroach-sql --insecure \
--execute="SELECT SUM(count) FROM crdb_internal.node_statement_statistics" \
--watch 1m

```

```
  sum
-------
  926
(1 row)
  sum
--------
  4227
(1 row)
^C

```

In this example, the statement is executed every minute. We let the process run for a couple minutes before terminating it with **Ctrl+C**.

### Connect to a cluster listening for Unix domain socket connections [Anchor link for: connect to a cluster listening for unix domain socket connections](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql\#connect-to-a-cluster-listening-for-unix-domain-socket-connections)

To connect to a cluster that is running on the same machine as your client and is listening for [Unix domain socket](https://wikipedia.org/wiki/Unix_domain_socket) connections, [specify a Unix domain socket URI](https://www.cockroachlabs.com/docs/v25.1/connection-parameters#example-uri-for-a-unix-domain-socket) with the `--url` connection parameter.

For example, suppose you start a single-node cluster with the following [`cockroach start-single-node`](https://www.cockroachlabs.com/docs/v25.1/cockroach-start-single-node) command:

icon/buttons/copy

```shell
cockroach start-single-node --insecure --socket-dir=/tmp

```

```
CockroachDB node starting at  (took 1.3s)
build:               CCL v25.1.0 @ 2025-02-18 00:00:00
webui:               http://Jesses-MBP-2:8080
sql:                 postgresql://root@Jesses-MBP-2:26257?sslmode=disable
RPC client flags:    ./cockroach <client cmd> --host=Jesses-MBP-2:26257 --insecure
socket:              /tmp/.s.PGSQL.26257
logs:                /Users/jesseseldess/Downloads/cockroach-.darwin-10.9-amd64/cockroach-data/logs
temp dir:            /Users/jesseseldess/Downloads/cockroach-.darwin-10.9-amd64/cockroach-data/cockroach-temp805054895
external I/O path:   /Users/jesseseldess/Downloads/cockroach-.darwin-10.9-amd64/cockroach-data/extern
store[0]:            path=/Users/jesseseldess/Downloads/cockroach-.darwin-10.9-amd64/cockroach-data
storage engine:      pebble
status:              initialized new cluster
clusterID:           455ad71d-21d4-424a-87ad-8097b6b5b99f
nodeID:              1

```

To connect to this cluster with a socket:

icon/buttons/copy

```shell
cockroach-sql --url='postgres://root@?host=/tmp&port=26257'

```

## See also [Anchor link for: see also](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql\#see-also)

- [Client Connection Parameters](https://www.cockroachlabs.com/docs/v25.1/connection-parameters)
- [`cockroach demo`](https://www.cockroachlabs.com/docs/v25.1/cockroach-demo)
- [`cockroach` Commands Overview](https://www.cockroachlabs.com/docs/v25.1/cockroach-commands)
- [SQL Statements](https://www.cockroachlabs.com/docs/v25.1/sql-statements)
- [Learn CockroachDB SQL](https://www.cockroachlabs.com/docs/v25.1/learn-cockroachdb-sql)

Was this helpful?

[![Yes](https://www.cockroachlabs.com/docs/images/icon-thumbs-up.svg)](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#yes-feedback)[![No](https://www.cockroachlabs.com/docs/images/icon-thumbs-down.svg)](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#no-feedback)

Contribute
![Carat arrow pointing down](https://www.cockroachlabs.com/docs/images/carat-down-fill.svg)

- [View Page Source](https://github.com/cockroachdb/docs/tree/main/src/current/v25.1/cockroach-sql.md)
- [Edit This Page](https://github.com/cockroachdb/docs/edit/main/src/current/v25.1/cockroach-sql.md)
- [Report Doc Issue](https://github.com/cockroachdb/docs/issues/new?title=Feedback:%20cockroach%20sql&body=Page%3A%20https%3A%2F%2Fcockroachlabs.com/docs/v25.1/cockroach-sql.html%0A%0A%23%23%20What%20is%20the%20reason%20for%20your%20feedback?%0A%0A[%20]%20Missing%20the%20information%20I%20need%0A%0A[%20]%20Too%20complicated%0A%0A[%20]%20Out%20of%20date%0A%0A[%20]%20Something%20is%20broken%0A%0A[%20]%20Other%0A%0A%23%23%20Additional%20details&)

On this page

- [Before you begin](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#before-you-begin)
- [Synopsis](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#synopsis)
- [Flags](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#flags)
  - [General](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#general)
  - [Client connection](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#client-connection)
  - [Logging](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#logging)
- [Session and output types](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#session-and-output-types)
- [SQL shell](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#sql-shell)
  - [Welcome message](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#welcome-message)
  - [Commands](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#commands)
  - [Client-side options](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#client-side-options)
  - [Help](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#help)
  - [Shortcuts](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#shortcuts)
  - [macOS terminal configuration](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#macos-terminal-configuration)
  - [Error messages and `SQLSTATE` codes](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#error-messages-and-sqlstate-codes)
- [Examples](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#examples)
  - [Start a SQL shell](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#start-a-sql-shell)
  - [Execute SQL statement within the SQL shell](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#execute-sql-statement-within-the-sql-shell)
  - [Execute SQL statements from the command line](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#execute-sql-statements-from-the-command-line)
  - [Control how table rows are printed](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#control-how-table-rows-are-printed)
  - [Show borders around the statement output within the SQL shell](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#show-borders-around-the-statement-output-within-the-sql-shell)
  - [Make the output of `SHOW` statements selectable](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#make-the-output-of-show-statements-selectable)
  - [Execute SQL statements from a file](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#execute-sql-statements-from-a-file)
  - [Run external commands from the SQL shell](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#run-external-commands-from-the-sql-shell)
  - [Allow potentially unsafe SQL statements](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#allow-potentially-unsafe-sql-statements)
  - [Reveal the SQL statements sent implicitly by the command-line utility](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#reveal-the-sql-statements-sent-implicitly-by-the-command-line-utility)
  - [Repeat a SQL statement](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#repeat-a-sql-statement)
  - [Connect to a cluster listening for Unix domain socket connections](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#connect-to-a-cluster-listening-for-unix-domain-socket-connections)
- [See also](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#see-also)

Was this helpful?

[![Yes](https://www.cockroachlabs.com/docs/images/icon-thumbs-up.svg)](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#yes-feedback)[![No](https://www.cockroachlabs.com/docs/images/icon-thumbs-down.svg)](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#no-feedback)

![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=-1777624096&_biz_u=77c7ed020755477ab749fa2e6cc5a234&_biz_l=https%3A%2F%2Fwww.cockroachlabs.com%2Fdocs%2Fv25.1%2Fcockroach-sql&_biz_t=1740660112491&_biz_i=cockroach%20sql&_biz_n=0&rnd=769425&cdn_o=a&_biz_z=1740660112492)![](https://cdn.bizibly.com/u?_biz_u=77c7ed020755477ab749fa2e6cc5a234&_biz_l=https%3A%2F%2Fwww.cockroachlabs.com%2Fdocs%2Fv25.1%2Fcockroach-sql&_biz_t=1740660112509&_biz_i=cockroach%20sql&rnd=514162&cdn_o=a&_biz_z=1740660112509)[iframe](https://td.doubleclick.net/td/rul/947366135?random=1740660112525&cv=11&fst=1740660112525&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be52o0v897240538za200&gcd=13l3l3l3l1l1&dma=0&tag_exp=101732282~101732284~102067808~102482433~102539968~102558064~102587591~102605417~102640600~102658453~102717421&u_w=1280&u_h=1024&url=https%3A%2F%2Fwww.cockroachlabs.com%2Fdocs%2Fv25.1%2Fcockroach-sql&hn=www.googleadservices.com&frm=0&tiba=cockroach%20sql&npa=0&pscdl=noapi&auid=297768901.1740660112&uaa=&uab=&uafvl=&uamb=0&uam=&uap=&uapv=&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/ga/rul?tid=G-913SQ8GKPR&gacid=1164394387.1740660112&gtm=45je52o0v878753894z872012025za200zb72012025&dma=0&gcd=13l3l3l3l1l1&npa=0&pscdl=noapi&aip=1&fledge=1&frm=0&tag_exp=101732282~101732284~102067808~102482433~102539968~102558064~102587591~102605417~102640600~102658453~102717422&z=851135497)

[iframe](https://www.google.com/recaptcha/enterprise/anchor?ar=1&k=6Lck4YwlAAAAAEIE1hR--varWp0qu9F-8-emQn2v&co=aHR0cHM6Ly93d3cuY29ja3JvYWNobGFicy5jb206NDQz&hl=en&v=rW64dpMGAGrjU7JJQr9xxPl8&size=invisible&cb=eau76mwqimg)

[iframe](https://td.doubleclick.net/td/rul/947366135?random=1740660114180&cv=11&fst=1740660114180&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be52o0v897240538z872012025za200&gcd=13l3l3l3l1l1&dma=0&tag_exp=101732282~101732284~102067808~102482433~102539968~102558064~102587591~102605417~102640600~102658453~102717421&u_w=1280&u_h=1024&url=https%3A%2F%2Fwww.cockroachlabs.com%2Fdocs%2Fv25.1%2Fcockroach-sql&hn=www.googleadservices.com&frm=0&tiba=cockroach%20sql&npa=0&pscdl=noapi&auid=297768901.1740660112&uaa=&uab=&uafvl=&uamb=0&uam=&uap=&uapv=&uaw=0&fledge=1)

# cockroach-sql

Docs Menu


- [Version v25.1.0](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#)  - [v25.1.0\\
       (Stable)](https://www.cockroachlabs.com/docs/stable/cockroach-sql-binary) [v25.1.0\\
       (Stable)](https://www.cockroachlabs.com/docs/stable/cockroach-sql-binary)
  - [v24.3.6](https://www.cockroachlabs.com/docs/v24.3/cockroach-sql-binary) [v24.3.6](https://www.cockroachlabs.com/docs/v24.3/cockroach-sql-binary)
  - [v24.2.10](https://www.cockroachlabs.com/docs/v24.2/cockroach-sql-binary) [v24.2.10](https://www.cockroachlabs.com/docs/v24.2/cockroach-sql-binary)
  - [v24.1.13 LTS](https://www.cockroachlabs.com/docs/v24.1/cockroach-sql-binary) [v24.1.13 LTS](https://www.cockroachlabs.com/docs/v24.1/cockroach-sql-binary)
  - [v23.2.20 LTS](https://www.cockroachlabs.com/docs/v23.2/cockroach-sql-binary) [v23.2.20 LTS](https://www.cockroachlabs.com/docs/v23.2/cockroach-sql-binary)
  - [v23.1.30 LTS](https://www.cockroachlabs.com/docs/v23.1/cockroach-sql-binary) [v23.1.30 LTS](https://www.cockroachlabs.com/docs/v23.1/cockroach-sql-binary)
  - [v22.2.19](https://www.cockroachlabs.com/docs/v22.2/cockroach-sql-binary) [v22.2.19](https://www.cockroachlabs.com/docs/v22.2/cockroach-sql-binary)
  - [v22.1.22](https://www.cockroachlabs.com/docs/v22.1/cockroach-sql-binary) [v22.1.22](https://www.cockroachlabs.com/docs/v22.1/cockroach-sql-binary)
  - v21.2.17



     This page does not exist in v21.2

     v21.2.17


  - v21.1.21



     This page does not exist in v21.1

     v21.1.21


  - v20.2.19



     This page does not exist in v20.2

     v20.2.19


  - v20.1.17



     This page does not exist in v20.1

     v20.1.17


  - v19.2.12



     This page does not exist in v19.2

     v19.2.12


  - v19.1.11



     This page does not exist in v19.1

     v19.1.11


  - v2.1.11



     This page does not exist in v2.1

     v2.1.11


  - v2.0.7



     This page does not exist in v2.0

     v2.0.7


  - v1.1.9



     This page does not exist in v1.1

     v1.1.9


  - v1.0.7



     This page does not exist in v1.0

     v1.0.7

# cockroach-sql

Contribute
![Carat arrow pointing down](https://www.cockroachlabs.com/docs/images/carat-down-fill.svg)

- [View Page Source](https://github.com/cockroachdb/docs/tree/main/src/current/v25.1/cockroach-sql-binary.md)
- [Edit This Page](https://github.com/cockroachdb/docs/edit/main/src/current/v25.1/cockroach-sql-binary.md)
- [Report Doc Issue](https://github.com/cockroachdb/docs/issues/new?title=Feedback:%20cockroach-sql&body=Page%3A%20https%3A%2F%2Fcockroachlabs.com/docs/v25.1/cockroach-sql-binary.html%0A%0A%23%23%20What%20is%20the%20reason%20for%20your%20feedback?%0A%0A[%20]%20Missing%20the%20information%20I%20need%0A%0A[%20]%20Too%20complicated%0A%0A[%20]%20Out%20of%20date%0A%0A[%20]%20Something%20is%20broken%0A%0A[%20]%20Other%0A%0A%23%23%20Additional%20details&)

On this page ![Carat arrow pointing down](https://www.cockroachlabs.com/docs/images/carat-down-fill.svg)

- [Install `cockroach-sql`](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#install-cockroach-sql)
- [Before you begin](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#before-you-begin)
- [Synopsis](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#synopsis)
- [Flags](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#flags)
  - [General](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#general)
  - [Client connection](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#client-connection)
  - [Logging](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#logging)
- [Session and output types](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#session-and-output-types)
- [SQL shell](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#sql-shell)
  - [Welcome message](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#welcome-message)
  - [Commands](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#commands)
  - [Client-side options](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#client-side-options)
  - [Help](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#help)
  - [Shortcuts](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#shortcuts)
  - [macOS terminal configuration](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#macos-terminal-configuration)
  - [Error messages and `SQLSTATE` codes](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#error-messages-and-sqlstate-codes)
- [Examples](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#examples)
  - [Start a SQL shell](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#start-a-sql-shell)
  - [Execute SQL statement within the SQL shell](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#execute-sql-statement-within-the-sql-shell)
  - [Execute SQL statements from the command line](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#execute-sql-statements-from-the-command-line)
  - [Control how table rows are printed](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#control-how-table-rows-are-printed)
  - [Show borders around the statement output within the SQL shell](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#show-borders-around-the-statement-output-within-the-sql-shell)
  - [Make the output of `SHOW` statements selectable](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#make-the-output-of-show-statements-selectable)
  - [Execute SQL statements from a file](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#execute-sql-statements-from-a-file)
  - [Run external commands from the SQL shell](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#run-external-commands-from-the-sql-shell)
  - [Allow potentially unsafe SQL statements](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#allow-potentially-unsafe-sql-statements)
  - [Reveal the SQL statements sent implicitly by the command-line utility](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#reveal-the-sql-statements-sent-implicitly-by-the-command-line-utility)
  - [Repeat a SQL statement](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#repeat-a-sql-statement)
  - [Connect to a cluster listening for Unix domain socket connections](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#connect-to-a-cluster-listening-for-unix-domain-socket-connections)
- [See also](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#see-also)

The `cockroach-sql` command is a client for executing SQL statements from an interactive shell or directly from the command line. To use this client, run `cockroach-sql` as described below.

Note:

`cockroach-sql` is functionally equivalent to the [`cockroach sql` command](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql).

To exit the interactive shell, enter **\\q**, **quit**, **exit**, or **Ctrl+D**.

The output of `cockroach-sql` when used non-interactively is part of a stable interface, and can be used programmatically, with the exception of informational output lines that begin with the hash symbol ( `#`). Informational output can change from release to release, and should not be used programmatically.

## Install `cockroach-sql` [Anchor link for: install cockroach sql](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary\#install-cockroach-sql)

**Mac****Linux****Windows**

1. Visit [Releases](https://www.cockroachlabs.com/docs/releases/) and download the SQL Shell binary for CockroachDB.

1. Follow the instructions to [install CockroachDB](https://www.cockroachlabs.com/docs/v25.1/install-cockroachdb) on your local system. The resulting `cockroach` binary supports only `cockroach sql` subcommands.

1. Follow the instructions to [install CockroachDB](https://www.cockroachlabs.com/docs/v25.1/install-cockroachdb) on your local system. The resulting `cockroach` binary supports only `cockroach sql` subcommands.

1. Follow the instructions to [install CockroachDB](https://www.cockroachlabs.com/docs/v25.1/install-cockroachdb) on your local system. The resulting `cockroach.exe` binary supports only `cockroach sql` subcommands.

## Before you begin [Anchor link for: before you begin](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary\#before-you-begin)

- The [role option of the user](https://www.cockroachlabs.com/docs/v25.1/security-reference/authorization#role-options) logging in must be `LOGIN` or `SQLLOGIN`, which are granted by default. If the user has been set to use the `NOLOGIN` role or the `NOSQLLOGIN` [system privilege](https://www.cockroachlabs.com/docs/v25.1/security-reference/authorization#supported-privileges) (or the legacy `NOSQLLOGIN` role option), the user cannot log in using the SQL CLI with any authentication method.
- **macOS users only:** By default, macOS-based terminals do not enable handling of the Alt key modifier. This prevents access to many keyboard shortcuts in the unix shell and `cockroach sql`. See the section [macOS terminal configuration](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#macos-terminal-configuration) below for details.

## Synopsis [Anchor link for: synopsis](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary\#synopsis)

Start the interactive SQL shell:

```shell
cockroach-sql <flags>

```

Execute SQL from the command line:

icon/buttons/copy

```shell
cockroach-sql -e="<sql statement>;<sql statement>" -e="<sql-statement>" <flags>

```

icon/buttons/copy

```shell
echo "<sql statement>;<sql statement>" | cockroach-sql <flags>

```

icon/buttons/copy

```shell
cockroach-sql <flags> -f file-containing-statements.sql

```

Exit the interactive SQL shell:

```sql
\q

```

View help:

```shell
cockroach-sql --help

```

## Flags [Anchor link for: flags](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary\#flags)

The `sql` command supports the following types of flags:

- [General Use](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#general)
- [Client Connection](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#client-connection)
- [Logging](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#logging)

### General [Anchor link for: general](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary\#general)

- To start an interactive SQL shell, run `cockroach-sql` with all appropriate connection flags or use just the [`--url` flag](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#sql-flag-url), which includes [connection details](https://www.cockroachlabs.com/docs/v25.1/connection-parameters#connect-using-a-url).
- To execute SQL statements from the command line, use the [`--execute` flag](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#sql-flag-execute).

| Flag | Description |
| --- | --- |
| `--database`<br>`-d` | A database name to use as [current database](https://www.cockroachlabs.com/docs/v25.1/sql-name-resolution#current-database) in the newly created session. |
| `--embedded` | Minimizes the SQL shell [welcome text](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#welcome-message) to be appropriate for embedding in playground-type environments. Specifically, this flag removes details that users in an embedded environment have no control over (e.g., networking information). |
| `--echo-sql` | Reveal the SQL statements sent implicitly by the command-line utility. For a demonstration, see the [example](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#reveal-the-sql-statements-sent-implicitly-by-the-command-line-utility) below.<br>This can also be enabled within the interactive SQL shell via the `\set echo` [shell command](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#commands). |
| `--execute`<br>`-e` | Execute SQL statements directly from the command line, without opening a shell. This flag can be set multiple times, and each instance can contain one or more statements separated by semi-colons. If an error occurs in any statement, the command exits with a non-zero status code and further statements are not executed. The results of each statement are printed to the standard output (see `--format` for formatting options).<br>For a demonstration of this and other ways to execute SQL from the command line, see the [example](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#execute-sql-statements-from-the-command-line) below. |
| `--file <filename>`<br>`-f <filename>` | Read SQL statements from `<filename>`. |
| `--format` | How to display table rows printed to the standard output. Possible values: `tsv`, `csv`, `table`, `raw`, `records`, `sql`, `html`.<br>**Default:** `table` for sessions that [output on a terminal](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#session-and-output-types); `tsv` otherwise<br>This flag corresponds to the `display_format` [client-side option](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#client-side-options). |
| `--read-only` | Sets the `default_transaction_read_only` [session variable](https://www.cockroachlabs.com/docs/v25.1/show-vars#supported-variables) to `on` upon connecting. |
| `--safe-updates` | Disallow potentially unsafe SQL statements, including `DELETE` without a `WHERE` clause, `UPDATE` without a `WHERE` clause, and `ALTER TABLE ... DROP COLUMN`.<br>**Default:** `true` for [interactive sessions](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#session-and-output-types); `false` otherwise<br>Potentially unsafe SQL statements can also be allowed/disallowed for an entire session via the `sql_safe_updates` [session variable](https://www.cockroachlabs.com/docs/v25.1/set-vars). |
| `--set` | Set a [client-side option](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#client-side-options) before starting the SQL shell or executing SQL statements from the command line via `--execute`. This flag may be specified multiple times, once per option.<br>After starting the SQL shell, the `\set` and `unset` commands can be use to enable and disable client-side options as well. |
| `--watch` | Repeat the SQL statements specified with `--execute` or `-e` until a SQL error occurs or the process is terminated. `--watch` applies to all `--execute` or `-e` flags in use.<br>You must also specify an interval at which to repeat the statement, followed by a time unit. For example, to specify an interval of 5 seconds, use `5s`.<br> Note that this flag is intended for simple monitoring scenarios during development and testing. See the [example](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#repeat-a-sql-statement) below. |

### Client connection [Anchor link for: client connection](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary\#client-connection)

| Flag | Description |
| --- | --- |
| `--url` | A [connection URL](https://www.cockroachlabs.com/docs/v25.1/connection-parameters#connect-using-a-url) to use instead of the other arguments. To convert a connection URL to the syntax that works with your client driver, run [`cockroach convert-url`](https://www.cockroachlabs.com/docs/v25.1/connection-parameters#convert-a-url-for-different-drivers).<br>**Env Variable:** `COCKROACH_URL`<br>**Default:** no URL |
| `--host` | The server host and port number to connect to. This can be the address of any node in the cluster. <br>**Env Variable:** `COCKROACH_HOST`<br>**Default:** `localhost:26257` |
| `--port`<br>`-p` | The server port to connect to. Note: The port number can also be specified via `--host`. <br>**Env Variable:** `COCKROACH_PORT`<br>**Default:** `26257` |
| `--user`<br>`-u` | The [SQL user](https://www.cockroachlabs.com/docs/v25.1/create-user) that will own the client session.<br>**Env Variable:** `COCKROACH_USER`<br>**Default:** `root` |
| `--insecure` | Use an insecure connection.<br>**Env Variable:** `COCKROACH_INSECURE`<br>**Default:** `false` |
| `--cert-principal-map` | A comma-separated list of `<cert-principal>:<db-principal>` mappings. This allows mapping the principal in a cert to a DB principal such as `node` or `root` or any SQL user. This is intended for use in situations where the certificate management system places restrictions on the `Subject.CommonName` or `SubjectAlternateName` fields in the certificate (e.g., disallowing a `CommonName` like `node` or `root`). If multiple mappings are provided for the same `<cert-principal>`, the last one specified in the list takes precedence. A principal not specified in the map is passed through as-is via the identity function. A cert is allowed to authenticate a DB principal if the DB principal name is contained in the mapped `CommonName` or DNS-type `SubjectAlternateName` fields. |
| `--certs-dir` | The path to the [certificate directory](https://www.cockroachlabs.com/docs/v25.1/cockroach-cert) containing the CA and client certificates and client key.<br>**Env Variable:** `COCKROACH_CERTS_DIR`<br>**Default:** `${HOME}/.cockroach-certs/` |

See [Client Connection Parameters](https://www.cockroachlabs.com/docs/v25.1/connection-parameters) for more details.

### Logging [Anchor link for: logging](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary\#logging)

By default, this command logs messages to `stderr`. This includes events with `WARNING` [severity](https://www.cockroachlabs.com/docs/v25.1/logging#logging-levels-severities) and higher.

If you need to troubleshoot this command's behavior, you can [customize its logging behavior](https://www.cockroachlabs.com/docs/v25.1/configure-logs).

## Session and output types [Anchor link for: session and output types](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary\#session-and-output-types)

`cockroach-sql` exhibits different behaviors depending on whether or not the session is interactive and/or whether or not the session outputs on a terminal.

- A session is **interactive** when `cockroach-sql` is invoked without the `-e` or `-f` flag, and the input is a terminal. In such cases:


  - The [`errexit` option](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#sql-option-errexit) defaults to `false`.
  - The [`check_syntax` option](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#sql-option-check-syntax) defaults to `true` if supported by the CockroachDB server (this is checked when the shell starts up).
  - **Ctrl+C** at the prompt will only terminate the shell if no other input was entered on the same line already.
  - The shell will attempt to set the `safe_updates` [session variable](https://www.cockroachlabs.com/docs/v25.1/set-vars) to `true` on the server.
  - The shell continues to read input after the last command entered.
- A session **outputs on a terminal** when output is not redirected to a file. In such cases:


  - The [`--format` flag](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#sql-flag-format) and its corresponding [`display_format` option](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#sql-option-display-format) default to `table`. These default to `tsv` otherwise.
  - The `show_times` option defaults to `true`.

When a session is both interactive and outputs on a terminal, `cockroach-sql` also activates the interactive prompt with a line editor that can be used to modify the current line of input. Also, command history becomes active.

## SQL shell [Anchor link for: sql shell](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary\#sql-shell)

### Welcome message [Anchor link for: welcome message](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary\#welcome-message)

When the SQL shell connects (or reconnects) to a CockroachDB node, it prints a welcome text with some tips and CockroachDB version and cluster details:

```shell
#
# Welcome to the CockroachDB SQL shell.
# All statements must be terminated by a semicolon.
# To exit, type: \q.
#
# Server version: CockroachDB CCL v25.1.0 (x86_64-apple-darwin17.7.0, built 2025-02-18 00:00:00) (same version as client)
# Cluster ID: 7fb9f5b4-a801-4851-92e9-c0db292d03f1
#
# Enter \? for a brief introduction.
#

```

The **Version** and **Cluster ID** details are particularly noteworthy:

- When the client and server versions of CockroachDB are the same, the shell prints the `Server version` followed by `(same version as client)`.
- When the client and server versions are different, the shell prints both the `Client version` and `Server version`. In this case, you may want to [plan an upgrade](https://www.cockroachlabs.com/docs/v25.1/upgrade-cockroach-version) of earlier client or server versions.
- Since every CockroachDB cluster has a unique ID, you can use the `Cluster ID` field to verify that your client is always connecting to the correct cluster.

### Commands [Anchor link for: commands](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary\#commands)

The following commands can be used within the interactive SQL shell:

| Command | Usage |
| --- | --- |
| `\?`, `help` | View this help within the shell. |
| `\q`, `quit`, `exit`, `ctrl-d` | Exit the shell.<br>When no text follows the prompt, `ctrl-c` exits the shell as well; otherwise, `ctrl-c` clears the line. |
| `\!` | Run an external command and print its results to `stdout`. [See an example](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#run-external-commands-from-the-sql-shell). |
| `\|` | Run the output of an external command as SQL statements. [See an example](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#run-external-commands-from-the-sql-shell). |
| `\set <option>`, `\unset <option>` | Enable or disable a client-side option. For more details, see [Client-side options](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#client-side-options).<br>You can also use the [`--set` flag](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#general) to enable or disable client-side options before starting the SQL shell. |
| `\p`, `\show` | During a multi-line statement or transaction, show the SQL that has been entered but not yet executed.<br>`\show` was deprecated as of v21.1. Use `\p` instead. |
| `\h <statement>`, `\hf <function>` | View help for specific SQL statements or functions. See [SQL shell help](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#help) for more details. |
| `\c <option>`, `\connect <option>` | Display or change the current [connection parameters](https://www.cockroachlabs.com/docs/v25.1/connection-parameters). Using `\c` without an argument lists the current connection parameters. <br>To reuse the existing connection and change the current database, use `\c <dbname>`. This is equivalent to `SET <database>` and `USE <database>`. <br>To connect to a cluster using individual connection parameters, use `\c <dbname> <user> <host> <port>`. Use the dash character ( `-`) to omit one parameter. To reconnect to the cluster using the current connection parameters enter `\c -`. When using individual connection parameters, the TLS settings from the original connection are reused. To use different TLS settings, connect using a connection URL. <br>To connect to a cluster using a [connection URL](https://www.cockroachlabs.com/docs/v25.1/connection-parameters#connect-using-a-url) use `\c <url>` |
| `\l` | List all databases in the CockroachDB cluster. This command is equivalent to [`SHOW DATABASES`](https://www.cockroachlabs.com/docs/v25.1/show-databases). |
| `\d[S+] [<pattern>]` | Show details about the relations in the current database. By default this command will show all the user tables, indexes, views, materialized views, and sequences in the current database. Add the `S` modifier to also show all system objects. If you specify a relation or a [pattern](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#patterns), it will show the details of matching relations. Add the `+` modifier to show additional information. |
| `\dC[+] [<pattern>]` | Show the type casts. If you specify a type or a [pattern](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#patterns), it will show the details of matching types. Add the `+` modifier to show additional information. |
| `\dd[S] [<pattern>]` | Show the objects of type `constraint` in the current database. Add the `S` modifier to also show all system objects. If you specify a type or a [pattern](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#patterns), it will show the details of matching objects. |
| `\df[S+] [<pattern>]` | Show the [user-defined functions](https://www.cockroachlabs.com/docs/v25.1/user-defined-functions) of the current database. Add the `S` modifier to also show all [system functions](https://www.cockroachlabs.com/docs/v25.1/functions-and-operators). If you specify a function name or a [pattern](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#patterns), it will show the details of matching function. Add the `+` modifier to show additional information. |
| `\dg[S+] [<pattern>]` | Show the [roles](https://www.cockroachlabs.com/docs/v25.1/authorization) of the current database. Add the `S` modifier to also show all system objects. If you specify a role name or a [pattern](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#patterns), it will show the details of matching roles. Add the `+` modifier to show additional information. |
| `\di[S+] [<pattern>]` | Show the indexes of the current database. Add the `S` modifier to also show all system objects. If you specify an index name or a [pattern](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#patterns), it will show the details of matching indexes. Add the `+` modifier to show additional information. |
| `\dm[S+] [<pattern>]` | Show the materialized views of the current database. Add the `S` modifier to also show all system objects. If you specify a materialized view name or a [pattern](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#patterns), it will show the details of matching materialized views. Add the `+` modifier to show additional information. |
| `\dn[S+] [<pattern>]` | List all [schemas](https://www.cockroachlabs.com/docs/v25.1/sql-name-resolution#naming-hierarchy) in the current database. Add the `S` modifier to also show all system schemas. Add the `+` modifier to show the permissions of each schema. Specify a [pattern](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#patterns) to limit the output to schemas that match the pattern. These commands are equivalent to [`SHOW SCHEMAS`](https://www.cockroachlabs.com/docs/v25.1/show-schemas). |
| `\ds[S+] [<pattern>]` | Show the sequences of the current database. Add the `S` modifier to also show all system objects. If you specify a sequence name or a [pattern](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#patterns), it will show the details of matching sequences. Add the `+` modifier to show additional information. |
| `\dt[S+] [<pattern>]` | Show the tables of the current database. Add the `S` modifier to also show all system objects. If you specify a table name or a [pattern](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#patterns), it will show the details of matching tables. Add the `+` modifier to show additional information. |
| `\dT[S+] [<pattern>]` | Show the [user-defined types](https://www.cockroachlabs.com/docs/v25.1/enum) in the current database. Add the `S` modifier to also show all system objects. If you specify a type name or a [pattern](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#patterns), it will show the details of matching types. Add the `+` modifier to show additional information. |
| `\du[S+] [<pattern>]` | Show the [roles](https://www.cockroachlabs.com/docs/v25.1/authorization) of the current database. Add the `S` modifier to also show all system objects. If you specify a role name or a [pattern](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#patterns), it will show the details of matching roles. Add the `+` modifier to show additional information. |
| `\dv[S+] [<pattern>]` | Show the views of the current database. Add the `S` modifier to also show all system objects. If you specify a view name or a [pattern](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#patterns), it will show the details of matching views. Add the `+` modifier to show additional information. |
| `\r` | Resets the query input buffer, clearing all SQL statements that have been entered but not yet executed. |
| `\statement-diag list` | List available [diagnostic bundles](https://www.cockroachlabs.com/docs/v25.1/cockroach-statement-diag). |
| `\statement-diag download <bundle-id> [<filename>]` | Download diagnostic bundle. |
| `\i <filename>` | Reads and executes input from the file `<filename>`, in the current working directory. |
| `\ir <filename>` | Reads and executes input from the file `<filename>`.<br>When invoked in the interactive shell, `\i` and `\ir` behave identically (i.e., CockroachDB looks for `<filename>` in the current working directory). When invoked from a script, CockroachDB looks for `<filename>` relative to the directory in which the script is located. |
| `\echo <arguments>` | Evaluate the `<arguments>` and print the results to the standard output. |
| `\x <boolean>` | When `true`/ `on`/ `yes`/ `1`, [sets the display format](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#sql-flag-format) to `records`. When `false`/ `off`/ `no`/ `0`, sets the session's format to the default ( `table`/ `tsv`). |

#### Patterns [Anchor link for: patterns](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary\#patterns)

Commands use the SQL [`LIKE` syntax](https://www.cockroachlabs.com/docs/v25.1/scalar-expressions#string-pattern-matching) for string pattern matching, not POSIX regular expressions.

For example to list all schemas that begin with the letter "p" you'd use the following pattern:

icon/buttons/copy

```sql
\dn p%

```

```
List of schemas:
      Name     | Owner
---------------+--------
  pg_catalog   | NULL
  pg_extension | NULL
  public       | admin
(3 rows)

```

### Client-side options [Anchor link for: client side options](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary\#client-side-options)

- To view option descriptions and how they are currently set, use `\set` without any options.
- To enable or disable an option, use `\set <option> <value>` or `\unset <option> <value>`. You can also use the form `<option>=<value>`.
- If an option accepts a boolean value:

  - `\set <option>` without `<value>` is equivalent to `\set <option> true`, and `\unset <option>` without `<value>` is equivalent to `\set <option> false`.
  - `on`, `yes`, and `1` are aliases for `true`, and `off`, `no`, and `0` are aliases for `false`.

| Client Options | Description |
| --- | --- |
| `auto_trace` | For every statement executed, the shell also produces the trace for that statement in a separate result below. A trace is also produced in case the statement produces a SQL error.<br>**Default:** `off`<br>To enable this option, run `\set auto_trace on`. |
| `border` | Display a border around the output of the SQL statement when using the `table` display format. Set the level of borders using `border=<level>` to configure how many borders and lines are in the output, where `<level>` is an integer between 0 and 3. The higher the integer, the more borders and lines are in the output. <br>A level of `0` shows the output with no outer lines and no row line separators. <br>A level of `1` adds row line separators. A level of `2` adds an outside border and no row line separators. A level of `3` adds both an outside border and row line separators. <br>**Default:** `0`<br>To change this option, run `\set border=<level>`. [See an example](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#show-borders-around-the-statement-output-within-the-sql-shell). |
| `check_syntax` | Validate SQL syntax. This ensures that a typo or mistake during user entry does not inconveniently abort an ongoing transaction previously started from the interactive shell.<br>**Default:** `true` for [interactive sessions](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#session-and-output-types); `false` otherwise.<br>To disable this option, run `\unset check_syntax`. |
| `display_format` | How to display table rows printed within the interactive SQL shell. Possible values: `tsv`, `csv`, `table`, `raw`, `records`, `sql`, `html`.<br>**Default:** `table` for sessions that [output on a terminal](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#session-and-output-types); `tsv` otherwise<br>To change this option, run `\set display_format <format>`. [See an example](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#make-the-output-of-show-statements-selectable). |
| `echo` | Reveal the SQL statements sent implicitly by the SQL shell.<br>**Default:** `false`<br>To enable this option, run `\set echo`. [See an example](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#reveal-the-sql-statements-sent-implicitly-by-the-command-line-utility). |
| `errexit` | Exit the SQL shell upon encountering an error.<br>**Default:** `false` for [interactive sessions](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql#session-and-output-types); `true` otherwise<br>To enable this option, run `\set errexit`. |
| `prompt1` | Customize the interactive prompt within the SQL shell. See [Customizing the prompt](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#customizing-the-prompt) for information on the available prompt variables. |
| `show_times` | Reveal the time a query takes to complete. Possible values:<br>- `execution` time refers to the time taken by the SQL execution engine to execute the query.<br>- `network` time refers to the network latency between the server and the SQL client command.<br>- `other` time refers to all other forms of latency affecting the total query completion time, including query planning.<br>**Default:** `true`<br>To disable this option, run `\unset show_times`. |

#### Customizing the prompt [Anchor link for: customizing the prompt](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary\#customizing-the-prompt)

The `\set prompt1` option allows you to customize the interactive prompt in the SQL shell. Use the following prompt variables to set a custom prompt.

| Prompt variable | Description |
| --- | --- |
| `%>` | The port of the node you are connected to. |
| `%/` | The current database name. |
| `%M` | The fully qualified host name and port of the node. |
| `%m` | The fully qualified host name of the node. |
| `%n` | The username of the connected SQL user. |
| `%x` | The transaction status of the current statement. |

For example, to change the prompt to just the user, host, and database:

icon/buttons/copy

```sql
\set prompt1 %n@%m/%/

```

```
maxroach@blue-dog-595.g95.cockroachlabs.cloud/defaultdb>

```

### Help [Anchor link for: help](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary\#help)

Within the SQL shell, you can get interactive help about statements and functions:

| Command | Usage |
| --- | --- |
| `\h`<br>`??` | List all available SQL statements, by category. |
| `\hf` | List all available SQL functions, in alphabetical order. |
| `\h <statement>`<br>`<statement> ?` | View help for a specific SQL statement. |
| `\hf <function>`<br>`<function> ?` | View help for a specific SQL function. |

#### Examples [Anchor link for: examples](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary\#examples)

```sql
\h UPDATE

```

```
Command:     UPDATE
Description: update rows of a table
Category:    data manipulation
Syntax:
UPDATE <tablename> [[AS] <name>] SET ... [WHERE <expr>] [RETURNING <exprs...>]

See also:
  SHOW TABLES
  INSERT
  UPSERT
  DELETE
  https://www.cockroachlabs.com/docs/v25.1/update.html

```

```sql
\hf uuid_v4

```

```
Function:    uuid_v4
Category:    built-in functions
Returns a UUID.

Signature          Category
uuid_v4() -> bytes [ID Generation]

See also:
  https://www.cockroachlabs.com/docs/v25.1/functions-and-operators.html

```

### Shortcuts [Anchor link for: shortcuts](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary\#shortcuts)

Note: macOS users may need to manually enable Alt-based shortcuts in their terminal configuration. See the section [macOS terminal configuration](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#macos-terminal-configuration) below for details.

| Shortcut | Description |
| --- | --- |
| Tab | Use [context-sensitive command completion](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#tab-completion). |
| Ctrl+C | Clear/cancel the input. |
| Ctrl+M, Enter | New line/enter. |
| Ctrl+O | Force a new line on the current statement, even if the statement has a semicolon. |
| Ctrl+F, Right arrow | Forward one character. |
| Ctrl+B, Left arrow | Backward one character. |
| Alt+F, Ctrl+Right arrow | Forward one word. |
| Alt+B, Ctrl+Left arrow | Backward one word. |
| Ctrl+L | Refresh the display. |
| Delete | Delete the next character. |
| Ctrl+H, Backspace | Delete the previous character. |
| Ctrl+D | Delete the next character, or terminate the input if the input is currently empty. |
| Alt+D, Alt+Delete | Delete next word. |
| Ctrl+W, Alt+Backspace | Delete previous word. |
| Ctrl+E, End | End of line. |
| Alt+>, Ctrl+End | Move cursor to the end of a multi-line statement. |
| Ctrl+A, Home | Move cursor to the beginning of the current line. |
| Alt+<, Ctrl+Home | Move cursor to the beginning of a multi-line statement. |
| Ctrl+T | Transpose current and next characters. |
| Ctrl+K | Delete from cursor position until end of line. |
| Ctrl+U | Delete from beginning of line to cursor position. |
| Alt+Q | Reflow/reformat the current line. |
| Alt+Shift+Q, Alt+\` | Reflow/reformat the entire input. |
| Alt+L | Convert the current word to lowercase. |
| Alt+U | Convert the current word to uppercase. |
| Alt+. | Toggle the visibility of the prompt. |
| Alt+2, Alt+F2 | Invoke external editor on current input. |
| Alt+P, Up arrow | Recall previous history entry. |
| Alt+N, Down arrow | Recall next history entry. |
| Ctrl+R | Start searching through input history. |

When searching for history entries, the following shortcuts are active:

| Shortcut | Description |
| --- | --- |
| Ctrl+C, Ctrl+G | Cancel the search, return to normal mode. |
| Ctrl+R | Recall next entry matching current search pattern. |
| Enter | Accept the current recalled entry. |
| Backspace | Delete previous character in search pattern. |
| Other | Add character to search pattern. |

#### Tab completion [Anchor link for: tab completion](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary\#tab-completion)

The SQL client offers context-sensitive tab completion when entering commands. Use the **Tab** key on your keyboard when entering a command to initiate the command completion interface. You can then navigate to database objects, keywords, and functions using the arrow keys. Press the **Tab** key again to select the object, function, or keyword from the command completion interface and return to the console.

### macOS terminal configuration [Anchor link for: macos terminal configuration](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary\#macos-terminal-configuration)

In **Apple Terminal**:

1. Navigate to "Preferences", then "Profiles", then "Keyboard".
2. Enable the checkbox "Use Option as Meta Key".

![Apple Terminal Alt key configuration](https://www.cockroachlabs.com/docs/images/v24.2/terminal-configuration.png)

In **iTerm2**:

1. Navigate to "Preferences", then "Profiles", then "Keys".
2. Select the radio button "Esc+" for the behavior of the Left Option Key.

![iTerm2 Alt key configuration](https://www.cockroachlabs.com/docs/images/v24.2/iterm2-configuration.png)

### Error messages and `SQLSTATE` codes [Anchor link for: error messages and sqlstate codes](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary\#error-messages-and-sqlstate-codes)

When CockroachDB encounters a SQL error, it returns the following information to the client (whether `cockroach-sql` or another [client application](https://www.cockroachlabs.com/docs/v25.1/developer-guide-overview)):

1. An error message, prefixed with [the "Severity" field of the PostgreSQL wire protocol](https://www.postgresql.org/docs/current/protocol-error-fields.html). For example, `ERROR: insert on table "shipments" violates foreign key constraint "fk_customers"`.
2. A [5-digit `SQLSTATE` error code](https://wikipedia.org/wiki/SQLSTATE) as defined by the SQL standard. For example, `SQLSTATE: 23503`.

For example, the following query (taken from [this example of adding multiple foreign key constraints](https://www.cockroachlabs.com/docs/v25.1/foreign-key#add-multiple-foreign-key-constraints-to-a-single-column)) results in a SQL error, and returns both an error message and a `SQLSTATE` code as described above.

icon/buttons/copy

```sql
INSERT INTO shipments (carrier, status, customer_id) VALUES ('DHL', 'At facility', 2000);

```

```
ERROR: insert on table "shipments" violates foreign key constraint "fk_customers"
SQLSTATE: 23503
DETAIL: Key (customer_id)=(2000) is not present in table "customers".

```

The [`SQLSTATE` code](https://wikipedia.org/wiki/SQLSTATE) in particular can be helpful in the following ways:

- It is a standard SQL error code that you can look up in documentation and search for on the web. For any given error state, CockroachDB tries to produce the same `SQLSTATE` code as PostgreSQL.
- If you are developing automation that uses the CockroachDB SQL shell, it is more reliable to check for `SQLSTATE` values than for error message strings, which are likely to change.

## Examples [Anchor link for: examples](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary\#examples)

### Start a SQL shell [Anchor link for: start a sql shell](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary\#start-a-sql-shell)

In these examples, we connect a SQL shell to a **secure cluster**.

icon/buttons/copy

```shell
# Using the --url flag:
cockroach-sql \
--url="postgresql://maxroach@12.345.67.89:26257/critterdb?sslcert=certs/client.maxroach.crt&sslkey=certs/client.maxroach.key&sslmode=verify-full&sslrootcert=certs/ca.crt"

```

icon/buttons/copy

```shell
# Using standard connection flags:
cockroach-sql \
--certs-dir=certs \
--user=maxroach \
--host=12.345.67.89 \
--database=critterdb

```

In these examples, we connect a SQL shell to an **insecure cluster**.

icon/buttons/copy

```shell
# Using the --url flag:
cockroach-sql \
--url="postgresql://maxroach@12.345.67.89:26257/critterdb?sslmode=disable"

```

icon/buttons/copy

```shell
# Using standard connection flags:
cockroach-sql --insecure \
--user=maxroach \
--host=12.345.67.89 \
--database=critterdb

```

### Execute SQL statement within the SQL shell [Anchor link for: execute sql statement within the sql shell](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary\#execute-sql-statement-within-the-sql-shell)

This example assumes that we have already started the SQL shell (see examples above).

icon/buttons/copy

```sql
CREATE TABLE animals (id INT PRIMARY KEY DEFAULT unique_rowid(), name STRING);

```

icon/buttons/copy

```sql
INSERT INTO animals (name) VALUES ('bobcat'), ('🐢 '), ('barn owl');

```

icon/buttons/copy

```sql
SELECT * FROM animals;

```

```
          id         |   name
---------------------+-----------
  710907071259213825 | bobcat
  710907071259279361 | 🐢
  710907071259312129 | barn owl
(3 rows)

```

### Execute SQL statements from the command line [Anchor link for: execute sql statements from the command line](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary\#execute-sql-statements-from-the-command-line)

In these examples, we use the `--execute` flag to execute statements from the command line:

icon/buttons/copy

```shell
# Statements with a single --execute flag:
cockroach-sql --insecure \
--execute="CREATE TABLE roaches (name STRING, country STRING); INSERT INTO roaches VALUES ('American Cockroach', 'United States'), ('Brownbanded Cockroach', 'United States')" \
--user=maxroach \
--host=12.345.67.89 \
--database=critterdb

```

```
CREATE TABLE
INSERT 2

```

icon/buttons/copy

```shell
# Statements with multiple --execute flags:
cockroach-sql --insecure \
--execute="CREATE TABLE roaches (name STRING, country STRING)" \
--execute="INSERT INTO roaches VALUES ('American Cockroach', 'United States'), ('Brownbanded Cockroach', 'United States')" \
--user=maxroach \
--host=12.345.67.89 \
--database=critterdb

```

```
CREATE TABLE
INSERT 2

```

In this example, we use the `echo` command to execute statements from the command line:

icon/buttons/copy

```shell
# Statements with the echo command:
echo "SHOW TABLES; SELECT * FROM roaches;" | cockroach-sql --insecure --user=maxroach --host=12.345.67.89 --database=critterdb

```

```
  schema_name | table_name | type  | owner | estimated_row_count | locality
--------------+------------+-------+-------+---------------------+-----------
  public      | animals    | table | demo  |                   0 | NULL
  public      | roaches    | table | demo  |                   0 | NULL
(2 rows)

          name          |    country
------------------------+----------------
  American Cockroach    | United States
  Brownbanded Cockroach | United States

```

### Control how table rows are printed [Anchor link for: control how table rows are printed](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary\#control-how-table-rows-are-printed)

In these examples, we show tables and special characters printed in various formats.

When the standard output is a terminal, `--format` defaults to `table` and tables are printed with ASCII art and special characters are not escaped for easy human consumption:

icon/buttons/copy

```shell
cockroach-sql --insecure \
--execute="SELECT '🐥' AS chick, '🐢' AS turtle" \
--user=maxroach \
--host=12.345.67.89 \
--database=critterdb

```

```
  chick | turtle
--------+---------
  🐥    | 🐢

```

However, you can explicitly set `--format` to another format (e.g., `tsv` or `html`):

icon/buttons/copy

```shell
cockroach-sql --insecure \
--format=tsv \
--execute="SELECT '🐥' AS chick, '🐢' AS turtle" \
--user=maxroach \
--host=12.345.67.89 \
--database=critterdb

```

```
chick   turtle
🐥    🐢

```

icon/buttons/copy

```shell
cockroach-sql --insecure \
--format=html \
--execute="SELECT '🐥' AS chick, '🐢' AS turtle" \
--user=maxroach \
--host=12.345.67.89 \
--database=critterdb

```

```
<table>
<thead><tr><th>row</th><th>chick</th><th>turtle</th></tr></thead>
<tbody>
<tr><td>1</td><td>🐥</td><td>🐢</td></tr>
</tbody>
<tfoot><tr><td colspan=3>1 row</td></tr></tfoot></table>

```

When piping output to another command or a file, `--format` defaults to `tsv`:

icon/buttons/copy

```shell
cockroach-sql --insecure \
--execute="SELECT '🐥' AS chick, '🐢' AS turtle" > out.txt \
--user=maxroach \
--host=12.345.67.89 \
--database=critterdb

```

icon/buttons/copy

```shell
cat out.txt

```

```
1 row
chick   turtle
🐥    🐢

```

However, you can explicitly set `--format` to another format (e.g., `table`):

icon/buttons/copy

```shell
cockroach-sql --insecure \
--format=table \
--execute="SELECT '🐥' AS chick, '🐢' AS turtle" > out.txt \
--user=maxroach \
--host=12.345.67.89 \
--database=critterdb

```

icon/buttons/copy

```shell
cat out.txt

```

```
  chick | turtle
--------+---------
  🐥    | 🐢
(1 row)

```

### Show borders around the statement output within the SQL shell [Anchor link for: show borders around the statement output within the sql shell](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary\#show-borders-around-the-statement-output-within-the-sql-shell)

To display outside and inside borders in the statement output, set the `border` [SQL shell option](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#client-side-options) to `3`.

icon/buttons/copy

```sql
\set border=3
SELECT * FROM animals;

```

```
+--------------------+----------+
|         id         |   name   |
+--------------------+----------+
| 710907071259213825 | bobcat   |
+--------------------+----------+
| 710907071259279361 | 🐢       |
+--------------------+----------+
| 710907071259312129 | barn owl |
+--------------------+----------+

```

### Make the output of `SHOW` statements selectable [Anchor link for: make the output of show statements selectable](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary\#make-the-output-of-show-statements-selectable)

To make it possible to select from the output of `SHOW` statements, set `--format` to `raw`:

icon/buttons/copy

```shell
cockroach-sql --insecure \
--format=raw \
--user=maxroach \
--host=12.345.67.89 \
--database=critterdb

```

icon/buttons/copy

```sql
SHOW CREATE customers;

```

```
# 2 columns
# row 1
## 14
test.customers
## 185
CREATE TABLE customers (
    id INT NOT NULL,
    email STRING NULL,
    CONSTRAINT "primary" PRIMARY KEY (id ASC),
    UNIQUE INDEX customers_email_key (email ASC),
    FAMILY "primary" (id, email)
)
# 1 row

```

When `--format` is not set to `raw`, you can use the `display_format` [SQL shell option](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#client-side-options) to change the output format within the interactive session:

icon/buttons/copy

```sql
\set display_format raw

```

```
# 2 columns
# row 1
## 14
test.customers
## 185
CREATE TABLE customers (
  id INT NOT NULL,
  email STRING NULL,
  CONSTRAINT "primary" PRIMARY KEY (id ASC),
  UNIQUE INDEX customers_email_key (email ASC),
  FAMILY "primary" (id, email)
)
# 1 row

```

### Execute SQL statements from a file [Anchor link for: execute sql statements from a file](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary\#execute-sql-statements-from-a-file)

In this example, we show and then execute the contents of a file containing SQL statements.

icon/buttons/copy

```shell
cat statements.sql

```

```
CREATE TABLE roaches (name STRING, country STRING);
INSERT INTO roaches VALUES ('American Cockroach', 'United States'), ('Brownbanded Cockroach', 'United States');

```

icon/buttons/copy

```shell
cockroach-sql --insecure \
--user=maxroach \
--host=12.345.67.89 \
--database=critterdb \
-f statements.sql

```

```
CREATE TABLE
INSERT 2

```

### Run external commands from the SQL shell [Anchor link for: run external commands from the sql shell](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary\#run-external-commands-from-the-sql-shell)

In this example, we use `\!` to look at the rows in a CSV file before creating a table and then using `\|` to insert those rows into the table.

Note:

This example works only if the values in the CSV file are numbers. For values in other formats, use an online CSV-to-SQL converter or make your own import program.

icon/buttons/copy

```sql
\! cat test.csv

```

```
12, 13, 14
10, 20, 30

```

icon/buttons/copy

```sql
CREATE TABLE csv (x INT, y INT, z INT);

```

icon/buttons/copy

```sql
\| IFS=","; while read a b c; do echo "insert into csv values ($a, $b, $c);"; done < test.csv;

```

icon/buttons/copy

```sql
SELECT * FROM csv;

```

```
  x  | y  | z
-----+----+-----
  12 | 13 | 14
  10 | 20 | 30

```

In this example, we create a table and then use `\|` to programmatically insert values.

icon/buttons/copy

```sql
CREATE TABLE for_loop (x INT);

```

icon/buttons/copy

```sql
\| for ((i=0;i<10;++i)); do echo "INSERT INTO for_loop VALUES ($i);"; done

```

icon/buttons/copy

```sql
SELECT * FROM for_loop;

```

```
  x
-----
  0
  1
  2
  3
  4
  5
  6
  7
  8
  9

```

### Allow potentially unsafe SQL statements [Anchor link for: allow potentially unsafe sql statements](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary\#allow-potentially-unsafe-sql-statements)

The `--safe-updates` flag defaults to `true`. This prevents SQL statements that may have broad, undesired side effects. For example, by default, we cannot use `DELETE` without a `WHERE` clause to delete all rows from a table:

icon/buttons/copy

```shell
cockroach-sql --insecure --execute="SELECT * FROM db1.t1"

```

```
  id | name
-----+-------
   1 | a
   2 | b
   3 | c
   4 | d
   5 | e
   6 | f
   7 | g
   8 | h
   9 | i
  10 | j
-----+-------
(10 rows)

```

icon/buttons/copy

```shell
cockroach-sql --insecure --execute="DELETE FROM db1.t1"

```

```
Error: pq: rejected: DELETE without WHERE clause (sql_safe_updates = true)
Failed running "sql"

```

However, to allow an "unsafe" statement, you can set `--safe-updates=false`:

icon/buttons/copy

```shell
cockroach-sql --insecure --safe-updates=false --execute="DELETE FROM db1.t1"

```

```
DELETE 10

```

Note:

Potentially unsafe SQL statements can also be allowed/disallowed for an entire session via the `sql_safe_updates` [session variable](https://www.cockroachlabs.com/docs/v25.1/set-vars).

### Reveal the SQL statements sent implicitly by the command-line utility [Anchor link for: reveal the sql statements sent implicitly by the command line utility](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary\#reveal-the-sql-statements-sent-implicitly-by-the-command-line-utility)

In this example, we use the `--execute` flag to execute statements from the command line and the `--echo-sql` flag to reveal SQL statements sent implicitly:

icon/buttons/copy

```shell
cockroach-sql --insecure \
--execute="CREATE TABLE t1 (id INT PRIMARY KEY, name STRING)" \
--execute="INSERT INTO t1 VALUES (1, 'a'), (2, 'b'), (3, 'c')" \
--user=maxroach \
--host=12.345.67.89 \
--database=db1
--echo-sql

```

```
# Server version: CockroachDB CCL f8f3c9317 (darwin amd64, built 2017/09/13 15:05:35, go1.8) (same version as client)
# Cluster ID: 847a4ba5-c78a-465a-b1a0-59fae3aab520
> SET sql_safe_updates = TRUE
> CREATE TABLE t1 (id INT PRIMARY KEY, name STRING)
CREATE TABLE
> INSERT INTO t1 VALUES (1, 'a'), (2, 'b'), (3, 'c')
INSERT 3

```

In this example, we start the interactive SQL shell and enable the `echo` shell option to reveal SQL statements sent implicitly:

icon/buttons/copy

```shell
cockroach-sql --insecure \
--user=maxroach \
--host=12.345.67.89 \
--database=db1

```

icon/buttons/copy

```sql
\set echo

```

icon/buttons/copy

```sql
INSERT INTO db1.t1 VALUES (4, 'd'), (5, 'e'), (6, 'f');

```

```
> INSERT INTO db1.t1 VALUES (4, 'd'), (5, 'e'), (6, 'f');
INSERT 3

Time: 2.426534ms

> SHOW TRANSACTION STATUS
> SHOW DATABASE

```

### Repeat a SQL statement [Anchor link for: repeat a sql statement](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary\#repeat-a-sql-statement)

Repeating SQL queries on a table can be useful for monitoring purposes. With the `--watch` flag, you can repeat the statements specified with a `--execute` or `-e` flag periodically, until a SQL error occurs or the process is terminated.

For example, if you want to monitor the number of queries running on the current node, you can use `cockroach-sql` with the `--watch` flag to query the node's `crdb_internal.node_statement_statistics` table for the query count:

icon/buttons/copy

```shell
cockroach-sql --insecure \
--execute="SELECT SUM(count) FROM crdb_internal.node_statement_statistics" \
--watch 1m

```

```
  sum
-------
  926
(1 row)
  sum
--------
  4227
(1 row)
^C

```

In this example, the statement is executed every minute. We let the process run for a couple minutes before terminating it with **Ctrl+C**.

### Connect to a cluster listening for Unix domain socket connections [Anchor link for: connect to a cluster listening for unix domain socket connections](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary\#connect-to-a-cluster-listening-for-unix-domain-socket-connections)

To connect to a cluster that is running on the same machine as your client and is listening for [Unix domain socket](https://wikipedia.org/wiki/Unix_domain_socket) connections, [specify a Unix domain socket URI](https://www.cockroachlabs.com/docs/v25.1/connection-parameters#example-uri-for-a-unix-domain-socket) with the `--url` connection parameter.

For example, suppose you start a single-node cluster with the following [`cockroach start-single-node`](https://www.cockroachlabs.com/docs/v25.1/cockroach-start-single-node) command:

icon/buttons/copy

```shell
cockroach start-single-node --insecure --socket-dir=/tmp

```

```
CockroachDB node starting at  (took 1.3s)
build:               CCL v25.1.0 @ 2025-02-18 00:00:00
webui:               http://Jesses-MBP-2:8080
sql:                 postgresql://root@Jesses-MBP-2:26257?sslmode=disable
RPC client flags:    ./cockroach <client cmd> --host=Jesses-MBP-2:26257 --insecure
socket:              /tmp/.s.PGSQL.26257
logs:                /Users/jesseseldess/Downloads/cockroach-.darwin-10.9-amd64/cockroach-data/logs
temp dir:            /Users/jesseseldess/Downloads/cockroach-.darwin-10.9-amd64/cockroach-data/cockroach-temp805054895
external I/O path:   /Users/jesseseldess/Downloads/cockroach-.darwin-10.9-amd64/cockroach-data/extern
store[0]:            path=/Users/jesseseldess/Downloads/cockroach-.darwin-10.9-amd64/cockroach-data
storage engine:      pebble
status:              initialized new cluster
clusterID:           455ad71d-21d4-424a-87ad-8097b6b5b99f
nodeID:              1

```

To connect to this cluster with a socket:

icon/buttons/copy

```shell
cockroach-sql --url='postgres://root@?host=/tmp&port=26257'

```

## See also [Anchor link for: see also](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary\#see-also)

- [Client Connection Parameters](https://www.cockroachlabs.com/docs/v25.1/connection-parameters)
- [`cockroach demo`](https://www.cockroachlabs.com/docs/v25.1/cockroach-demo)
- [`cockroach` Commands Overview](https://www.cockroachlabs.com/docs/v25.1/cockroach-commands)
- [SQL Statements](https://www.cockroachlabs.com/docs/v25.1/sql-statements)
- [Learn CockroachDB SQL](https://www.cockroachlabs.com/docs/v25.1/learn-cockroachdb-sql)

Was this helpful?

[![Yes](https://www.cockroachlabs.com/docs/images/icon-thumbs-up.svg)](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#yes-feedback)[![No](https://www.cockroachlabs.com/docs/images/icon-thumbs-down.svg)](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#no-feedback)

Contribute
![Carat arrow pointing down](https://www.cockroachlabs.com/docs/images/carat-down-fill.svg)

- [View Page Source](https://github.com/cockroachdb/docs/tree/main/src/current/v25.1/cockroach-sql-binary.md)
- [Edit This Page](https://github.com/cockroachdb/docs/edit/main/src/current/v25.1/cockroach-sql-binary.md)
- [Report Doc Issue](https://github.com/cockroachdb/docs/issues/new?title=Feedback:%20cockroach-sql&body=Page%3A%20https%3A%2F%2Fcockroachlabs.com/docs/v25.1/cockroach-sql-binary.html%0A%0A%23%23%20What%20is%20the%20reason%20for%20your%20feedback?%0A%0A[%20]%20Missing%20the%20information%20I%20need%0A%0A[%20]%20Too%20complicated%0A%0A[%20]%20Out%20of%20date%0A%0A[%20]%20Something%20is%20broken%0A%0A[%20]%20Other%0A%0A%23%23%20Additional%20details&)

On this page

- [Install `cockroach-sql`](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#install-cockroach-sql)
- [Before you begin](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#before-you-begin)
- [Synopsis](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#synopsis)
- [Flags](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#flags)
  - [General](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#general)
  - [Client connection](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#client-connection)
  - [Logging](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#logging)
- [Session and output types](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#session-and-output-types)
- [SQL shell](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#sql-shell)
  - [Welcome message](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#welcome-message)
  - [Commands](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#commands)
  - [Client-side options](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#client-side-options)
  - [Help](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#help)
  - [Shortcuts](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#shortcuts)
  - [macOS terminal configuration](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#macos-terminal-configuration)
  - [Error messages and `SQLSTATE` codes](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#error-messages-and-sqlstate-codes)
- [Examples](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#examples)
  - [Start a SQL shell](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#start-a-sql-shell)
  - [Execute SQL statement within the SQL shell](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#execute-sql-statement-within-the-sql-shell)
  - [Execute SQL statements from the command line](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#execute-sql-statements-from-the-command-line)
  - [Control how table rows are printed](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#control-how-table-rows-are-printed)
  - [Show borders around the statement output within the SQL shell](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#show-borders-around-the-statement-output-within-the-sql-shell)
  - [Make the output of `SHOW` statements selectable](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#make-the-output-of-show-statements-selectable)
  - [Execute SQL statements from a file](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#execute-sql-statements-from-a-file)
  - [Run external commands from the SQL shell](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#run-external-commands-from-the-sql-shell)
  - [Allow potentially unsafe SQL statements](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#allow-potentially-unsafe-sql-statements)
  - [Reveal the SQL statements sent implicitly by the command-line utility](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#reveal-the-sql-statements-sent-implicitly-by-the-command-line-utility)
  - [Repeat a SQL statement](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#repeat-a-sql-statement)
  - [Connect to a cluster listening for Unix domain socket connections](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#connect-to-a-cluster-listening-for-unix-domain-socket-connections)
- [See also](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#see-also)

Was this helpful?

[![Yes](https://www.cockroachlabs.com/docs/images/icon-thumbs-up.svg)](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#yes-feedback)[![No](https://www.cockroachlabs.com/docs/images/icon-thumbs-down.svg)](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql-binary#no-feedback)

[iframe](https://www.google.com/recaptcha/enterprise/anchor?ar=1&k=6Lck4YwlAAAAAEIE1hR--varWp0qu9F-8-emQn2v&co=aHR0cHM6Ly93d3cuY29ja3JvYWNobGFicy5jb206NDQz&hl=en&v=rW64dpMGAGrjU7JJQr9xxPl8&size=invisible&cb=wytdlhf1uljq)

[iframe](https://go.cockroachlabs.com/index.php/form/XDFrame)

# cockroach sqlfmt

Docs Menu


- [Version v25.1.0](https://www.cockroachlabs.com/docs/v25.1/cockroach-sqlfmt#)  - [v25.1.0\\
       (Stable)](https://www.cockroachlabs.com/docs/stable/cockroach-sqlfmt) [v25.1.0\\
       (Stable)](https://www.cockroachlabs.com/docs/stable/cockroach-sqlfmt)
  - [v24.3.6](https://www.cockroachlabs.com/docs/v24.3/cockroach-sqlfmt) [v24.3.6](https://www.cockroachlabs.com/docs/v24.3/cockroach-sqlfmt)
  - [v24.2.10](https://www.cockroachlabs.com/docs/v24.2/cockroach-sqlfmt) [v24.2.10](https://www.cockroachlabs.com/docs/v24.2/cockroach-sqlfmt)
  - [v24.1.13 LTS](https://www.cockroachlabs.com/docs/v24.1/cockroach-sqlfmt) [v24.1.13 LTS](https://www.cockroachlabs.com/docs/v24.1/cockroach-sqlfmt)
  - [v23.2.20 LTS](https://www.cockroachlabs.com/docs/v23.2/cockroach-sqlfmt) [v23.2.20 LTS](https://www.cockroachlabs.com/docs/v23.2/cockroach-sqlfmt)
  - [v23.1.30 LTS](https://www.cockroachlabs.com/docs/v23.1/cockroach-sqlfmt) [v23.1.30 LTS](https://www.cockroachlabs.com/docs/v23.1/cockroach-sqlfmt)
  - [v22.2.19](https://www.cockroachlabs.com/docs/v22.2/cockroach-sqlfmt) [v22.2.19](https://www.cockroachlabs.com/docs/v22.2/cockroach-sqlfmt)
  - [v22.1.22](https://www.cockroachlabs.com/docs/v22.1/cockroach-sqlfmt) [v22.1.22](https://www.cockroachlabs.com/docs/v22.1/cockroach-sqlfmt)
  - [v21.2.17](https://www.cockroachlabs.com/docs/v21.2/cockroach-sqlfmt) [v21.2.17](https://www.cockroachlabs.com/docs/v21.2/cockroach-sqlfmt)
  - [v21.1.21](https://www.cockroachlabs.com/docs/v21.1/cockroach-sqlfmt) [v21.1.21](https://www.cockroachlabs.com/docs/v21.1/cockroach-sqlfmt)
  - [v20.2.19](https://www.cockroachlabs.com/docs/v20.2/cockroach-sqlfmt) [v20.2.19](https://www.cockroachlabs.com/docs/v20.2/cockroach-sqlfmt)
  - [v20.1.17](https://www.cockroachlabs.com/docs/v20.1/cockroach-sqlfmt) [v20.1.17](https://www.cockroachlabs.com/docs/v20.1/cockroach-sqlfmt)
  - [v19.2.12](https://www.cockroachlabs.com/docs/v19.2/cockroach-sqlfmt) [v19.2.12](https://www.cockroachlabs.com/docs/v19.2/cockroach-sqlfmt)
  - [v19.1.11](https://www.cockroachlabs.com/docs/v19.1/use-the-query-formatter) [v19.1.11](https://www.cockroachlabs.com/docs/v19.1/use-the-query-formatter)
  - [v2.1.11](https://www.cockroachlabs.com/docs/v2.1/use-the-query-formatter) [v2.1.11](https://www.cockroachlabs.com/docs/v2.1/use-the-query-formatter)
  - v2.0.7



     This page does not exist in v2.0

     v2.0.7


  - v1.1.9



     This page does not exist in v1.1

     v1.1.9


  - v1.0.7



     This page does not exist in v1.0

     v1.0.7

# cockroach sqlfmt

Contribute
![Carat arrow pointing down](https://www.cockroachlabs.com/docs/images/carat-down-fill.svg)

- [View Page Source](https://github.com/cockroachdb/docs/tree/main/src/current/v25.1/cockroach-sqlfmt.md)
- [Edit This Page](https://github.com/cockroachdb/docs/edit/main/src/current/v25.1/cockroach-sqlfmt.md)
- [Report Doc Issue](https://github.com/cockroachdb/docs/issues/new?title=Feedback:%20cockroach%20sqlfmt&body=Page%3A%20https%3A%2F%2Fcockroachlabs.com/docs/v25.1/cockroach-sqlfmt.html%0A%0A%23%23%20What%20is%20the%20reason%20for%20your%20feedback?%0A%0A[%20]%20Missing%20the%20information%20I%20need%0A%0A[%20]%20Too%20complicated%0A%0A[%20]%20Out%20of%20date%0A%0A[%20]%20Something%20is%20broken%0A%0A[%20]%20Other%0A%0A%23%23%20Additional%20details&)

On this page ![Carat arrow pointing down](https://www.cockroachlabs.com/docs/images/carat-down-fill.svg)

- [Synopsis](https://www.cockroachlabs.com/docs/v25.1/cockroach-sqlfmt#synopsis)
- [Flags](https://www.cockroachlabs.com/docs/v25.1/cockroach-sqlfmt#flags)
- [Examples](https://www.cockroachlabs.com/docs/v25.1/cockroach-sqlfmt#examples)
  - [Reformat a query with constrained column width](https://www.cockroachlabs.com/docs/v25.1/cockroach-sqlfmt#reformat-a-query-with-constrained-column-width)
  - [Reformat a query with vertical alignment](https://www.cockroachlabs.com/docs/v25.1/cockroach-sqlfmt#reformat-a-query-with-vertical-alignment)
  - [Reformat a query with simplification of parentheses](https://www.cockroachlabs.com/docs/v25.1/cockroach-sqlfmt#reformat-a-query-with-simplification-of-parentheses)
- [See also](https://www.cockroachlabs.com/docs/v25.1/cockroach-sqlfmt#see-also)

The `cockroach sqlfmt` [command](https://www.cockroachlabs.com/docs/v25.1/cockroach-commands) changes the textual formatting of
one or more SQL queries. It recognizes all SQL extensions supported by
CockroachDB.

A [web interface to this feature](https://sqlfum.pt/) is also available.

Note:

**This feature is in [preview](https://www.cockroachlabs.com/docs/v25.1/cockroachdb-feature-availability)** and subject to change. To share feedback and/or issues, contact [Support](https://support.cockroachlabs.com/hc/en-us).

## Synopsis [Anchor link for: synopsis](https://www.cockroachlabs.com/docs/v25.1/cockroach-sqlfmt\#synopsis)

Use the query formatter interactively:

```shell
cockroach sqlfmt <flags>
<sql stmt>
CTRL+D

```

Reformat a SQL query given on the command line:

```shell
cockroach sqlfmt <flags> -e "<sql stmt>"

```

Reformat a SQL query already stored in a file:

```shell
cat query.sql | cockroach sqlfmt <flags>

```

## Flags [Anchor link for: flags](https://www.cockroachlabs.com/docs/v25.1/cockroach-sqlfmt\#flags)

The `sqlfmt` command supports the following flags.

| Flag | Description | Default value |
| --- | --- | --- |
| `--execute`<br>`-e` | Reformat the given SQL query, without reading from standard input. | N/A |
| `--print-width` | Desired column width of the output. | 80 |
| `--tab-width` | Number of spaces occupied by a tab character on the final display device. | 4 |
| `--use-spaces` | Always use space characters for formatting; avoid tab characters. | Use tabs. |
| `--align` | Use vertical alignment during formatting. | Do not align vertically. |
| `--no-simplify` | Avoid removing optional grouping parentheses during formatting. | Remove unnecessary grouping parentheses. |

## Examples [Anchor link for: examples](https://www.cockroachlabs.com/docs/v25.1/cockroach-sqlfmt\#examples)

### Reformat a query with constrained column width [Anchor link for: reformat a query with constrained column width](https://www.cockroachlabs.com/docs/v25.1/cockroach-sqlfmt\#reformat-a-query-with-constrained-column-width)

Using the interactive query formatter, output with the default column width (80 columns):

1. Start the interactive query formatter:

icon/buttons/copy



```shell
cockroach sqlfmt

```

2. Press **Enter**.

3. Run the query:

icon/buttons/copy



```sql
CREATE TABLE animals (id INT PRIMARY KEY DEFAULT unique_rowid(), name STRING);

```

4. Press **CTRL+D**.



```sql
CREATE TABLE animals (
           id INT PRIMARY KEY DEFAULT unique_rowid(),
           name STRING
)

```


Using the command line, output with the column width set to `40`:

icon/buttons/copy

```shell
cockroach sqlfmt --print-width 40 -e "CREATE TABLE animals (id INT PRIMARY KEY DEFAULT unique_rowid(), name STRING);"

```

```sql
CREATE TABLE animals (
        id
                INT
                PRIMARY KEY
                DEFAULT unique_rowid(),
        name STRING
)

```

### Reformat a query with vertical alignment [Anchor link for: reformat a query with vertical alignment](https://www.cockroachlabs.com/docs/v25.1/cockroach-sqlfmt\#reformat-a-query-with-vertical-alignment)

Output with the default vertical alignment:

```shell
cockroach sqlfmt -e "SELECT winner, round(length / (60 * 5)) AS counter FROM players WHERE build = $1 AND (hero = $2 OR region = $3);"

```

```sql
SELECT
winner, round(length / (60 * 5)) AS counter
FROM
players
WHERE
build = $1 AND (hero = $2 OR region = $3)

```

Output with vertical alignment:

icon/buttons/copy

```shell
cockroach sqlfmt --align -e "SELECT winner, round(length / (60 * 5)) AS counter FROM players WHERE build = $1 AND (hero = $2 OR region = $3);"

```

```sql
SELECT winner, round(length / (60 * 5)) AS counter
  FROM players
 WHERE build = $1 AND (hero = $2 OR region = $3);

```

### Reformat a query with simplification of parentheses [Anchor link for: reformat a query with simplification of parentheses](https://www.cockroachlabs.com/docs/v25.1/cockroach-sqlfmt\#reformat-a-query-with-simplification-of-parentheses)

Output with the default simplification of parentheses:

icon/buttons/copy

```shell
cockroach sqlfmt -e "SELECT (1 * 2) + 3, (1 + 2) * 3;"

```

```sql
SELECT 1 * 2 + 3, (1 + 2) * 3

```

Output with no simplification of parentheses:

icon/buttons/copy

```shell
cockroach sqlfmt --no-simplify -e "SELECT (1 * 2) + 3, (1 + 2) * 3;"

```

```sql
SELECT (1 * 2) + 3, (1 + 2) * 3

```

## See also [Anchor link for: see also](https://www.cockroachlabs.com/docs/v25.1/cockroach-sqlfmt\#see-also)

- [Sequel Fumpt](https://sqlfum.pt/)
- [`cockroach demo`](https://www.cockroachlabs.com/docs/v25.1/cockroach-demo)
- [`cockroach sql`](https://www.cockroachlabs.com/docs/v25.1/cockroach-sql)
- [`cockroach` Commands Overview](https://www.cockroachlabs.com/docs/v25.1/cockroach-commands)

Was this helpful?

[![Yes](https://www.cockroachlabs.com/docs/images/icon-thumbs-up.svg)](https://www.cockroachlabs.com/docs/v25.1/cockroach-sqlfmt#yes-feedback)[![No](https://www.cockroachlabs.com/docs/images/icon-thumbs-down.svg)](https://www.cockroachlabs.com/docs/v25.1/cockroach-sqlfmt#no-feedback)

Contribute
![Carat arrow pointing down](https://www.cockroachlabs.com/docs/images/carat-down-fill.svg)

- [View Page Source](https://github.com/cockroachdb/docs/tree/main/src/current/v25.1/cockroach-sqlfmt.md)
- [Edit This Page](https://github.com/cockroachdb/docs/edit/main/src/current/v25.1/cockroach-sqlfmt.md)
- [Report Doc Issue](https://github.com/cockroachdb/docs/issues/new?title=Feedback:%20cockroach%20sqlfmt&body=Page%3A%20https%3A%2F%2Fcockroachlabs.com/docs/v25.1/cockroach-sqlfmt.html%0A%0A%23%23%20What%20is%20the%20reason%20for%20your%20feedback?%0A%0A[%20]%20Missing%20the%20information%20I%20need%0A%0A[%20]%20Too%20complicated%0A%0A[%20]%20Out%20of%20date%0A%0A[%20]%20Something%20is%20broken%0A%0A[%20]%20Other%0A%0A%23%23%20Additional%20details&)

On this page

- [Synopsis](https://www.cockroachlabs.com/docs/v25.1/cockroach-sqlfmt#synopsis)
- [Flags](https://www.cockroachlabs.com/docs/v25.1/cockroach-sqlfmt#flags)
- [Examples](https://www.cockroachlabs.com/docs/v25.1/cockroach-sqlfmt#examples)
  - [Reformat a query with constrained column width](https://www.cockroachlabs.com/docs/v25.1/cockroach-sqlfmt#reformat-a-query-with-constrained-column-width)
  - [Reformat a query with vertical alignment](https://www.cockroachlabs.com/docs/v25.1/cockroach-sqlfmt#reformat-a-query-with-vertical-alignment)
  - [Reformat a query with simplification of parentheses](https://www.cockroachlabs.com/docs/v25.1/cockroach-sqlfmt#reformat-a-query-with-simplification-of-parentheses)
- [See also](https://www.cockroachlabs.com/docs/v25.1/cockroach-sqlfmt#see-also)

Was this helpful?

[![Yes](https://www.cockroachlabs.com/docs/images/icon-thumbs-up.svg)](https://www.cockroachlabs.com/docs/v25.1/cockroach-sqlfmt#yes-feedback)[![No](https://www.cockroachlabs.com/docs/images/icon-thumbs-down.svg)](https://www.cockroachlabs.com/docs/v25.1/cockroach-sqlfmt#no-feedback)

[iframe](https://www.google.com/recaptcha/enterprise/anchor?ar=1&k=6Lck4YwlAAAAAEIE1hR--varWp0qu9F-8-emQn2v&co=aHR0cHM6Ly93d3cuY29ja3JvYWNobGFicy5jb206NDQz&hl=en&v=rW64dpMGAGrjU7JJQr9xxPl8&size=invisible&cb=nfbxeakyomtg)

[iframe](https://go.cockroachlabs.com/index.php/form/XDFrame)

