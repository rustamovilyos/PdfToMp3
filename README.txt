If your are using Ubuntu 20.01 (and 18.04) like me, the solution is to Install Oracle JDK 17. Do the following:

sudo add-apt-repository ppa:linuxuprising/java
sudo apt update
sudo apt install oracle-java17-installer



Type java -version on the terminal. You should see the following print-out:

java version "17.0.1" 2021-10-19 LTS`
Java(TM) SE Runtime Environment (build 17.0.1+12-LTS-39)`
Java HotSpot(TM) 64-Bit Server VM (build 17.0.1+12-LTS-39, mixed mode, sharing)


tika should then be able to extract text from your pdf in python.

parser.from_file(<your pdf file>)
