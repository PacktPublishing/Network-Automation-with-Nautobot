import os
from typing import Optional, List

try:
    from typing import TypedDict  # Python>=3.9
except ImportError:
    from typing_extensions import TypedDict  # Python<3.9
import yaml
from diffsync import DiffSync
from diffsync.enum import DiffSyncFlags
from nautobot.ipam.models import VRF, Prefix
from nautobot_ssot.contrib import NautobotModel, NautobotAdapter
from nautobot_ssot.jobs.base import DataSource

name = "An SSoT Example"

#####
# Defining Data Models
#####


class PrefixModel(NautobotModel):
    """Prefix Model for DiffSync."""

    _model = Prefix
    _modelname = "prefix"
    _identifiers = ("network", "prefix_length", "namespace__name")
    _attributes = ("status__name", "type")

    network: str
    type: str = "network"
    namespace__name: str = "Global"
    prefix_length: int
    status__name: str = "Active"
    vrf_name: Optional[str] = None


class PrefixDict(TypedDict):
    """This typed dict is 100% decoupled from the `NautobotPrefix` class defined above."""

    network: str
    prefix_length: int


class VRFModel(NautobotModel):
    """VRF Model for DiffSync."""

    _model = VRF
    _modelname = "vrf"
    _identifiers = ("name", "namespace__name")
    _attributes = ("rd", "description", "prefixes")

    name: str
    namespace__name: str = "Global"
    rd: Optional[str]
    description: Optional[str]
    prefixes: List[PrefixDict] = []


#####
# Defining Nautobot Adapter
#####


class ExampleNautobotAdapter(NautobotAdapter):
    """DiffSync adapter for Nautobot."""

    vrf = VRFModel
    prefix = PrefixModel
    top_level = (
        "prefix",
        "vrf",
    )


#####
# Defining Remote YAML Adapter
#####


class ExampleRemoteAdapter(DiffSync):
    """DiffSync adapter for remote system."""

    vrf = VRFModel
    prefix = PrefixModel
    top_level = (
        "prefix",
        "vrf",
    )

    def load(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(os.path.join(dir_path, "example.yaml")) as yaml_content:
            data = yaml.safe_load(yaml_content)

        for prefix in data["prefixes"]:
            network, prefix_length = prefix["prefix"].split("/")
            loaded_prefix = self.prefix(
                network=network,
                prefix_length=int(prefix_length),
                vrf_name=prefix["virtual_routing_instance"],
            )
            self.add(loaded_prefix)

        for vrf in data["virtual_routing_instances"]:
            prefixes = []
            for prefix in self.get_all("prefix"):
                if prefix.vrf_name == vrf["name"]:
                    prefixes.append(
                        {
                            "network": prefix.network,
                            "prefix_length": prefix.prefix_length,
                        }
                    )
            loaded_vrf = self.vrf(
                name=vrf["name"],
                rd=vrf["route_distinguisher"],
                description=vrf["comments"],
                prefixes=prefixes,
            )
            self.add(loaded_vrf)


#####
# Defining the DataSource Job
#####


class ExampleYAMLDataSource(DataSource):
    """SSoT Job class."""

    def __init__(self):
        """Initialize ExampleYAMLDataSource."""
        super().__init__()
        self.diffsync_flags = self.diffsync_flags | DiffSyncFlags.SKIP_UNMATCHED_DST

    class Meta:
        name = "Example YAML Data Source"
        description = "SSoT job example to get data from YAML"
        data_target = "Nautobot (remote)"

    def run(
        self, dryrun, memory_profiling, *args, **kwargs
    ):  # pylint:disable=arguments-differ
        """Run sync."""
        self.dryrun = dryrun
        self.memory_profiling = memory_profiling
        super().run(dryrun, memory_profiling, *args, **kwargs)

    def load_source_adapter(self):
        self.source_adapter = ExampleRemoteAdapter()
        self.source_adapter.load()

    def load_target_adapter(self):
        self.target_adapter = ExampleNautobotAdapter(job=self, sync=self.sync)
        self.target_adapter.load()


jobs = [ExampleYAMLDataSource]
