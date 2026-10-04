program hola_fisica

implicit none
real(8) :: masa, velocidad, energia
masa = 2.0d0
velocidad = 3.0d0
energia = 0.5d0 * masa * velocidad**2
print *, "Energia cinetica =", energia

end program hola_fisica
