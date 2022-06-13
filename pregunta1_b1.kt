/**
 * Version recursiva de la operacion a^b mod c
 * 
 * Parametros:
 *      a: Numero entero mayor o igual que cero
 *      b: Numero entero mayor o igual que cero 
 *      c: Numero entero mayor o igual que 2
 * 
 * Return: Devuelve un numero entero resultado de aplicar
 *         la operacion a^b mod c.     
 */
fun potencia_modulada(a:Int, b:Int, c:Int):Int {
    if (b == 0){
        return 1
    } else {
        return ((a % c)*potencia_modulada(a,b-1,c)) % c
    } 
}

fun main() {
    println("Casos de prueba simples")

    println("a:1, b:1, c:2")
    println("a^b mod c:${potencia_modulada(1,1,2)}\n")

    println("a:1, b:0, c:2")
    println("a^b mod c:${potencia_modulada(1,0,2)}\n")

    println("a:4, b:9, c:16")
    println("a^b mod c:${potencia_modulada(4,9,16)}\n")

    println("Casos de prueba aleatorios")
    var a: Int
    var b: Int
    var c: Int

    for (i in 1..10) {
        a = (0..1000).random()
        b = (0..1000).random()
        c = (0..1000).random()
        println("a:${a}, b:${b}, c:${c}")
        println("a^b mod c:${potencia_modulada(a,b,c)}\n")
    }
}