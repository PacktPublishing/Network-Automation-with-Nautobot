from nautobot.apps.jobs import Job, ObjectVar, register_jobs
from nautobot.dcim.models.locations import Location
from nautobot.dcim.models.devices import Device

name = "Nautobot Book Jobs"


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


register_jobs(SerialNumberReport)
