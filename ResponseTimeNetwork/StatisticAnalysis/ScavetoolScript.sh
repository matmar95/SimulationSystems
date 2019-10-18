cd ../results
for n in "First" "Second" "Third"
do
  for j in 2 5 8 9
  do
    scavetool x -f 'module("*.QueueU1") AND (name("queueLength:mean"))' -o ../StatisticAnalysis/data/${n}_config/${n}_exit_${j}/LengthQueueU1.csv -F CSV-S ${n}_exit_${j}-*.sca
    scavetool x -f 'module("*.QueueU2") AND (name("queueLength:mean"))' -o ../StatisticAnalysis/data/${n}_config/${n}_exit_${j}/LengthQueueU2.csv -F CSV-S ${n}_exit_${j}-*.sca
    scavetool x -f 'module("*.SS1") AND (name("queueLength:mean"))' -o ../StatisticAnalysis/data/${n}_config/${n}_exit_${j}/LengthSS1.csv -F CSV-S ${n}_exit_${j}-*.sca
    scavetool x -f 'module("*.SS2") AND (name("queueLength:mean"))' -o ../StatisticAnalysis/data/${n}_config/${n}_exit_${j}/LengthSS2.csv -F CSV-S ${n}_exit_${j}-*.sca
    scavetool x -f 'module("*.sink") AND (name("lifeTime:mean"))'   -o  ../StatisticAnalysis/data/${n}_config/${n}_exit_${j}/LifeTimeTot.csv -F CSV-S ${n}_exit_${j}-*.sca
    scavetool x -f 'module("*.sink") AND (name("lifeTimeU1:mean"))' -o  ../StatisticAnalysis/data/${n}_config/${n}_exit_${j}/LifeTimeU1.csv -F CSV-S ${n}_exit_${j}-*.sca
    scavetool x -f 'module("*.sink") AND (name("lifeTimeU2:mean"))' -o  ../StatisticAnalysis/data/${n}_config/${n}_exit_${j}/LifeTimeU2.csv -F CSV-S ${n}_exit_${j}-*.sca
    scavetool x -f 'module("*.sink") AND (name("lifeTimeU1:max"))'  -o  ../StatisticAnalysis/data/${n}_config/${n}_exit_${j}/LifeTimeU1max.csv -F CSV-S ${n}_exit_${j}-*.sca
    scavetool x -f 'module("*.sink") AND (name("lifeTimeU1:min"))'  -o  ../StatisticAnalysis/data/${n}_config/${n}_exit_${j}/LifeTimeU1min.csv -F CSV-S ${n}_exit_${j}-*.sca
    scavetool x -f 'module("*.sink") AND (name("lifeTimeU2:max"))'  -o  ../StatisticAnalysis/data/${n}_config/${n}_exit_${j}/LifeTimeU2max.csv -F CSV-S ${n}_exit_${j}-*.sca
    scavetool x -f 'module("*.sink") AND (name("lifeTimeU2:min"))'  -o  ../StatisticAnalysis/data/${n}_config/${n}_exit_${j}/LifeTimeU2min.csv -F CSV-S ${n}_exit_${j}-*.sca
  done
done
