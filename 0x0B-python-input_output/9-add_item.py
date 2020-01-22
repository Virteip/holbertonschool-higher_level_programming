#!/usr/bin/python3


def main():
    list_args = []
    try:
        if (len(sys.argv) - 1) >= 1:
            list = load_from_json_file("add_item.json")
            for data in list:
                list_args.append(data)
    except:
            pass

    for arg in sys.argv[1:]:
        if (len(sys.argv) - 1) >= 1:
            list_args.append(str(arg))
        else:
            list_args.append("")

    save_to_json_file(list_args, "add_item.json")

if __name__ == '__main__':
    import sys
    save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('8-load_from_json_file').\
        load_from_json_file
    main()
