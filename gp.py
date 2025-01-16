import sys

# Function to retrieve driver information from a data file
def get_driver_info(file_path):
    drivers = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                details = line.strip().split(",")
                if len(details) < 4:
                    print(f"Invalid entry ignored: {line.strip()}")
                    continue
                code = details[1].strip().upper()
                name = details[2].strip()
                team = details[3].strip()
                drivers[code] = {"name": name, "team": team}
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    return drivers

# Function to process and analyze lap data
def evaluate_lap_data(file_name, drivers):
    try:
        with open(file_name, 'r') as file:
            race_title = file.readline().strip()
            lap_data = {}

            for line in file:
                line = line.strip()
                if not line:
                    continue
                code = line[:3].strip().upper()
                lap_time = float(line[4:])
                if code not in lap_data:
                    lap_data[code] = []
                lap_data[code].append(lap_time)

            fastest_driver = None
            best_lap_time = float('inf')
            total_lap_time = 0
            lap_count = 0

            fastest_laps = {}
            average_laps = {}

            for driver, times in lap_data.items():
                fastest = min(times)
                average = sum(times) / len(times)

                fastest_laps[driver] = fastest
                average_laps[driver] = average

                total_lap_time += sum(times)
                lap_count += len(times)

                if fastest < best_lap_time:
                    fastest_driver = driver
                    best_lap_time = fastest

            overall_average = total_lap_time / lap_count if lap_count else 0

            print(f"\nRace: {race_title}")
            print(f"Fastest Lap: {fastest_driver} - {best_lap_time:.3f} seconds\n")

            print("Driver Performance:")
            for driver in sorted(fastest_laps, key=lambda x: fastest_laps[x], reverse=True):
                info = drivers.get(driver, {"name": "Unknown", "team": "Unknown"})
                print(
                    f"{driver} ({info['name']}, {info['team']}): Best Lap = {fastest_laps[driver]:.3f}, "
                    f"Average Lap = {average_laps[driver]:.3f}, Total Laps = {len(lap_data[driver])}"
                )

            print(f"\nOverall Average Lap Time: {overall_average:.3f} seconds")
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as ex:
        print(f"Error processing file '{file_name}': {ex}")

# Main execution logic
def main():
    if len(sys.argv) < 3:
        print("Usage: python analyze_f1_data.py <driver_file> <lap_file1> [<lap_file2> ...]")
        sys.exit(1)

    driver_file = sys.argv[1]
    lap_files = sys.argv[2:]

    driver_info = get_driver_info(driver_file)

    print("\nLoaded Driver Information:")
    for code, data in driver_info.items():
        print(f"{code}: {data}")

    for lap_file in lap_files:
        if lap_file == driver_file:
            print(f"\nSkipping driver file: {driver_file}")
            continue
        print(f"\nProcessing file: {lap_file}")
        evaluate_lap_data(lap_file, driver_info)

if __name__ == "__main__":
    main()
