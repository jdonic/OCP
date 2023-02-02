#!/usr/bin/env python

import click
import logging

from database import DatabaseHandler
from main import main

logger = logging.getLogger(__name__)


@click.group()
def cli() -> None:
    """Create CLI group to run click commands directly.

    This group command will be used to run various sub-commands related to the project.
    """


@cli.command(name="listener")
def listener() -> None:
    """Start a listener functionality.

    This command will start the main listener functionality, which listens for messages from kafka.
    """
    logging.info("Starting a listener functionality.")
    main()


@cli.command(name="categories")
def get_categories() -> None:
    """Retrieve stored data for categories.

    This command will retrieve the stored data for categories and print it on the console.
    """
    logging.info("The stored data for categories...")
    db = DatabaseHandler()
    categories = db.get_categories()
    print(categories)


@cli.command(name="offers")
def get_offers() -> None:
    """Retrieve stored data for offers.

    This command will retrieve the stored data for offers and print it on the console.
    """
    logging.info("The stored data for offers...")
    db = DatabaseHandler()
    offers = db.get_offers()
    print(offers)


@cli.command(name="products")
def get_products() -> None:
    """Retrieve stored data for products.

    This command will retrieve the stored data for products and print it on the console.
    """
    logging.info("The stored data for products...")
    db = DatabaseHandler()
    products = db.get_products()
    print(products)


if __name__ == "__main__":
    cli()
