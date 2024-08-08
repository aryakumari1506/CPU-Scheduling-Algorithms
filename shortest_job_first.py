class Proc:
    def __init__(self, pid, at, bt):
        self.pid = pid
        self.at = at
        self.bt = bt
        self.rt = bt
        self.ct = 0
        self.wt = 0
        self.tat = 0

# Function to define Shortest Job First (Non-preemptive)
def sjf_np(procs):
    procs.sort(key=lambda x: (x.at, x.bt))
    curr_time = 0
    completed = []
    while procs:
        available = [p for p in procs if p.at <= curr_time]
        if not available:
            curr_time = procs[0].at
            continue
        short_p = min(available, key=lambda x: x.bt)
        procs.remove(short_p)
        short_p.wt = curr_time - short_p.at
        curr_time += short_p.bt
        short_p.ct = curr_time
        short_p.tat = short_p.ct - short_p.at
        completed.append(short_p)
    procs.extend(completed)

# Function to take process inputs
def get_procs():
    n = int(input("Enter number of processes: "))
    procs = []
    for _ in range(n):
        pid = input("Enter process ID: ")
        at = int(input("Enter arrival time: "))
        bt = int(input("Enter burst time: "))
        procs.append(Proc(pid, at, bt))
    return procs

def print_metrics(procs):
    total_wt = 0
    total_tat = 0
    for p in procs:
        print(f"Process {p.pid}: WT = {p.wt}, TAT = {p.tat}")
        total_wt += p.wt
        total_tat += p.tat
    print(f"Average WT: {total_wt / len(procs)}")
    print(f"Average TAT: {total_tat / len(procs)}")

# Main Function
if __name__ == "__main__":

    processes = get_procs()
    sjf_np(processes)
    print_metrics(processes)