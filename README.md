# 🔓 ECDSA Private Key Recovery from Two Signatures

This Python script demonstrates how to **mathematically recover an ECDSA private key (`d`)** using two signatures that were produced with a related or reused nonce (`k`).  
It implements modular arithmetic operations and the ECDSA equation to reconstruct the private key when a nonce reuse vulnerability occurs.

---

## 🧩 Overview

In ECDSA, each signature `(r, s)` for a message hash `z` is generated as:

\[
s = k^{-1}(z + d \cdot r) \pmod{n}
\]

If two different signatures share the same or correlated `k`, they can leak the private key `d`.

By manipulating the equations for two signatures:

\[
\begin{cases}
s_1 = k^{-1}(z_1 + d \cdot r_1) \pmod{n} \\
s_2 = k^{-1}(z_2 + d \cdot r_2) \pmod{n}
\end{cases}
\]

we can eliminate `k` and derive:

\[
d = \frac{r_1 s_2 - r_2 s_1}{z_2 s_1 - z_1 s_2} \pmod{n}
\]

This is exactly what this script computes.

---

## ⚙️ How It Works

1. **`modinv(a, n)`**  
   Implements the extended Euclidean algorithm to find the modular inverse of `a` modulo `n`.  
   Returns `x` such that `(a * x) % n == 1`.

2. **`compute_private_key(r1, s1, z1, r2, s2, z2, n)`**  
   Uses the formula:
   \[
   d = (r_1 s_2 - r_2 s_1) \cdot (z_2 s_1 - z_1 s_2)^{-1} \pmod{n}
   \]
   to compute the private key.

3. **`main()`**  
   Loads example ECDSA signature data and outputs the computed private key.

---

## 🧮 Example Code

```python
def modinv(a, n):
    """Compute modular inverse of a modulo n."""
    t, new_t = 0, 1
    r, new_r = n, a
    while new_r != 0:
        quotient = r // new_r
        t, new_t = new_t, t - quotient * new_t
        r, new_r = new_r, r - quotient * new_r
    if r > 1:
        raise ValueError(f"No modular inverse for {a} mod {n}")
    if t < 0:
        t += n
    return t

def compute_private_key(r1, s1, z1, r2, s2, z2, n):
    """Compute private key d given two signatures with same or related k."""
    numerator = (r1 * s2 - r2 * s1) % n
    denominator = (z2 * s1 - z1 * s2) % n
    inv_denominator = modinv(denominator, n)
    return (numerator * inv_denominator) % n
🧾 Example Output
Obliczony prywatny klucz d = 51762293150226378344177631012693936892603461211481966174304368340569388768931

🧠 Key Concepts Illustrated

✅ How nonce (k) reuse in ECDSA can expose the private key
✅ Modular arithmetic and modular inverse in cryptography
✅ How two signatures with related k can be exploited mathematically
✅ Relationship between signature components (r, s, z) and private key d

⚠️ Security & Ethical Notice

⚠️ This script is for educational and research use only.
It demonstrates a real cryptographic vulnerability when k is reused.
Do not use it on live systems or without explicit authorization.
Always follow responsible disclosure and legal guidelines when analyzing cryptographic data.

BTC donation address: bc1q4nyq7kr4nwq6zw35pg0zl0k9jmdmtmadlfvqhr
