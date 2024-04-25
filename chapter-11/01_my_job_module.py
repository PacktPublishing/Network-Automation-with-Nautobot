from nautobot.apps.jobs import Job, register_jobs


class HelloWorld(Job):

    def run(self):
        self.logger.debug("Hello, this is my first Nautobot Job.")


register_jobs(HelloWorld)
