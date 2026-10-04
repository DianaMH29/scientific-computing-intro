program suma_vectores
implicit none
integer, parameter :: n = 5
real(8), dimension(n) :: a, b, c
integer :: i

a = [1.0d0, 2.0d0, 3.0d0, 4.0d0, 5.0d0]
b = [10.0d0, 20.0d0, 30.0d0, 40.0d0, 50.0d0]

do i = 1, n
    c(i) = a(i) + b(i)
end do

print *, "Resultado:", c
end program suma_vectores

