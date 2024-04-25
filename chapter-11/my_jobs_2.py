import os

from nautobot.apps.jobs import MultiChoiceVar, Job, ObjectVar, register_jobs, StringVar
from nautobot.dcim.models.locations import Location
from nautobot.dcim.models.devices import Device
from netmiko import ConnectHandler

name = "Nautobot Book Jobs Part 2"

COMMAND_CHOICES = (
    ("show ip interface brief", "show ip int bri"),
    ("show ip route", "show ip route"),
    ("show version", "show version"),
    ("show log", "show log"),
    ("show ip ospf neighbor", "show ip ospf neighbor"),
)


class SerialNumberReport(Job):

    location_to_check = ObjectVar(
        model=Location,
    )

    class Meta:
        name = "Check Serial Numbers"
        has_sensitive_variables = False
        description = "First Nautobot Job: Reading and reporting data"

    def run(self, location_to_check):
        device_query = Device.objects.filter(location=location_to_check)

        for device in device_query:
            self.logger.info(
                "Checking the device %s for a serial number.",
                device.name,
                extra={"object": device},
            )
            if device.serial == "":
                self.logger.error(
                    "Device %s does not have serial number defined.",
                    device.name,
                    extra={"object": device},
                )
            else:
                self.logger.debug(
                    "Device %s has serial number: %s",
                    device.name,
                    device.serial,
                    extra={"object": device},
                )


class CommandRunner(Job):
    device_location = ObjectVar(model=Location, required=False)

    user_name = StringVar(description="Input your user name", required=False)

    device = ObjectVar(
        model=Device,
        query_params={
            "location": "$device_location",
        },
    )

    commands = MultiChoiceVar(choices=COMMAND_CHOICES)

    class Meta:
        name = "Command Runner"
        has_sensitive_variables = False
        description = "Command Runner"

    def run(self, device_location, user_name, device, commands):
        self.logger.info("Device name: %s", device.name)
        if user_name != "":
            self.logger.debug("User executing the command: %s", user_name)

        # Verify that the device has a primary IP
        if device.primary_ip is None:
            self.logger.fatal("Device does not have a primary IP address set.")
            return

        if device.platform is None:
            self.logger.fatal("Device does not have a platform set.")
            return

        if device.platform.network_driver_mappings.get("netmiko") is None:
            self.logger.fatal("Device mapping for Netmiko is not present, please set.")
            return

        # Connect to the device, get some output - comment this out if you are simulating
        net_connect = ConnectHandler(
            device_type=device.platform.network_driver_mappings["netmiko"],
            host=device.primary_ip.host,  # or device.name if your name is an FQDN
            username=os.getenv("DEVICE_USERNAME"),  # change to use user_name
            password=os.getenv("DEVICE_PASSWORD"),
        )
        for command in commands:
            output = net_connect.send_command(
                command
            )  # comment this out if you are only
            # output = "show command response goes here"
            self.create_file(f"{device.name}-{command}.txt", output)


register_jobs(SerialNumberReport, CommandRunner)
