def checkVulnerabilityScan(inputFile: str) -> None:
    m: dict[str, set[str]] = {}
    with open(inputFile, 'r') as file:
        for line in file:
            if line:
                source, destination = line.strip().rsplit(':', 1)
                if source in m:
                    m[source].add(destination)
                    if len(m[source]) >= 3:
                        print(source)
                else:
                    m[source] = {destination}
    key = "192.168.1.1:30 -> 10.10.1.1"
    print(m[key])

checkVulnerabilityScan("iplogs.txt")