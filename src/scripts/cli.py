import argparse
from importlib.resources import files
from . import red_blue, red_green, red_grey


DEFAULT_INPUTS = {
    "red-blue": "redblue.png",
    "red-green": "redgreen.png",
    "red-grey": "redgrey.png",
}


def add_red_args(parser):
    parser.add_argument("--red_radius", type=float, metavar="", default=1.8, help="Adjust the radius of the red dots")
    parser.add_argument("--red_density", type=int, metavar="", default=10, help="Set the density (concentration) of the red dots")
    parser.add_argument("--red_jitter", type=float, metavar="", default=0.65, help="Control the jitter of the red dots")
    parser.add_argument("--red_ratio", type=float, metavar="", default=0.55, help="Manipulate the ratio of small:large red dots")
    parser.add_argument("--red_shape", choices=["circle", "square"], default="circle", help="Change the shape of the red dots")


def add_blue_args(parser):
    parser.add_argument("--blue_radius", type=float, metavar="", default=1.5, help="Adjust the radius of the blue dots")
    parser.add_argument("--blue_density", type=int, metavar="", default=7, help="Set the density (concentration) of the blue dots")
    parser.add_argument("--blue_jitter", type=float, metavar="", default=0.25, help="Control the jitter of the blue dots")
    parser.add_argument("--blue_ratio", type=float, metavar="", default=0.75, help="Manipulate the ratio of small:large blue dots")
    parser.add_argument("--blue_shape", choices=["circle", "square"], default="square", help="Change the shape of the blue dots")


def add_green_args(parser):
    parser.add_argument("--green_radius", type=float, metavar="", default=1.5, help="Adjust the radius of the green dots")
    parser.add_argument("--green_density", type=int, metavar="", default=7, help="Set the density (concentration) of the green dots")
    parser.add_argument("--green_jitter", type=float, metavar="", default=0.25, help="Control the jitter of the green dots")
    parser.add_argument("--green_ratio", type=float, metavar="", default=0.75, help="Manipulate the ratio of small:large green dots")
    parser.add_argument("--green_shape", choices=["circle", "square"], default="square", help="Change the shape of the green dots")


def add_grey_args(parser):
    parser.add_argument("--grey_radius", type=float, metavar="", default=1.5, help="Adjust the radius of the grey dots")
    parser.add_argument("--grey_density", type=int, metavar="", default=7, help="Set the density (concentration) of the grey dots")
    parser.add_argument("--grey_jitter", type=float, metavar="", default=0.25, help="Control the jitter of the grey dots")
    parser.add_argument("--grey_ratio", type=float, metavar="", default=0.75, help="Manipulate the ratio of small:large grey dots")
    parser.add_argument("--grey_shape", choices=["circle", "square"], default="square", help="Change the shape of the grey dots")


def main():
    parser = argparse.ArgumentParser(
        description="Chromostereopsis stimulus generator",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        add_help=False
    )

    parser.add_argument(
    "--help",
    action="help",
    help="Help for CLI"
)

    subparsers = parser.add_subparsers(
        dest="mode",
        required=True,
    )


    # Red-blue
    rb = subparsers.add_parser(
        "red-blue",
        help="RED-BLUE chromostereopsis",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    rb.add_argument("--input", metavar="PATH", default="src/media/redblue.png", help="State the path of the chosen input image")
    rb.add_argument("--save", metavar="PATH", default="red-blue.png", help="State the save name/path of the output image")
    
    add_red_args(rb)
    add_blue_args(rb)


    # Red-green
    rg = subparsers.add_parser(
        "red-green",
        help="RED-GREEN chromostereopsis",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    rg.add_argument("--input", metavar="PATH", default="src/media/redgreen.png", help="State the path of the chosen input image")
    rg.add_argument("--save", metavar="PATH", default="red-green.png", help="State the save name/path of the output image")

    add_red_args(rg)
    add_green_args(rg)


    # Red-grey
    rgr = subparsers.add_parser(
        "red-grey",
        help="RED-GREY chromostereopsis",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    rgr.add_argument("--input", metavar="PATH", default="src/media/redgrey.png", help="State the path of the chosen input image")
    rgr.add_argument("--save", metavar="PATH", default="red-grey.png", help="State the save name/path of the output image")
    
    add_red_args(rgr)
    add_grey_args(rgr)

    args = parser.parse_args()

    input_path = (
        args.input
        if args.input
        else files("scripts.default_input") / DEFAULT_INPUTS[args.mode]
    )

    red_dots = dict(
        radius=args.red_radius,
        density=args.red_density,
        jitter=args.red_jitter,
        ratio=args.red_ratio,
        shape=args.red_shape,
    )

    if args.mode == "red-blue":
        blue_dots = dict(
            radius=args.blue_radius,
            density=args.blue_density,
            jitter=args.blue_jitter,
            ratio=args.blue_ratio,
            shape=args.blue_shape,
        )

        red_blue.generate(
            input_path=input_path,
            output_path=args.save,
            red_dots=red_dots,
            blue_dots=blue_dots,
        )

    elif args.mode == "red-green":
        green_dots = dict(
            radius=args.green_radius,
            density=args.green_density,
            jitter=args.green_jitter,
            ratio=args.green_ratio,
            shape=args.green_shape,
        )

        red_green.generate(
            input_path=input_path,
            output_path=args.save,
            red_dots=red_dots,
            green_dots=green_dots,
        )

    elif args.mode == "red-grey":
        grey_dots = dict(
            radius=args.grey_radius,
            density=args.grey_density,
            jitter=args.grey_jitter,
            ratio=args.grey_ratio,
            shape=args.grey_shape,
        )

        red_grey.generate(
            input_path=input_path,
            output_path=args.save,
            red_dots=red_dots,
            grey_dots=grey_dots,
        )