program oscilador
  implicit none
  integer :: i
  real(8) :: t, x, A, omega, dt

  A = 1.0d0
  omega = 2.0d0
  dt = 0.01d0

  open(unit=10, file="salida.dat")
  do i = 0, 999
    t = i * dt
    x = A * cos(omega * t)
    write(10,*) t, x
  end do
  close(10)
end program oscilador

