import argparse

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', help='Path to file')
    parser.add_argument('--format', help='Output file format: json or csv', choices=['json','csv'], type=str.lower)

    return parser

def main():
    import sys
    from hr import export, users
    from hr import users as u

    args = create_parser().parse_args()
    users = u.fetch_users()

    if args.path:
        file = open(args.path, 'w', newline='')
    else:
        file = sys.stdout

    if args.format == 'json':
        export.to_json(file, users)
    else:
        export.to_csv(file, users)

if __name__ == '__main__':
    main()


