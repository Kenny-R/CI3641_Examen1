fun mul_matrix(A:Array<Array<Int>>,B:Array<Array<Int>>): Array<Array<Int>> {
    if (A[0].size != B.size) {
        println("Las dimensiones de las matrices no son compatibles")
        return arrayOf(arrayOf(-1))
    }
    
    var c: Array<Array<Int>> = Array(A.size,{Array(B[0].size,{0})})

    for (j in B[0].indices){ // Pasamos por las filas
        for (i in A.indices){
            c[i][j] = 0

            for (a in A[0].indices){
                c[i][j] += A[i][a]*B[a][j]
            }
        }
    }

    return c
}

fun main() {
    var a = arrayOf(arrayOf(1,2,3),arrayOf(4,5,6),arrayOf(7,8,9))
    var b = arrayOf(arrayOf(2,4,6),arrayOf(8,10,12),arrayOf(14,16,18))

    var c = mul_matrix(a,b)
    println("a: ${a.contentDeepToString()}")
    println("b: ${b.contentDeepToString()}")
    println("a*b: ")
    for (i in 0 until c.size){
        println(c[i].joinToString())
    }

    println()

    a = arrayOf(arrayOf(23,5),arrayOf(17,10))
    b = arrayOf(arrayOf(11,18),arrayOf(32,89))

    c = mul_matrix(a,b)
    println("a: ${a.contentDeepToString()}")
    println("b: ${b.contentDeepToString()}")
    println("a*b: ")
    for (i in 0 until c.size){
        println(c[i].joinToString())
    }

    println()

    a = arrayOf(arrayOf(89,64))
    b = arrayOf(arrayOf(20),arrayOf(82))

    c = mul_matrix(a,b)
    println("a: ${a.contentDeepToString()}")
    println("b: ${b.contentDeepToString()}")
    println("a*b: ")
    for (i in 0 until c.size){
        println(c[i].joinToString())
    }

    println()

    a = arrayOf(arrayOf(89),arrayOf(78),arrayOf(2),arrayOf(9))
    b = arrayOf(arrayOf(20,32,4,5))

    c = mul_matrix(a,b)
    println("a: ${a.contentDeepToString()}")
    println("b: ${b.contentDeepToString()}")
    println("a*b: ")
    for (i in 0 until c.size){
        println(c[i].joinToString())
    }

    
}