def sjf_scheduling(process_list):
    process_list.sort(key=lambda p: (p['burst_time'], p['pid']))
    current_time = 0

    for p in process_list:
        p['waiting_time'] = current_time
        p['turnaround_time'] = p['waiting_time'] + p['burst_time']
        current_time += p['burst_time']


def output(process_list):
    print(f"{'Process':<10}{'Burst':<10}{'Waiting':<10}{'Turnaround':<10}")
    for p in process_list:
        print(f"P{p['pid']:<9}{p['burst_time']:<10}{p['waiting_time']:<10}{p['turnaround_time']:<10}") 
    print(f"Average Waiting Time: {sum(p['waiting_time'] for p in process_list) / len(process_list)}")
    print(f"Average Turnaround Time: {sum(p['turnaround_time'] for p in process_list) / len(process_list)}")


if __name__ == "__main__":
    processes = [
        {'pid': 1, 'burst_time': 6},
        {'pid': 2, 'burst_time': 8},
        {'pid': 3, 'burst_time': 7},
        {'pid': 4, 'burst_time': 3}
    ]

    sjf_scheduling(processes)
    output(processes)
