from nautobot.apps.jobs import Job, register_jobs


class HelloWorld(Job):

    def run(self):
        self.logger.debug("Hello, this is my first Nautobot Job.")
        self.logger.debug("Hello World, this is a debug log.")
        self.logger.info("This is an informational log.")
        self.logger.warning("This is a warning log.")
        self.logger.error("This is an error log.")
        self.logger.critical("This is a critical log.")


register_jobs(HelloWorld)
