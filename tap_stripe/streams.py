"""Stream type classes for tap-stripe."""

from __future__ import annotations

import datetime
import sys
import typing as t

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_stripe.client import StripeStream

if sys.version_info >= (3, 9):
    import importlib.resources as importlib_resources
else:
    import importlib_resources


class CustomersStream(StripeStream):

    name = "customers"
    path = "/customers"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("id", th.StringType, required=True),
        th.Property("object", th.StringType, required=True),
        th.Property("address", th.AnyType),
        th.Property("balance", th.IntegerType, required=True),
        th.Property("created", th.IntegerType, required=True),
        th.Property("currency", th.StringType),
        th.Property("default_source", th.StringType),
        th.Property("delinquent", th.BooleanType, required=True),
        th.Property("description", th.StringType),
        th.Property("discount", th.AnyType),
        th.Property("email", th.StringType, required=True),
        th.Property("invoice_prefix", th.StringType, required=True),
        th.Property(
            "invoice_settings",
            th.ObjectType(
                th.Property("custom_fields", th.AnyType),
                th.Property("default_payment_method", th.StringType),
                th.Property("footer", th.StringType),
                th.Property("rendering_options", th.AnyType),
            ),
            required=True,
        ),
        th.Property("livemode", th.BooleanType, required=True),
        th.Property("metadata", th.ObjectType(), required=True),
        th.Property("name", th.StringType),
        th.Property("next_invoice_sequence", th.IntegerType, required=True),
        th.Property("phone", th.StringType),
        th.Property("preferred_locales", th.ArrayType(th.StringType), required=True),
        th.Property("shipping", th.AnyType),
        th.Property(
            "tax_exempt",
            th.StringType,
            required=True,
            allowed_values=["none", "exempt", "reverse"],
        ),
        th.Property("test_clock", th.AnyType),
    ).to_dict()


class SubscriptionsStream(StripeStream):

    name = "subscriptions"
    path = "/subscriptions"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("id", th.StringType, required=True),
        th.Property("object", th.StringType, required=True),
        th.Property("created", th.IntegerType, required=True),
        th.Property("cancel_at", th.IntegerType),
        th.Property("cancel_at_period_end", th.BooleanType, required=True),
        th.Property("canceled_at", th.IntegerType),
        th.Property(
            "cancellation_details",
            th.ObjectType(
                th.Property("comment", th.StringType),
                th.Property("feedback", th.StringType),
                th.Property("reason", th.StringType),
            ),
            required=True,
        ),
        th.Property("collection_method", th.StringType, required=True),
        th.Property("customer", th.StringType, required=True),
        th.Property("default_payment_method", th.StringType),
        th.Property("current_period_end", th.IntegerType, required=True),
        th.Property("current_period_start", th.IntegerType, required=True),
        th.Property(
            "items",
            th.ObjectType(
                th.Property("object", th.StringType, required=True),
                th.Property(
                    "data",
                    th.ArrayType(
                        th.ObjectType(
                            th.Property("id", th.StringType, required=True),
                            th.Property("object", th.StringType, required=True),
                            th.Property(
                                "billing_thresholds",
                                th.ObjectType(additional_properties=True),
                            ),
                            th.Property("created", th.IntegerType, required=True),
                            th.Property("discounts", th.ArrayType(th.StringType)),
                            th.Property(
                                "metadata",
                                th.ObjectType(additional_properties=True),
                                required=True,
                            ),
                            th.Property(
                                "price", th.ObjectType(additional_properties=True)
                            ),
                            th.Property("quantity", th.IntegerType),
                            th.Property("subscription", th.StringType, required=True),
                            th.Property(
                                "tax_rates",
                                th.ArrayType(th.ObjectType(additional_properties=True)),
                            ),
                            additional_properties=True,
                        )
                    ),
                    required=True,
                ),
                th.Property("total_count", th.IntegerType, required=True),
                additional_properties=True,
            ),
            required=True,
        ),
        th.Property("latest_invoice", th.StringType),
        th.Property("livemode", th.BooleanType, required=True),
        th.Property(
            "metadata", th.ObjectType(additional_properties=True), required=True
        ),
        th.Property(
            "payment_settings", th.ObjectType(additional_properties=True), required=True
        ),
        th.Property("start_date", th.IntegerType, required=True),
        th.Property("status", th.StringType, required=True),
        th.Property("trial_end", th.IntegerType),
        th.Property(
            "trial_settings", th.ObjectType(additional_properties=True), required=True
        ),
        th.Property("trial_start", th.IntegerType),
    ).to_dict()


class ProductsStream(StripeStream):

    name = "products"
    path = "/products"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("id", th.StringType, required=True),
        th.Property("object", th.StringType, required=True),
        th.Property("active", th.BooleanType, required=True),
        th.Property("attributes", th.ArrayType(th.StringType), required=True),
        th.Property("created", th.IntegerType, required=True),
        th.Property("default_price", th.StringType, required=True),
        th.Property("description", th.StringType),
        th.Property(
            "features",
            th.ArrayType(th.ObjectType(additional_properties=True)),
            required=True,
        ),
        th.Property("images", th.ArrayType(th.StringType), required=True),
        th.Property("livemode", th.BooleanType, required=True),
        th.Property(
            "marketing_features",
            th.ArrayType(th.ObjectType(additional_properties=True)),
            required=True,
        ),
        th.Property(
            "metadata", th.ObjectType(additional_properties=True), required=True
        ),
        th.Property("name", th.StringType, required=True),
        th.Property("package_dimensions", th.ObjectType(additional_properties=True)),
        th.Property("shippable", th.BooleanType),
        th.Property("statement_descriptor", th.StringType),
        th.Property("tax_code", th.StringType),
        th.Property("type", th.StringType, required=True),
        th.Property("unit_label", th.StringType),
        th.Property("updated", th.IntegerType, required=True),
        th.Property("url", th.StringType),
    ).to_dict()


class EventsStream(StripeStream):

    name = "events"
    path = "/events"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("id", th.StringType, required=True),
        th.Property("object", th.StringType, required=True),
        th.Property("type", th.StringType, required=True),
        th.Property("created", th.IntegerType, required=True),
        th.Property("data", th.ObjectType(additional_properties=True)),
    ).to_dict()

    def get_url_params(self, context, next_page_token):
        params = {"limit": 100, "type": "*"}
        start_date = self.get_starting_replication_key_value(context)

        if start_date:
            if type(start_date) == str:
                start_date = int(
                    datetime.timestamp(
                        datetime.strptime(start_date, "%Y-%m-%dT%H:%M:%SZ")
                    )
                )
            params["created[gt]"] = start_date

        if next_page_token:
            params["starting_after"] = next_page_token

        return params
