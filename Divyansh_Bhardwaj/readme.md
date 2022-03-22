# FLO CPU & GPU mining Docker

This Dockerfile will make a container that can run both CPU and GPU mining seperately.




## Deployment

Make a Docker Image using this dockerfile 

```bash
  docker build .
```

To run the docker Image

```bash
  docker run -it <docker_image>
```

This will Start the container and a terminal will pop up.
Now run the following code to start the CPU miner..

```bash
  ./minerd -o stratum+tcp://rm-pool.duckdns.org:3333 -a scrypt -u <user>.<worker> -p <workerpassword>
```


