import argparse
from importlib.resources import files
from PIL import Image

from . import red_blue, red_green, red_grey, flexible


# --------------------------------------------------
# Default input images
# --------------------------------------------------

DEFAULT_INPUTS = {
    "red-blue": "redblue.png",
    "red-green": "redgreen.png",
    "red-grey": "redgrey.png",
    "flexible": "orangeyellow.png"
}


def load_default_image(mode):
    return Image.open(
        files("src.scripts.default_input") / DEFAULT_INPUTS[mode]
    ).convert("RGB")


# --------------------------------------------------
# Argument helpers
# --------------------------------------------------

def add_red_args(parser):
    parser.add_argument("--red_radius", type=float, metavar="", default=1.8, help="Radius of the red dots")
    parser.add_argument("--red_density", type=int, metavar="", default=10, help="Density (concentration) of the red dots")
    parser.add_argument("--red_jitter", type=float, metavar="", default=0.65, help="Jitter of the red dots")
    parser.add_argument("--red_ratio", type=float, metavar="", default=0.55, help="Ratio of small:large red dots")
    parser.add_argument("--red_shape", choices=["circle", "square"], default="circle", help="Shape of the red dots")


def add_blue_args(parser):
    parser.add_argument("--blue_radius", type=float, metavar="", default=1.5, help="Radius of the blue dots")
    parser.add_argument("--blue_density", type=int, metavar="", default=7, help="Density (concentration) of the blue dots")
    parser.add_argument("--blue_jitter", type=float, metavar="", default=0.25, help="Jitter of the blue dots")
    parser.add_argument("--blue_ratio", type=float, metavar="", default=0.75, help="Ratio of small:large blue dots")
    parser.add_argument("--blue_shape", choices=["circle", "square"], default="square", help="Shape of the blue dots")


def add_green_args(parser):
    parser.add_argument("--green_radius", type=float, metavar="", default=1.5, help="Radius of the green dots")
    parser.add_argument("--green_density", type=int, metavar="", default=7, help="Density (concentration) of the green dots")
    parser.add_argument("--green_jitter", type=float, metavar="", default=0.25, help="Jitter of the green dots")
    parser.add_argument("--green_ratio", type=float, metavar="", default=0.75, help="Ratio of small:large green dots")
    parser.add_argument("--green_shape", choices=["circle", "square"], default="square", help="Shape of the green dots")


def add_grey_args(parser):
    parser.add_argument("--grey_radius", type=float, metavar="", default=1.5, help="Radius of the grey dots")
    parser.add_argument("--grey_density", type=int, metavar="", default=7, help="Density (concentration) of the grey dots")
    parser.add_argument("--grey_jitter", type=float, metavar="", default=0.25, help="Jitter of the grey dots")
    parser.add_argument("--grey_ratio", type=float, metavar="", default=0.75, help="Ratio of small:large grey dots")
    parser.add_argument("--grey_shape", choices=["circle", "square"], default="square", help="Shape of the grey dots")


def add_colour1_args(parser):
    parser.add_argument(f"--colour1_radius", type=float, metavar="", default=1.8, help="Radius of the coloured dots")
    parser.add_argument(f"--colour1_density", type=int, metavar="", default=10, help="Density (concentration) of the coloured dots")
    parser.add_argument(f"--colour1_jitter", type=float, metavar="", default=0.65, help="Jitter of the coloured dots")
    parser.add_argument(f"--colour1_ratio", type=float, metavar="", default=0.55, help="Ratio of small:large coloured dots")
    parser.add_argument(f"--colour1_shape", choices=["circle", "square"], default="circle", help="Shape of the coloured dots")


def add_colour2_args(parser):
    parser.add_argument(f"--colour2_radius", type=float, metavar="", default=1.5, help="Radius of the coloured dots")
    parser.add_argument(f"--colour2_density", type=int, metavar="", default=7, help="Density (concentration) of the coloured dots")
    parser.add_argument(f"--colour2_jitter", type=float, metavar="", default=0.25, help="Jitter of the coloured dots")
    parser.add_argument(f"--colour2_ratio", type=float, metavar="", default=0.75, help="Ratio of small:large coloured dots")
    parser.add_argument(f"--colour2_shape", choices=["circle", "square"], default="square", help="Shape of the coloured dots")

# --------------------------------------------------
# CLI entry point
# --------------------------------------------------

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
    
    subparsers = parser.add_subparsers(dest="mode", required=True)

    # ---------------- RED-BLUE ----------------
    rb = subparsers.add_parser("red-blue", help="RED-BLUE chromostereopsis", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    rb.add_argument("--input", metavar="", default=None, help="Path of the chosen input image")
    rb.add_argument("--save", metavar="", default="redblue.png", help="Save name/path of the output image")
    add_red_args(rb)
    add_blue_args(rb)

    # ---------------- RED-GREEN ----------------
    rg = subparsers.add_parser("red-green", help="RED-GREEN chromostereopsis", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    rg.add_argument("--input", metavar="", default=None, help="Path of the chosen input image")
    rg.add_argument("--save", metavar="", default="redgreen.png", help="Save name/path of the output image")
    add_red_args(rg)
    add_green_args(rg)

    # ---------------- RED-GREY ----------------
    rgr = subparsers.add_parser("red-grey", help="RED-GREY chromostereopsis", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    rgr.add_argument("--input", metavar="", default=None, help="Path of the chosen input image")
    rgr.add_argument("--save", metavar="", default="redgrey.png", help="Save name/path of the output image")
    add_red_args(rgr)
    add_grey_args(rgr)

    # ---------------- FLEXIBLE ----------------
    flex = subparsers.add_parser("flexible", help="FLEXIBLE chromostereopsis", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    flex.add_argument("--input", metavar="", default=None, help="Path of the chosen input image")
    flex.add_argument("--save", metavar="", default="orangeyellow.png", help="Save name/path of the output image")

    flex.add_argument("--colour1", type=str, metavar="", default="#FF8C00", help="HEX colour 1")
    flex.add_argument("--colour2", type=str, metavar="", default="#FFFF00", help="HEX colour 2")
    flex.add_argument("--tolerance", type=int, metavar="", default=40, help="Maximum allowed colour distance away from target colours")

    add_colour1_args(flex)
    add_colour2_args(flex)
    

    args = parser.parse_args()

    # --------------------------------------------------
    # Resolve input image
    # --------------------------------------------------

    if args.input:
        img = Image.open(args.input).convert("RGB")
    else:
        img = load_default_image(args.mode)

    # --------------------------------------------------
    # Dispatch to rendering scripts
    # --------------------------------------------------

    if args.mode == "red-blue":
        red_dots = dict(
            radius=args.red_radius,
            density=args.red_density,
            jitter=args.red_jitter,
            ratio=args.red_ratio,
            shape=args.red_shape,
        ) 
        
        blue_dots = dict(
            radius=args.blue_radius,
            density=args.blue_density,
            jitter=args.blue_jitter,
            ratio=args.blue_ratio,
            shape=args.blue_shape,
        )

        red_blue.generate(
            img=img,
            output_path=args.save,
            red_dots=red_dots,
            blue_dots=blue_dots,
        )

    elif args.mode == "red-green":
        red_dots = dict(
            radius=args.red_radius,
            density=args.red_density,
            jitter=args.red_jitter,
            ratio=args.red_ratio,
            shape=args.red_shape,
        )
        
        green_dots = dict(
            radius=args.green_radius,
            density=args.green_density,
            jitter=args.green_jitter,
            ratio=args.green_ratio,
            shape=args.green_shape,
        )

        red_green.generate(
            img=img,
            output_path=args.save,
            red_dots=red_dots,
            green_dots=green_dots,
        )

    elif args.mode == "red-grey":
        red_dots = dict(
            radius=args.red_radius,
            density=args.red_density,
            jitter=args.red_jitter,
            ratio=args.red_ratio,
            shape=args.red_shape,
        )
        
        
        grey_dots = dict(
            radius=args.grey_radius,
            density=args.grey_density,
            jitter=args.grey_jitter,
            ratio=args.grey_ratio,
            shape=args.grey_shape,
        )

        red_grey.generate(
            img=img,
            output_path=args.save,
            red_dots=red_dots,
            grey_dots=grey_dots,
        )

    elif args.mode == "flexible":

        dots1 = dict(
            radius=args.colour1_radius,
            density=args.colour1_density,
            jitter=args.colour1_jitter,
            ratio=args.colour1_ratio,
            shape=args.colour1_shape,
        )

        dots2 = dict(
            radius=args.colour2_radius,
            density=args.colour2_density,
            jitter=args.colour2_jitter,
            ratio=args.colour2_ratio,
            shape=args.colour2_shape,
        )

        flexible.generate(
            img=img,
            output_path=args.save,
            colour1_hex=args.colour1,
            colour2_hex=args.colour2,
            dots1=dots1,
            dots2=dots2,
            tolerance=args.tolerance,
        )