# eve/cli.py
from __future__ import annotations
import os
from typing import Optional

import click
from .config import load_config, Config

@click.group(help="Eve demo CLI with config support.")
@click.option("--config", "config_path", type=click.Path(exists=True, dir_okay=False), required=False,
              help="Path to config file (yaml|yml|toml|json).")
@click.pass_context
def cli(ctx: click.Context, config_path: Optional[str]):
    # Load once, store in Click's context
    cfg = load_config(config_path)
    ctx.obj = {"config": cfg}

@cli.command(help="Say hello")
@click.option("--name", type=str, help="Who to greet")
@click.option("--shout/--no-shout", default=None, help="Uppercase output")
@click.pass_context
def greet(ctx: click.Context, name: Optional[str], shout: Optional[bool]):
    cfg: Config = ctx.obj["config"]

    # Precedence: CLI > config > default
    final_name = name or cfg.default_name or "world"
    final_shout = (cfg.default_shout if shout is None else shout)

    msg = f"Hello, {final_name}"
    click.echo(msg.upper() if final_shout else msg)

@cli.command(help="Add two integers")
@click.option("--a", type=int, help="Left operand")
@click.option("--b", type=int, help="Right operand")
@click.pass_context
def add(ctx: click.Context, a: Optional[int], b: Optional[int]):
    cfg: Config = ctx.obj["config"]

    final_a = cfg.default_a if a is None else a
    final_b = cfg.default_b if b is None else b

    if final_a is None or final_b is None:
        raise click.UsageError("Missing operands. Provide --a and --b or set default_a/default_b in config.")
    click.echo(final_a + final_b)

@cli.command(help="Show where config came from (debug)")
@click.option("--config", "config_path", type=str, required=False, hidden=True)
@click.pass_context
def where(ctx: click.Context, config_path: Optional[str] = None):
    # Not perfect, but helpful: re-run loader to echo result.
    from .config import discover_config_path
    p = discover_config_path(config_path or os.getenv("EVE_CONFIG"))
    click.echo(str(p) if p else "(no config file)")
