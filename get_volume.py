def get_volume():
    actual_volume = subprocess.check_output(
        "amixer get '{}' | awk '$0~/%/{{print $4}}' | tr -d '[]%'".format(DEVICE),
        shell=True)

    if version_info[0] >= 3:
        actual_volume = actual_volume.strip().decode('utf-8')
    else:
        actual_volume = actual_volume.strip()

    actual_volume = int(actual_volume)
    actual_volume = min(100, actual_volume)
    actual_volume = max(0, actual_volume)

    return actual_volume
    print(actual_volume)