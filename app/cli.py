#!/usr/bin/env python

import click
import logging

from database import DatabaseHandler
from main import main

logger = logging.getLogger(__name__)


@click.group()
def cli() -> None:
    """Create CLI group to run click commands directly."""


@cli.command(name="listener")
def listener() -> None:
    logging.info("Starting a listener functionality.")
    main()


@cli.command(name="categories")
def get_categories() -> None:
    logging.info("The stored data for categories...")
    db = DatabaseHandler()
    categories = db.get_categories()
    print(categories)


@cli.command(name="offers")
def get_offers() -> None:
    logging.info("The stored data for offers...")
    db = DatabaseHandler()
    offers = db.get_offers()
    print(offers)


@cli.command(name="products")
def get_products() -> None:
    logging.info("The stored data for products...")
    db = DatabaseHandler()
    products = db.get_products()
    print(products)


if __name__ == "__main__":
    cli()
