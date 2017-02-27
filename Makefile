DIR = ./scripts


run_locally: prepare run


run:
	${DIR}/run.sh


prepare:
	${DIR}/prepare.sh


run_docker:
	${DIR}/run_docker.sh

