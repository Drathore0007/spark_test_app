import org.apache.spark.{SparkContext, SparkConf}

object wordcount {

  def main(argv:Array[String]): Unit ={
    System.out.println("Entering wordcount main")
    
    if(argv.length != 1){
      println("Please provide 1 parameters <inputFileName>")
      System.exit(1)
    }

    val fileName = argv(0)
    val sparkConf = new SparkConf().setAppName("WordCount").setMaster("local[*]") //.getOrCreate()
    val sc = new SparkContext(sparkConf)
    val tf = sc.textFile(fileName)
    //val splits = tf.flatMap(line => line.split(" ")).map(word =>(word,1))
    //val counts = splits.reduceByKey((x,y)=>x+y).collect()
    //System.out.println(counts)
    val counts = tf.flatMap(line => line.split(" ")).map(word => (word,1)).reduceByKey(_+_)
    System.out.println(counts.collect().mkString(", "))
  

  }

}