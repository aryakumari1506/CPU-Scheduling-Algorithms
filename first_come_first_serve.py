class Proc:
    def __init__(self, pid, at, bt):
        self.pid = pid
        self.at = at
        self.bt = bt
        self.rt = bt
        self.ct = 0
        self.wt = 0
        self.tat = 0

# Function to define First Come First serve
def fcfs(procs):
    procs.sort(key=lambda x: x.at)
    curr_time = 0
    for p in procs:
        if curr_time < p.at:
            curr_time = p.at
        p.wt = curr_time - p.at
        curr_time += p.bt
        p.ct = curr_time
        p.tat = p.ct - p.at

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
    fcfs(processes)
    print_metrics(processes)