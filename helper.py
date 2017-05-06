def get_stats(filename):
    stats = {}
    try:
        with open(filename, 'r') as workfile:
            for line in workfile:
                line = line.strip('\n').split(':')
                stats[line[0]] = int(line[1])
    except FileNotFoundError:
        pass
    return stats
