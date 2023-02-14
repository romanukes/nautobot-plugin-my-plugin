"""Plugin declaration for my_plugin."""
# Metadata is inherited from Nautobot. If not including Nautobot in the environment, this should be added
try:
    from importlib import metadata
except ImportError:
    # Python version < 3.8
    import importlib_metadata as metadata

__version__ = metadata.version(__name__)

from nautobot.extras.plugins import PluginConfig


class MyPluginConfig(PluginConfig):
    """Plugin configuration for the my_plugin plugin."""

    name = "my_plugin"
    verbose_name = "My Plugin"
    version = __version__
    author = "Network to Code, LLC"
    description = "My Plugin."
    base_url = "my-plugin"
    required_settings = []
    min_version = "1.5.0"
    max_version = "1.9999"
    default_settings = {}
    caching_config = {}


config = MyPluginConfig  # pylint:disable=invalid-name
