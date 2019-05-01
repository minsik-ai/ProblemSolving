import java.util.*
import java.io.*

fun main(args: Array<String>) {
    val `in` = Scanner(BufferedReader(InputStreamReader(System.`in`)))
    val t = `in`.nextInt()  // Scanner has functions to read ints, longs, strings, chars, etc.
    for (i in 1..t) {
        val n = `in`.nextInt()
        val p = `in`.next()

        val ans = solveGoYourOwnWay(n, p)

        println("Case #" + i + ": " + ans)
    }
}

private fun solveGoYourOwnWay(n: Int, p: String): String = p.map { ch -> if (ch == 'E') 'S' else 'E' }.joinToString("")
