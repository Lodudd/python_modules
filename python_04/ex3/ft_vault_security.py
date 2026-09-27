#!/usr/bin/env python3


def secure_archive(f_name: str, action: str = '',
                   content: str = '') -> tuple[bool, str]:
    try:
        with open(f_name, action) as f:
            if action == 'r':
                return (True, f.read())
            elif action == 'w':
                f.write(content)
                return (True, "Content successfully written to file")
        return (False, "Just in case")
    except OSError as e:
        return (False, str(e))
    except TypeError as e:
        return (False, str(e))
    except ValueError:
        return (False, "Pls provide proper action: 'r' or 'w'")
    except Exception as e:
        return (False, str(e))


def main() -> None:
    print("=== Cyber Archives Security ===")
    print("\nUsing'secure_archive' to read from a nonexistent file:")
    test = secure_archive("/not/existing/file", 'r')
    print(test)

    print("\nUsing'secure_archive' to read from an inaccessible file:")
    test = secure_archive("/etc/master.passwd", 'r')
    print(test)

    print("\nUsing'secure_archive' to read from a regular file:")
    test1 = secure_archive("test.txt", 'r')
    print(test1)

    print("\nUsing'secure_archive' to write previous content to a new file:")
    test = secure_archive("test1.txt", 'w', test1[1])
    print(test)


if __name__ == "__main__":
    main()
