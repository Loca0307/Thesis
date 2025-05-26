    pre_exec_cmd: Annotated[
        str | None,
        typer.Option(
            "--pre-exec-cmd", help="The pre-execution command to use for the python script."
        ),
    ] = None,