import random

racers = ["Kast", "Maku", "Kiku", "Tartu", "Meinberg"]
alg, lopp = 23, 26
times = []
lap_times = {}
sector_times = {}


def suvalineaeg(a, b):
    aeg = round(random.uniform(a, b), 3)
    return aeg


def taisringi_aeg(racer):
    total = 0
    koperdused = []
    best_lap_time = float('inf')
    sector1_best_time = float('inf')
    sector2_best_time = float('inf')
    sector3_best_time = float('inf')

    for i in range(10):
        s1 = suvalineaeg(alg, lopp)
        s2 = suvalineaeg(alg, lopp)
        s3 = suvalineaeg(alg, lopp)

        # Generate random number in the range of 1-10
        number = random.randint(1, 10)
        if number == 2:
            s1 = suvalineaeg(30, 90)
            s2 = suvalineaeg(30, 90)
            s3 = suvalineaeg(30, 90)
            koperdused.append(i + 1)  # Add the lap number with a mistake

        kokku = round(s1 + s2 + s3, 3)
        total += kokku
        best_lap_time = min(best_lap_time, kokku)

        sector1_best_time = min(sector1_best_time, s1)
        sector2_best_time = min(sector2_best_time, s2)
        sector3_best_time = min(sector3_best_time, s3)

    lap_times[racer] = best_lap_time
    sector_times[racer] = [sector1_best_time, sector2_best_time, sector3_best_time]
    return total, koperdused


for racer in racers:
    total_time, koperdused = taisringi_aeg(racer)
    times.append([racer, total_time, koperdused])

sorted_times = sorted(times, key=lambda x: x[1])


def format_time(total_time, fastest=False):
    if isinstance(total_time, float):
        total_time = str(total_time)

    tunnid, minutes = divmod(int(float(total_time)) // 60, 60)
    seconds = int(float(total_time)) % 60
    milliseconds = int(total_time.split(".")[1][:3])

    if fastest:
        return f"{tunnid:02}:{minutes:02}:{seconds:02}.{milliseconds:03}"
    else:
        return f"{tunnid:02}:{minutes:02}:{seconds:02}.{milliseconds:03}"


for i, (racer, time, koperdused) in enumerate(sorted_times):
    total_time = str(time)
    time_formatted = format_time(total_time)
    koperdused_formatted = ",".join(map(str, koperdused))

    fastest_lap_time = lap_times[racer]
    fastest_formatted = format_time(fastest_lap_time, fastest=True)

    if i == 0:
        print(f"{racer:10}{time_formatted:13}[{koperdused_formatted:}] {fastest_formatted:13}")
    else:
        difference = time - sorted_times[0][1]
        difference_formatted = format_time(str(difference))
        print(f"{racer:10}{time_formatted:13}{difference_formatted:13}[{koperdused_formatted:}]")

print("\nSectors best")
for sector in range(3):
    sector_best_time = float('inf')
    sector_best_racers = []

    for racer in sector_times:
        sector_time = sector_times[racer][sector]
        if sector_time < sector_best_time:
            sector_best_time = sector_time
            sector_best_racers = [racer]
        elif sector_time == sector_best_time:
            sector_best_racers.append(racer)

    sector_best_formatted = format_time(sector_best_time)
    print(f"Sector {sector + 1} {' '.join(sector_best_racers)} {sector_best_formatted}")

dream_lap_time = sum([sector_best for sector_best in sector_times.values()], [])
dream_lap_time_formatted = format_time(sum(dream_lap_time))
print(f"Dream lap time: {dream_lap_time_formatted}")
