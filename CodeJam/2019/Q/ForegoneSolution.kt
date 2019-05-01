import java.math.BigInteger
import java.util.*
import java.io.*
import java.lang.Math.pow

fun main(args: Array<String>) {
    val `in` = Scanner(BufferedReader(InputStreamReader(System.`in`)))
    val t = `in`.nextInt()  // Scanner has functions to read ints, longs, strings, chars, etc.
    for (i in 1..t) {
        val n = `in`.nextBigInteger()

        val ans = solveForegoneSolution(n)

        println("Case #" + i + ": " + ans[0] + " " + ans[1])
    }
}

private val ZERO = 0.toBigInteger()
private val TEN = 10.toBigInteger()

private fun solveForegoneSolution(n: BigInteger): Array<BigInteger> {

    var temp = n

    var digitCount = 0
    while (temp > ZERO) {
        temp /= TEN
        digitCount++
    }

    temp = n
    val digits = IntArray(digitCount)

    var i = 0
    while (temp > ZERO) {
        digits[i] = (temp % TEN).toInt()
        temp /= TEN
        i++
    }

    val digitsA = IntArray(digitCount)
    val digitsB = IntArray(digitCount)

    for (j in 0 until digitCount) {
        val digit = digits[j]
        if (digit == 4) {
            digitsA[j] = 2
            digitsB[j] = 2
            continue
        }
        digitsA[j] = digit
        digitsB[j] = 0
    }

    return arrayOf(digitsToNumber(digitsA), digitsToNumber(digitsB))
}

private fun digitsToNumber(digits: IntArray): BigInteger {
    var number = ZERO
    for (i in digits.indices) {
        number += (digits[i] * pow(10.0, i.toDouble()).toInt()).toBigInteger()
    }
    return number
}
