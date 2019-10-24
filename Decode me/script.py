import base64
s = "Habl bl max yetz: E5BIFgmsGI6pHRByMeI8L75qxRBdLsJ6EgA8tLF6JRSpue4RALPhA6X4 Xnlm wxvhwx bm :D"
t = s.maketrans("OPQRSTUVWXYZABCDEFGHIJKLMNtuvwxyzabcdefghijklmnopqrs1234567890", "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz6789012345")
print(s.translate(t))
print(base64.b64decode(b'Q0NURntzSU1wTDNfYlU3X20xeDNkXzV1QnM3aXR1VDEwbl9DMXBoM1J9').decode())