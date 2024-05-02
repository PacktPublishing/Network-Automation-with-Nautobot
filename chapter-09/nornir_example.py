# nornir_example.py
import os
from nornir import InitNornir
from nornir.core.task import Task, Result
from nornir_utils.plugins.functions import print_result


def hello_world(task):
    return Result(host=task.host, result=f"{task.host.name} says hello world!")


def main():
    locations = ["AMS01"]
    book_nornir = InitNornir(
        inventory={
            "plugin": "NautobotInventory",
            "options": {
                "nautobot_url": os.getenv("NAUTOBOT_URL"),
                "nautobot_token": os.getenv("NAUTOBOT_TOKEN"),
                "filter_parameters": {"location": locations},
                "ssl_verify": True,
            },
        },
    )

    print(f"Hosts found: {len(book_nornir.inventory.hosts)}")
    print(book_nornir.inventory.hosts.keys())
    result = book_nornir.run(task=hello_world)
    print_result(result)


if __name__ == "__main__":
    main()
