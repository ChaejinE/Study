import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s:[%(levelname)s] %(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p",
)


def main(x, y):
    result = x + y
    logging.info(f"result={result}")


if __name__ == "__main__":
    import argparse

    args = argparse.ArgumentParser()
    args.add_argument("--x", type=int, required=True)
    args.add_argument("--y", type=int, required=True)
    args = args.parse_args()

    main(args.x, args.y)
