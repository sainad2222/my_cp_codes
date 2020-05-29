fun main(){
    val n = readLine()!!.toInt()
    for (i in 0 until n){
        val (n, k) = readLine()!!.split(' ').map(String::toInt)
        val n1=n/(k*k*k+k*k+k+1)
        val n2 = k*n1
        val n3 = k*n2
        val n4 = k*n3
        println("$n1 $n2 $n3 $n4")
        }
    }