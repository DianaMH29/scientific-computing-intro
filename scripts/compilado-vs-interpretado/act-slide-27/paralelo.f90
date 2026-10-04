program paralelo
    use omp_lib
    implicit none
    integer :: i
    real(8) :: suma
    real(8), dimension(1000000) :: datos

    datos = 1.0d0
    suma = 0.0d0

    !$omp parallel do reduction(+:suma)
    do i = 1, 1000000
        suma = suma + datos(i)
    end do
    !$omp end parallel do

    print *, "Suma total:", suma
end program paralelo

