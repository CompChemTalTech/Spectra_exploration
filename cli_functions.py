import argparse

# Import your functions
from functions import (
    extract_data,
    get_orbitals_chart,
    get_rvel_chart,
    get_elect_dipole_chart,
    get_magnet_dipole_chart,
    get_em_angle_chart,
    get_spectra,
)

def main():
    parser = argparse.ArgumentParser(description="Execute functions with command line flags.")
    
    # Add arguments for each function
    parser.add_argument("--extract_data", action="store_true", help="Run extract_data function")
    parser.add_argument("--get_orbitals_chart", action="store_true", help="Run get_orbitals_chart function")
    parser.add_argument("--get_rvel_chart", action="store_true", help="Run get_rvel_chart function")
    parser.add_argument("--get_elect_dipole_chart", action="store_true", help="Run get_elect_dipole_chart function")
    parser.add_argument("--get_magnet_dipole_chart", action="store_true", help="Run get_magnet_dipole_chart function")
    parser.add_argument("--get_em_angle_chart", action="store_true", help="Run get_em_angle_chart function")
    parser.add_argument("--get_spectra", action="store_true", help="Run get_spectra function")


    parser.add_argument("--subpath", type=str, help="Path")
    parser.add_argument("--states", nargs="+",  type=int, default=[3,4], help="List of states needed. Default [3, 4]")
    parser.add_argument("--r_vel_states_number", type=int, default=6, help="number of r_vel needed to be extragated. Default 6")
    
    parser.add_argument("--x_title", type=str, default="", help="X title of the chart is 'Dihedral angle' + x_title + ', degree'. Default ")
    parser.add_argument("--y_lim_1", nargs="+", type=float, default=None, help="list of 2 numbers for HOMO chart [lower_limit, upper_limit]. Default None")
    parser.add_argument("--y_lim_2", nargs="+", type=float, default=None, help="list of 2 numbers for LUMO chart [lower_limit, upper_limit]. Default None")
    parser.add_argument("--conformers_names", type=bool, default=False, help="if all conformer names are int (rotation angles etc) - True, else - False. Default - False")

    parser.add_argument("--y_lim", nargs="+", type=float, default=None, help="list of 2 numbers [lower_limit, upper_limit]. Default None")
    parser.add_argument("--show_legend", type=bool, default=True, help="If True - shows legend, False - does not show legend. Default True")
    parser.add_argument("--fig_width", type=int, default=None, help="width of the chart. Default None")

    parser.add_argument("--special_style", nargs="+", type=int, default=None, help="ECD for conformers in this list will be plotted with dashed line")
    parser.add_argument("--legend_from_file", type=str, default=None, help="file name with legend. Default None")
    parser.add_argument("--x_lim", nargs="+", type=float, default=[None, None], help="ist of 2 numbers [left_limit, right_limit]. Default [None, None] ")
    parser.add_argument("--y_lim_ecd", nargs="+", type=float, default=[None, None], help="ist of 2 numbers [left_limit, right_limit]. Default [None, None] ")

    # Add additional flags for specific function arguments if needed

    args = parser.parse_args()

    # Call functions based on the provided flags
    if args.extract_data:
        extract_data(args.subpath, args.states, args.r_vel_states_number)
    elif args.get_orbitals_chart:
        get_orbitals_chart(args.subpath, args.x_title, args.y_lim_1, args.y_lim_2, args.conformers_names)
    elif args.get_rvel_chart:
        get_rvel_chart(args.subpath, args.states,  args.x_title, args.y_lim, args.show_legend, args.conformers_names)
    elif args.get_elect_dipole_chart:
        get_elect_dipole_chart(args.subpath, args.states,  args.x_title, args.y_lim, args.fig_width, args.conformers_names)
    elif args.get_magnet_dipole_chart:
        get_magnet_dipole_chart(args.subpath, args.states,  args.x_title, args.y_lim, args.fig_width, args.conformers_names)
    elif args.get_em_angle_chart:
        get_em_angle_chart(args.subpath, args.states,  args.x_title, args.y_lim, args.fig_width, args.show_legend, args.conformers_names)
    elif args.get_spectra:
        get_spectra(args.subpath, args.x_lim, args.y_lim_ecd, args.special_style, args.legend_from_file)

if __name__ == "__main__":
    main()