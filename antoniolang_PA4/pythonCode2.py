#Set up a docker environment for this code, and don't try to include superfluous packages!
from PIL import Image, ImageDraw
import csv
from scipy import constants
import numpy as np
from OpenSSL import crypto, SSL
import os

color = 128 * np.ones(shape=[3], dtype=np.uint8)
tuplevals = tuple(color)
im = Image.new('RGB', (512, 512), tuplevals)
draw = ImageDraw.Draw(im)
draw.rectangle((200, 100, 300, 200), fill=(0, 192, 192), outline=(255, 255, 255))
draw.text((100, 200), "You did it!", fill=(int(constants.speed_of_light), 0, 0))
im.save( "pythonCode2Image.png")

try:
    with open('temp.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
except:
    pass

key = crypto.PKey()
key.generate_key(crypto.TYPE_RSA, 2048)
certFile = os.path.join(os.getcwd(), 'antoniolang_selfSignedCertificate.PEM')
pubKeyFile = os.path.join(os.getcwd(), 'antoniolang_publicKey.key')
privKeyFile = os.path.join(os.getcwd(), 'antoniolang_privateKey.PEM')

certificate = crypto.X509()
certificate.get_subject().C = 'US'
certificate.get_subject().ST = 'Nevada'
certificate.get_subject().L = 'Reno'
certificate.get_subject().O = 'University of Nevada, Reno'
certificate.get_subject().OU = 'CSE'
certificate.get_subject().CN = os.environ.get('USER')

certificate.set_serial_number(42)
certificate.gmtime_adj_notAfter(1577788000) # corresponds to 5 years in seconds
certificate.set_issuer(certificate.get_subject())

certificate.set_pubkey(key)

certificate.sign(key, 'sha512')

open(certFile, "wb").write(crypto.dump_certificate(crypto.FILETYPE_PEM, certificate))
open(pubKeyFile, "wb").write(crypto.dump_publickey(crypto.FILETYPE_PEM, pkey = key))
open(privKeyFile, "wb").write(crypto.dump_privatekey(crypto.FILETYPE_PEM, pkey = key))