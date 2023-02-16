hare run -it  -e SDL_VIDEODRIVER=x11 -e DISPLAY=$DISPLAY -p 17799:17799 -p 17800:17800 -p 17801:17801 --runtime=nvidia --gpus all carlasim/carla:0.9.10.1 ./CarlaUE4.sh -world-port=17799 -opengl
