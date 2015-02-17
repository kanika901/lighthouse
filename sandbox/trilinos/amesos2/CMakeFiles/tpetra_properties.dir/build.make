# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.0

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list

# Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /curc/tools/x_86_64/rh6/cmake/3.0.0/bin/cmake

# The command to remove a file.
RM = /curc/tools/x_86_64/rh6/cmake/3.0.0/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/pamo8800/lighthouse_phd_work/amesos2

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/pamo8800/lighthouse_phd_work/amesos2

# Include any dependencies generated for this target.
include CMakeFiles/tpetra_properties.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/tpetra_properties.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/tpetra_properties.dir/flags.make

CMakeFiles/tpetra_properties.dir/tpetra_properties.cpp.o: CMakeFiles/tpetra_properties.dir/flags.make
CMakeFiles/tpetra_properties.dir/tpetra_properties.cpp.o: tpetra_properties.cpp
	$(CMAKE_COMMAND) -E cmake_progress_report /home/pamo8800/lighthouse_phd_work/amesos2/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object CMakeFiles/tpetra_properties.dir/tpetra_properties.cpp.o"
	/curc/tools/x_86_64/rh6/openmpi/1.8.3/gcc/4.9.1/bin/mpicxx   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/tpetra_properties.dir/tpetra_properties.cpp.o -c /home/pamo8800/lighthouse_phd_work/amesos2/tpetra_properties.cpp

CMakeFiles/tpetra_properties.dir/tpetra_properties.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/tpetra_properties.dir/tpetra_properties.cpp.i"
	/curc/tools/x_86_64/rh6/openmpi/1.8.3/gcc/4.9.1/bin/mpicxx  $(CXX_DEFINES) $(CXX_FLAGS) -E /home/pamo8800/lighthouse_phd_work/amesos2/tpetra_properties.cpp > CMakeFiles/tpetra_properties.dir/tpetra_properties.cpp.i

CMakeFiles/tpetra_properties.dir/tpetra_properties.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/tpetra_properties.dir/tpetra_properties.cpp.s"
	/curc/tools/x_86_64/rh6/openmpi/1.8.3/gcc/4.9.1/bin/mpicxx  $(CXX_DEFINES) $(CXX_FLAGS) -S /home/pamo8800/lighthouse_phd_work/amesos2/tpetra_properties.cpp -o CMakeFiles/tpetra_properties.dir/tpetra_properties.cpp.s

CMakeFiles/tpetra_properties.dir/tpetra_properties.cpp.o.requires:
.PHONY : CMakeFiles/tpetra_properties.dir/tpetra_properties.cpp.o.requires

CMakeFiles/tpetra_properties.dir/tpetra_properties.cpp.o.provides: CMakeFiles/tpetra_properties.dir/tpetra_properties.cpp.o.requires
	$(MAKE) -f CMakeFiles/tpetra_properties.dir/build.make CMakeFiles/tpetra_properties.dir/tpetra_properties.cpp.o.provides.build
.PHONY : CMakeFiles/tpetra_properties.dir/tpetra_properties.cpp.o.provides

CMakeFiles/tpetra_properties.dir/tpetra_properties.cpp.o.provides.build: CMakeFiles/tpetra_properties.dir/tpetra_properties.cpp.o

# Object files for target tpetra_properties
tpetra_properties_OBJECTS = \
"CMakeFiles/tpetra_properties.dir/tpetra_properties.cpp.o"

# External object files for target tpetra_properties
tpetra_properties_EXTERNAL_OBJECTS =

tpetra_properties: CMakeFiles/tpetra_properties.dir/tpetra_properties.cpp.o
tpetra_properties: CMakeFiles/tpetra_properties.dir/build.make
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libmesquite.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libmoochothyra.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libmoocho.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/librythmos.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libmoertel.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/liblocathyra.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/liblocaepetra.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/liblocalapack.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libloca.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libnoxepetra.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libnoxlapack.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libnox.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libintrepid.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libfei_trilinos.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libfei_base.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libstratimikos.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libstratimikosbelos.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libstratimikosaztecoo.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libstratimikosamesos.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libstratimikosml.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libstratimikosifpack.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libifpack2-adapters.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libifpack2.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libanasazitpetra.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libModeLaplace.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libanasaziepetra.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libanasazi.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libbelostpetra.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libbelosepetra.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libbelos.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libml.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libkomplex.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libifpack.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libpamgen_extras.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libpamgen.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libamesos.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libamesos2.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libgaleri-xpetra.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libgaleri.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libaztecoo.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libdpliris.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libisorropia.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/liboptipack.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libthyratpetra.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libthyraepetraext.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libthyraepetra.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libthyracore.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libthyratpetra.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libthyraepetraext.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libthyraepetra.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libthyracore.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libxpetra-sup.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libxpetra-ext.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libxpetra.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libepetraext.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libtpetraext.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libtpetrainout.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libtpetra.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libtriutils.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libglobipack.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libshards.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libzoltan.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libepetra.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libsacado.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libkokkosdisttsqr.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libkokkosnodetsqr.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libkokkoslinalg.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libkokkosnodeapi.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libkokkos.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libkokkosTPL_unused_dummy.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libkokkosdisttsqr.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libkokkosnodetsqr.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libkokkoslinalg.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libkokkosnodeapi.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libkokkos.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libkokkosTPL_unused_dummy.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/librtop.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libtpi.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libteuchosremainder.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libteuchosnumerics.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libteuchoscomm.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libteuchosparameterlist.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libteuchoscore.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libteuchosremainder.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libteuchosnumerics.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libteuchoscomm.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libteuchosparameterlist.a
tpetra_properties: /home/pamo8800/TRILINOS_MPI/lib/libteuchoscore.a
tpetra_properties: /curc/tools/x_86_64/rh6/lapack/3.5.0/gcc/4.8.2/lib/liblapack.a
tpetra_properties: /curc/tools/x_86_64/rh6/lapack/3.5.0/gcc/4.8.2/lib/librefblas.a
tpetra_properties: CMakeFiles/tpetra_properties.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking CXX executable tpetra_properties"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/tpetra_properties.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/tpetra_properties.dir/build: tpetra_properties
.PHONY : CMakeFiles/tpetra_properties.dir/build

CMakeFiles/tpetra_properties.dir/requires: CMakeFiles/tpetra_properties.dir/tpetra_properties.cpp.o.requires
.PHONY : CMakeFiles/tpetra_properties.dir/requires

CMakeFiles/tpetra_properties.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/tpetra_properties.dir/cmake_clean.cmake
.PHONY : CMakeFiles/tpetra_properties.dir/clean

CMakeFiles/tpetra_properties.dir/depend:
	cd /home/pamo8800/lighthouse_phd_work/amesos2 && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/pamo8800/lighthouse_phd_work/amesos2 /home/pamo8800/lighthouse_phd_work/amesos2 /home/pamo8800/lighthouse_phd_work/amesos2 /home/pamo8800/lighthouse_phd_work/amesos2 /home/pamo8800/lighthouse_phd_work/amesos2/CMakeFiles/tpetra_properties.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/tpetra_properties.dir/depend
