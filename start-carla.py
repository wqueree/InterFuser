from subprocess import Popen, PIPE
from tqdm import tqdm
from typing import List
from argparse import ArgumentParser, Namespace

def main() -> None:
    parser: ArgumentParser = ArgumentParser("Start a number of CARLA servers through docker.")
    parser.add_argument("-n", "--numservers", type=int)
    parser.add_argument("-p", "--startport", type=int)
    parser.add_argument("-g", "--gpus", type=int, nargs="+")
    args: Namespace = parser.parse_args()
    start_servers(args.numservers, args.startport, args.gpus)


def start_servers(num_servers: int, start_port: int, gpus: List[int]) -> None:
    with open("running-carla-containers.txt", encoding="utf-8", mode="w") as running_carla_containers_file:
        for server in tqdm(range(num_servers)):
            world_port: int = start_port + (server * 2)
            traffic_manager_port: int = world_port + 1
            gpu: int = gpus[server % 4]
            command: List[str] = ["hare", "run", "-p", f"127.0.0.1:{world_port}:{world_port}", "-p", f"127.0.0.1:{traffic_manager_port}:{traffic_manager_port}", "-dit", "--rm", "--gpus", f"'\"device={gpu}\"'", "-e", "SDL_VIDEODRIVER='offscreen'", "-e", "SDL_AUDIODRIVER='dsp'", "--runtime=nvidia", "carlasim/carla:0.9.10.1", "./CarlaUE4.sh", f"--world-port={world_port}", f"-carla-rpc-port={traffic_manager_port}", "-opengl"]
            process: Popen = Popen(" ".join(command), stdout=PIPE, stderr=PIPE, shell=True)
            stdout, stderr = process.communicate()
            running_carla_containers_file.write(stdout.decode("utf-8"))
            running_carla_containers_file.write(stderr.decode("utf-8"))



if __name__ == "__main__":
    main()