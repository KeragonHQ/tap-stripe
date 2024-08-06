"""Stripe tap class."""

from __future__ import annotations

from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers

# TODO: Import your custom stream types here:
from tap_stripe import streams


class TapStripe(Tap):
    """Stripe tap class."""

    name = "tap-stripe"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "api_key",
            th.StringType,
            required=True,
            secret=True,
            description="The token to authenticate against the API service",
        ),
        th.Property(
            "account_id",
            th.StringType,
            required=True,
            secret=True,
            description="Stripe account ID",
        ),
        th.Property(
            "start_date",
            th.DateTimeType,
            description="The earliest record date to sync",
        )
    ).to_dict()

    def discover_streams(self) -> list[streams.StripeStream]:

        return [
            streams.CustomersStream(self),
            streams.SubscriptionsStream(self),
            streams.ProductsStream(self),
            streams.EventsStream(self),
            streams.InvoicesStream(self),
        ]


if __name__ == "__main__":
    TapStripe.cli()
