    def print_to_console(self, span_kind: str, interaction: Mapping[str, Any]) -> None:
        """Print the span to the console."""
        if not self.console:
            msg = "Console is not initialized"
            raise RuntimeError(msg)
        style = getattr(self.tracing_config, span_kind.lower(), None)
        if not style or interaction == {}:
            return

        self.console.rule(span_kind, style=style)

        for key, value in interaction.items():
            if key == "output":
                self.console.print(
                    Panel(
                        Markdown(str(value or "")),
                        title="Output",
                    ),
                )
            else:
                self.console.print(f"{key}: {value}")

        self.console.rule(style=style)
