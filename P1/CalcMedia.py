
def text_prompt(msg):
   try:
     return raw_input(msg)
   except NameError:
     return input(msg)

print ( "CALCULADORA DE MÉDIA" )

print ( "digite suas notas da N1" )
n1_1 = float( text_prompt( "sua 1° nota: " ) )
n1_2 = float( text_prompt( "sua 2° nota: " ) )
sm1 = n1_1 + n1_2
md1 = sm1 / 2
print ( "sua média da N1: " + str(md1) )
if 6 <= md1:
   print ( "está acima da média" )
if 6 > md1:
   print ( "está abaixo da média" )

print ( "digite suas notas da N2" )
n2_1 = float( text_prompt( "sua 1° nota: " ) )
n2_2 = float( text_prompt( "sua 2° nota: " ) )
sm2 = n2_1 + n2_2
md2 = sm2 / 2
print ( "sua média da N2: " + str(md2) )
if 6 <= md2:
   print ( "está acima da média" )
if 6 > md2:
   print ( "está abaixo da média" )

mfp1 = md1 * 2
mfp1_2 = md2 * 3
smf = mfp1 + mfp1_2
media_final_p1 = smf / 5

print ( "sua média final é: " + str(media_final_p1) )
if media_final_p1 < 3:
   print ( "você está REPROVADO" )
  
if media_final_p1 >= 6:
   print ( "você está APROVADO")

if 6 > media_final_p1 > 3: 
  print ( "você vai para a avaliação final" )
  af = float( text_prompt( "sua nota da avaliação final: " ) )
  maf = media_final_p1 + af
  maf_1 = maf / 2

  print ( "sua média final com a nota da AF é: " + str(maf_1) )
  if maf_1 < 6:
   print ( "você foi REPROVADO")
  if maf_1 >= 6:
   print ( "você foi APROVADO" )

