! archivo: energia.f90
subroutine calc_energia(masa, velocidad, resultado)
    real(8), intent(in) :: masa, velocidad
    real(8), intent(out) :: resultado

    resultado = 0.5d0 * masa * velocidad**2
end subroutine calc_energia
