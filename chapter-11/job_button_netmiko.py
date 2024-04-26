import os

from nautobot.apps.jobs import MultiChoiceVar, Job, ObjectVar, register_jobs, StringVar
from nautobot.dcim.models.locations import Location
from nautobot.dcim.models.devices import Device
from netmiko import ConnectHandler
from nautobot.apps.jobs import JobButtonReceiver


name = "Nautobot Book Job Button with Netmiko"


class UpdateSerialNumber(JobButtonReceiver):
    """Updates the serial number via Netmiko and JobButton."""

    class Meta:
        name = "Update Serial Number JobButton Receiver."

    def receive_job_button(self, obj):
        self.logger.info("Running job button receiver.", extra={"object": obj})
        if obj.primary_ip is None:
            self.logger.fatal("Device does not have a primary IP address set.")
            return

        if obj.platform is None:
            self.logger.fatal("Device does not have a platform set.")
            return

        if obj.platform.network_driver_mappings.get("netmiko") is None:
            self.logger.fatal("Device mapping for Netmiko is not present, please set.")
            return

        # Do not forget to add creds to your environment
        ## cat /etc/systemd/system/nautobot.service | grep Environment
        # Environment="NAUTOBOT_ROOT=/opt/nautobot"
        # Environment="DEVICE_USERNAME=<>"
        # Environment="DEVICE_PASSWORD=<>"
        ##
        ## cat /etc/systemd/system/nautobot-worker.service | grep Environment
        # Environment="NAUTOBOT_ROOT=/opt/nautobot"
        # Environment="DEVICE_USERNAME=<>"
        # Environment="DEVICE_PASSWORD=<>"
        ##

        net_connect = ConnectHandler(
            device_type=obj.platform.network_driver_mappings["netmiko"],
            host=obj.primary_ip.host,
            username=os.getenv("DEVICE_USERNAME"),
            password=os.getenv("DEVICE_PASSWORD"),
        )

        # New code for the Job Button
        output = net_connect.send_command("show version", use_textfsm=True)
        # Note that this is for demo purposes only, this may need some tuning
        # and work when working within production environments (such as with
        # stack switches)
        device_serial = output[0]["serial"][0]
        if device_serial != obj.serial:
            self.logger.warning(
                "Updating the device serial number to %s",
                device_serial,
                extra={"object": obj},
            )

            obj.serial = device_serial
            obj.validated_save()

            self.logger.info(
                "Device serial number updated successfully.", extra={"object": obj}
            )
        else:
            self.logger.info("Device serial number is correct.", extra={"object": obj})


register_jobs(UpdateSerialNumber)
