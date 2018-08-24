# Pyspark Test APP 
This GIT repo is about how to build a basic Spark Application with sbt.

SBT (scala build tool) is the most popular tool for creating jar for apache spark in scala language.

### Preinstallation required
* Apache spark 2.3.1
* python 3.6.5
* sbt 1.2.1

Note: if you have different versions that change sbt in project>build.properties and Apache spark in build.sbt file and python 3.x.x is must required. 

#### Creating a APP structure with python script (createsbtpackage.py)
* To create a pyspark package structure use below command
$ *python createsbtpackage.py project_name PATH(directory_path_where_you_want_create_project)*


or if you are allready in same directory where you want to create you project than no need of giving path as sys argument.

when you create a new project with this script, you will get a folder with project name inside the path you have give with below file in it.
* project (folder where all you  build.properties fiel resides)
    * build.properties ( contains all versions deatil of sbt and modules)
* build.sbt (file required to create a jar package with sbt )
* src (project directory)
    * main (main project directory for codes)
        * resource (all resource required for project)
        * scala (all scala codes)
        * java (all java codes)

    * test (test directory for unit testing )
        * resource 
        * scala
        * java


####  Create jar file from package

* To create you app or to create jar file use below command in you project folder.  
    * sbt ( to launch sbt, which will download dependecies for project)
    * sbt:project_name> compile (to compile and checking codes)
    * sbt:project_name> package (to create jar for project)

you need to be in you app directory to build your app with sbt. this command will create a folder name target in you project directory and jar will be inside that folder.


#### submiting application

./spark-submit --master local[*] --class className --jars jar1.jar,jar2.jar path-to_jar/app.jar arguments [if required]

spark-submit --master local[*]  --class wordcount spark_basics_2.11-0.1.jar  file:///home/dharm/Documents/Doofenshmirtz_Evil_corp_Develpoment/GitHub/Spark_test_app/resources/wordsfile.txt
