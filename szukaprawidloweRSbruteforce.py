def modinv(a, n):
    """
    Oblicza modularny odwrotność liczby a modulo n.
    Zwraca x takie, że (a * x) % n == 1.
    Jeśli odwrotność nie istnieje, zgłasza wyjątek.
    """
    t, new_t = 0, 1
    r, new_r = n, a
    while new_r != 0:
        quotient = r // new_r
        t, new_t = new_t, t - quotient * new_t
        r, new_r = new_r, r - quotient * new_r
    if r > 1:
        raise ValueError(f"Odwrotność modulo nie istnieje dla {a} mod {n}")
    if t < 0:
        t += n
    return t

def compute_private_key(r1, s1, z1, r2, s2, z2, n):
    """
    Oblicza prywatny klucz d na podstawie wzoru:
    
    d = (r1 * s2 - r2 * s1) / (z2 * s1 - z1 * s2) mod n
    """
    numerator = (r1 * s2 - r2 * s1) % n  # Licznik
    denominator = (z2 * s1 - z1 * s2) % n  # Mianownik
    try:
        inv_denominator = modinv(denominator, n)  # Odwrotność mianownika
        d = (numerator * inv_denominator) % n  # Obliczanie d
        return d
    except ValueError as e:
        print(f"Błąd: {e}")
        return None

def main():
    # Przykładowe dane (należy je podmienić na właściwe wartości)
    r1 = 46159134511846639653039227807867168677952429760806101162575716914492122120852  # Pierwszy r
    s1 = 7519772703183545940918986660617875086369147038649256132503899290067419860069  # Pierwszy s
    z1 = 96305888925087028226280700902788330707257073607110099029890896029884121755055  # Pierwsza wiadomość
    r2 = 111616838599096250300489315075857406212435899769031134709979742002100806022869  # Drugi r
    s2 = 16473844652988003574805773187527026768208893032028674194682143648834372476120  # Drugi s
    z2 = 82526933124808898216141238576469063794369340677613970807733221005881288311205  # Druga wiadomość
    
    # Moduł n (np. rząd grupy w używanym systemie ECDSA)
    n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141  # Moduł dla secp256k1
    
    # Obliczamy prywatny klucz d
    d = compute_private_key(r1, s1, z1, r2, s2, z2, n)
    if d is not None:
        print(f"Obliczony prywatny klucz d = {d}")
    else:
        print("Nie udało się obliczyć d")

if __name__ == '__main__':
    main()
