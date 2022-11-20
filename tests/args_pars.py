from argparse import Action, ArgumentParser

class DriverAction(Action):
    def __call__(self, parser, namespace, values, otion_string=None):
        driver, destination = values
        namespace.driver = driver.lower()
        namespace.destination = destination

def create_parser():
    parser = ArgumentParser(description="Parser")
    parser.add_argument("url", help="url")
    parser.add_argument("--driver", help="driver name", nargs=2, action=DriverAction, required=True)

    return parser
