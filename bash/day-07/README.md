Skrypt ma na celu zebrac najwazniejsze informacje o wybranej domenie, takie jak NS, A, TXT, MX


MEMORY:
- aby sprawdzic czy komedna jest dostepna trzeba uzyc command -V lub which

aby sprawdzic konkretny rekors i w jego wersji krotkiej wystarczy:
dig +short <domena> MX | TXT itd
