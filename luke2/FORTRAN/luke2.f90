
INTEGER FUNCTION is_prime(number)
    integer :: k, number
    is_prime = 1
    
    DO k = 2, number-1
        IF (MOD(number, k) == 0) THEN
            is_prime = 0
        END IF
    END DO
    RETURN
END


PROGRAM luke2
    IMPLICIT NONE

    integer :: N, i, j, nr_packages, nr_skips, is_prime
    character(len=30) :: number_string

    N = 5433000

    nr_packages = 0
    i = 1
    DO WHILE (i <= N)
        WRITE(number_string , *) i-1
        IF (INDEX(number_string, "7") > 0) THEN
            DO j = i, 0, -1
                IF (is_prime(j) == 1) THEN
                    nr_skips = j
                    i = i + j + 1
                    EXIT
                END IF
            END DO
        ELSE
            nr_packages = nr_packages + 1
            i = i + 1
        END IF
    END DO

    WRITE(*,*) nr_packages

END PROGRAM