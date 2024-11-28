<!DOCTYPE html> 
<html> 
    <head> 
    <title>Diffie-Hellman Key Exchange</title> 
    </head> 
    <body> 
        <script> 
            function power(a, b, p) 
            { 
                if (b == 1) 
                return a; 
                else 
                return((Math.pow(a, b)) % p); 
            } 
            var P, G, x, a, y, b, ka, kb; 
            P = parseInt(prompt("Enter a prime number P:")); 
            document.write("The value of P: " + P + "<br>"); 
            G = parseInt(prompt("Enter a primitive root G:")); 
            document.write("The value of G: " + G + "<br>"); 
            a = parseInt(prompt("Enter the private key for Alice (a):")); 
            document.write("The private key (a) for Alice: " + a + "<br>"); 
            x = power(G, a, P); 
            b = parseInt(prompt("Enter the private key for Bob (b):")); 
            document.write("The private key (b) for Bob: " + b + "<br>"); 
            y = power(G, b, P); 
            ka = power(y, a, P); 
            kb = power(x, b, P); 
            document.write("Secret key for Alice is: " + ka + "<br>"); 
            document.write("Secret key for Bob is: " + kb + "<br>"); 
        </script> 
    </body> 
</html>
