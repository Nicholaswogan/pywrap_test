module pywrap_test
  implicit none
  
  ! default, parameter, allocatable
  integer :: i1
  integer, parameter :: i2 = 3
  integer, allocatable :: i3
  
  ! real, logical, complex
  real :: r1
  logical :: l1
  complex :: c1
  
  ! arrays
  real :: arr1(8)
  real, parameter :: arr2(3) = [1.0,2.0,3.0]
  real, allocatable :: arr3(:)
  logical, allocatable :: arr4(:,:)
  integer :: arr5(i2)
  
  ! derived types
  type :: mytype
    integer :: i
    real, allocatable :: arr(:)
  end type
  
  ! not supported now, but will eventually be
  type(mytype) :: t1
  character(len=10) :: ch1
  
  
  ! types that may never be supported?
  real, pointer :: p1
  
end module