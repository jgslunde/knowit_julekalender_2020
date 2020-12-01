program luke1
    implicit none

    integer                     :: i, idx
    integer, dimension(99999)   :: numbers
    integer, dimension(100000)  :: sorted_numbers

    numbers = 0
    sorted_numbers = 0

    OPEN(UNIT=99999, FILE="../data/numbers.txt")
    READ(99999,*) numbers

    do 69 i = 1, 99999
        idx = numbers(i)
        sorted_numbers(idx) = 1
    69 continue

    do 420 i = 2, 99999
        if ((sorted_numbers(i)) == 0) then
            write(*,*)  i
            exit
        end if
    420 continue

end program