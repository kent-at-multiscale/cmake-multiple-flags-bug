import glob
import os
import shutil
import subprocess
import tempfile

import conans


class CMakeMultipleFlagsBug(conans.ConanFile):
    """
    A reproduction case for the cmake multiple flags bug.
    """
    name = 'cmake-multiple-flags-bug'
    external_version_major = 1
    external_version_minor = 0
    external_version_patch = 0
    external_version = '%s.%s.%s' % (external_version_major, external_version_minor, external_version_patch)
    version = '%s' % external_version
    description = 'A reproduction case for the cmake multiple flags bug.'
    url = 'git@github.com:kent-at-multiscale/cmake-multiple-flags-bug.git'
    license = 'GPL'
    author = 'Kent Rosenkoetter <kent.rosenkoetter@multiscalehn.com>'
    settings = 'os', 'compiler', 'build_type', 'arch'
    generators = 'env'
    
    def build(self):
        pass
    
    def package(self):
        pass
    
    def package_info(self):
        self.cpp_info.includedirs = []  # Ordered list of include paths
        self.cpp_info.libs = []  # The libs to link against
        self.cpp_info.libdirs = []  # Directories where libraries can be found
        self.cpp_info.resdirs = []  # Directories where resources, data, etc can be found
        self.cpp_info.bindirs = []  # Directories where executables and shared libs can be found
        self.cpp_info.defines = ['THREAD_SAFE=YES', 'THREAD_SAFE_=NO']  # preprocessor definitions
        self.cpp_info.cflags = ['-Wall', '-Werror']  # pure C flags
        self.cpp_info.cppflags = ['-pthread', '-Dplacebo', '-Dfoo']  # C++ compilation flags
        self.cpp_info.sharedlinkflags = ['-Wl,-rpath,@loader_path/', '-Wl,-rpath,\\$$ORIGIN/']  # linker flags
        self.cpp_info.exelinkflags = ['-Wl,-rpath,\\$$ORIGIN/../lib', '-Wl,-rpath,@executable_path/../lib']  # linker flags
        
        self.output.info('%s libs: %s' % (self.name, self.cpp_info.libs))
        self.output.info('%s defines: %s' % (self.name, self.cpp_info.defines))
        self.output.info('%s cflags: %s' % (self.name, self.cpp_info.cflags))
        self.output.info('%s cppflags: %s' % (self.name, self.cpp_info.cppflags))
        self.output.info('%s sharedlinkflags: %s' % (self.name, self.cpp_info.sharedlinkflags))
        self.output.info('%s exelinkflags: %s' % (self.name, self.cpp_info.exelinkflags))
