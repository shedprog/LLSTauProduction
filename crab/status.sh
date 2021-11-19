REG_EXP=$1
CMD=$2
DIRS=(`readlink -f ./*/*/*${REG_EXP}*`)
for PATH_GLOB in ${DIRS[@]}; do
echo $PATH_GLOB
crab ${CMD} -d ${PATH_GLOB}
done
