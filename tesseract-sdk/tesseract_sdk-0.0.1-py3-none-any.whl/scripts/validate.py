import argparse


def validate_command(args):
    import tesseract.validate as validate
    validator = validate.ValidationManager(image=args.image, cli=True)
    validator.run()


def make_parser():
    parser = argparse.ArgumentParser(prog="tesseract-sdk")
    parser.set_defaults(func=lambda args: parser.print_help())

    subparsers = parser.add_subparsers(
        title="subcommand",
        description="valid subcommands",
        help="which action to run"
    )

    # Tesseract Model image testing
    parser_model_validation = subparsers.add_parser(
        "validate", help="validate your model container for use in Tesseract jobs")
    parser_model_validation.add_argument(
        "image",
        type=str,
        help="the image and tag to validate, e.g. my-model-container:v0.0.1"
    )
    parser_model_validation.set_defaults(func=validate_command)

    return parser


def main():
    args = make_parser().parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
