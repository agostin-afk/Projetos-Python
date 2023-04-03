import qrcode

imagem = qrcode.make("ola mundo")
imagem.save("teste.jpg")